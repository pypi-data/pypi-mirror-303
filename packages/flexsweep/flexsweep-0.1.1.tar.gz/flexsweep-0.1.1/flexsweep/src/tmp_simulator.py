##########################
# def generate_simulation(self, param_iter):
#     (_s, _t, _t_end, _f_i, _f_t, _burn_in, iteration) = param_iter

#     tmp_parameters = deepcopy(self.parameters)

#     # Change manually to test og Flex-sweep
#     tmp_parameters.mutation_rate = np.random.uniform(2 * 1e-9, 5.2 * 1e-8)
#     tmp_parameters.contig.recombination_map = msprime.RateMap(
#         position=tmp_parameters.contig.recombination_map.position,
#         rate=np.array([np.random.exponential(1e-8)]),
#     )

#     # adaptive_position = np.random.randint(1.2e6*0.25,1.2e6*0.75)
#     adaptive_position = sum(tmp_parameters.contig.original_coordinates[1:]) / 2

#     tmp_parameters.contig.add_single_site(
#         id=tmp_parameters.sweep_class, coordinate=adaptive_position
#     )

#     if tmp_parameters.sweep_class == "hard":
#         extended_events = stdpopsim.ext.selective_sweep(
#             single_site_id=tmp_parameters.sweep_class,
#             population=list(tmp_parameters.sample.keys())[0],
#             selection_coeff=_s,
#             min_freq_at_end=_f_t,
#             mutation_generation_ago=_t,
#             end_generation_ago=_t_end,
#         )
#     else:
#         # start_generation_ago _t + 5000 to ensure the soft sweep achieve the desired freq (up to 0.2)
#         extended_events = stdpopsim.ext.selective_sweep(
#             single_site_id=tmp_parameters.sweep_class,
#             population=list(tmp_parameters.sample.keys())[0],
#             selection_coeff=_s,
#             min_freq_at_start=_f_i,
#             min_freq_at_end=_f_t,
#             # mutation_generation_ago=_t + 1000,
#             mutation_generation_ago=_t + 1,
#             end_generation_ago=_t_end,
#             start_generation_ago=_t,
#         )

#         # _f_i_end = 0.01 if _f_i < 0.01 else 0.1

#         end_condition = stdpopsim.ext.ConditionOnAlleleFrequency(
#             start_time=_t,
#             end_time=_t,
#             single_site_id=tmp_parameters.sweep_class,
#             population=list(tmp_parameters.sample)[0],
#             op="<=",
#             allele_frequency=_f_t + 0.1,
#             # allele_frequency=0.2,
#         )

#         extended_events.append(end_condition)

#     if _f_t != 1:
#         # f_step = 0.1 if _f_t == 0.9 else 0.1

#         end_condition = stdpopsim.ext.ConditionOnAlleleFrequency(
#             start_time=_t_end,
#             end_time=_t_end,
#             single_site_id=tmp_parameters.sweep_class,
#             population=list(tmp_parameters.sample)[0],
#             op="<",
#             allele_frequency=_f_t + 0.1,
#         )

#         extended_events.append(end_condition)

#     engine = stdpopsim.get_engine("slim")

#     def timeout_handler(signum, frame):
#         raise TimeoutError("Execution timed out")

#     signal.signal(signal.SIGALRM, timeout_handler)
#     signal.alarm(int(self.timeout))
#     timeout_occurred = False

#     with open("/home/jmurgamoreno/test.slim", "w") as f:
#         with redirect_stdout(f):
#             ts_sweep = engine.simulate(
#                 tmp_parameters.model,
#                 tmp_parameters.contig,
#                 tmp_parameters.sample,
#                 extended_events=extended_events,
#                 slim_scaling_factor=tmp_parameters.rescale_factor,
#                 slim_burn_in=_burn_in,
#                 slim_script=True,
#                 verbosity=0,
#             )

#     try:
#         ts_sweep = engine.simulate(
#             tmp_parameters.model,
#             tmp_parameters.contig,
#             tmp_parameters.sample,
#             extended_events=extended_events,
#             slim_scaling_factor=tmp_parameters.rescale_factor,
#             slim_burn_in=_burn_in,
#         )
#     except TimeoutError:
#         # print(param_iter)
#         timeout_occurred = True
#     finally:
#         signal.alarm(0)

#     if timeout_occurred:
#         return (None, None, None, None)

#     if self.output_folder is not None:
#         ts_string = (
#             self.output_folder + "/sweeps/sweep_" + str(iteration) + ".trees"
#         )
#         ts_sweep.dump(ts_string)

