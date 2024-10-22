
hap_file_name = "Flex-sweep/flex-sweep/calculate_stats/sweep_data_1_c600000_full.hap.gz"
pos_file_name = "Flex-sweep/flex-sweep/calculate_stats/sweep_data_1_c600000_full.map.gz"

def read_hapmap(hap_file_name,pos_file_name):

	hap = []
	pos = pd.read_csv(pos_file_name,sep=' ',header=None)

	with open(hap_file_name, 'rt') as hap_file:
		for variants in hap_file:
			hap.append(np.array(list(variants.strip())))

	hap = np.vstack(hap).astype(np.int8)

	return(hap,pos.iloc[:,-1])

def dind_og(hap_file_name,pos_file_name):  
	data = list()
	with gzip.open(hap_file_name, 'rt') as hap_file:
		with gzip.open(pos_file_name, 'rt') as pos_file:        
			for info, variants in zip(pos_file, hap_file):
				chrom, lab, gen_pos, phys_pos = info.split()
				ba = bitarray(variants.strip())
				data.append((int(gen_pos), int(phys_pos), ba))

	window_size     = 50000
	max_ancest_freq = 0.25
	min_tot_freq    = 0
	min_focal_freq  = 0.25
	max_focal_freq  = 0.95
	
	results = list()
	out = list()
	for k, (phys_pos, gen_pos, ba) in enumerate(data):

		# gen_pos is same as phys_pos unless a recombination map is provided
		freq = ba.count() / len(ba)
		if freq < min_focal_freq or freq > max_focal_freq:
			continue

		gen_dist = False
		a2,b2 = sq_freq_pairs(data, k, 0, window_size/2, max_ancest_freq, min_tot_freq, gen_dist)
		c2,d2 = sq_freq_pairs(data, k, len(data), window_size/2, max_ancest_freq, min_tot_freq, gen_dist)
		sq_freqs = a2+c2

		if len(b2) == 0:
			b = [0,0]
		if len(d2) == 0:
			d=[0,0]
		tmp = (b2[::-1][0],b2[::-1][-1],d2[0],d2[-1])

		if sq_freqs:
			num = sum(x - x + y for x,y in sq_freqs)
			den = sum(y - y + x for x,y in sq_freqs) + 0.001
			hapdaf = num / den
			results.append((k,hapdaf, freq))
			out.append(tmp)

	return(np.array(results),np.array(out))

def sq_freq_pairs(lst, pos, end, size, max_ancest_freq, min_tot_freq, gen_dist=False):
	"""
	Computes pairs of squared freqencies of derived variants to the
	left or right of the focal SNP. Called twice for each focal SNP.
	"""
	focal_pos, focal_gen_pos, focal_deriv = lst[pos]
	focal_ancest = ~focal_deriv
	# focal_deriv &= mask
	# focal_ancest &= mask
	focal_deriv_count = focal_deriv.count()
	focal_ancest_count = focal_ancest.count()
	
	f_vals = list()        
	positions = pos < end and range(pos+1, end) or range(pos-1, end-1, -1)
	# print(positions)
	tmp = []
	for p in positions:
		deriv_pos, deriv_gen_pos, deriv = lst[p]

		if gen_dist and abs(focal_gen_pos - deriv_gen_pos) > size:
			break
		if not gen_dist and abs(focal_pos - deriv_pos) > size:
			break
				
		f_d = (focal_deriv & deriv).count() / focal_deriv_count
		f_a = (focal_ancest & deriv).count() / focal_ancest_count
		f_tot = deriv.count() / len(deriv)
		f_d2 = f_d * (1 - f_d) * focal_deriv_count / (focal_deriv_count - 1)
		f_a2 = f_a * (1 - f_a) * focal_ancest_count / (focal_ancest_count- 1 + 0.001)
		tmp.append(p)
		f_vals.append((f_d2,f_a2))

	return (f_vals,tmp)

