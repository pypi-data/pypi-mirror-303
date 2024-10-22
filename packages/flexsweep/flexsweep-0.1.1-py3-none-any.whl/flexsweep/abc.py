import numpy as np
from scipy.stats import median_abs_deviation
from sklearn.neighbors import DistanceMetric
import numpy as np
from numba import njit, float64
import pandas as pd


@njit
def median_absolute_deviation(arr, scale=1.4826):
    median = np.median(arr)
    deviations = np.abs(arr - median)
    mad = np.median(deviations)
    mad *= scale
    return mad


@njit
def normalise(x, y):
    if median_absolute_deviation(y) != 0:
        return x / median_absolute_deviation(y)
    else:
        return x


# @njit
def distances(target, sumstat, param):
    # Scale everything and compute Euclidean distance
    sumstat_scaled = np.zeros(sumstat.shape)
    target_scaled = np.zeros(target.shape)
    dist = np.zeros(sumstat.shape[0])

    for j in range(target.shape[0]):
        sumstat_scaled[:, j] = normalise(sumstat[:, j], sumstat[:, j])
        target_scaled[j] = normalise(target[j], sumstat[:, j])
        dist += np.square(sumstat_scaled[:, j] - target_scaled[j])

    dist = np.sqrt(dist)
    return target_scaled, sumstat_scaled, dist


def rejection(target, sumstat, param, tol, kernel="epanechnikov"):
    target_scaled, sumstat_scaled, dist = distances(target, sumstat, param)

    # Sort and get minimum distance to return values inside tolerance range
    n_accept = int(np.ceil(len(dist) * tol))
    n_limit = np.sort(dist)[n_accept]
    # Ensure getting only n_limit, if more than one
    n_idx = np.where(dist <= n_limit)[0][:n_accept]

    # Weighted distances
    if kernel == "epanechnikov":
        wts = 1 - np.square(dist[n_idx] / n_limit)
    elif kernel == "rectangular":
        wts = dist[n_idx] / n_limit
    elif kernel == "gaussian":
        d = DistanceMetric.get_metric("euclidean")
        ds = np.median(d.pairwise(sumstat))
        wts = 1 / np.sqrt(2 * np.pi) * np.exp(-0.5 * np.square(dist / (ds / 2)))
    elif kernel == "triangular":
        wts = 1 - np.abs(dist[n_idx] / n_limit)
    elif kernel == "biweight":
        wts = np.square(1 - np.square(dist[n_idx] / n_limit))
    elif kernel == "cosine":
        wts = np.cos(np.pi / 2 * dist[n_idx] / n_limit)

    return (
        target_scaled,
        sumstat[n_idx],
        sumstat_scaled[n_idx],
        param[n_idx],
        dist[n_idx],
        wts,
    )


def lsfit(x, y, wt=None, intercept=True, tolerance=1e-07):
    # Check if the intercept term should be included
    if intercept:
        x = np.column_stack((np.ones(len(x)), x))

    # Apply weights if provided
    if wt is not None:
        x = x * np.sqrt(wt[:, None])
        y = y * np.sqrt(wt[:, None])

    # Perform least squares estimation
    q, r = np.linalg.qr(x)
    coef = np.linalg.lstsq(r, q.T @ y, rcond=None)[0]
    # new_coef = np.vstack((coef[-1:], coef[:-1]))
    residuals = y - x @ coef

    # Create the result dictionary
    # result = {
    #     "coef": coef,
    #     "residuals": residuals,
    #     "intercept": intercept,
    #     "qr": (q, r),
    # }

    return coef, residuals


