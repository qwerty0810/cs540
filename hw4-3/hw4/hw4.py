# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 17:37:35 2023

@author: Sharan
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram

def load_data(filepath):
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]
def calc_features(row):
    x1 = int(row["Attack"])
    x2 = int(row["Sp. Atk"])
    x3 = int(row["Speed"])
    x4 = int(row["Defense"])
    x5 = int(row["Sp. Def"])
    x6 = int(row["HP"])
    features = np.array([x1, x2, x3, x4, x5, x6], dtype=np.int64)
    return features
    
def hac(features):
    pairwise_distances = squareform(pdist(features, metric='euclidean'))
    linkage_matrix = linkage(pairwise_distances, method='complete')
    cluster_sizes = np.zeros((len(features),), dtype=int)
    cluster_sizes[:len(features)] = 1
    for i in range(len(cluster_sizes)-1):
        left, right = int(linkage_matrix[i, 0]), int(linkage_matrix[i, 1])
        cluster_sizes[left] += cluster_sizes[right]
    return np.column_stack((linkage_matrix, cluster_sizes[linkage_matrix[:, 0].astype(int)]))
    
    
def imshow_hac(Z, names):
    plt.figure(figsize=(15, 5))
    dendrogram(Z, labels=names, leaf_rotation=90)
    plt.show()
    