def lowfreq_og(hap_file_name,pos_file_name):  
	data = list()
	with gzip.open(hap_file_name, 'rt') as hap_file:
		with gzip.open(pos_file_name, 'rt') as pos_file:        
			for info, variants in zip(pos_file, hap_file):
				chrom, lab, gen_pos, phys_pos = info.split()
				ba = bitarray(variants.strip())
				data.append((int(gen_pos), int(phys_pos), ba))

	window_size     = 50000
	max_ancest_freq = 0.25
	min_tot_freq    = 0
	min_focal_freq  = 0.25
	max_focal_freq  = 0.95


	def sq_freq_pairs(lst, pos, end, size, max_ancest_freq, min_tot_freq, gen_dist=False):
		"""
		Computes pairs of squared freqencies of derived variants to the
		left or right of the focal SNP. Called twice for each focal SNP.
		"""
		focal_pos, focal_gen_pos, focal_deriv = lst[pos]
		focal_ancest = ~focal_deriv
		# focal_deriv &= mask
		# focal_ancest &= mask
		focal_deriv_count = focal_deriv.count()
		focal_ancest_count = focal_ancest.count()
		
		f_vals = list()        
		positions = pos < end and range(pos+1, end) or range(pos-1, end-1, -1)
		for i in positions:
			deriv_pos, deriv_gen_pos, deriv = lst[i]
			# deriv &= mask

			if gen_dist and abs(focal_gen_pos - deriv_gen_pos) > size:
				break
			if not gen_dist and abs(focal_pos - deriv_pos) > size:
				break
					
			f_d = (focal_deriv & deriv).count() / focal_deriv_count
			f_a = (focal_ancest & deriv).count() / focal_ancest_count

			f_tot = deriv.count() / len(deriv)
			f_diff = 1 - f_d
			if f_d < max_ancest_freq:
				f_vals.append((f_diff**2))

				#print(f_tot,f_d,f_a)
		return f_vals

	results = list()
	for i, (phys_pos, gen_pos, ba) in enumerate(data):
		# gen_pos is same as phys_pos unless a recombination map is provided

	#    freq = ba.count() / ba.length()
		freq = ba.count() / len(ba)
		if freq < min_focal_freq or freq > max_focal_freq:
			continue


		gen_dist = False
		sq_freqs = sq_freq_pairs(data, i, 0, window_size/2, max_ancest_freq, min_tot_freq, gen_dist) + \
			sq_freq_pairs(data, i, len(data), window_size/2, max_ancest_freq, min_tot_freq, gen_dist)
		#print(freq)

		if sq_freqs:
			hapdaf = sum( x for x in sq_freqs) / len(sq_freqs)
			results.append((i, hapdaf, freq))
		
	return(np.array(results))

def highfreq_og(hap_file_name,pos_file_name):  
	data = list()
	with gzip.open(hap_file_name, 'rt') as hap_file:
		with gzip.open(pos_file_name, 'rt') as pos_file:        
			for info, variants in zip(pos_file, hap_file):
				chrom, lab, gen_pos, phys_pos = info.split()
				ba = bitarray(variants.strip())
				data.append((int(gen_pos), int(phys_pos), ba))

	window_size     = 50000
	max_ancest_freq = 0.25
	min_tot_freq    = 0
	min_focal_freq  = 0.25
	max_focal_freq  = 0.95

	def sq_freq_pairs(lst, pos, end, size, max_ancest_freq, min_tot_freq, gen_dist=False):
		"""
		Computes pairs of squared freqencies of derived variants to the
		left or right of the focal SNP. Called twice for each focal SNP.
		"""
		focal_pos, focal_gen_pos, focal_deriv = lst[pos]
		focal_ancest = ~focal_deriv
		# focal_deriv &= mask
		# focal_ancest &= mask
		focal_deriv_count = focal_deriv.count()
		focal_ancest_count = focal_ancest.count()
		
		f_vals = list()        
		positions = pos < end and range(pos+1, end) or range(pos-1, end-1, -1)
		for i in positions:
			deriv_pos, deriv_gen_pos, deriv = lst[i]
			# deriv &= mask

			if gen_dist and abs(focal_gen_pos - deriv_gen_pos) > size:
				break
			if not gen_dist and abs(focal_pos - deriv_pos) > size:
				break

			f_d = (focal_deriv & deriv).count() / focal_deriv_count
			f_a = (focal_ancest & deriv).count() / focal_ancest_count
			f_tot = deriv.count() / len(deriv)
			f_diff = f_d
			if f_d > max_ancest_freq:

				f_vals.append((f_diff**2))

		return f_vals

	results = list()
	for i, (phys_pos, gen_pos, ba) in enumerate(data):
		# gen_pos is same as phys_pos unless a recombination map is provided

	#    freq = ba.count() / ba.length()
		freq = ba.count() / len(ba)
		if freq < min_focal_freq or freq > max_focal_freq:
			continue

		#print(freq)

		gen_dist = False
		sq_freqs = sq_freq_pairs(data, i, 0, window_size/2, max_ancest_freq, min_tot_freq, gen_dist) + \
			sq_freq_pairs(data, i, len(data), window_size/2, max_ancest_freq, min_tot_freq, gen_dist)

		if sq_freqs:
			hapdaf = sum( x for x in sq_freqs) / len(sq_freqs)
			results.append((i, hapdaf, freq))
		
	return(np.array(results))

