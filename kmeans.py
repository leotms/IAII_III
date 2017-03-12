import numpy  as np
from math import sqrt
from sys import maxsize
from random import random, sample

def calculate_distance(x, y):
    '''
        Calculates distance between two vectors.
    '''

    dist = np.linalg.norm(np.array(x) - np.array(y))
    return float(dist)

def calculate_mean(X):
    '''
        Calculates mean of set of vectors X.
    '''

    mean = []

    if X != []:
        np_array = np.array(X)
        mean = np_array.mean(axis=0).tolist()

    return mean

def random_initialize(X, n):
    '''
        Select a random vector of X for every centroid.
    '''
    k = sample(X,n)

    return k

def cost(X, c, k):

    len_vector = len(X[0])
    n_examples = len(X)

    cost = 0

    for i in range(n_examples):
        cost += (calculate_distance(X[1],k[c[i]]))**2

    return cost/n_examples

def converged(oldk, newk):
    return oldk == newk

def clustering(X,k):
    n_examples = len(X)
    c = np.zeros(n_examples).tolist()

    for i in range(n_examples):
        index = 0
        min_dist = maxsize
        for j in range(0,len(k)):
            if k[j] != []:
                new_min = calculate_distance(X[i],k[j])
                if new_min < min_dist:
                    index = j
                    min_dist = new_min
        c[i] = index

    return c

def rearrange_k(X,c,k):

    clusters = []
    new_k    = []

    #Separate clusters
    for i in range(len(k)):
        clusters.append([])
        new_k.append([])

    for i in range(len(X)):
        clusters[c[i]].append(X[i])

    for i in range(len(k)):
        if k != []:
            new_k[i] = calculate_mean(clusters[i])
            if new_k[i] == []:
                # this means this cluster is empty
                pass
                # print("Cluster %d is empty"%(i))

    return new_k

def k_means(X, n):

    oldk = random_initialize(X, n)

    c = clustering(X, oldk)

    newk = rearrange_k(X,c, oldk)


    j = 1

    while not converged(oldk, newk):
        oldk = newk
        c = clustering(X,oldk)
        newk = rearrange_k(X,c,oldk)
        j += 1

    J = cost(X, c, newk)

    return c, J
