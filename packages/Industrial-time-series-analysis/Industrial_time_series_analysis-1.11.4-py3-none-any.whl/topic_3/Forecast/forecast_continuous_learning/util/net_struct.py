import glob
import os.path


def get_feature_map(path):
    # feature_file = open(f"../data/{dataset}/list.txt", 'r')
    feature_file = open(f"{path}/list.txt")
    feature_list = []
    for ft in feature_file:
        feature_list.append(ft.strip())

    return feature_list

# graph is 'fully-connect'
def get_fc_graph_struc(path):
    feature_file = open(f'{path}/list.txt', 'r')

    struc_map = {}
    feature_list = []
    for ft in feature_file:
        feature_list.append(ft.strip())

    for ft in feature_list:
        if ft not in struc_map:
            struc_map[ft] = []

        for other_ft in feature_list:
            if other_ft is not ft:
                struc_map[ft].append(other_ft)
    
    return struc_map

def get_prior_graph_struc(path):
    # feature_file = open(f'../data/{dataset}/list.txt', 'r')
    feature_file = open(f'{path}/list.txt', 'r')


    # adjacency_matrix = [[1, 0, 0, 0, 1, 1, 0, 1],
    #                     [0, 1, 0, 0, 0, 0, 0, 0],
    #                     [0, 1, 1, 1, 1, 0, 0, 0],
    #                     [1, 0, 0, 1, 0, 0, 0, 0],
    #                     [0, 1, 0, 0, 1, 1, 0, 0],
    #                     [0, 0, 0, 1, 0, 1, 1, 1],
    #                     [0, 1, 1, 1, 0, 0, 1, 1],
    #                     [0, 1, 0, 1, 0, 0, 0, 1]]

    # adjacency_matrix = [[1, 0, 0, 1, 0, 0, 0, 0],
    #                     [0, 1, 1, 0, 1, 0, 1, 1],
    #                     [0, 0, 1, 0, 0, 0, 1, 0],
    #                     [0, 0, 1, 1, 0, 1, 1, 1],
    #                     [1, 0, 1, 0, 1, 0, 0, 0],
    #                     [1, 0, 0, 0, 1, 1, 0, 0],
    #                     [0, 0, 0, 0, 0, 1, 1, 0],
    #                     [1, 0, 0, 0, 0, 1, 1, 1]]

    # adjacency_matrix = [[1, 0, 0, 0, 0, 0, 0, 0],
    #                     [0, 1, 1, 1, 1, 0, 0, 0],
    #                     [0, 1, 1, 1, 1, 0, 0, 0],
    #                     [0, 1, 1, 1, 1, 0, 0, 0],
    #                     [0, 1, 1, 1, 1, 0, 0, 0],
    #                     [0, 0, 0, 0, 0, 1, 0, 1],
    #                     [0, 0, 0, 0, 0, 0, 1, 0],
    #                     [1, 1, 1, 1, 1, 1, 1, 1]]

    # adjacency_matrix = [[1, 0, 0, 0, 0, 0, 0, 0],
    #                     [1, 1, 0, 0, 0, 1, 1, 0],
    #                     [1, 0, 1, 0, 0, 1, 1, 0],
    #                     [1, 0, 0, 1, 0, 1, 1, 0],
    #                     [1, 0, 0, 0, 1, 1, 1, 0],
    #                     [0, 0, 0, 0, 0, 1, 0, 1],
    #                     [1, 0, 0, 0, 0, 0, 1, 0],
    #                     [1, 1, 1, 1, 1, 1, 1, 1]]
    adjacency_matrix = [[1, 0, 0, 0, 0, 0, 0, 0],
                        [1, 1, 0, 1, 1, 0, 1, 0],
                        [1, 0, 1, 1, 0, 0, 1, 0],
                        [1, 0, 0, 1, 0, 0, 1, 0],
                        [1, 0, 0, 0, 1, 0, 1, 0],
                        [1, 0, 1, 1, 1, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 0],
                        [1, 1, 1, 1, 1, 0, 1, 1]]

    # adjacency_matrix = [[1, 0, 0, 0, 0, 0, 0, 1],
    #                     [0, 1, 1, 1, 1, 0, 0, 1],
    #                     [0, 1, 1, 1, 1, 0, 0, 1],
    #                     [0, 1, 1, 1, 1, 0, 0, 1],
    #                     [0, 1, 1, 1, 1, 0, 0, 1],
    #                     [0, 0, 0, 0, 0, 1, 0, 1],
    #                     [0, 0, 0, 0, 0, 0, 1, 1],
    #                     [0, 0, 0, 0, 0, 0, 0, 1]]




    struc_map = {}
    feature_list = []
    for ft in feature_file:
        feature_list.append(ft.strip())

    for ft in feature_list:
        ft_index = feature_list.index(ft)
        if ft not in struc_map:
            struc_map[ft] = []
        for other_ft in feature_list:
            other_ft_index = feature_list.index(other_ft)
            if other_ft is not ft and adjacency_matrix[ft_index][other_ft_index] == 1:
                struc_map[ft].append(other_ft)

    # for ft in feature_list:
    #     ft_index = feature_list.index(ft)
    #     if ft not in struc_map:
    #         struc_map[ft] = []
    #     for other_ft in feature_list:
    #         other_ft_index = feature_list.index(other_ft)
    #         if dataset == 'wadi' or dataset == 'wadi2':
    #             # same group, 1_xxx, 2A_xxx, 2_xxx
    #             if other_ft is not ft and other_ft[0] == ft[0]:
    #                 struc_map[ft].append(other_ft)
    #
    #         elif dataset == 'swat':
    #             # FIT101, PV101
    #             if other_ft is not ft and other_ft[-3] == ft[-3]:
    #                 struc_map[ft].append(other_ft)
    #
    #         elif dataset == 'steel':
    #             if other_ft is not ft and adjacency_matrix[ft_index][other_ft_index] == 1:
    #                 struc_map[ft].append(other_ft)
    
    return struc_map


 