def abc_loclinear(
    target_file,
    param_summaries_file,
    P,
    tol,
    transformation="none",
    kernel="epanechnikov",
):
    # Reading into matrix using np.loadtxt
    target = pd.read_csv(target_file).values
    summaries = pd.read_csv(param_summaries_file, sep="\t").values

    target = target[0, 48:]
    param = summaries[:, :P]
    param[:, 0] = -np.log10(param[:, 0])
    sumstat = summaries[:, 48:]

    # transformation="none"; kernel="epanechnikov"; tol=0.025

    assert kernel.lower() in [
        "gaussian",
        "epanechnikov",
        "rectangular",
        "triangular",
        "biweight",
        "cosine",
    ], "Kernel is incorrectly defined. Use gaussian, epanechnikov, rectangular, triangular, biweight, or cosine"
    assert transformation.lower() in [
        "none",
        "log",
        "tan",
    ], "Apply one of the following transformations: none, log, tan"

    assert (
        len(target) == sumstat.shape[1]
    ), "Number of summary statistics in target has to be the same as in sumstat."

    num_params = param.shape[1]
    num_stats = sumstat.shape[1]

    mins = np.min(param, axis=0)
    maxs = np.max(param, axis=0)

    # Scale and compute Euclidean distance
    (
        target_scaled,
        sumstat_accepted,
        sumstat_scaled,
        param_accepted,
        dist_accepted,
        wts,
    ) = rejection(target, sumstat, param, tol, kernel)

    num_accepted = sumstat_accepted.shape[0]

    # Transform parameters
    if transformation != "none":
        for i, v in enumerate(param_accepted.T):
            if transformation.lower() == "log" & np.any(param <= 0):
                v[v <= 0] = np.min(v[np.nonzero(v)])
                v = np.log(v)
            elif transformation.lower() == "tan":
                v = tangent_transformation(v, mins[i], maxs[i])

    sumstat_intercept = np.hstack((np.ones((num_accepted, 1)), sumstat_scaled))

    # Linear regression
    lm_coefficients, lm_residuals = lsfit(sumstat_intercept, param_accepted, wts)

    pred = np.dot(
        lm_coefficients, np.vstack((np.ones_like(target_scaled), target_scaled))
    )
    pred = np.repeat(pred.T, num_accepted, axis=0)

    rsdl_mean = np.mean(lm_residuals, axis=0)
    rsdl_corrected = lm_residuals - rsdl_mean

    pred_corrected = pred + rsdl_mean

    def f(x, wts):
        return np.sum(np.square(x) * wts) / np.sum(wts)

    σ = np.apply_along_axis(f, axis=1, arr=rsdl_corrected, wts=wts)
    aic = num_accepted * np.sum(np.log(σ)) + 2 * (num_stats + 1) * num_params
    bic = (
        num_accepted * np.sum(np.log(σ))
        + np.log(np.sum(num_accepted)) * (num_stats + 1) * num_params
    )

    # Heteroscedasticity correction
    rsdl_log = np.log(np.square(lm_residuals))
    lm_coefficients, lm_residuals = regression(sumstat_intercept, rsdl_log, wts)

    pred_sd = np.dot(
        lm_coefficients, np.vstack((np.ones_like(target_scaled), target_scaled))
    )
    pred_sd = np.sqrt(np.exp(pred_sd))
    pred_sd = np.repeat(pred_sd.T, num_accepted, axis=0)
    pred_si = np.dot(lm_coefficients, sumstat_intercept.T)
    pred_si = np.sqrt(np.exp(pred_si))

    param_adjusted = pred + (pred_sd * rsdl_corrected) / pred_si
    rsdl_adjusted = (pred_sd * rsdl_corrected) / pred_si

    # Back transform parameter values
    for i in range(num_params):
        if transformation.lower() == "log":
            param_accepted[:, i] = np.exp(param_accepted[:, i])
            param_adjusted[:, i] = np.exp(param_adjusted[:, i])
        elif transformation.lower() == "tan":
            param_accepted[:, i] = undo_tangent_transformation(
                param_accepted[:, i], mins[i], maxs[i]
            )
            param_adjusted[:, i] = undo_tangent_transformation(
                param_adjusted[:, i], mins[i], maxs[i]
            )

    return param_accepted, param_adjusted


import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error

# Create an MLP-based ridge regressor
mlp = MLPRegressor(hidden_layer_sizes=(64, 32), activation="relu", max_iter=2000)
mlp.fit(sumstat_accepted, param_accepted)

# Predict using the trained MLP
target_pred = mlp.predict(target_scaled.reshape(-1, 1))

# Predict using the trained regressor
y_pred = mlp_regressor.predict(X_test)

# Calculate the Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)


####################################################

## normalise parameters

import numpy as np
from sklearn.linear_model import Ridge

# Assuming you have the data loaded as NumPy arrays: param, lambda, wt1, gwt, scaled_sumstat, target

# Get the number of parameters

# Initialize an array to store the Median Absolute Deviation (MAD) for each parameter
param_mad = np.zeros(num_params)
param_scaled = np.empty_like(param_accepted)
# Compute MAD and normalize the parameters
for i in range(num_params):
    param_mad[i] = median_absolute_deviation(param_accepted)
    param_scaled[:, i] = normalise(param_accepted[:, i], param_accepted[:, i])

# Convert the lambda values to a numpy array
lambdas = np.array([0.0001, 0.001, 0.01])

numnet = lambdas.size
fv = np.zeros((wts.size, num_params, numnet))
pred = np.zeros((num_params, numnet))
mataux = np.sqrt(np.diag(wts))
paramaux = np.dot(mataux, param_scaled)
scaledaux = np.dot(mataux, sumstat_scaled)

# Perform ridge regression for each parameter
for i in range(num_params):
    for j in range(numnet):
        alpha = lambdas[j]
        ridge_model = Ridge(alpha=alpha)
        ridge_model.fit(scaledaux, paramaux[:, i])
        coef_i = ridge_model.coef_

        fv[:, i, j] = np.dot(
            np.hstack((np.ones((np.sum(wt1), 1)), scaled_sumstat[wt1, :])), coef_i
        )
        pred[i, j] = np.dot(np.hstack((1, target)), coef_i)

pred_med = np.median(pred, axis=1)
pred_med = np.tile(pred_med, (np.sum(wt1), 1))

fitted_values = np.median(fv, axis=2)
residuals = param[wt1, :] - fitted_values
