import os
import pandas as pd
import pickle
import statistics
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import top_k_accuracy_score
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


if os.path.exists("cross_validation.obj"):
    with open("cross_validation.obj", "rb") as f:
        rows = pickle.load(f)
else:
    id_set = [num for num in range(1, 26) if num != 22]
    rows = make_validation_matrix(id_set)
    with open("cross_validation.obj", "wb") as f:
        pickle.dump(rows, f)
table = tabulate(
    rows, headers=["Platform", "ITAD", "Similarity", "Absolute"], tablefmt="plain"
)
heatmap_table(rows)
print(table)