#         return (
#             ts_string,
#             self.interpolate_genetic_map(ts_sweep),
#             np.column_stack(
#                 [_s, _t, _t_end, _f_i, _f_t, frequency(ts_sweep, 6e5)]
#             ).flatten(),
#         )
#     else:
#         return (
#             ts_sweep,
#             self.interpolate_genetic_map(ts_sweep),
#             np.column_stack(
#                 [_s, _t, _t_end, _f_i, _f_t, frequency(ts_sweep, 6e5)]
#             ).flatten(),
#         )


# def timing_selection_incomplete_sweep(
#     self, i, j, t_lower, t_upper, mutation_generation_ago=None
# ):
#     current_sweep = self.parameters.sweep_class

#     t = []
#     s = []

#     s_t_lower = self.parameters.sweep_diffusion_time[current_sweep][round(i, 1)]
#     s_t_upper = self.parameters.sweep_diffusion_time[current_sweep][
#         round(i + 0.1, 1)
#     ]

#     # We search for the previous diffusion mean value to ensure the condition.
#     # Otherwise the rounded values search for the nearest estimated value and some condition cannot achieve because of the arise time is shorter than expected
#     # Diffusion value are estimated in the range [0:0.05:1]
#     # if j > 0.05:
#     #     _j = round(round(j, 1) - 0.05, 2)
#     # else:
#     _j = j

#     if self.parameters.sweep_class == "soft":
#         s_t_lower = s_t_lower[_j]
#         s_t_upper = s_t_upper[_j]

#     # Minimum number of simulation to achieve current frequency in old sweeps
#     min_gen = s_t_lower[-1, 1]
#     # max_gen = s_t_lower[0, 1]
#     max_gen = s_t_lower[
#         np.where(t_upper + s_t_lower[:, 1] < t_lower - s_t_lower[:, 1])[0]
#     ][0, 1]
#     if mutation_generation_ago is None:
#         _t = np.random.uniform(max_gen, min_gen, 1).astype(int)[0]
#     else:
#         _t = mutation_generation_ago

#     if t_upper >= 2000:
#         # Checking if mutation_generation_ago or random t value is greater than the minimum amount diffusion time estimated
#         # Otherwise there is no s value to achieve f_t at generations 2000.
#         # Reducing t_lower by mutation_generation_ago or random t value in order to obtain t_lower == max(t)
#         _t_end = np.random.choice(np.arange(t_upper + _t, t_lower - _t), 1)[0]

#         s_lower = s_t_lower[s_t_lower[:, 1] <= _t, 0]
#         s_upper = s_t_lower[s_t_upper[:, 1] >= _t, 0]
#         _s = np.intersect1d(s_lower, s_upper)

#         _t = _t_end + _t
#     else:
#         s_lower = s_t_lower[(s_t_lower[:, 1] <= _t), 0]
#         s_upper = s_t_lower[(s_t_upper[:, 1] >= _t), 0]
#         _s = np.intersect1d(s_lower, s_upper)
#         _t_end = 0

#     while _s.size == 0:
#         if mutation_generation_ago is None:
#             _t = np.random.uniform(t_lower, t_upper, 1).astype(int)
#         else:
#             _t = np.array([mutation_generation_ago])

#             s_lower = s_t_lower[(s_t_lower[:, 1] < _t), 0]
#             s_upper = s_t_lower[(s_t_upper[:, 1] > _t), 0]
#             _s = np.intersect1d(s_lower, s_upper)

#     _s = np.random.uniform(_s.min(), _s.max(), 1).astype(int)[0]

#     return (_t, _t_end, _s)

# def timing_selection_incomplete_sweep(
#     self, i, j, t_lower, t_upper, mutation_generation_ago=None
# ):
#     current_sweep = self.parameters.sweep_class

#     t = []
#     s = []

#     s_t_lower = self.parameters.sweep_diffusion_time[current_sweep][round(i, 1)]
#     s_t_upper = self.parameters.sweep_diffusion_time[current_sweep][
#         round(i + 0.1, 1)
#     ]

#     # We search for the previous diffusion mean value to ensure the condition.
#     # Otherwise the rounded values search for the nearest estimated value and some condition cannot achieve because of the arise time is shorter than expected
#     # Diffusion value are estimated in the range [0:0.05:1]
#     # if j > 0.05:
#     #     _j = round(round(j, 1) - 0.05, 2)
#     # else:
#     _j = j

#     if self.parameters.sweep_class == "soft":
#         s_t_lower = s_t_lower[_j]
#         s_t_upper = s_t_upper[_j]

