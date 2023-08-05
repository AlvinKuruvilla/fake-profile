import enum
import statistics
import numpy as np


class FusionAlgorithm(enum.Enum):
    MEAN = 1
    MEDIAN = 2
    MIN = 3
    MAX = 4


def choose_score(algorithm, score1, score2, score3):
    if algorithm == FusionAlgorithm.MEAN:
        return statistics.mean([score1, score2, score3])
    elif algorithm == FusionAlgorithm.MEDIAN:
        return statistics.median([score1, score2, score3])
    elif algorithm == FusionAlgorithm.MIN:
        return min(score1, score2, score3)
    elif algorithm == FusionAlgorithm.MAX:
        return max(score1, score2, score3)
    else:
        raise ValueError("Invalid algorithm")


class ScoreFuser:
    def __init__(self, itad_matrix, similarity_matrix, absolute_matrix):
        self.itad_matrix = np.array(itad_matrix)
        self.similarity_matrix = np.array(similarity_matrix)
        self.absolute_matrix = np.array(absolute_matrix)
        assert (
            len(self.itad_matrix)
            == len(self.absolute_matrix)
            == len(self.similarity_matrix)
        )
        assert (
            len([row[0] for row in self.similarity_matrix])
            == len([row[0] for row in self.absolute_matrix])
            == len([row[0] for row in self.itad_matrix])
        )

    def find_matrix(self, algorithm: FusionAlgorithm):
        rows = len(self.absolute_matrix)
        cols = len([row[0] for row in self.absolute_matrix])
        res_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        for row_index, _ in enumerate(self.absolute_matrix):
            for column_index in range(len(self.absolute_matrix[row_index])):
                absolute_matrix_element = self.absolute_matrix[row_index, column_index]
                similarity_matrix_element = self.similarity_matrix[
                    row_index, column_index
                ]
                itad_matrix_element = self.itad_matrix[row_index, column_index]
                res_matrix[row_index][column_index] = choose_score(
                    algorithm,
                    itad_matrix_element,
                    similarity_matrix_element,
                    absolute_matrix_element,
                )
        return res_matrix
