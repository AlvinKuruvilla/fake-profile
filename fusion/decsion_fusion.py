from classifiers.template_generator import all_ids
import classifiers.verifiers_library as vl

from features.keystroke_features import create_kht_data_from_df, create_kit_data_from_df
from performance_evaluation.heatmap import VerifierType, get_user_by_platform


def verdict(similarity_score, verifier_type):
    # We have individual empirically defined verdict thresholds for each verifier
    # print(verifier_type)
    # print(similarity_score)
    if verifier_type == VerifierType.ABSOLUTE and similarity_score >= 0.8:
        return False
    elif verifier_type == VerifierType.SIMILARITY and similarity_score >= 0.8:
        return False
    # I think with how we coded ITAD our perfect matches cap just about 0.25 and the non-matches are much lower
    # most likely this is because we set p to 0 implicitly
    elif verifier_type == VerifierType.ITAD and similarity_score >= 0.25:
        return False
    else:
        return True


def is_fake_profile(verdicts):
    # The verdicts then will determine if a profile is fake or not
    # and we take a simple majority to see whether the fake counts beat out the
    # genuine counts
    genuine_count = verdicts.count(False)
    fake_profile_count = verdicts.count(True)
    if genuine_count >= fake_profile_count:
        return "Genuine"
    return "Fake"


def get_actual_designation(enrollment_id, probe_id):
    # We define a genuine profile to have the same enrollment_id and probe_id
    if enrollment_id == probe_id:
        return "Genuine"
    return "Fake"


if __name__ == "__main__":
    ids = all_ids()
    for user_id in ids:
        enrollment = user_id
        probe = user_id
        df = get_user_by_platform(enrollment, 1, None)
        kht_enrollment = create_kht_data_from_df(df)
        kit_enrollment = create_kit_data_from_df(df, 1)
        combined_enrollment = kht_enrollment | kit_enrollment

        df = get_user_by_platform(probe, 1, None)
        kht_probe = create_kht_data_from_df(df)
        kit_probe = create_kit_data_from_df(df, 1)
        combined_probe = kht_probe | kit_probe
        v = vl.Verify(combined_enrollment, combined_probe)
        print("ID: " + str(enrollment) + " Score: " + str(v.itad_similarity()))