#     # Minimum number of simulation to achieve current frequency in old sweeps
#     min_gen = s_t_lower[-1, 1]
#     _t_lower = np.random.choice(t_upper, t_lower)
#     _t_lower = 5000 if _t_lower < 2000 else t_lower

#     if _t_lower <= 2000:
#         max_gen = s_t_lower[s_t_lower[:, 1] < 2000, 1][0]
#     else:
#         # max_gen = s_t_lower[
#         #     np.where(t_upper + s_t_lower[:, 1] < t_lower - s_t_lower[:, 1])[0]
#         # ][0, 1]
#         max_gen = s_t_lower[(s_t_lower[:, 1] < (t_lower - t_upper))][0, 1]

#     if mutation_generation_ago is None:
#         _t = np.random.uniform(max_gen, min_gen, 1).astype(int)[0]
#     else:
#         _t = mutation_generation_ago

#     if t_upper >= 2000:
#         # Checking if mutation_generation_ago or random t value is greater than the minimum amount diffusion time estimated
#         # Otherwise there is no s value to achieve f_t at generations 2000.
#         # Reducing t_lower by mutation_generation_ago or random t value in order to obtain t_lower == max(t)

#         _t_end = np.random.choice(
#             np.arange(t_upper + min_gen, t_lower - min_gen), 1
#         )[0]
#         _t = np.random.choice(s_t_lower[(s_t_lower[:, 1] + _t_end) < t_lower, 1])
#         s_lower = s_t_lower[s_t_lower[:, 1] <= _t, 0]
#         s_upper = s_t_upper[s_t_upper[:, 1] >= _t, 0]
#         _s = np.intersect1d(s_lower, s_upper)
#         _t += _t_end
#     else:
#         s_lower = s_t_lower[(s_t_lower[:, 1] <= _t), 0]
#         s_upper = s_t_upper[(s_t_upper[:, 1] >= _t), 0]
#         _s = np.intersect1d(s_lower, s_upper)
#         _t_end = 0

#     while _s.size == 0:
#         if mutation_generation_ago is None:
#             _t = np.random.uniform(t_lower, t_upper, 1).astype(int)
#         else:
#             _t = np.array([mutation_generation_ago])

#             s_lower = s_t_lower[(s_t_lower[:, 1] < _t), 0]
#             s_upper = s_t_lower[(s_t_upper[:, 1] > _t), 0]
#             _s = np.intersect1d(s_lower, s_upper)

#     _s = np.random.uniform(_s.min(), _s.max(), 1).astype(int)[0]

#     return (_t, _t_end, _s)

# def timing_selection_incomplete_sweep(
#     self, i, j, t_lower, t_upper, mutation_generation_ago=None
# ):
#     current_sweep = self.parameters.sweep_class

#     t = []
#     s = []

#     s_t_lower = self.parameters.sweep_diffusion_time[current_sweep][round(i, 1)]
#     s_t_upper = self.parameters.sweep_diffusion_time[current_sweep][
#         round(i + 0.1, 1)
#     ]

#     # We search for the previous diffusion mean value to ensure the condition.
#     # Otherwise the rounded values search for the nearest estimated value and some condition cannot achieve because of the arise time is shorter than expected
#     # Diffusion value are estimated in the range [0:0.05:1]
#     # if j > 0.05:
#     #     _j = round(round(j, 1) - 0.05, 2)
#     # else:
#     _j = j

#     if self.parameters.sweep_class == "soft":
#         s_t_lower = s_t_lower[_j]
#         s_t_upper = s_t_upper[_j]

#     # Minimum number of simulation to achieve current frequency in old sweeps
#     min_gen = s_t_lower[-1, 1]

#     if mutation_generation_ago is None:
#         _t = np.random.uniform(t_upper, t_lower, 1).astype(int)[0]
#     else:
#         _t = mutation_generation_ago

#     if _t <= 2000:
#         max_gen = s_t_lower[s_t_lower[:, 1] < 2000, 1][0]
#     else:
#         max_gen = s_t_lower[(s_t_lower[:, 1] < (t_lower - t_upper))][0, 1]

#     if _t >= 2000:
#         _t = 2000 + min_gen if _t < (2000 + min_gen) else _t
#         # Checking if mutation_generation_ago or random t value is greater than the minimum amount diffusion time estimated
#         # Otherwise there is no s value to achieve f_t at generations 2000.
#         # Reducing t_lower by mutation_generation_ago or random t value in order to obtain t_lower == max(t)

