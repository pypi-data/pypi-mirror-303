"""
Import graph data
Calculate Gaussian similarity
Calculate sigmoid similarity
Fuse similarity
Import node walker sampling information
Import node ST sampling information
Calculate Euclidean distance
"""
import csv
import os
import torch as t
import numpy as np
from math import e
import pandas as pd
from scipy import io
from .HypergraphConstructKNN import Eu_dis
import math

def read_csv(path):
    with open(path, "r", newline="") as csv_file:
        reader = csv.reader(csv_file)
        md_data = []
        md_data += [[float(i) for i in row] for row in reader]
        return t.FloatTensor(md_data)


def read_txt(path):
    with open(path, "r", newline="") as txt_file:
        reader = txt_file.readlines()
        md_data = []
        md_data += [[float(i) for i in row.split()] for row in reader]
        return t.FloatTensor(md_data)


def read_mat(path, name):
    matrix = io.loadmat(path)
    matrix = t.FloatTensor(matrix[name])
    return matrix


def read_md_data(path, validation):
    result = [{} for _ in range(validation)]
    for filename in os.listdir(path):
        data_type = filename[filename.index("_") + 1 : filename.index(".") - 1]
        num = int(filename[filename.index(".") - 1])
        result[num - 1][data_type] = read_csv(os.path.join(path, filename))
    return result


def get_edge_index(matrix):
    edge_index = [[], []]
    for i in range(matrix.size(0)):
        for j in range(matrix.size(1)):
            if matrix[i][j] != 0:
                edge_index[0].append(i)
                edge_index[1].append(j)
    return t.LongTensor(edge_index)


def Gauss_M(adj_matrix, N):
    GM = np.zeros((N, N))
    rm = N * 1.0 / sum(sum(adj_matrix * adj_matrix))
    for i in range(N):
        for j in range(N):
            GM[i][j] = e ** (
                -rm
                * (
                    np.dot(
                        adj_matrix[i, :] - adj_matrix[j, :],
                        adj_matrix[i, :] - adj_matrix[j, :],
                    )
                )
            )
    return GM


def Gauss_D(adj_matrix, M):
    GD = np.zeros((M, M))
    T = adj_matrix.transpose()
    rd = M * 1.0 / sum(sum(T * T))
    for i in range(M):
        for j in range(M):
            GD[i][j] = e ** (-rd * (np.dot(T[i] - T[j], T[i] - T[j])))
    return GD


def SigmoidKernelDisease(DiseaseAndRNABinary):
    DiseasePolynomialKernel = []
    counter = 0
    while counter < len(DiseaseAndRNABinary):
        row = []
        counter1 = 0
        while counter1 < len(DiseaseAndRNABinary):
            sum = 0
            counter2 = 0
            while counter2 < len(DiseaseAndRNABinary[counter]):
                sum = (
                    sum
                    + DiseaseAndRNABinary[counter][counter2]
                    * DiseaseAndRNABinary[counter1][counter2]
                )
                counter2 = counter2 + 1
            sum = sum / (782 / len(DiseaseAndRNABinary))
            sum = (math.exp(sum) - math.exp(-sum)) / (math.exp(sum) + math.exp(-sum))
            row.append(sum)
            counter1 = counter1 + 1
        DiseasePolynomialKernel.append(row)
        counter = counter + 1
    return DiseasePolynomialKernel


def SigmoidKernelRNA(DiseaseAndRNABinary):
    MDiseaseAndRNABinary = np.array(DiseaseAndRNABinary)
    RNAAndDiseaseBinary = MDiseaseAndRNABinary.T
    RNAPolynomialKernel = []
    counter = 0
    while counter < len(RNAAndDiseaseBinary):
        row = []
        counter1 = 0
        while counter1 < len(RNAAndDiseaseBinary):
            sum = 0
            counter2 = 0
            while counter2 < len(RNAAndDiseaseBinary[counter]):
                sum = (
                    sum
                    + RNAAndDiseaseBinary[counter][counter2]
                    * RNAAndDiseaseBinary[counter1][counter2]
                )
                counter2 = counter2 + 1
            sum = sum / (782 / len(RNAAndDiseaseBinary))
            sum = (math.exp(sum) - math.exp(-sum)) / (math.exp(sum) + math.exp(-sum))
            row.append(sum)
            counter1 = counter1 + 1
        RNAPolynomialKernel.append(row)
        counter = counter + 1
    return RNAPolynomialKernel


def ReadMyCsv(SaveList, fileName):
    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:
        SaveList.append(row)
    return


