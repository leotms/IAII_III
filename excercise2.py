'''
    File:        excercise2.py
    Description: Defines activities for Excercise 2.
    Authors:     Joel Rivas        #11-10866
                 Nicolas Manan     #06-39883
                 Leonardo Martinez #11-10576
    Updated:     03/17/2017
'''

import pandas as pd
from kmeans import *

def readData(trainset):
    '''
        Reads data inside a .txt file containing the vectors of training/testing data.
        returns the attributes normalized.
    '''

    dataset = pd.read_csv(trainset, delimiter = "," ,header = None,index_col = False)

    #fix the dataset as an array of [x1, x2, x3,..., y]
    aux_dataset = list()
    y = []
    for i in range(len(dataset)):
        row = dataset.iloc[i]
        aux_row = list()
        for j in range(len(row)):
            if (j == len(row) - 1):
                y.append(row[j])
            else:
                aux_row.append(row[j])

        aux_dataset.append(aux_row)

    dataset = aux_dataset

    return dataset, y

def count_data(data):
    ocurrences = {}
    for elem in data:
        if elem in ocurrences:
            ocurrences[elem] += 1
        else:
            ocurrences[elem] = 1

    for ocurrence in ocurrences:
        print("Class %d: %d ocurrences."%(ocurrence, ocurrences[ocurrence]))

def print_result(results):
    iris =  results[0:50]
    versicolor = results[50:100]
    virginica  = results[100:150]

    print("Clasification for Iris-Setosa:")
    count_data(iris)
    print("Clasification for Iris-Versicolor:")
    count_data(versicolor)
    print("Clasification for Iris-Virginica:")
    count_data(virginica)

if __name__ == "__main__":

    X, y = readData('data/iris_dataset.txt')

    # print(y)

    print("Runing Kmeans 3 times each to select the best clustering.")

    for i in range(2, 6):

        print("--- %d CLUSTERS ---"%(i))
        min_J  = -maxsize
        best_c = []

        #Tun k_means several times to find the best custering sets
        for j in range(3):
            c, J, k = k_means(X, i)
            if J > min_J:
                min_J = J
                best_c = c

        print("\nResults with %d clusters\n"%(i))
        print_result(best_c)
        print("----------------------")
