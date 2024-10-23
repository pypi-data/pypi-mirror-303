import copy, random
import numpy as np
import pandas as pd
import sklearn
import sklearn.linear_model as lm
from sklearn.neighbors import kneighbors_graph
from scipy.sparse import csr_matrix, csc_matrix

CLUSTERING_AGO = 'lv'
SKNETWORK = True
try:
    from sknetwork.clustering import Louvain
except ImportError:
    print('WARNING: sknetwork not installed. GMM will be used for clustering.')
    CLUSTERING_AGO = 'km'
    SKNETWORK = False