#         _t_end = np.random.choice(np.arange(2000, _t), 1)[0]
#         # while _t - _t_end < min_gen:
#         while (_t - _t_end) < min_gen or (_t - _t_end) > max_gen:
#             _t_end = np.random.choice(np.arange(2000, _t), 1)[0]
#         # print(_t,_t_end,_t - _t_end)

#         s_lower = s_t_lower[s_t_lower[:, 1] <= (_t - _t_end), 0]
#         s_upper = s_t_upper[s_t_upper[:, 1] >= (_t - _t_end), 0]
#         _s = np.intersect1d(s_lower, s_upper)
#     else:
#         _t = min_gen if _t < min_gen else _t

#         s_lower = s_t_lower[(s_t_lower[:, 1] <= _t), 0]
#         s_upper = s_t_upper[(s_t_upper[:, 1] >= _t), 0]
#         _s = np.intersect1d(s_lower, s_upper)
#         _t_end = 0

#     while _s.size == 0:
#         if mutation_generation_ago is None:
#             _t = np.random.uniform(t_lower, t_upper, 1).astype(int)
#         else:
#             _t = np.array([mutation_generation_ago])

#             s_lower = s_t_lower[(s_t_lower[:, 1] < _t), 0]
#             s_upper = s_t_lower[(s_t_upper[:, 1] > _t), 0]
#             _s = np.intersect1d(s_lower, s_upper)

#     _s = np.random.uniform(_s.min(), _s.max(), 1).astype(int)[0]

#     return (_t, _t_end, _s)


# @dataclass
# class parameters:
#     """
#     Create a class container to automatize sweep simulations using stdpopsim.
#     """

#     specie: str
#     region: str
#     genetic_map: str
#     dfe: str
#     demes: str
#     sample: dict
#     contig: stdpopsim.genomes.Contig = None
#     model: stdpopsim.models = None
#     slim_region: dict = None
#     recombination_map: pd.DataFrame = None
#     annotation: str = "exons"
#     f_i: list = field(default_factory=lambda: [0.05, 0.1, 0.15, 0.2])
#     f_t: list = field(default_factory=lambda: np.arange(0.2, 1.1, 0.1))
#     del_dfe: dict = field(default_factory=lambda: {"mean_strength": 0, "shape": 0})
#     proportions: list = field(default_factory=lambda: [0, 0])
#     burn_in: int = 1
#     rescale_factor: int = 1
#     dominance: float = 0.5
#     Ne: int = (1e4,)
#     sweep_diffusion_time: list = field(default_factory=lambda: {"hard": {}, "soft": {}})

#     def diffusion_time_value(self, N, s, f_i, f_t, c=2) -> float:
#         _N = 2 * N
#         s = s / _N
#         result = integrate.quad(
#             lambda x: (
#                 (exp(2 * c * _N * s * x) - 1) * (exp(2 * c * _N * s * (1 - x)) - 1)
#             )
#             / (s * x * (1 - x) * (exp(2 * c * _N * s) - 1)),
#             f_i,
#             f_t,
#         )
#         return result[0]

#     def diffusion_time(self, N):
#         if (
#             len(self.sweep_diffusion_time["hard"]) != 0
#             and list(self.sweep_diffusion_time["hard"].keys()) == self.f_t
#             and len(self.sweep_diffusion_time["soft"]) != 0
#             and list(self.sweep_diffusion_time["soft"].keys()) == self.f_t
#         ):
#             print("Diffusion mean time is estimated")
#         else:
#             func = np.vectorize(self.diffusion_time_value)
#             # Hard sweeps

#             # s_v = np.arange(20,1001,1)
#             # Correcting SLIM 1+s vs diffusion 1+2s on AA
#             s_v = np.arange(10, 1001, 1)
#             for i in self.f_t:
#                 t_fix = func(N, s_v, 1 / (2 * N), i).astype(int)
#                 s_t = np.vstack([s_v, t_fix]).T
#                 self.sweep_diffusion_time["hard"][round(i, 2)] = s_t

#             # Soft sweeps
#             iterables = np.array(list(product(self.f_t, self.f_i)))
#             iterables = iterables[iterables[:, 1] < iterables[:, 0]]

#             for end, start in iterables:
#                 # for (end,start) in tqdm(iterables,desc="Diffusion mean time"):

#                 t_fix = func(N, s_v, start, end).astype(int)
#                 s_t = np.vstack([s_v, t_fix]).T

