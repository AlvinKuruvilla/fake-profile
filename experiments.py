import sys
import os
import json
import numpy as np
from sklearn.metrics import top_k_accuracy_score
from classifiers.template_generator import all_ids
from performance_evaluation.heatmap import HeatMap, VerifierType
from tabulate import tabulate


def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
            It must be "yes" (the default), "no" or None (meaning
            an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")


def print_k_table(matrix, ids):
    rows = []
    rows.append([1, top_k_accuracy_score(np.array(ids), np.array(matrix), k=1)])
    rows.append([2, top_k_accuracy_score(np.array(ids), np.array(matrix), k=2)])
    rows.append([3, top_k_accuracy_score(np.array(ids), np.array(matrix), k=3)])
    rows.append([4, top_k_accuracy_score(np.array(ids), np.array(matrix), k=4)])
    rows.append([5, top_k_accuracy_score(np.array(ids), np.array(matrix), k=5)])
    table = tabulate(rows, headers=["K", "Score"], tablefmt="plain")
    print(table)


def same_platform_even_split():
    heatmap = HeatMap(VerifierType.SIMILARITY)

    matrix = heatmap.combined_keystroke_matrix(1, 1, [1, 3], [4, 6], 1)
    matrix2 = heatmap.combined_keystroke_matrix(2, 2, [1, 3], [4, 6], 1)
    matrix3 = heatmap.combined_keystroke_matrix(3, 3, [1, 3], [4, 6], 1)

    ids = all_ids()
    print()
    print("Facebook")
    print_k_table(matrix=matrix, ids=ids)
    print("Instagram")
    print_k_table(matrix=matrix2, ids=ids)
    print("Twitter")
    print_k_table(matrix=matrix3, ids=ids)


def train_session_one_test_two():
    heatmap = HeatMap(VerifierType.ITAD)

    matrix = heatmap.combined_keystroke_matrix(1, 1, 1, 4, 1)
    matrix2 = heatmap.combined_keystroke_matrix(2, 2, 1, 4, 1)
    matrix3 = heatmap.combined_keystroke_matrix(3, 3, 1, 4, 1)
    ids = all_ids()
    print()
    print("Facebook")
    print_k_table(matrix=matrix, ids=ids)
    print("Instagram")
    print_k_table(matrix=matrix2, ids=ids)
    print("Twitter")
    print_k_table(matrix=matrix3, ids=ids)


def train_on_one_test_another():
    heatmap = HeatMap(VerifierType.SIMILARITY)

    matrix = heatmap.combined_keystroke_matrix(1, 2, None, None, 1)
    matrix2 = heatmap.combined_keystroke_matrix(1, 3, None, None, 1)
    matrix3 = heatmap.combined_keystroke_matrix(2, 1, None, None, 1)
    matrix4 = heatmap.combined_keystroke_matrix(2, 3, None, None, 1)
    matrix5 = heatmap.combined_keystroke_matrix(3, 1, None, None, 1)
    matrix6 = heatmap.combined_keystroke_matrix(3, 2, None, None, 1)
    ids = all_ids()
    print()
    print("F vs. I")
    print_k_table(matrix=matrix, ids=ids)
    input()
    print("F vs. T")
    print_k_table(matrix=matrix2, ids=ids)
    input()
    print("I vs. F")
    print_k_table(matrix=matrix3, ids=ids)
    input()
    print("I vs. T")
    print_k_table(matrix=matrix4, ids=ids)
    input()
    print("T vs. F")
    print_k_table(matrix=matrix5, ids=ids)
    input()
    print("T vs. I")
    print_k_table(matrix=matrix6, ids=ids)


def cross_platform_2v1():
    heatmap = HeatMap(VerifierType.ABSOLUTE)
    matrix = heatmap.combined_keystroke_matrix([1, 2], 3, None, None, 1)
    matrix2 = heatmap.combined_keystroke_matrix([1, 3], 2, None, None, 1)
    matrix3 = heatmap.combined_keystroke_matrix([2, 1], 3, None, None, 1)
    matrix4 = heatmap.combined_keystroke_matrix([2, 3], 1, None, None, 1)
    matrix5 = heatmap.combined_keystroke_matrix([3, 1], 2, None, None, 1)
    matrix6 = heatmap.combined_keystroke_matrix([3, 2], 1, None, None, 1)
    ids = all_ids()
    print()
    print("FI")
    print_k_table(matrix=matrix, ids=ids)
    input()
    print("FT")
    print_k_table(matrix=matrix2, ids=ids)
    input()
    print("IF")
    print_k_table(matrix=matrix3, ids=ids)
    input()
    print("IT")
    print_k_table(matrix=matrix4, ids=ids)
    input()
    print("TF")
    print_k_table(matrix=matrix5, ids=ids)
    input()
    print("TI")
    print_k_table(matrix=matrix6, ids=ids)


with open(os.path.join(os.getcwd(), "classifier_config.json"), "r") as f:
    config = json.load(f)
print("Using feature selection is: ", config["use_feature_selection"])
query_yes_no("Proceed?")
train_on_one_test_another()
