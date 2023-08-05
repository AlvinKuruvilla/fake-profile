import random
import os
from classifiers.template_generator import all_ids
from experiments import print_k_table
from features.word_parser import SentenceParser
from fusion.decsion_fusion import get_actual_designation, is_fake_profile, verdict
from fusion.score_fusion import FusionAlgorithm, ScoreFuser
from performance_evaluation.heatmap import HeatMap, VerifierType, get_user_by_platform
from features.keystroke_features import (
    create_kht_data_from_df,
    create_kit_data_from_df,
    word_hold,
)
import classifiers.verifiers_library as vl
from rich.progress import track


def decision_fusion_test():
    correct = 0
    ids = all_ids()
    for _ in track(range(100)):
        enrollment = random.choice(ids)
        probe = random.choice(ids)
        df = get_user_by_platform(enrollment, 1, None)
        sp = SentenceParser(os.path.join(os.getcwd(), "cleaned2.csv"))
        word_list = sp.get_words(df)
        word_hold_enrollment = word_hold(word_list, df)
        kht_enrollment = create_kht_data_from_df(df)
        kit_enrollment = create_kit_data_from_df(df, 1)
        combined_enrollment = kht_enrollment | kit_enrollment | word_hold_enrollment

        df = get_user_by_platform(probe, 1, None)
        kht_probe = create_kht_data_from_df(df)
        kit_probe = create_kit_data_from_df(df, 1)
        word_list = sp.get_words(df)
        word_hold_probe = word_hold(word_list, df)
        combined_probe = kht_probe | kit_probe | word_hold_probe
        v = vl.Verify(combined_enrollment, combined_probe)
        print("Enrollment:" + str(enrollment))
        print("Probe:" + str(probe))
        verdicts = []
        verdicts.append(verdict(v.get_abs_match_score(), VerifierType.ABSOLUTE))
        verdicts.append(verdict(v.get_similarity_score(), VerifierType.SIMILARITY))
        verdicts.append(verdict(v.itad_similarity(), VerifierType.ITAD))
        res = is_fake_profile(verdicts)
        if res == get_actual_designation(enrollment, probe):
            correct += 1
    print("Correct fusion classifications = " + str(correct / 100))


def score_fusion_test(fusion_algorithm: FusionAlgorithm):
    itad_heatmap = HeatMap(VerifierType.ITAD)
    itad_matrix = itad_heatmap.combined_keystroke_matrix(1, 2, None, None, 1)
    similarity_heatmap = HeatMap(VerifierType.SIMILARITY)
    similarity_matrix = similarity_heatmap.combined_keystroke_matrix(
        1, 2, None, None, 1
    )
    absolute_heatmap = HeatMap(VerifierType.ABSOLUTE)
    absolute_matrix = absolute_heatmap.combined_keystroke_matrix(1, 2, None, None, 1)
    sf = ScoreFuser(itad_matrix, similarity_matrix, absolute_matrix)
    res = sf.find_matrix(fusion_algorithm)
    ids = all_ids()
    print(fusion_algorithm)
    print_k_table(matrix=res, ids=ids)
    print(
        "________________________________________________________________________________________________________________________________"
    )


def platform_fusion_cross_test():
    heatmap = HeatMap(VerifierType.SIMILARITY)
    similarity_matrix = heatmap.combined_keystroke_matrix(3, 2, None, None, 1)
    heatmap = HeatMap(VerifierType.ABSOLUTE)
    absolute_matrix = heatmap.combined_keystroke_matrix(3, 2, None, None, 1)
    heatmap = HeatMap(VerifierType.ITAD)
    itad_matrix = heatmap.combined_keystroke_matrix(3, 2, None, None, 1)
    sf = ScoreFuser(itad_matrix, similarity_matrix, absolute_matrix)
    for fusion_algorithm in FusionAlgorithm:
        res = sf.find_matrix(fusion_algorithm)
        ids = all_ids()
        print(fusion_algorithm)
        print("T vs. I")
        print_k_table(matrix=res, ids=ids)


if __name__ == "__main__":
    platform_fusion_cross_test()