#                 if round(end, 1) not in self.sweep_diffusion_time["soft"]:
#                     self.sweep_diffusion_time["soft"][round(end, 1)] = {}
#                     self.sweep_diffusion_time["soft"][round(end, 1)].update(
#                         {start: s_t}
#                     )
#                 else:
#                     self.sweep_diffusion_time["soft"][round(end, 1)].update(
#                         {start: s_t}
#                     )

#     def check_stdpopsim(self, return_df=True):
#         out = {}
#         for i in stdpopsim.all_species():
#             tmp_specie = stdpopsim.get_species(i.id)
#             tmp_parameters.models = ", ".join(
#                 [i.id for i in tmp_specie.demographictmp_parameters.models]
#             )
#             tmp_dfes = ", ".join(
#                 [i.id for i in tmp_specie.demographictmp_parameters.models]
#             )
#             tmp_genetic_maps = ", ".join([i.id for i in tmp_specie.genetic_maps])
#             out[i.id] = {
#                 "models": tmptmp_parameters.models,
#                 "genetic_maps": tmp_genetic_maps,
#                 "dfes": tmp_dfes,
#             }

#         print(
#             "\n\nPlease check the available specie and the asociated annotation, dfe and demographic model\n"
#         )
#         if return_df:
#             out = pd.DataFrame(out).T
#         return out

#     def check_parameters(self):
#         assert self.specie in [
#             i.id for i in stdpopsim.all_species()
#         ], "Please select a correct species among the catalog: {}".format(
#             [i.id for i in stdpopsim.all_species()]
#         )
#         assert "yaml" in self.demes or self.demes in np.array(
#             [i.id for i in stdpopsim.all_demographic_models()]
#             + ["PiecewiseConstantSize"]
#         ), "Please select a correct demographic model among the catalog: {}".format(
#             [i.id for i in stdpopsim.all_demographic_models()]
#         )
#         assert (
#             self.annotation == "exons" or self.annotation == "cds"
#         ), "Please select cds or exon annotations"
#         assert (
#             self.dfe == "neutral"
#             or self.dfe == "custom"
#             or self.dfe in [i.id for i in stdpopsim.all_dfes()]
#         ), "Please select cds or exon annotations"

#     def deleterious_dfe(self):
#         muts = [
#             stdpopsim.MutationType(
#                 dominance_coeff=self.dominance,
#                 distribution_type="f",
#                 distribution_args=[0],
#             )
#         ]

#         muts.append(
#             stdpopsim.MutationType(
#                 dominance_coeff=self.dominance,
#                 distribution_type="g",
#                 distribution_args=[self.del_dfe],
#             )
#         )
#         return stdpopsim.DFE(
#             id=self.dfe,
#             description=self.dfe,
#             long_description=self.dfe,
#             mutation_types=muts,
#             proportions=self.proportions,
#         )

#     def neutral_dfe(self):
#         muts = [
#             stdpopsim.MutationType(
#                 dominance_coeff=self.dominance,
#                 distribution_type="f",
#                 distribution_args=[0],
#             )
#         ]
#         return stdpopsim.DFE(
#             id=self.dfe,
#             description=self.dfe,
#             long_description=self.dfe,
#             mutation_types=muts,
#             proportions=[1],
#         )

#     def create_model(self):
#         self.check_parameters()

#         species = stdpopsim.get_species(self.specie)

#         self.Ne = species.population_size

#         # if self.rescale_factor < 10:
#         #     timeout = timeout * 10 / self.rescale_factor
#         # elif self.rescale_factor > 10:
#         #     timeout = timeout * 1 / self.rescale_factor

#         if "yaml" in self.demes:
#             pop_history = demes.load(self.demes)
#             model = msprime.Demography().from_demes(pop_history)
#             model = stdpopsim.DemographicModel(
#                 id=self.demes.split("/")[-1].split(".")[0],
#                 description="custom",
#                 long_description="custom",
#                 model=model,
#             )
#         elif self.demes == "PiecewiseConstantSize":
#             model = stdpopsim.PiecewiseConstantSize(species.population_size)
#             model.generation_time = species.generation_time
#             # Force to sample to pop0 is PiecewiseConstantSize selected
#             sample_tmp = {"pop_0": list(self.sample.values())[0]}
#             self.sample = sample_tmp
#         else:
#             model = species.get_demographic_model(self.demes)

#         if self.annotation == "exons":
#             annotation = 0
#         else:
#             annotation = 1

#         if self.dfe == "neutral":
#             dfe = self.neutral_dfe()
#         elif self.dfe == "deleterious":
#             dfe = deleterious_dfe(
#                 self.dfe,
#                 [self.shape / self.mean_strength, self.shape],
#                 self.proportions,
#             )
#         else:
#             dfe = species.get_dfe(self.dfe)

