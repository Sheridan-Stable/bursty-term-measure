import scipy
import numpy as np

def get_Ni(collection):
  """
  Input is the vectorized collection
  A vector with all the ni's
  """
  return collection.sum(axis=0)

def get_Nj(collection):
  """
  Input is the vectorized collection
  Output a vector containing all the nj's
  """
  return collection.sum(axis=1)

def get_N(nj_vector):
  """
  Input is the vector containing all the nj's, or the ni's
  Output is the total number of words, including multiplicities (n)
  """
  return nj_vector.sum()

def get_Bij(collection):
  """
  Input is the vectorized collection
  Output is a matrix consisting of all the bij's
  """
  return collection.__gt__(0).astype(int)

def get_Bi(matrix_bij):
  """
  Input is the matrix of all bij's
  Output a vector containing all of the Bi's
  """
  return matrix_bij.sum(axis=0)

def get_Bj(matrix_bij):
  """
  Input is the matrix of all bij's
  Output a vector consisting of all the bj's.
  """
  return matrix_bij.sum(axis=1)

def get_cf(vector_ni):
  """
  Input is the vector containing all ni's, and index i
  Output is a vector of the collection frequency, where cf(i) = ni/n
  """
  return vector_ni/get_N(vector_ni)

def get_df(vector_bi, d):
  """
  Input the vector of all bi's, and the number of docs, d.
  Output a vector of the document frequency, where df(i) = bi/b
  """
  return vector_bi/d

def get_idf(vector_df):
  """
  Input is the vector of all df's
  Output  a vector of the inverse document frequency, where idf(i) = -log(df(i))
  """
  return -np.log(vector_df)

def get_icf(vector_cf):
  """
  Input is a vector containing all of cf's.
  Output a vector of the inverse collection frequency
  """
  return -np.log(vector_cf)

def get_church(vector_ni, vector_bi):
  """
  Input is a vector containig all of ni's, and vector contaning all of bi's.
  Output a vector of the Church and Gale score, where church(i) = ni/bi
  """
  return vector_ni/vector_bi

def get_nij_by_nj(collection, vector_nj):
  """
  Vectorized collection, and the vector containing all nj's.
  Output
  """
  return vector_nj.T*collection

def get_alpha_i(collection, vector_bj, vector_nj):
  """
  Input the vectorized collection, vectorized bj's, and vectorized nj's
  Outpout is a matrix of estimated alpha i's
  """
  bj = scipy.sparse.csr_array(vector_bj)
  nj = scipy.sparse.csr_array(vector_nj)
  col = scipy.sparse.csr_array(collection)
  vect = bj/nj
  return col * vect

def get_mu_alpha_i(matrix_aplha_i, d):
  """
   Input the matrix of alpha i's, and the number of docs, d
   Output is a vector containing all means of alpha i, for all i's
  """
  return (1/d)*matrix_aplha_i.sum(axis=0)

def get_sigma_alpha_i(matrix_alpha_i, vector_mu_alpha_i, d):
  """
  Input the matrix of alpha i's, the vector of mean of alpha i's, and number of docs d
  Output is a vector containing the variance for all the alpha i's
  """
  sigma_matrix = matrix_alpha_i - vector_mu_alpha_i
  sigma_matrix = np.float_power(sigma_matrix, 2)
  return (1/d)*sigma_matrix.sum(axis=0)

def get_matrix_bernoulli(vector_theta, d):
  """
  Input is the vector of probabilities theta and the collection length, d
  Output is a matrix containing 1 - theta for all thetas with d rows
  """
  return np.array([1- vector_theta]*d)

def get_meanBi(vector_theta, vector_nj, d):
  """
  Input vector of theta i's, vector of nj's, and number of docs in collection, d.
  Output a vector containing the means of Bi for all i's.
  """
  phi = np.array([1 - vector_theta,]*d)
  if type(vector_nj) is matrix:
    array_nj = np.concatenate(vector_nj.A, axis=0)
  else:
    array_nj = vector_nj
  powers = np.array([[nj]*len(vector_theta) for nj in array_nj])
  phi = np.float_power(phi, powers)
  return d - phi.sum(axis=0)

def get_varianceBi(vector_nj, matrix_bernoulli):
  """
  Input is a matrix containing 1-theta in every entry, and the vector of nj's
  Output is a vector containig the variances for Bi
  """
  if type(vector_nj) is matrix:
    array_nj = np.concatenate(vector_nj.A, axis=0)
  else:
    array_nj = vector_nj
  powers = np.array([[nj]*len(matrix_bernoulli[0]) for nj in array_nj])
  term2 = np.float_power(matrix_bernoulli, 2*powers)
  term1 = np.float_power(matrix_bernoulli, powers)
  ans = term1 - term2
  return ans.sum(axis=0)

