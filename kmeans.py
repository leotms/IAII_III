'''
    File:        kmeans.py
    Description: Defines kmeans algorithm.
    Authors:     Joel Rivas        #11-10866
                 Nicolas Manan     #06-39883
                 Leonardo Martinez #11-10576
    Updated:     03/17/2017
'''

import numpy  as np
from math import sqrt
from sys import maxsize
from random import random, sample, shuffle

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

def random_initialize_alter(X, n, prevcentroids = None):
    '''
        Select a random vector of X for half centroids centroid, using other previous
        centroids as the other half.
    '''

    if prevcentroids:
        n = n - len(prevcentroids)
        k = sample(X,n)
        k = k + prevcentroids
        shuffle(k)
    else:
        k = sample(X,n)

    return k

def cost(X, c, k):
    '''
        Calculates cost function.
    '''
    len_vector = len(X[0])
    n_examples = len(X)

    cost = 0

    for i in range(n_examples):
        cost += (calculate_distance(X[1],k[c[i]]))**2

    return cost/n_examples

def converged(oldk, newk):
    '''
        Rerturns if centroids have converged.
    '''
    return oldk == newk

def clustering(X,k):
    '''
        Performs clustering for X vectors.
    '''
    n_examples = len(X)
    c = np.zeros(n_examples).tolist()

    clusters = []

    #initializing clusters
    for i in range(len(k)):
        clusters.append([])

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
        clusters[index].append(X[i])


    return c, clusters

def rearrange_k(k, clusters):
    '''
        Rearranges centroids to the mean of its clusters.
    '''
    new_k    = []

    #Initializate new k
    for i in range(len(k)):
        new_k.append([])

    for i in range(len(k)):
        if k != []:
            new_k[i] = calculate_mean(clusters[i])
            if new_k[i] == []:
                pass

    return new_k

def k_means(X, n):
    '''
        Performs kmeans using random initialization for all centroids.
    '''
    oldk = random_initialize(X, n)

    c, clusters = clustering(X, oldk)

    newk = rearrange_k(oldk, clusters)


    j = 1

    while not converged(oldk, newk):
        oldk = newk
        c, clusters = clustering(X, oldk)
        newk = rearrange_k(oldk, clusters)
        j += 1

    print("Total iterations for kmeans: %d"%(j))

    J = cost(X, c, newk)

    return c, J, newk

def k_means_alter(X, n, prevcentroids):
    '''
        Calculates kmeans using random initialization for only for half centroids.
    '''
    oldk = random_initialize_alter(X, n, prevcentroids)

    c, clusters = clustering(X, oldk)

    newk = rearrange_k(oldk, clusters)

    j = 1

    while not converged(oldk, newk):
        oldk = newk
        c, clusters = clustering(X, oldk)
        newk = rearrange_k(oldk, clusters)
        j += 1

    print("Total iterations for kmeans: %d"%(j))

    J = cost(X, c, newk)

    return c, J, newk
