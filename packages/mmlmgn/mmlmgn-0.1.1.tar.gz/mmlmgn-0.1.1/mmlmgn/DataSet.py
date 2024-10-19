from __future__ import division

class Dataset_MDA(object):
    def __init__(self, validation, dataset):
        self.data_set = dataset
        self.nums = validation

    def __getitem__(self, index):

        # ID IM: similarity fusion matrix
        # md train test: Relationship between positive and negative samples
        # md_p md_true: Adjacency Matrix
        # SD_OD SM_OD: Euclidean distance calculation for random walks
        # SD_S SM_S: Random walk feature
        # SD_S_ST SM_S_ST: Functional similarity features
        # SD_OD_ST SM_OD_ST: Functional similarity Euclidean distance

        return (
            self.data_set["ID"],
            self.data_set["IM"],
            self.data_set["md"][index]["train"],
            self.data_set["md"][index]["test"],
            self.data_set["md_p"],
            self.data_set["md_true"],
            self.data_set["row_indexes_MDA"],
            self.data_set["column_indexes_MDA"],
            self.data_set["MDA_SD_OD"],
            self.data_set["MDA_SM_OD"],
            self.data_set["MDA_SD_S"],
            self.data_set["MDA_SM_S"],
            self.data_set["MDA_SD_OD_ST"],
            self.data_set["MDA_SM_OD_ST"],
            self.data_set["MDA_SD_S_ST"],
            self.data_set["MDA_SM_S_ST"],
        )

    def __len__(self):
        return self.nums