def sratio_og(hap_file_name,pos_file_name):  
	data = list()
	with gzip.open(hap_file_name, 'rt') as hap_file:
		with gzip.open(pos_file_name, 'rt') as pos_file:        
			for info, variants in zip(pos_file, hap_file):
				chrom, lab, gen_pos, phys_pos = info.split()
				ba = bitarray(variants.strip())
				data.append((int(gen_pos), int(phys_pos), ba))

	window_size     = 50000
	max_ancest_freq = 0.25
	min_tot_freq    = 0
	min_focal_freq  = 0.25
	max_focal_freq  = 0.95


	def sq_freq_pairs(lst, pos, end, size, max_ancest_freq, min_tot_freq, gen_dist=False):
		"""
		Computes pairs of squared freqencies of derived variants to the
		left or right of the focal SNP. Called twice for each focal SNP.
		"""
		focal_pos, focal_gen_pos, focal_deriv = lst[pos]
		focal_ancest = ~focal_deriv
		# focal_deriv &= mask
		# focal_ancest &= mask
		focal_deriv_count = focal_deriv.count()
		focal_ancest_count = focal_ancest.count()
		
		f_vals = list()        
		positions = pos < end and range(pos+1, end) or range(pos-1, end-1, -1)
		for i in positions:
			deriv_pos, deriv_gen_pos, deriv = lst[i]
			# deriv &= mask

			if gen_dist and abs(focal_gen_pos - deriv_gen_pos) > size:
				break
			if not gen_dist and abs(focal_pos - deriv_pos) > size:
				break
					
			f_d = (focal_deriv & deriv).count() / focal_deriv_count
			f_a = (focal_ancest & deriv).count() / focal_ancest_count

			f_tot = deriv.count() / len(deriv)

			f_d2 = 0
			f_a2 = 0

			if f_d > 0.0000001 and f_d < 1:
				f_d2 = 1

			if f_a > 0.0000001 and f_a < 1:
				f_a2 = 1
				
			f_vals.append((f_d2,f_a2))

				#print(f_tot,f_d,f_a)
		return f_vals

	results = list()
	for i, (phys_pos, gen_pos, ba) in enumerate(data):
		# gen_pos is same as phys_pos unless a recombination map is provided

	#    freq = ba.count() / ba.length()
		freq = ba.count() / len(ba)
		if freq < min_focal_freq or freq > max_focal_freq:
			continue

		#print(freq)

		gen_dist = False
		sq_freqs = sq_freq_pairs(data, i, 0, window_size/2, max_ancest_freq, min_tot_freq, gen_dist) + \
			sq_freq_pairs(data, i, len(data), window_size/2, max_ancest_freq, min_tot_freq, gen_dist)

		if sq_freqs:


			num = sum(x - x + y + 1 for x,y in sq_freqs)
			den = sum(y - y + x + 1 for x,y in sq_freqs) # redefine to add one to get rid of blowup issue introduced by adding 0.001 to denominator

			hapdaf = num / den
			results.append((i, hapdaf, freq))
	
	return(np.array(results))

