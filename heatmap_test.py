import numpy as np
from sklearn.metrics import top_k_accuracy_score
from performance_evaluation.heatmap import HeatMap, VerifierType

heatmap = HeatMap(VerifierType.SIMILARITY)
matrix = heatmap.combined_keystroke_matrix(1, 1, None, None, 1)
# print(matrix)
heatmap.plot_heatmap(matrix, "FF Combined (new) Similarity (new file)")
# matrix = heatmap.make_kit_matrix(1, 1, [1, 3], [4, 6], 1)
# heatmap.plot_heatmap(matrix, "Facebook KIT even split")

ids = [num for num in range(1, 26) if num != 22]
print("k=1 : ", top_k_accuracy_score(np.array(ids), np.array(matrix), k=1))
print("k=2 : ", top_k_accuracy_score(np.array(ids), np.array(matrix), k=2))
print("k=3 : ", top_k_accuracy_score(np.array(ids), np.array(matrix), k=3))
print("k=4 : ", top_k_accuracy_score(np.array(ids), np.array(matrix), k=4))
print("k=5 : ", top_k_accuracy_score(np.array(ids), np.array(matrix), k=4))
