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

if __name__ == "__main__":

    X, y = readData('data/iris_dataset.txt')

    # print(y)

    for i in range(2, 6):
        min_J  = -maxsize
        best_c = []

        #Tun k_means several times to find the best custering sets
        for j in range(100):
            c, J = k_means(X, i)
            if J > min_J:
                min_J = J
                best_c = c

        print("Asignacion para %d clusters"%(i))
        print(best_c)
