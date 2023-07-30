import os
import json
import pandas as pd
import pickle
import statistics
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import top_k_accuracy_score
from classifiers.template_generator import Genders, all_ids
from performance_evaluation.heatmap import HeatMap, VerifierType
from tabulate import tabulate


def six_fold_validation(platform, ids, verifier_type: VerifierType):
    heatmap = HeatMap(verifier_type)
    cv = []

    # Define the configurations for the heatmap.combined_keystroke_matrix function
    configurations = [
        (platform, platform, [1, 5], 6),
        (platform, platform, [2, 6], 1),
        (platform, platform, [1, 3, 4, 5, 6], 2),
        (platform, platform, [1, 2, 4, 5, 6], 3),
        (platform, platform, [1, 2, 3, 5, 6], 4),
        (platform, platform, [1, 2, 3, 4, 6], 5),
    ]

    for config in configurations:
        platform, session, key_order, user = config
        matrix = heatmap.combined_keystroke_matrix(
            platform, session, key_order, user, 1
        )
        for i in range(1, 5):
            cv.append(top_k_accuracy_score(np.array(ids), np.array(matrix), k=i))

    return statistics.mean(cv)


def heatmap_table(matrix):
    # Have to remove the platform name, since the index will handle that
    result = [row[1:] for row in matrix]
    df = pd.DataFrame(
        result,
        columns=["ITAD", "Similarity", "Absolute"],
        index=["Facebook", "Instagram", "Twitter"],
    )
    df.style.background_gradient(cmap="Blues")
    sns.heatmap(result, annot=True, fmt="g", cmap="viridis")
    plt.savefig("cross_validation.png")


def make_validation_matrix(id_set):
    rows = []
    rows.append(
        [
            "Facebook",
            six_fold_validation(1, id_set, VerifierType.ITAD),
            six_fold_validation(1, id_set, VerifierType.SIMILARITY),
            six_fold_validation(1, id_set, VerifierType.ABSOLUTE),
        ]
    )
    rows.append(
        [
            "Instagram",
            six_fold_validation(2, id_set, VerifierType.ITAD),
            six_fold_validation(2, id_set, VerifierType.SIMILARITY),
            six_fold_validation(2, id_set, VerifierType.ABSOLUTE),
        ]
    )
    rows.append(
        [
            "Twitter",
            six_fold_validation(3, id_set, VerifierType.ITAD),
            six_fold_validation(3, id_set, VerifierType.SIMILARITY),
            six_fold_validation(3, id_set, VerifierType.ABSOLUTE),
        ]
    )
    return rows


def main():
    id_set = all_ids()
    with open(os.path.join(os.getcwd(), "classifier_config.json"), "r") as f:
        config = json.load(f)
    gender = str(config["gender"])
    if gender == Genders.ALL():
        if os.path.exists("all_cross_validation.obj"):
            with open("all_cross_validation.obj", "rb") as f:
                rows = pickle.load(f)
        else:
            rows = make_validation_matrix(id_set)
            with open("all_cross_validation.obj", "wb") as f:
                pickle.dump(rows, f)
    elif gender == Genders.MALE():
        if os.path.exists("male_cross_validation.obj"):
            with open("male_cross_validation.obj", "rb") as f:
                rows = pickle.load(f)
        else:
            rows = make_validation_matrix(id_set)
            with open("male_cross_validation.obj", "wb") as f:
                pickle.dump(rows, f)
    elif gender == Genders.FEMALE():
        if os.path.exists("female_cross_validation.obj"):
            with open("female_cross_validation.obj", "rb") as f:
                rows = pickle.load(f)
        else:
            rows = make_validation_matrix(id_set)
            with open("female_cross_validation.obj", "wb") as f:
                pickle.dump(rows, f)
    elif gender == Genders.OTHER():
        if os.path.exists("other_cross_validation.obj"):
            with open("other_cross_validation.obj", "rb") as f:
                rows = pickle.load(f)
        else:
            rows = make_validation_matrix(id_set)
            with open("other_cross_validation.obj", "wb") as f:
                pickle.dump(rows, f)

    table = tabulate(
        rows, headers=["Platform", "ITAD", "Similarity", "Absolute"], tablefmt="plain"
    )
    heatmap_table(rows)
    print(table)


if __name__ == "__main__":
    main()
