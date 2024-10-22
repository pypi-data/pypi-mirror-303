# Tratamiento de datos
import numpy as np
import pandas as pd
import statsmodels.api as sm

import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import classification_report
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RepeatedKFold
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import ParameterGrid
from sklearn.inspection import permutation_importance
from joblib import Parallel, delayed
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

import warnings

df_training = pd.read_csv("/home/jmurgamoreno/training_hard.txt.gz", sep=",")
df_training2 = pd.read_csv("/home/jmurgamoreno/training_soft.txt.gz", sep=",")
df_test = pd.read_csv("/home/jmurgamoreno/testing_hard_fixed.txt.gz", sep=",")


class RandomForest:
    def __init__(self, simulations, data):
        self.simulations = simulations
        self.test = data
        self.params = ["iter", "s", "t", "t_end", "f_i", "f_t", "f_t_end"]
        self.train = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def RF(self):
        param_grid = ParameterGrid(
            {
                "n_estimators": [100, 1000],
                "max_features": [10, "sqrt", "log2"],
                "max_depth": [None, 3, 10, 20],
                "criterion": ["gini", "entropy", "log_loss"],
            }
        )

        # log_loss sqrt None 1000

        X_train = self.simulations.loc[
            :, ~self.simulations.columns.isin(self.params)
        ].drop("model", axis=1)
        d = {
            "hard_young_incomplete": 0,
            "hard_old_incomplete": 1,
            "hard_young_complete": 2,
            "hard_old_complete": 3,
            "soft_young_incomplete": 4,
            "soft_old_incomplete": 5,
            "soft_young_complete": 6,
            "soft_old_complete": 7,
        }
        d = {"old": 0, "young": 1}

        y_train = self.simulations.model.apply(lambda r: d[r])

        lda = LinearDiscriminantAnalysis(n_components=3)
        df_lda = pd.DataFrame(
            lda.fit(X_train, y_train).transform(X_train), columns=["ld1", "ld2", "ld3"]
        )
        X_train_lda = pd.concat([X_train, df_lda], axis=1)
        output = {"params": [], "oob_accuracy": []}

        model = RandomForestClassifier(
            oob_score=True,
            n_jobs=200,
            random_state=123,
            criterion="log_loss",
            max_depth=None,
            max_features="sqrt",
            n_estimators=1000,
        )

        # model.fit(X_train_lda, y_train)
        model.fit(X_train, y_train)

        X_test = self.test.loc[:, ~self.test.columns.isin(self.params)].drop(
            "model", axis=1
        )
        y_test = self.test.model.apply(lambda r: d[r])
        for params in tqdm(param_grid):
            model = RandomForestClassifier(
                oob_score=True, n_jobs=200, random_state=123, **params
            )

            model.fit(X_train_lda, y_train)

            output["params"].append(params)
            output["oob_accuracy"].append(model.oob_score_)
            # print(f"Modelo: {params} ✓")

        # Resultados
        output = pd.DataFrame(output)
        output = pd.concat([output, output["params"].apply(pd.Series)], axis=1)
        output = output.sort_values("oob_accuracy", ascending=False)
        output = output.drop(columns="params")
        output.head(4)


# # Define the parameter grid to search
param_grid = {
    "max_depth": [None, 5, 10, 20],  # Maximum depth of the trees
    "min_samples_split": [
        2,
        5,
        10,
    ],  # Minimum samples required to split an internal node
    "min_samples_leaf": [
        0.01,
        1,
        2,
        4,
    ],  # Minimum samples required to be at a leaf node
    "max_features": [None, "sqrt", "log2"],
    "class_weight": [None, "balanced"],
    "criterion": ["gini", "entropy", "log_loss"],
    "ccp_alpha": [0, 0.01],
}

# # Initialize the RandomForestClassifier
rf_classifier = RandomForestClassifier()

# # Initialize GridSearchCV with the classifier and parameter grid
grid_search = GridSearchCV(
    rf_classifier, param_grid, cv=5, scoring="accuracy", n_jobs=20
)

##################
import pandas as pd
import numpy as np
import typing
from typing import Optional, Union, Tuple
import logging
import tqdm

from sklearn.base import clone
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import ParameterGrid
from sklearn.metrics import roc_auc_score, accuracy_score, f1_score
from sklearn.metrics import mean_absolute_error, mean_squared_error