#         chrom = self.region.split(":")[0]
#         region = list(map(int, self.region.split(":")[1].split("-")))

#         # Need to save original map
#         if self.genetic_map in [i.id for i in species.genetic_maps]:
#             contig = species.get_contig(
#                 chrom,
#                 genetic_map=self.genetic_map,
#                 mutation_rate=model.mutation_rate,
#                 left=region[0],
#                 right=region[1],
#             )

#             _rec_path = str(species.get_genetic_map(self.genetic_map).map_cache_dir)
#             _rec_map = pd.read_csv(
#                 _rec_path + "/" + _rec_path.split("/")[-1] + "_" + chrom + ".txt",
#                 sep=" ",
#             )
#             _rec_map = _rec_map[_rec_map.iloc[:, 0] == chrom]
#             recombination_map = pd.DataFrame(
#                 {
#                     "chrom": chrom,
#                     "id": _rec_map.index,
#                     "genetic": _rec_map.iloc[:, -1],
#                     "physical": _rec_map.iloc[:, 1],
#                 }
#             )

#         elif self.genetic_map.lower() == "uniform":
#             contig = species.get_contig(
#                 chrom,
#                 mutation_rate=model.mutation_rate,
#                 left=region[0],
#                 right=region[1],
#             )
#             recombination_map = None
#         else:
#             contig = species.get_contig(
#                 chrom,
#                 mutation_rate=model.mutation_rate,
#                 left=region[0],
#                 right=region[1],
#             )
#             rate_map = msprime.RateMaparameters.read_hapmap(self.genetic_map)
#             rate_map_sliced = rate_maparameters.slice(
#                 left=region[0], right=region[1], trim=True
#             )
#             contig.recombination_map = rate_map_sliced

#             _rec_map = pd.read_csv(self.genetic_map, sep="\t")
#             _rec_map = _rec_map[_rec_map.iloc[:, 0] == chrom]
#             recombination_map = pd.DataFrame(
#                 {
#                     "chrom": chrom,
#                     "id": _rec_map.index,
#                     "genetic": _rec_map.iloc[:, -1],
#                     "physical": _rec_map.iloc[:, 1],
#                 }
#             )
#         self.recombination_map = recombination_map

#         slim_region = {i: v for (i, v) in enumerate(range(region[0], region[1] + 1))}

#         self.slim_region = slim_region

#         raw_annotation = species.get_annotations(species.annotations[annotation].id)
#         annotations_intervals = raw_annotation.get_chromosome_annotations(chrom)

#         contig.add_dfe(intervals=annotations_intervals, DFE=dfe)

#         if (
#             len(self.sweep_diffusion_time["hard"]) == 0
#             or len(self.sweep_diffusion_time["soft"]) == 0
#         ):
#             logging.info("Solving sweep diffusion times")
#             self.diffusion_time(self.Ne)

#         self.contig = contig
#         self.model = model


# params = parameters(
#     specie="HomSap",
#     region="chr2:135212517-136412517",
#     genetic_map="uniform",
#     dfe="neutral",
#     demes="PiecewiseConstantSize",
#     sample={"AFR": 50},
#     rescale_factor=10,
# )


# class Generator:
#     def __init__(self, parameters):
#         self.parameters = parameters
#         self.model = None
#         self.timing_selection(1)
#         self.timeout = 180

#     def timing_selection(self, f_t, t_lower=5000, t_upper=200):
#         # f_i = np.random.choice(np.hstack([(1 / self.parameters.Ne),self.parameters.f_i]))
#         # f_t = np.random.choice(self.parameters.f_t).round(1)
#         # f_i = 1 / 1e4
#         # f_t = np.random.choice(self.parameters.f_t).round(1)
#         f_i = np.random.choice(self.parameters.f_i).round(1)

#         if f_t - round(f_i, 1) < 0.2:
#             f_t += 0.2

#         if f_t == 1:
#             _t, _s = self.timing_selection_complete_sweep(f_t, f_i, t_lower, t_upper)
#         else:
#             _t, _s = self.timing_selection_incomplete_sweep(f_t, f_i, t_lower, t_upper)

#         if self.parameters.sweep_class == "hard":
#             # Reduce _burn_in but increasing a little bit to avoid problems drawing the mutation
#             _burn_in = ((_t + 1) / self.parameters.Ne).round(2)
#             _burn_in = _burn_in + 0.01
#         else:
#             # Neutral arise 5000 gens ago from selection
#             _burn_in = ((_t + 5001) / self.parameters.Ne).round(2)
#             _burn_in = _burn_in + 0.01

