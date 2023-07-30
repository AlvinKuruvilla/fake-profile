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
    mat1 = heatmap.combined_keystroke_matrix(platform, platform, [1, 5], 6, 1)
    mat2 = heatmap.combined_keystroke_matrix(platform, platform, [2, 6], 1, 1)
    mat3 = heatmap.combined_keystroke_matrix(platform, platform, [1, 3, 4, 5, 6], 2, 1)
    mat4 = heatmap.combined_keystroke_matrix(platform, platform, [1, 2, 4, 5, 6], 3, 1)
    mat5 = heatmap.combined_keystroke_matrix(platform, platform, [1, 2, 3, 5, 6], 4, 1)
    mat6 = heatmap.combined_keystroke_matrix(platform, platform, [1, 2, 3, 4, 6], 5, 1)
    for i in range(1, 5):
        cv.append(top_k_accuracy_score(np.array(ids), np.array(mat1), k=i))
    for i in range(1, 5):
        cv.append(top_k_accuracy_score(np.array(ids), np.array(mat2), k=i))
    for i in range(1, 5):
        cv.append(top_k_accuracy_score(np.array(ids), np.array(mat3), k=i))
    for i in range(1, 5):
        cv.append(top_k_accuracy_score(np.array(ids), np.array(mat4), k=i))
    for i in range(1, 5):
        cv.append(top_k_accuracy_score(np.array(ids), np.array(mat5), k=i))
    for i in range(1, 5):
        cv.append(top_k_accuracy_score(np.array(ids), np.array(mat6), k=i))

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


if os.path.exists("cross_validation.obj"):
    with open("cross_validation.obj", "rb") as f:
        rows = pickle.load(f)
else:
    id_set = [num for num in range(1, 26) if num != 22]
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
    with open("cross_validation.obj", "wb") as f:
        pickle.dump(rows, f)
table = tabulate(
    rows, headers=["Platform", "ITAD", "Similarity", "Absolute"], tablefmt="plain"
)
heatmap_table(rows)
print(table)