def hapdaf_o_og(hap_file_name,pos_file_name):  
	data = list()
	with gzip.open(hap_file_name, 'rt') as hap_file:
		with gzip.open(pos_file_name, 'rt') as pos_file:        
			for info, variants in zip(pos_file, hap_file):
				chrom, lab, gen_pos, phys_pos = info.split()
				ba = bitarray(variants.strip())
				data.append((int(gen_pos), int(phys_pos), ba))

	window_size     = 50000
	max_ancest_freq = 0.25
	min_tot_freq    = 0
	min_focal_freq  = 0.25
	max_focal_freq  = 0.95


	def sq_freq_pairs(lst, pos, end, size, max_ancest_freq, min_tot_freq, gen_dist=False):
		"""
		Computes pairs of squared freqencies of derived variants to the
		left or right of the focal SNP. Called twice for each focal SNP.
		"""
		focal_pos, focal_gen_pos, focal_deriv = lst[pos]
		focal_ancest = ~focal_deriv
		# focal_deriv &= mask
		# focal_ancest &= mask
		focal_deriv_count = focal_deriv.count()
		focal_ancest_count = focal_ancest.count()
		
		f_vals = list()        
		positions = pos < end and range(pos+1, end) or range(pos-1, end-1, -1)
		for i in positions:
			deriv_pos, deriv_gen_pos, deriv = lst[i]
			# deriv &= mask

			if gen_dist and abs(focal_gen_pos - deriv_gen_pos) > size:
				break
			if not gen_dist and abs(focal_pos - deriv_pos) > size:
				break
					
			f_d = (focal_deriv & deriv).count() / focal_deriv_count
			f_a = (focal_ancest & deriv).count() / focal_ancest_count
			f_tot = deriv.count() / len(deriv)
			
			if f_d > f_a and f_a <= max_ancest_freq and f_tot >= min_tot_freq:
				f_vals.append((f_d**2, f_a**2))

		return f_vals

	results = list()
	for i, (phys_pos, gen_pos, ba) in enumerate(data):
		# gen_pos is same as phys_pos unless a recombination map is provided

		freq = ba.count() / len(ba)
		if freq < min_focal_freq or freq > max_focal_freq:
			continue

		#print(freq)

		gen_dist = False
		sq_freqs = sq_freq_pairs(data, i, 0, window_size/2, max_ancest_freq, min_tot_freq, gen_dist) + \
			sq_freq_pairs(data, i, len(data), window_size/2, max_ancest_freq, min_tot_freq, gen_dist)
		if i ==6:
			break

		if sq_freqs:
			hapdaf = sum(x - y for x, y in sq_freqs) / len(sq_freqs)

			results.append((i, hapdaf, freq))

	return(np.array(results))

def hapdaf_s_og(hap_file_name,pos_file_name):  
	data = list()
	with gzip.open(hap_file_name, 'rt') as hap_file:
		with gzip.open(pos_file_name, 'rt') as pos_file:        
			for info, variants in zip(pos_file, hap_file):
				chrom, lab, gen_pos, phys_pos = info.split()
				ba = bitarray(variants.strip())
				data.append((int(gen_pos), int(phys_pos), ba))

	window_size     = 50000
	max_ancest_freq = 0.25
	min_tot_freq    = 0
	min_focal_freq  = 0.25
	max_focal_freq  = 0.95


	def sq_freq_pairs(lst, pos, end, size, max_ancest_freq, min_tot_freq, gen_dist=False):
		"""
		Computes pairs of squared freqencies of derived variants to the
		left or right of the focal SNP. Called twice for each focal SNP.
		"""
		focal_pos, focal_gen_pos, focal_deriv = lst[pos]
		focal_ancest = ~focal_deriv
		# focal_deriv &= mask
		# focal_ancest &= mask
		focal_deriv_count = focal_deriv.count()
		focal_ancest_count = focal_ancest.count()
		
		f_vals = list()        
		positions = pos < end and range(pos+1, end) or range(pos-1, end-1, -1)
		for i in positions:
			deriv_pos, deriv_gen_pos, deriv = lst[i]
			# deriv &= mask

			if gen_dist and abs(focal_gen_pos - deriv_gen_pos) > size:
				break
			if not gen_dist and abs(focal_pos - deriv_pos) > size:
				break
					
			f_d = (focal_deriv & deriv).count() / focal_deriv_count
			f_a = (focal_ancest & deriv).count() / focal_ancest_count
			f_tot = deriv.count() / len(deriv)
			
			if f_d > f_a and f_a <= max_ancest_freq and f_tot >= min_tot_freq:
				f_vals.append((f_d**2, f_a**2))

		return f_vals

	results = list()
	for i, (phys_pos, gen_pos, ba) in enumerate(data):
		# gen_pos is same as phys_pos unless a recombination map is provided

		freq = ba.count() / len(ba)
		if freq < min_focal_freq or freq > max_focal_freq:
			continue

		#print(freq)

		gen_dist = False
		sq_freqs = sq_freq_pairs(data, i, 0, window_size/2, max_ancest_freq, min_tot_freq, gen_dist) + \
			sq_freq_pairs(data, i, len(data), window_size/2, max_ancest_freq, min_tot_freq, gen_dist)
		if i ==6:
			break

		if sq_freqs:
			hapdaf = sum(x - y for x, y in sq_freqs) / len(sq_freqs)

			results.append((i, hapdaf, freq))

	return(np.array(results))



