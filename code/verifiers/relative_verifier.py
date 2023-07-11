from verifiers.verifier import Verifier


def max_disorder(n):
    return ((n * n)) / 2 if n % 2 == 0 else ((n * n) - 1) / 2


class RelativeVerifier(Verifier):
    def __init__(self, raw_template, raw_verification):
        super().__init__(raw_template, raw_verification)

    def keys_for_template_and_verification(self):
        return (list(self.enroll.keys()), list(self.verification.keys()))

    # The disorder is calculated as the difference in position between all of the matching keys
    # between the template and the verification attempt
    # Then that value is divided by the max disorder.
    # For the unigraphs I believe it is just one less than the number of
    # matching keys squared (though I'm not 100% certain of that)
    # For digraphs it is the same as unigraphs except divided by 2
    def calculate_disorder(self):
        matching_keys = self.get_all_matching_keys()
        disorder = 0
        if len(matching_keys) == 0:
            return 0
        template_keys, verification_keys = self.keys_for_template_and_verification()
        for key in matching_keys:
            disorder = disorder + abs(
                template_keys.index(key) - verification_keys.index(key)
            )
        print(max_disorder(1))
        print(len(matching_keys))
        return disorder / max_disorder(len(matching_keys))
