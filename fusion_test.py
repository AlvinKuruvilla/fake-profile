import random
from classifiers.template_generator import all_ids
from fusion.decsion_fusion import get_actual_designation, is_fake_profile, verdict
from performance_evaluation.heatmap import VerifierType, get_user_by_platform
from features.keystroke_features import create_kht_data_from_df, create_kit_data_from_df
import classifiers.verifiers_library as vl
from rich.progress import track


def decision_fusion_test():
    correct = 0
    ids = all_ids()
    for _ in track(range(100)):
        enrollment = random.choice(ids)
        probe = random.choice(ids)
        df = get_user_by_platform(enrollment, 1, None)
        kht_enrollment = create_kht_data_from_df(df)
        kit_enrollment = create_kit_data_from_df(df, 1)
        combined_enrollment = kht_enrollment | kit_enrollment

        df = get_user_by_platform(probe, 1, None)
        kht_probe = create_kht_data_from_df(df)
        kit_probe = create_kit_data_from_df(df, 1)
        combined_probe = kht_probe | kit_probe
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


if __name__ == "__main__":
    decision_fusion_test()