%time x = dind_og("Flex-sweep/FlexABC/data/sweep_data_1_c600000_full.hap.gz","Flex-sweep/FlexABC/data/sweep_data_1_c600000_full.map.gz")
%time y = s_ratio(hap,ac,rec_map)


##################

def complete_timing(params,f_i,f_t,t_lower,t_upper):
	
	current_sweep = '_'.join([params.sweep_class,params.sweep_status])

	t = []
	s = []
	for (start,end) in zip(f_i,f_t):

		if params.sweep_class == 'soft':
			k = start
		else:
			k = end

		s_t_lower = params.sweep_diffusion_time[current_sweep][k.round(1)]

		_t = np.random.uniform(t_lower,t_upper,1).astype(int)
		_s = s_t_lower[(s_t_lower[:,1] < (_t - t_upper)),0]

		while _s.size == 0:
			_t = np.random.uniform(t_lower,t_upper,1).astype(int)
			_s = s_t_lower[(s_t_lower[:,1] < (_t - t_upper)),0]

		_s = np.random.uniform(_s.min(),_s.max(),1).astype(int)

		t.append(_t)
		s.append(_s)

	t = np.hstack(t)
	s = np.hstack(s)
	return(t,s)

	if params.sweep_status == 'complete':
		f_t = np.repeat(1,replicas)

		t = []
		s = []
		for (i,j) in zip(f_t,f_i):
			
			s_t_lower = params.sweep_diffusion_time[current_sweep][1]
			
			if params.sweep_class == 'soft':
				s_t_lower = s_t_lower[round(j+0.01,1)]

			_t = np.random.uniform(t_lower,t_upper,1).astype(int)
			_s = s_t_lower[(s_t_lower[:,1] < (_t - t_upper)),0]

			while _s.size == 0:
				_t = np.random.uniform(t_lower,t_upper,1).astype(int)
				_s = s_t_lower[(s_t_lower[:,1] < (_t - t_upper)),0]

			_s = np.random.uniform(_s.min(),_s.max(),1).astype(int)

			t.append(_t)
			s.append(_s)

		t = np.hstack(t)
		s = np.hstack(s)
	else:
		f_t = np.random.uniform(0.8, 0.9,replicas).round(1)

		t = []
		s = []

		for (i,j) in zip(f_t,f_i):
			s_t_lower = params.sweep_diffusion_time[current_sweep][round(i,1)]
			s_t_upper = params.sweep_diffusion_time[current_sweep][round(i+0.1,1)]

			# k = np.array(list(s_t_lower.keys()))

			if params.sweep_class == 'soft':
				try:
					s_t_lower = s_t_lower[round(j,1)]
					s_t_upper = s_t_upper[round(j,1)]
				except:
					s_t_lower = s_t_lower[j]
					s_t_upper = s_t_upper[j]

			_t = np.random.uniform(t_lower,t_upper,1).astype(int)
			s_lower = s_t_lower[(s_t_lower[:,1] < _t),0]
			s_upper = s_t_lower[(s_t_upper[:,1] > _t),0]
			_s = np.intersect1d(s_lower,s_upper)
			
			while _s.size == 0:
				_t = np.random.uniform(t_lower,t_upper,1).astype(int)
				s_lower = s_t_lower[(s_t_lower[:,1] < _t),0]
				s_upper = s_t_lower[(s_t_upper[:,1] > _t),0]
				_s = np.intersect1d(s_lower,s_upper)

			_s = np.random.uniform(_s.min(),_s.max(),1).astype(int)

			t.append(_t)
			s.append(_s)

		t = np.hstack(t)
		s = np.hstack(s)