#         self.model = (_s / self.parameters.Ne, _t, f_i, f_t, _burn_in)

#     def timing_selection_complete_sweep(self, i, j, t_lower, t_upper):
#         current_sweep = np.random.choice(["hard", "soft"])

#         t = []
#         s = []
#         # for (i,j) in tqdm(zip(f_t,f_i),total=f_i.size,desc="Sampling uniform t [{0},{1}] and s [{2},{3}]".format(t_lower,t_upper,20,1000)):

#         s_t_lower = self.parameters.sweep_diffusion_time[current_sweep][1]

#         if self.parameters.sweep_class == "soft":
#             s_t_lower = s_t_lower[round(j + 0.01, 1)]

#         _t = np.random.uniform(t_lower, t_upper, 1).astype(int)
#         _s = s_t_lower[(s_t_lower[:, 1] < (_t - t_upper)), 0]

#         while _s.size == 0:
#             _t = np.random.uniform(t_lower, t_upper, 1).astype(int)
#             _s = s_t_lower[(s_t_lower[:, 1] < (_t - t_upper)), 0]

#         _s = np.random.uniform(_s.min(), _s.max(), 1).astype(int)

#         return (_t[0], _s[0])

#     def timing_selection_incomplete_sweep(self, i, j, t_lower, t_upper):
#         current_sweep = np.random.choice(["hard", "soft"])

#         t = []
#         s = []

#         s_t_lower = self.parameters.sweep_diffusion_time[current_sweep][round(i, 1)]
#         s_t_upper = self.parameters.sweep_diffusion_time[current_sweep][
#             round(i + 0.1, 1)
#         ]

#         # We search for the previous diffusion mean value to ensure the condition.
#         # Otherwise the rounded values search for the nearest estimated value and some condition cannot achieve because of the arise time is shorter than expected
#         # Diffusion value are estimated in the range [0:0.05:1]
#         if j > 0.05:
#             _j = round(round(j, 1) - 0.05, 2)
#         else:
#             _j = j

#         if self.parameters.sweep_class == "soft":
#             # Check rounded init frequency not equal or greater than end frequence.
#             # Otherwise change value and array.
#             while _j >= i:
#                 _j = round(np.random.uniform(self.parameters.f_i[0], j), 2)

#                 if _j > 0.05:
#                     _j = round(round(j, 1) - 0.05, 2)

#                 f_i[k] = _j

#             s_t_lower = s_t_lower[_j]
#             s_t_upper = s_t_upper[_j]

#         _t = np.random.uniform(t_lower, t_upper, 1).astype(int)
#         s_lower = s_t_lower[(s_t_lower[:, 1] < _t), 0]
#         s_upper = s_t_lower[(s_t_upper[:, 1] > _t), 0]
#         _s = np.intersect1d(s_lower, s_upper)

#         while _s.size == 0:
#             _t = np.random.uniform(t_lower, t_upper, 1).astype(int)
#             s_lower = s_t_lower[(s_t_lower[:, 1] < _t), 0]
#             s_upper = s_t_lower[(s_t_upper[:, 1] > _t), 0]
#             _s = np.intersect1d(s_lower, s_upper)

#         _s = np.random.uniform(_s.min(), _s.max(), 1).astype(int)

#         return (_t[0], _s[0])

#     def sweep_simulation(self, num_simulations, f_t, t_lower=5000, t_upper=200):
#         results = []
#         self.parameters
#         for _ in range(num_simulations):
#             # Generate simulation
#             ts_sweep, genetic_map, params = self.generate_simulation(
#                 f_t, t_lower, t_upper
#             )

#             if ts_sweep is not None:
#                 results.append((ts_sweep, genetic_map, params))

#         return results

#     def generate_simulation(self, f_t, t_lower=5000, t_upper=200):
#         self.timing_selection(f_t, t_lower, t_upper)

#         tmp_parameters = deepcopy(self.parameters)
#         sweep_class = np.random.choice(["hard", "soft"])

#         (_s, _t, _f_i, _f_t, _burn_in) = self.model

#         # adaptive_position = np.random.randint(1.2e6*0.25,1.2e6*0.75)
#         adaptive_position = sum(tmp_parameters.contig.original_coordinates[1:]) / 2

#         tmp_parameters.contig.add_single_site(
#             id=sweep_class, coordinate=adaptive_position
#         )

