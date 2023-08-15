import numpy as np
from sklearn.metrics import top_k_accuracy_score
from heatmap import HeatMap, VerifierType
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


enroll_platform = 1
probe_platform = 2
enroll_session = 1
probe_session = 1

heatmap = HeatMap(VerifierType.ITAD)
matrix = heatmap.combined_keystroke_matrix(enroll_platform_id=enroll_platform, probe_platform_id=probe_platform, enroll_session_id=enroll_session, probe_session_id=probe_session, kit_feature_type=1)
print(f'shape of matrix: row: {len(matrix)}, cols: {len(matrix[0])}')
# heatmap.plot_heatmap(matrix, "FF Combined Absolute (new file)")
# matrix = heatmap.make_kit_matrix(1, 1, [1, 3], [4, 6], 1)
# heatmap.plot_heatmap(matrix, "Facebook KIT even split")
ids = [num for num in range(1, 26) if num != 22]
print('k=1 : ', top_k_accuracy_score(np.array(ids), np.array(matrix), k=1))
print('k=2 : ', top_k_accuracy_score(np.array(ids), np.array(matrix), k=2))
print('k=3 : ', top_k_accuracy_score(np.array(ids), np.array(matrix), k=3))
print('k=4 : ', top_k_accuracy_score(np.array(ids), np.array(matrix), k=4))
print('k=5 : ', top_k_accuracy_score(np.array(ids), np.array(matrix), k=5))

enroll_platform = 1
probe_platform = 2
enroll_session = 2
probe_session = 2
heatmap = HeatMap(VerifierType.ITAD)
matrix = heatmap.combined_keystroke_matrix(enroll_platform_id=enroll_platform, probe_platform_id=probe_platform, enroll_session_id=enroll_session, probe_session_id=probe_session, kit_feature_type=1)
print(f'shape of matrix: row: {len(matrix)}, cols: {len(matrix[0])}')
# heatmap.plot_heatmap(matrix, "FF Combined Absolute (new file)")
# matrix = heatmap.make_kit_matrix(1, 1, [1, 3], [4, 6], 1)
# heatmap.plot_heatmap(matrix, "Facebook KIT even split")
ids = [num for num in range(1, 26) if num != 22]
print('k=1 : ', top_k_accuracy_score(np.array(ids), np.array(matrix), k=1))
print('k=2 : ', top_k_accuracy_score(np.array(ids), np.array(matrix), k=2))
print('k=3 : ', top_k_accuracy_score(np.array(ids), np.array(matrix), k=3))
print('k=4 : ', top_k_accuracy_score(np.array(ids), np.array(matrix), k=4))
print('k=5 : ', top_k_accuracy_score(np.array(ids), np.array(matrix), k=5))

enroll_platform = 1
probe_platform = 2
enroll_session = 3
probe_session = 3
heatmap = HeatMap(VerifierType.ITAD)
matrix = heatmap.combined_keystroke_matrix(enroll_platform_id=enroll_platform, probe_platform_id=probe_platform, enroll_session_id=enroll_session, probe_session_id=probe_session, kit_feature_type=1)
print(f'shape of matrix: row: {len(matrix)}, cols: {len(matrix[0])}')
# heatmap.plot_heatmap(matrix, "FF Combined Absolute (new file)")
# matrix = heatmap.make_kit_matrix(1, 1, [1, 3], [4, 6], 1)
# heatmap.plot_heatmap(matrix, "Facebook KIT even split")
ids = [num for num in range(1, 26) if num != 22]
print('k=1 : ', top_k_accuracy_score(np.array(ids), np.array(matrix), k=1))
print('k=2 : ', top_k_accuracy_score(np.array(ids), np.array(matrix), k=2))
print('k=3 : ', top_k_accuracy_score(np.array(ids), np.array(matrix), k=3))
print('k=4 : ', top_k_accuracy_score(np.array(ids), np.array(matrix), k=4))
print('k=5 : ', top_k_accuracy_score(np.array(ids), np.array(matrix), k=5))

