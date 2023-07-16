import numpy as np
from sklearn.metrics import top_k_accuracy_score
from verifiers.heatmap import HeatMap, VerifierType


def calculate_rankn_accuracy(similarity_matrix, n):
    num_users = len(similarity_matrix)
    correct_predictions = 0

    for user_id in range(num_users):
        row = similarity_matrix[user_id]
        top_n_indices = sorted(range(len(row)), key=lambda i: row[i], reverse=True)[:n]

        if user_id in top_n_indices:
            correct_predictions += 1

    rankn_accuracy = correct_predictions / num_users
    return rankn_accuracy


heatmap = HeatMap(VerifierType.Itad)
# matrix = heatmap.combined_keystroke_matrix(1, 1, None, None, 1)
# print(matrix)
# heatmap.plot_heatmap(matrix, "FF Combined Absolute (new file)")
matrix = heatmap.make_kit_matrix(1, 1, [1, 3], [4, 6], 1)
heatmap.plot_heatmap(matrix, "Facebook Absolute KIT even split")

print(calculate_rankn_accuracy(matrix, 2))
ids = [num for num in range(1, 26) if num != 22]
print(top_k_accuracy_score(np.array(ids), np.array(matrix), k=2))
