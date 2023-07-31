import os
import sys
import enum
import matplotlib.pyplot as plt
import seaborn as sns
from classifiers.template_generator import all_ids, read_compact_format
from features.keystroke_features import create_kht_data_from_df, create_kit_data_from_df
from rich.progress import track
import classifiers.verifiers_library as vl

path = os.path.dirname(os.getcwd())
print(path)
sys.path.insert(0, path)


class VerifierType(enum.Enum):
    RELATIVE = 1
    SIMILARITY = 2
    SIMILARITY_UNWEIGHTED = 3
    ABSOLUTE = 4
    ITAD = 5


def get_user_by_platform(user_id, platform_id, session_id=None):
    # print(f"user_id:{user_id}", end=" | ")
    df = read_compact_format()
    if session_id is None:
        if isinstance(platform_id, list):
            # Should only contain an inclusive range of the starting id and ending id
            assert len(platform_id) == 2
            if platform_id[0] < platform_id[1]:
                return df[
                    (df["user_ids"] == user_id)
                    & (df["platform_id"].between(platform_id[0], platform_id[1]))
                ]
            else:
                return df[
                    (df["user_ids"] == user_id)
                    & (df["platform_id"].between(platform_id[1], platform_id[0]))
                ]

        return df[(df["user_ids"] == user_id) & (df["platform_id"] == platform_id)]
    if isinstance(session_id, list):
        # Should only contain an inclusive range of the starting id and ending id
        if len(session_id) == 2:
            return df[
                (df["user_ids"] == user_id)
                & (df["platform_id"] == platform_id)
                & (df["session_id"].between(session_id[0], session_id[1]))
            ]
        elif len(session_id) > 2:
            test = df[
                (df["user_ids"] == user_id)
                & (df["platform_id"] == platform_id)
                & (df["session_id"].isin(session_id))
            ]
            # print(session_id)
            # print(test["session_id"].unique())
            # input()
            return df[
                (df["user_ids"] == user_id)
                & (df["platform_id"] == platform_id)
                & (df["session_id"].isin(session_id))
            ]

    return df[
        (df["user_ids"] == user_id)
        & (df["platform_id"] == platform_id)
        & (df["session_id"] == session_id)
    ]


class HeatMap:
    def __init__(self, verifier_type, p1=10, p2=10):
        self.verifier_type = verifier_type  # The verifier class to be used
        self.p1_threshold = p1
        self.p2_threshold = p2
        print(f"----selected {verifier_type}")

    def make_kht_matrix(
        self, enroll_platform_id, probe_platform_id, enroll_session_id, probe_session_id
    ):
        # if not 1 <= enroll_platform_id <= 3 or not 1 <= probe_platform_id <= 3:
        #     raise ValueError("Platform ID must be between 1 and 3")

        matrix = []
        # TODO: We have to do a better job of figuring out how many users there
        # are automatically so we don't need to keep changing it manually
        ids = all_ids()
        for i in track(ids):
            print(i)
            df = get_user_by_platform(i, enroll_platform_id, enroll_session_id)
            enrollment = create_kht_data_from_df(df)
            row = []
            # TODO: We have to do a better job of figuring out how many users there
            # are automatically so we don't need to keep changing it manually
            for j in ids:
                df = get_user_by_platform(j, probe_platform_id, probe_session_id)
                probe = create_kht_data_from_df(df)
                v = vl.Verify(enrollment, probe, self.p1_threshold, self.p2_threshold)
                if self.verifier_type == VerifierType.ABSOLUTE:
                    row.append(v.get_abs_match_score())
                elif self.verifier_type == VerifierType.SIMILARITY:
                    row.append(v.get_weighted_similarity_score())
                elif self.verifier_type == VerifierType.SIMILARITY_UNWEIGHTED:
                    row.append(v.get_similarity_score())
                elif self.verifier_type == VerifierType.ITAD:
                    row.append(v.itad_similarity())
                else:
                    raise ValueError(
                        "Unknown VerifierType {}".format(self.verifier_type)
                    )
            matrix.append(row)
        return matrix

    def make_kit_matrix(
        self,
        enroll_platform_id,
        probe_platform_id,
        enroll_session_id,
        probe_session_id,
        kit_feature_type,
    ):
        # if not 1 <= enroll_platform_id <= 3 or not 1 <= probe_platform_id <= 3:
        #     raise ValueError("Platform ID must be between 1 and 3")
        if not 1 <= kit_feature_type <= 4:
            raise ValueError("KIT feature type must be between 1 and 4")
        print(self.verifier_type)
        matrix = []
        ids = all_ids()
        for i in track(ids):
            df = get_user_by_platform(i, enroll_platform_id, enroll_session_id)
            enrollment = create_kit_data_from_df(df, kit_feature_type)
            row = []
            for j in ids:
                df = get_user_by_platform(j, probe_platform_id, probe_session_id)
                probe = create_kit_data_from_df(df, kit_feature_type)
                v = vl.Verify(enrollment, probe)
                if self.verifier_type == VerifierType.ABSOLUTE:
                    row.append(v.get_abs_match_score())
                elif self.verifier_type == VerifierType.SIMILARITY:
                    row.append(v.get_weighted_similarity_score())
                elif self.verifier_type == VerifierType.SIMILARITY_UNWEIGHTED:
                    row.append(v.get_similarity_score())
                elif self.verifier_type == VerifierType.ITAD:
                    row.append(v.itad_similarity())
                else:
                    raise ValueError(
                        "Unknown VerifierType {}".format(self.verifier_type)
                    )
            matrix.append(row)
        return matrix

    def combined_keystroke_matrix(
        self,
        enroll_platform_id,
        probe_platform_id,
        enroll_session_id,
        probe_session_id,
        kit_feature_type,
    ):
        # if not 1 <= enroll_platform_id <= 3 or not 1 <= probe_platform_id <= 3:
        #     raise ValueError("Platform ID must be between 1 and 3")
        if not 1 <= kit_feature_type <= 4:
            raise ValueError("KIT feature type must be between 1 and 4")
        matrix = []
        ids = all_ids()
        for i in track(ids):
            df = get_user_by_platform(i, enroll_platform_id, enroll_session_id)
            kht_enrollment = create_kht_data_from_df(df)
            kit_enrollment = create_kit_data_from_df(df, kit_feature_type)
            combined_enrollment = kht_enrollment | kit_enrollment
            row = []
            for j in ids:
                df = get_user_by_platform(j, probe_platform_id, probe_session_id)
                kht_probe = create_kht_data_from_df(df)
                kit_probe = create_kit_data_from_df(df, kit_feature_type)
                combined_probe = kht_probe | kit_probe
                v = vl.Verify(combined_enrollment, combined_probe)
                if self.verifier_type == VerifierType.ABSOLUTE:
                    row.append(v.get_abs_match_score())
                elif self.verifier_type == VerifierType.SIMILARITY:
                    row.append(v.get_weighted_similarity_score())
                elif self.verifier_type == VerifierType.SIMILARITY_UNWEIGHTED:
                    row.append(v.get_similarity_score())
                elif self.verifier_type == VerifierType.ITAD:
                    row.append(v.itad_similarity())
                else:
                    raise ValueError(
                        "Unknown VerifierType {}".format(self.verifier_type)
                    )
            matrix.append(row)
        return matrix

    def plot_heatmap(self, matrix, title=None):
        ax = sns.heatmap(matrix, linewidth=0.5).set_title(title)
        plt.savefig(title)