def diffusion_time_v2(self,N):
	"""
	Approximate mean diffusion time
	F mininum sweep frequency
	"""
	func = np.vectorize(self.diffusion_time_value)

	s_v = np.arange(20,1001,1)
	
	if self.sweep_class == 'soft':
		f_start = self.f_i
	else:
		f_start = 1/(2*N)

	if self.sweep_status == 'complete' and self.sweep_class == 'hard':
		print("Diffusion mean time")
		t_fix   = func(N,s_v,1/(2*N),1).astype(int)
		s_t = np.vstack([s_v,t_fix]).T
		self.sweep_diffusion_time['hard_complete'][1] = s_t
	elif self.sweep_status == 'incomplete' and self.sweep_class == 'hard':
		for i in tqdm(self.f_t,desc="Diffusion mean time"):
			t_fix   = func(N,s_v,1/(2*N),i).astype(int)
			s_t = np.vstack([s_v,t_fix]).T
			self.sweep_diffusion_time['hard_incomplete'][i] = s_t
	elif self.sweep_status == 'complete' and self.sweep_class == 'soft':
		for i in tqdm(f_start,desc="Diffusion mean time"):
			t_fix   = func(N,s_v,i,1).astype(int)
			s_t = np.vstack([s_v,t_fix]).T
			self.sweep_diffusion_time['soft_complete'][i] = s_t

	elif self.sweep_status == 'incomplete' and self.sweep_class == 'soft':
		iterables = np.array(list(product(self.f_t,self.f_i)))
		iterables = iterables[iterables[:,1] < iterables[:,0]]
		for (end,start) in tqdm(iterables,desc="Diffusion mean time"):

			t_fix = func(N,s_v,start,end).astype(int)
			s_t = np.vstack([s_v,t_fix]).T

			if round(end,1) not in self.sweep_diffusion_time['soft_incomplete']:
				self.sweep_diffusion_time['soft_incomplete'][round(end,1)] = {}
				self.sweep_diffusion_time['soft_incomplete'][round(end,1)].update({start:s_t})
			else:
				self.sweep_diffusion_time['soft_incomplete'][round(end,1)].update({start:s_t})

def msprime_recmap_to_hapmap(contig,_rec_map):
	
	# contig = species.get_contig('chr2', genetic_map=params.genetic_map, mutation_rate=model.mutation_rate)
	chrom,start,end = contig.original_coordinates
	current_rec_map = contig.recombination_map
	cm_mb = current_rec_map.rate*1e6*100

	physical_position    = _rec_map.position
	genetic_position     =  np.insert(np.nancumsum(_rec_map.mass), 0, 0)
	genetic_position = genetic_position[(physical_position >= (start-1)) & (physical_position <= end)]

	np_chrom = np.repeat(int(chrom.replace('chr','')),cm_mb.size)
	
	if cm_mb.size == 1:
		cm_mb = np.insert(cm_mb,0,0)
		physical_position = np.insert(physical_position,0,0)
		genetic_position = np.insert(genetic_position,0,0)
		np_chrom = np.insert(np_chrom,0,np_chrom[0])

	recombination_hapmap = pd.DataFrame({'chrom':np_chrom,'pos':current_rec_map.position,'cM_MB':cm_mb,'CM':genetic_position}).infer_objects()
	recombination_hapmap.fillna(0,inplace=True)

	return(recombination_hapmap)


def mean_fixation_time(N,s,c=2):
	return (2*np.log(c*N - 1)) / s