def check_early_stopping(
    scores: Union[list, np.ndarray],
    metric: str,
    stopping_rounds: int = 4,
    stopping_tolerance: float = 0.01,
    max_runtime_sec: int = None,
    start_time: pd.Timestamp = None,
) -> bool:
    """
    Check if early stopping condition is met.

    Parameters
    ----------

    scores: list, np.ndarray
        Scores used to evaluate early stopping conditions.

    metric: str
        Metric which scores referes to. Used to determine if higher score
        means a better model or the opposite.

    stopping_rounds: int, default 4
        Number of consecutive rounds without improvement needed to stop
        the training.

    stopping_tolerance: float, default 0.01
        Minimum percentage of positive change between two consecutive rounds
        needed to consider it as an improvement.

    max_runtime_sec: int, default `None`
        Maximum allowed runtime in seconds for model training. `None` means unlimited.

    start_time: pd.Timestamp, default `None`
        Time when training started. Used to determine if `max_runtime_sec` has been
        reached.


    Returns
    ------
    bool:
        `True` if any condition needed for early stopping is met. `False` otherwise.

    Notes
    -----

    Example of early stopping:

    Stop after 4 rounds without an improvement of 1% or higher: `stopping_rounds` = 4,
    `stopping_tolerance` = 0.01, `max_runtime_sec` = None.

    """

    allowed_metrics = [
        "accuracy",
        "auc",
        "f1",
        "mse",
        "mae",
        "squared_error",
        "absolute_error",
    ]

    if metric not in allowed_metrics:
        raise Exception(
            f"`metric` argument must be one of: {allowed_metrics}. " f"Got {metric}"
        )

    if isinstance(scores, list):
        scores = np.array(scores)

    if max_runtime_sec is not None:
        if start_time is None:
            start_time = pd.Timestamp.now()

        runing_time = (pd.Timestamp.now() - start_time).total_seconds()

        if runing_time > max_runtime_sec:
            logging.debug(
                f"Reached maximum time for training ({max_runtime_sec} seconds). "
                f"Early stopping activated."
            )
            return True

    if len(scores) < stopping_rounds:
        return False

    if metric in ["accuracy", "auc", "f1"]:
        # The higher the metric, the better
        diff_scores = scores[1:] - scores[:-1]
        improvement = diff_scores / scores[:-1]

    if metric in ["mse", "mae", "squared_error", "absolute_error"]:
        # The lower the metric, the better

        # scores = -1 * scores
        # diff_scores = scores[:-1] - scores[1:]
        # improvement = diff_scores / scores[1:]
        diff_scores = scores[1:] - scores[:-1]
        improvement = diff_scores / scores[:-1]
        improvement = -1 * improvement

    improvement = np.hstack((np.nan, improvement))
    logging.debug(f"Improvement: {improvement}")

    if (improvement[-stopping_rounds:] < stopping_tolerance).all():
        return True
    else:
        return False


def fit_RandomForest_early_stopping(
    model: Union[RandomForestClassifier, RandomForestRegressor],
    X: Union[np.ndarray, pd.core.frame.DataFrame],
    y: np.ndarray,
    metric: str,
    positive_class: int = 1,
    score_tree_interval: int = None,
    stopping_rounds: int = 4,
    stopping_tolerance: float = 0.01,
    max_runtime_sec: int = None,
) -> np.ndarray:
    """
    Fit a RandomForest model until an early stopping condition is met or
    `n_estimatos` is reached.

    Parameters
    ----------

    model: RandomForestClassifier, RandomForestRegressor
        Model to be fitted.

    X: np.ndarray, pd.core.frame.DataFrame
        Training input samples.

    y: np.ndarray, pd.core.frame.DataFrame
        Target value of the input samples.

    scores: list, np.ndarray
        Scores used to evaluate early stopping conditions.

    metric: str
        Metric used to generate the score. Used to determine if higher score
        means a better model or the opposite.

    score_tree_interval: int, default `None`
        Score the model after this many trees. If `None`, the model is scored after
        `n_estimators` / 10.

    stopping_rounds: int
        Number of consecutive rounds without improvement needed to stop the training.

    stopping_tolerance: float, default 0.01
        Minimum percentage of positive change between two consecutive rounds
        needed to consider it as an improvement.

    max_runtime_sec: int, default `None`
        Maximum allowed runtime in seconds for model training. `None` means unlimited.


    Returns
    ------
    oob_scores: np.ndarray
        Out of bag score for each scoring point.

    """

    if score_tree_interval is None:
        score_tree_interval = int(model.n_estimators / 10)

    allowed_metrics = [
        "accuracy",
        "auc",
        "f1",
        "mse",
        "mae",
        "squared_error",
        "absolute_error",
    ]

    if metric not in allowed_metrics:
        raise Exception(
            f"`metric` argument must be one of: {allowed_metrics}. " f"Got {metric}"
        )

    if not model.oob_score:
        model.set_params(oob_score=True)

    start_time = pd.Timestamp.now()
    oob_scores = []
    scoring_points = np.arange(0, model.n_estimators + 1, score_tree_interval)[1:]

    metrics = {
        "auc": roc_auc_score,
        "accuracy": accuracy_score,
        "f1": f1_score,
        "mse": mean_squared_error,
        "squared_error": mean_squared_error,
        "mae": mean_absolute_error,
        "absolute_error": mean_absolute_error,
    }

    for i, n_estimators in enumerate(scoring_points):
        logging.debug(f"Training with n_stimators: {n_estimators}")
        model.set_params(n_estimators=n_estimators)
        model.fit(X=X, y=y)

        if metric == "auc":
            if isinstance(model, RandomForestClassifier):
                oob_predictions = model.oob_decision_function_
                if oob_predictions.ndim == 1:
                    oob_score = metrics[metric](y_true=y, y_score=oob_predictions)
                else:
                    oob_score = metrics[metric](
                        y_true=y, y_score=oob_predictions, multi_class="ovr"
                    )
            else:
                raise ValueError(
                    "AUC metric is only applicable for classification models."
                )

        else:
            if isinstance(model, RandomForestClassifier):
                oob_predictions = np.argmax(model.oob_decision_function_, axis=1)
            else:
                oob_predictions = model.oob_prediction_
            oob_score = metrics[metric](y_true=y, y_pred=oob_predictions)

        oob_scores.append(oob_score)

        early_stopping = check_early_stopping(
            scores=oob_scores,
            metric=metric,
            stopping_rounds=stopping_rounds,
            stopping_tolerance=stopping_tolerance,
            max_runtime_sec=max_runtime_sec,
            start_time=start_time,
        )

        if early_stopping:
            logging.debug(
                f"Early stopping activated at round {i + 1}: n_estimators = {n_estimators}"
            )
            break

    logging.debug(f"Out of bag score = {oob_scores[-1]}")

    return np.array(oob_scores), scoring_points[: len(oob_scores)]


