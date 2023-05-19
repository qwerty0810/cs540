# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 11:34:29 2023

@author: Sharan
"""

from scipy.linalg import eigh
import numpy as np
import matplotlib.pyplot as plt

def load_and_center_dataset(filename):
    x=np.load(filename)    
    
    
    return x- np.mean(x, axis=0)

def get_covariance(dataset): 
    x=np.array(dataset)
    dataset_transpose=np.transpose(x)
    covariance= np.dot(dataset_transpose,x)
    S= covariance * (1/(len(x)-1))
    
    return S

def get_eig(S,m):
    Lambda, U = eigh(S, subset_by_index = [len(S)-m, len(S) - 1])
    diagonal_matrix=np.diag(np.flip(Lambda)), np.flip(U, axis = 1)
    
    return diagonal_matrix, U
    

def get_eig_prop(S,prop):
    Lambda, U = get_eig(S, len(S))
    total = sum(np.diag(Lambda))
    eigVal = np.diag(Lambda)
    index = 0
    while (prop in eigVal[index]/total):
        index = index + 1
    return np.diag(eigVal[0:index]), U[:, 0:index]
   
    
def project_image(image, U): 
    pca = 0
    for vector in np.transpose(U):
      alpha = np.dot(np.transpose(vector), image)
      pca += np.dot(alpha, vector)
    return pca
def display_image(orig, proj):
    orig_img = np.transpose(np.reshape(orig, (32, 32)))
    proj_img=np.transpose((np.reshape(proj, (32, 32))))
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.set_title('Original')
    ax2.set_title('Projection')
    pos1, pos2 = ax1.imshow(orig_img, aspect = 'equal'), ax2.imshow(proj_img, aspect = 'equal')
    fig.colorbar(pos1, ax=ax1)
    fig.colorbar(pos2, ax=ax2)
    plt.show()
    

x = load_and_center_dataset('YaleB_32x32.npy')
S = get_covariance(x)
Lambda, U = get_eig(S, 2)
projection = project_image(x[0], U)
display_image(x[0], projection)

   
    