def get_thetas(vector_cf, step):
  """
  Input is a vector of the collection frequencies, and a step
  Output is a vector containing theoretical thetas, all with a step in between
  """
  start = vector_cf.min()
  end = vector_cf.max()
  return np.exp(np.arange(np.log(start), np.log(end), step))

def get_eicf(vector_theta, n):
  """
  Input is a vector of thetas, and the number of terms in the collection, n
  Output is a vector containing the expected icf for each entry i
  """
  return (1-vector_theta)/(2*n*vector_theta) - np.log(vector_theta)

def get_eidf(mean_bi, var_bi, d):
  """
  Input is a vector of all means of bi, a vector of all variances of bi, and constant d
  Output is a vector containing all expected values of idf for any given i
  """
  ans = -np.log(mean_bi) + var_bi/(2*np.float_power(mean_bi, 2)) + math.log(d)
  return np.reshape(ans, (len(mean_bi),))

def get_kwok(ni, n):
  """
  Input: vector of term frequencies, and total term frequency
  Output: vector Kwok word burstiness scores
  """
  return np.log(ni/(n - ni))

def get_irvine(nij_by_nj_vector, vector_bi):
  """
  Input: i index, vector of all bi's,
  Output: Irvine and Callison-Burch score, irvine(i) = 1/bi(get_nij_by_nj(i))
  """
  bi_inverse = np.float_power(vector_bi, -1)
  return np.multiply(bi_inverse, nij_by_nj_vector)

def get_gries(collection, vector_ni, vector_nj, n):
  """
  Input: index i, vectorized collection N.
  Output: the Gries score, where gries(i) = 1-(1/2)*sum_j=1^d(abs(nij/ni - nj/n))
  """
  return 1 - 1/2*abs((collection/vector_ni) - (vector_nj/n)).sum(axis=0)

def get_dm(collection, vector_bj, vector_nj, d):
  """
  Input: index i, vectorized collection, vector of all bj's, vector of all nj's.
  Output: the Dirichlet Multinomial score, where dm(i) = (1/d)*sum_j=1^d(bj*nij/nj)
  """
  vector_dm = np.multiply(vector_bj, np.float_power(vector_nj, -1))
  return (1/d)*(vector_dm.T*collection)

def get_improved_dm(vector_sigma_alpha_i, vector_mu_alpha_i):
  """
  Input: vector of sigma alpha i's and the vector of mean alpha i's
  Output: vector of the improved Dirilecth-Multinomial word burstiness scores
  """
  return vector_sigma_alpha_i/vector_mu_alpha_i


def get_chisq_score(nji):
  """
  Input: array of word in document counts
  Output: vector of Chi-square test word burstiness scores 
  """
  d, m = nji.shape
  ni = word_stats.get_Ni(nji).A[0]
  chisq_values = []

  for i in range(m):
    if type(nji[:, i]) is scipy.sparse._csr.csr_matrix:
      observed = nji[:, i].A.T[0]
    else:
      observed = nji[:, i]
    expected = np.repeat(ni[i] / d, d)
    pvalue = scipy.stats.chisquare(f_obs=observed, f_exp=expected)[1]
    chisq_values.append(pvalue)

  return chisq_values

def get_naive_shms(nji):
  """
  Input: term-in-document matrix
  Output: vector of naive SHMS word burstiness scores
  """
  d, m = nji.shape
  bij = nji.__gt__(0).astype(int)
  
  if type(nji) is scipy.sparse._csr.csr_matrix:
    ni = nji.sum(axis=0).A[0]
    bi = bij.sum(axis=0).A[0]
  else:
    ni = nji.sum(axis=0)
    bi = bij.sum(axis=0)

  n = ni.sum()
  CP = ni/n
  ICF = -np.log(CP)
  EICF = (1 - CP)/(2*n*CP) - np.log(CP)
  CP_baseline = np.arange(start=1, stop=d + 1)/n
  EICF_baseline = (1 - CP_baseline)/(2*n*CP_baseline) - np.log(CP_baseline)
  scores = []

  for i in range(m):
    scores.append(EICF_baseline[bi[i] - 1] - ICF[i])
  
  scores = np.array(scores)
  return scores