def s_mean_fixation_time(N,t,c=2):
	return (2*np.log(c*N - 1)) / t

def s_limits(sweep_timing,sweep_status,N,replicas):
	# Define s range based on time and status.
	# Sweep cannot be young and complete unless s > s'
	# Sweep cannot be old and incomplete unless s < s'
	if (sweep_timing == 'young') and (sweep_status == 'complete'):
		s = np.random.uniform(600,1000,replicas)/(2*N)
	elif (sweep_timing == 'young') & (sweep_status == 'incomplete'):
		s = np.random.uniform(20,1000,replicas)/(2*N)
	elif (sweep_timing == 'old') and (sweep_status == 'complete'):
		s = np.random.uniform(20,400,replicas)/(2*N)
	elif (sweep_timing == 'old') and (sweep_status == 'incomplete'):
		s = np.random.uniform(20,40,replicas)/(2*N)

	s = s.round(5)

	return(s)

def conditioning_limits_by_t(N,s,s_t,t_max,t_min):
	# Define s range based on time .
	# Sweep cannot be young and complete unless s > s'
	# Sweep cannot be old and complete unless s < s'
	## CHECK INCOMPLETE!
	
	
	return(s)

def conditioning_limits_by_s(N,s,s_t,t_max,t_min):
	# Define s range based on time .
	# Sweep cannot be young and complete unless s > s'
	# Sweep cannot be old and complete unless s < s'
	## CHECK INCOMPLETE!

	t = []
	for j in range(s.size):

		# Subset mean to f given a random s value
		t_fix = s_t[s_t[:,0]==s[j],1][0]
		# t_fix = (t_fix * 0.25) + t_fix
		if t_fix < t_min:
			t_fix = t_min
		_t = np.random.uniform(t_max,t_fix)
		t.append(_t)
	
	t = np.array(t).astype(int)
	
	return(t)


####################
import stdpopsim
import pyslim

species = stdpopsim.get_species("HomSap")
model   = stdpopsim.PiecewiseConstantSize(int(1e4))
# Samples = current Ne
samples = {i.name: int(i.initial_size) for i in model.populations}

contig = species.get_contig("chr2", right=int(1e6))

engine = stdpopsim.get_engine("msprime")
ts  = engine.simulate(model, contig, samples,msprime_model='dtwf')
ts_anc = ts.delete_sites(ts.mutations_site)

ts_anc = pyslim.annotate(ts_anc, model_type="WF", tick=1, stage="late")

ts_anc.dump("/home/murgamoreno/neut.tree")

#################################
locus_id = "hard_sweep"
coordinate = round(135812517)
contig.add_single_site(
	id=locus_id,
	coordinate=coordinate)


end_condition = stdpopsim.ext.ConditionOnAlleleFrequency(start_time=0,end_time=0,single_site_id=locus_id,population='AFR',op='<=',allele_frequency=0.8)


engine = stdpopsim.get_engine("slim")

%time ts_sweep = engine.simulate(model,contig,samples,extended_events=extended_events,slim_scaling_factor=10,slim_burn_in=10)

replicas = 10
N = species.population_size
f_i      = np.random.uniform(1/N,0.1,replicas).astype(int)
t_old    = np.random.uniform(2000,5000,replicas).astype(int)
t_young = np.random.uniform(0,2000,replicas).astype(int)
s       = np.random.uniform(20,200,replicas)/(2*species.population_size)


sims = []
for (i,j) in zip(t_old,s):
	extended_events = stdpopsim.ext.selective_sweep(single_site_id=locus_id,population="AFR",selection_coeff=j,min_freq_at_end=1,mutation_generation_ago=i)
	params = (model,contig,samples,extended_events)
	sims.append(params)

engine = stdpopsim.get_engine("msprime")

ts_neutral = engine.simulate(model,contig,samples)



# extended_events.append(end_condition)

with open("/home/murgamoreno/hard_sweep.slim", "w") as f:
	with redirect_stdout(f):
		ts_sweep = engine.simulate(
			model,
			contig,
			samples,
			extended_events=extended_events,
			slim_scaling_factor=10,
			slim_burn_in=10,
			slim_script=True,
			verbosity=0,
		)

		