enroll_platform = 1
probe_platform = 2
enroll_session = 4
probe_session = 4
heatmap = HeatMap(VerifierType.ITAD)
matrix = heatmap.combined_keystroke_matrix(enroll_platform_id=enroll_platform, probe_platform_id=probe_platform, enroll_session_id=enroll_session, probe_session_id=probe_session, kit_feature_type=1)
print(f'shape of matrix: row: {len(matrix)}, cols: {len(matrix[0])}')
# heatmap.plot_heatmap(matrix, "FF Combined Absolute (new file)")
# matrix = heatmap.make_kit_matrix(1, 1, [1, 3], [4, 6], 1)
# heatmap.plot_heatmap(matrix, "Facebook KIT even split")
ids = [num for num in range(1, 26) if num != 22]
print('k=1 : ', top_k_accuracy_score(np.array(ids), np.array(matrix), k=1))
print('k=2 : ', top_k_accuracy_score(np.array(ids), np.array(matrix), k=2))
print('k=3 : ', top_k_accuracy_score(np.array(ids), np.array(matrix), k=3))
print('k=4 : ', top_k_accuracy_score(np.array(ids), np.array(matrix), k=4))
print('k=5 : ', top_k_accuracy_score(np.array(ids), np.array(matrix), k=5))


enroll_platform = 1
probe_platform = 2
enroll_session = 5
probe_session = 5
heatmap = HeatMap(VerifierType.ITAD)
matrix = heatmap.combined_keystroke_matrix(enroll_platform_id=enroll_platform, probe_platform_id=probe_platform, enroll_session_id=enroll_session, probe_session_id=probe_session, kit_feature_type=1)
print(f'shape of matrix: row: {len(matrix)}, cols: {len(matrix[0])}')
# heatmap.plot_heatmap(matrix, "FF Combined Absolute (new file)")
# matrix = heatmap.make_kit_matrix(1, 1, [1, 3], [4, 6], 1)
# heatmap.plot_heatmap(matrix, "Facebook KIT even split")
ids = [num for num in range(1, 26) if num != 22]
print('k=1 : ', top_k_accuracy_score(np.array(ids), np.array(matrix), k=1))
print('k=2 : ', top_k_accuracy_score(np.array(ids), np.array(matrix), k=2))
print('k=3 : ', top_k_accuracy_score(np.array(ids), np.array(matrix), k=3))
print('k=4 : ', top_k_accuracy_score(np.array(ids), np.array(matrix), k=4))
print('k=5 : ', top_k_accuracy_score(np.array(ids), np.array(matrix), k=5))


enroll_platform = 1
probe_platform = 2
enroll_session = 6
probe_session = 6
heatmap = HeatMap(VerifierType.ITAD)
matrix = heatmap.combined_keystroke_matrix(enroll_platform_id=enroll_platform, probe_platform_id=probe_platform, enroll_session_id=enroll_session, probe_session_id=probe_session, kit_feature_type=1)
print(f'shape of matrix: row: {len(matrix)}, cols: {len(matrix[0])}')
# heatmap.plot_heatmap(matrix, "FF Combined Absolute (new file)")
# matrix = heatmap.make_kit_matrix(1, 1, [1, 3], [4, 6], 1)
# heatmap.plot_heatmap(matrix, "Facebook KIT even split")
ids = [num for num in range(1, 26) if num != 22]
print('k=1 : ', top_k_accuracy_score(np.array(ids), np.array(matrix), k=1))
print('k=2 : ', top_k_accuracy_score(np.array(ids), np.array(matrix), k=2))
print('k=3 : ', top_k_accuracy_score(np.array(ids), np.array(matrix), k=3))
print('k=4 : ', top_k_accuracy_score(np.array(ids), np.array(matrix), k=4))
print('k=5 : ', top_k_accuracy_score(np.array(ids), np.array(matrix), k=5))