def storFile(data, fileName):
    with open(fileName, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    return


def association_to_matrix(fileName):
    print("Run MMGN")

    df = pd.read_csv(fileName, header=None, names=["node1", "node2"])

    nodes_col = sorted(list(set(df["node1"])))
    nodes_row = sorted(list(set(df["node2"])))

    num_rows = len(nodes_row)
    num_cols = len(nodes_col)
    adj_matrix = [[0] * num_cols for _ in range(num_rows)]

    for _, row in df.iterrows():
        node1_idx = nodes_col.index(row["node1"])
        node2_idx = nodes_row.index(row["node2"])
        adj_matrix[node2_idx][node1_idx] = 1

    adj_df = pd.DataFrame(adj_matrix, columns=nodes_col, index=nodes_row)

    return adj_df


def PrepareBinData(Bin_data_path,SimWalk_RNA_path,SimWalk_Dis_path,SimST_RNA_path,SimST_Dis_path):
    dataset = {}
    mi_dis_data = association_to_matrix(Bin_data_path)

    row_indexes = mi_dis_data.index

    column_indexes = mi_dis_data.columns
    dataset["row_indexes_MDA"] = row_indexes
    dataset["column_indexes_MDA"] = column_indexes

    dataset["md_p"] = t.FloatTensor(np.array(mi_dis_data).T)
    dataset["md_true"] = dataset["md_p"]

    all_zero_index = []
    all_one_index = []
    for i in range(dataset["md_p"].size(0)):
        for j in range(dataset["md_p"].size(1)):
            if dataset["md_p"][i][j] < 1:
                all_zero_index.append([i, j])
            if dataset["md_p"][i][j] >= 1:
                all_one_index.append([i, j])

    np.random.seed(0)
    np.random.shuffle(all_zero_index)
    np.random.shuffle(all_one_index)

    dataset["md"] = []
    zero_tensor = t.LongTensor(all_zero_index)
    one_tensor = t.LongTensor(all_one_index)

    train_zero_index = zero_tensor
    train_one_index = one_tensor

    dataset["md"].append(
        {
            "test": [train_one_index, train_zero_index],
            "train": [train_one_index, train_zero_index],
        }
    )

    DGSM = Gauss_D(dataset["md_p"].numpy(), dataset["md_p"].size(1))
    MGSM = Gauss_M(dataset["md_p"].numpy(), dataset["md_p"].size(0))

    Sigmoid_matrix1 = SigmoidKernelDisease(dataset["md_p"].numpy())
    Sigmoid_matrix2 = SigmoidKernelRNA(dataset["md_p"].numpy())

    Sigmoid_matrix1 = np.array(Sigmoid_matrix1)
    Sigmoid_matrix2 = np.array(Sigmoid_matrix2)

    nd = mi_dis_data.shape[0]
    nm = mi_dis_data.shape[1]
    ID = np.zeros([nd, nd])

    for h1 in range(nd):
        for h2 in range(nd):
            if Sigmoid_matrix2[h1, h2] == 0:
                ID[h1, h2] = DGSM[h1, h2]
            else:
                ID[h1, h2] = (Sigmoid_matrix2[h1, h2] + DGSM[h1, h2]) / 2

    IM = np.zeros([nm, nm])

    for q1 in range(nm):
        for q2 in range(nm):
            if Sigmoid_matrix1[q1, q2] == 0:
                IM[q1, q2] = MGSM[q1, q2]
            else:
                IM[q1, q2] = (Sigmoid_matrix1[q1, q2] + MGSM[q1, q2]) / 2

    dataset["ID"] = t.from_numpy(ID)
    dataset["IM"] = t.from_numpy(IM)

    # walker sampling features
    Walker_Mi = pd.read_csv(SimWalk_RNA_path, header=None, index_col=None)
    Walker_Dis = pd.read_csv(SimWalk_Dis_path, header=None, index_col=None)
    # Calculate the walker Euclidean distance
    Walker_Mi_Eu_dis = np.array(Eu_dis(Walker_Mi))
    Walker_Dis_Eu_dis = np.array(Eu_dis(Walker_Dis))

    dataset["MDA_SD_OD"] = t.from_numpy(Walker_Dis_Eu_dis)
    dataset["MDA_SM_OD"] = t.from_numpy(Walker_Mi_Eu_dis)

    dataset["MDA_SD_S"] = t.from_numpy(np.array(Walker_Dis))
    dataset["MDA_SM_S"] = t.from_numpy(np.array(Walker_Mi))

    # ST sampling features
    Walker_Mi_ST = pd.read_csv(SimST_RNA_path, header=None, index_col=None)
    Walker_Dis_ST = pd.read_csv(SimST_Dis_path, header=None, index_col=None)
    # Calculate the ST Euclidean distance
    Walker_Mi_Eu_dis_ST = np.array(Eu_dis(Walker_Mi_ST))
    Walker_Dis_Eu_dis_ST = np.array(Eu_dis(Walker_Dis_ST))

    dataset["MDA_SD_OD_ST"] = t.from_numpy(Walker_Dis_Eu_dis_ST)
    dataset["MDA_SM_OD_ST"] = t.from_numpy(Walker_Mi_Eu_dis_ST)

    dataset["MDA_SD_S_ST"] = t.from_numpy(np.array(Walker_Dis_ST))
    dataset["MDA_SM_S_ST"] = t.from_numpy(np.array(Walker_Mi_ST))

    return dataset
