import numpy as np
from sklearn.metrics import top_k_accuracy_score
from verifiers.heatmap import HeatMap, VerifierType
from tabulate import tabulate


def print_k_table(matrix, ids):
    rows = []
    rows.append([1, top_k_accuracy_score(np.array(ids), np.array(matrix), k=1)])
    rows.append([2, top_k_accuracy_score(np.array(ids), np.array(matrix), k=2)])
    rows.append([3, top_k_accuracy_score(np.array(ids), np.array(matrix), k=3)])
    rows.append([4, top_k_accuracy_score(np.array(ids), np.array(matrix), k=4)])
    rows.append([5, top_k_accuracy_score(np.array(ids), np.array(matrix), k=5)])
    table = tabulate(rows, headers=["K", "Score"], tablefmt="orgtbl")
    print(table)


def same_platform_even_split():
    heatmap = HeatMap(VerifierType.Similarity)

    matrix = heatmap.combined_keystroke_matrix(1, 1, [1, 3], [4, 6], 1)
    matrix2 = heatmap.combined_keystroke_matrix(2, 2, [1, 3], [4, 6], 1)
    matrix3 = heatmap.combined_keystroke_matrix(3, 3, [1, 3], [4, 6], 1)

    ids = [num for num in range(1, 26) if num != 22]
    print()
    print("Facebook")
    print_k_table(matrix=matrix, ids=ids)
    print("Instagram")
    print_k_table(matrix=matrix2, ids=ids)
    print("Twitter")
    print_k_table(matrix=matrix3, ids=ids)


def train_session_one_test_two():
    heatmap = HeatMap(VerifierType.Similarity)

    matrix = heatmap.combined_keystroke_matrix(1, 1, 1, 4, 1)
    matrix2 = heatmap.combined_keystroke_matrix(2, 2, 1, 4, 1)
    matrix3 = heatmap.combined_keystroke_matrix(3, 3, 1, 4, 1)
    ids = [num for num in range(1, 26) if num != 22]
    print()
    print("Facebook")
    print_k_table(matrix=matrix, ids=ids)
    print("Instagram")
    print_k_table(matrix=matrix2, ids=ids)
    print("Twitter")
    print_k_table(matrix=matrix3, ids=ids)


def simple_cross_platform():
    heatmap = HeatMap(VerifierType.Similarity)

    matrix = heatmap.combined_keystroke_matrix(1, 1, None, None, 1)
    matrix2 = heatmap.combined_keystroke_matrix(2, 2, None, None, 1)
    matrix3 = heatmap.combined_keystroke_matrix(3, 3, None, None, 1)
    ids = [num for num in range(1, 26) if num != 22]
    print()
    print("Facebook")
    print_k_table(matrix=matrix, ids=ids)
    print("Instagram")
    print_k_table(matrix=matrix2, ids=ids)
    print("Twitter")
    print_k_table(matrix=matrix3, ids=ids)


def cross_platform_2v1():
    heatmap = HeatMap(VerifierType.Similarity)
    matrix = heatmap.combined_keystroke_matrix([1, 2], 3, None, None, 1)
    matrix2 = heatmap.combined_keystroke_matrix([1, 3], 2, None, None, 1)
    matrix3 = heatmap.combined_keystroke_matrix([2, 3], 1, None, None, 1)
    ids = [num for num in range(1, 26) if num != 22]
    print()
    print("Facebook")
    print_k_table(matrix=matrix, ids=ids)
    print("Instagram")
    print_k_table(matrix=matrix2, ids=ids)
    print("Twitter")
    print_k_table(matrix=matrix3, ids=ids)


same_platform_even_split()
