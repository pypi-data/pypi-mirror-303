import warnings, math, time, copy, random, os
from contextlib import redirect_stdout, redirect_stderr
import logging, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import cluster, mixture
from sklearn.neighbors import kneighbors_graph
from sklearn.decomposition import PCA, IncrementalPCA, TruncatedSVD
from scipy import stats
from scipy.sparse import csr_matrix, csc_matrix
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neighbors import NearestNeighbors
import sklearn.linear_model as lm
import anndata
from scipy.signal import medfilt

from scoda.clustering import get_neighbors, clustering_alg, merge_clusters_with_seed
from scoda.clustering import get_cluster_lst_and_sizes, get_cluster_adj_mat_from_adj_dist
from scoda.clustering import initially_detect_major_clusters, convert_adj_mat_dist_to_conn
from scoda.clustering import clustering_subsample, get_normalized_agg_adj_mat

CLUSTERING_AGO = 'lv'
SKNETWORK = True
try:
    from sknetwork.clustering import Louvain
except ImportError:
    print('WARNING: sknetwork not installed. GMM will be used for clustering.')
    CLUSTERING_AGO = 'gm'
    SKNETWORK = False

INFERCNVPY = True
try:
    import infercnvpy as cnv
except ImportError:
    print('ERROR: infercnvpy not installed. Tumor cell identification will not be performed.')
    INFERCNVPY = False

#'''
UMAP_INSTALLED = True
try:
    import umap
except ImportError:
    print('WARNING: umap-learn not installed.')
    UMAP_INSTALLED = False
#'''

MIN_ABS_VALUE = 1e-8