def custom_gridsearch_RandomForestClassifier(
    model: RandomForestClassifier,
    X: Union[np.ndarray, pd.core.frame.DataFrame],
    y: np.ndarray,
    metric: str,
    param_grid: dict,
    positive_class: int = 1,
    score_tree_interval: int = None,
    stopping_rounds: int = 5,
    stopping_tolerance: float = 0.01,
    model_max_runtime_sec: int = None,
    max_models: int = None,
    max_runtime_sec: int = None,
    return_best: bool = True,
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Grid search for RandomForestClassifier model based on out-of-bag metric and
    early stopping for each model fit.

    Parameters
    ----------

    model: RandomForestClassifier
        Model to search over.

    X: np.ndarray, pd.core.frame.DataFrame
        The training input samples.

    y: np.ndarray, pd.core.frame.DataFrame
        The target of input samples.

    scores: list, np.ndarray
        Scores used to evaluate early stopping conditions.

    metric: str
        Metric used to generate the score. I is used to determine if higher score
        means a better model or the opposite.

    score_tree_interval: int, default `None`
        Score the model after this many trees. If `None`, the model is scored after
        `n_estimators` / 10.

    stopping_rounds: int
        Number of consecutive rounds without improvement needed to stop the training.

    stopping_tolerance: float, default 0.01
        Minimum percentage of positive change between two consecutive rounds
        needed to consider it as an improvement.

    model_max_runtime_sec: int, default `None`
        Maximum allowed runtime in seconds for model training. `None` means unlimited.

    max_models: int, default `None`
        Maximum number of models trained during the search.

    max_runtime_sec: int, default `None`
        Maximum number of seconds for the search.

    return_best : bool
        Refit model using the best found parameters on the whole data.


    Returns
    ------

    results: pd.DataFrame

    """

    results = {"params": [], "oob_metric": []}
    start_time = pd.Timestamp.now()
    history_scores = {}
    history_scoring_points = np.array([], dtype=int)
    param_grid = list(ParameterGrid(param_grid))

    if not model.oob_score:
        model.set_params(oob_score=True)

    if max_models is not None and max_models < len(param_grid):
        param_grid = np.random.choice(param_grid, max_models)

    for params in tqdm.tqdm(param_grid):
        if max_runtime_sec is not None:
            runing_time = (pd.Timestamp.now() - start_time).total_seconds()
            if runing_time > max_runtime_sec:
                logging.info(
                    f"Reached maximum time for GridSearch ({max_runtime_sec} seconds). "
                    f"Search stopped."
                )
                break

        model.set_params(**params)

        oob_scores, scoring_points = fit_RandomForest_early_stopping(
            model=clone(model),
            X=X,
            y=y,
            metric=metric,
            positive_class=positive_class,
            score_tree_interval=score_tree_interval,
            stopping_rounds=stopping_rounds,
            stopping_tolerance=stopping_tolerance,
            max_runtime_sec=model_max_runtime_sec,
        )

        history_scoring_points = np.union1d(history_scoring_points, scoring_points)
        history_scores[str(params)] = oob_scores
        params["n_estimators"] = scoring_points[-1]
        results["params"].append(params)
        results["oob_metric"].append(oob_scores[-1])
        logging.debug(f"Modelo: {params} \u2713")

    results = pd.DataFrame(results)
    history_scores = pd.DataFrame(
        dict([(k, pd.Series(v)) for k, v in history_scores.items()])
    )
    history_scores["n_estimators"] = history_scoring_points

    if metric in ["accuracy", "auc", "f1"]:
        results = results.sort_values("oob_metric", ascending=False)
    else:
        results = results.sort_values("oob_metric", ascending=True)

    results = results.rename(columns={"oob_metric": f"oob_{metric}"})

    if return_best:
        best_params = results["params"].iloc[0]
        print(
            f"Refitting mode using the best found parameters and the whole data set: \n {best_params}"
        )

        model.set_params(**best_params)
        model.fit(X=X, y=y)

    results = pd.concat([results, results["params"].apply(pd.Series)], axis=1)
    results = results.drop(columns="params")

    return results, history_scores