#         if sweep_class == "hard":
#             extended_events = stdpopsim.ext.selective_sweep(
#                 single_site_id=sweep_class,
#                 population=list(tmp_parameters.sample.keys())[0],
#                 selection_coeff=_s,
#                 min_freq_at_end=_f_t,
#                 mutation_generation_ago=_t,
#             )
#         else:
#             # start_generation_ago _t + 5000 to ensure the soft sweep achieve the desired freq (up to 0.25)
#             extended_events = stdpopsim.ext.selective_sweep(
#                 single_site_id=sweep_class,
#                 population=list(tmp_parameters.sample.keys())[0],
#                 selection_coeff=_s,
#                 min_freq_at_start=_f_i,
#                 min_freq_at_end=_f_t,
#                 mutation_generation_ago=_t + 5000,
#                 start_generation_ago=_t,
#             )

#             end_condition = stdpopsim.ext.ConditionOnAlleleFrequency(
#                 start_time=_t,
#                 end_time=_t,
#                 single_site_id=sweep_class,
#                 population=list(tmp_parameters.sample)[0],
#                 op="<",
#                 allele_frequency=_f_i + 0.1,
#             )

#             extended_events.append(end_condition)

#         if _f_t != 1:
#             f_step = 0.1 if _f_t == 0.9 else 0.1
#             end_condition = stdpopsim.ext.ConditionOnAlleleFrequency(
#                 start_time=0,
#                 end_time=0,
#                 single_site_id=sweep_class,
#                 population=list(tmp_parameters.sample)[0],
#                 op="<",
#                 allele_frequency=_f_t + 0.1,
#             )

#             extended_events.append(end_condition)

#         engine = stdpopsim.get_engine("slim")

#         with open("/home/jmurgamoreno/test.slim", "w") as f:
#             with redirect_stdout(f):
#                 ts_sweep = engine.simulate(
#                     tmp_parameters.model,
#                     tmp_parameters.contig,
#                     tmp_parameters.sample,
#                     extended_events=extended_events,
#                     slim_scaling_factor=tmp_parameters.rescale_factor,
#                     slim_burn_in=_burn_in,
#                     slim_script=True,
#                     verbosity=0,
#                 )

#         def timeout_handler(signum, frame):
#             raise TimeoutError("Execution timed out")

#         signal.signal(signal.SIGALRM, timeout_handler)
#         signal.alarm(self.timeout)
#         timeout_occurred = False
#         try:
#             ts_sweep = engine.simulate(
#                 tmp_parameters.model,
#                 tmp_parameters.contig,
#                 tmp_parameters.sample,
#                 extended_events=extended_events,
#                 slim_scaling_factor=tmp_parameters.rescale_factor,
#                 slim_burn_in=_burn_in,
#             )
#         except TimeoutError:
#             timeout_occurred = True
#         finally:
#             signal.alarm(0)

#         if timeout_occurred:
#             return (None, None, None)
#         else:
#             if _f_t != 1:
#                 _f_t = frequency(ts_sweep, 6e5)
#             return (
#                 ts_sweep,
#                 self.interpolate_genetic_map(ts_sweep),
#                 np.column_stack([_s, _t, _f_i, _f_t]),
#             )
#             # return np.concatenate(
#             #     [
#             #         np.hstack([_s, _t, _f_i, _f_t]),
#             #         calculate_stats(ts_sweep, self.interpolate_genetic_map(ts_sweep))[
#             #             -1
#             #         ].values.flatten()[44:],
#             #     ]
#             # )

#     def interpolate_genetic_map(self, ts):
#         _coordinates = np.array(
#             [(self.parameters.slim_region[i], i) for i in ts.sites_position]
#         )

#         if self.parameters.recombination_map is None:
#             recombination_hapmap = np.column_stack(
#                 [
#                     np.repeat(1, ts.sites_position.size),
#                     np.arange(1, ts.sites_position.size + 1),
#                     _coordinates[:, 1],
#                     _coordinates[:, 1],
#                 ]
#             )
#         else:
#             f = interp1d(
#                 self.parameters.recombination_map.physical.values,
#                 self.parameters.recombination_map.genetic.values,
#             )
#             recombination_hapmap = np.column_stack(
#                 [
#                     np.repeat(1, ts.sites_position.size),
#                     np.arange(1, ts.sites_position.size + 1),
#                     _coordinates[:, 1],
#                     f(_coordinates[:, 0]),
#                 ]
#             )

#         return recombination_hapmap

#     def update_params(self, parameters):
#         self.model = parameters
