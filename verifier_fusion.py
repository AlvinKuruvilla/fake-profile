import random
import classifiers.verifiers_library as vl

from features.keystroke_features import create_kht_data_from_df, create_kit_data_from_df
from performance_evaluation.heatmap import VerifierType, get_user_by_platform


def verdict(similarity_score, verifier_type):
    if verifier_type == VerifierType.ABSOLUTE and similarity_score >= 0.8:
        return False
    elif verifier_type == VerifierType.SIMILARITY and similarity_score >= 0.8:
        return False
    elif verifier_type == VerifierType.ITAD and similarity_score >= 0.35:
        return False
    else:
        return True


def is_fake_profile(verdicts):
    genuine_count = verdicts.count(False)
    fake_profile_count = verdicts.count(True)
    if genuine_count > fake_profile_count:
        return "Genuine"
    else:
        return "Fake"


ids = [num for num in range(1, 26) if num != 22]
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
print(res)
