import os
import statistics
import json
from classifiers.ecdf import ECDF


class Verify:
    def __init__(self, p1, p2, p1_t=10, p2_t=10):
        # p1 and p2 are dictionaries of features
        # keys in the dictionaries would be the feature names
        # feature names mean individual letters for KHT
        # feature names could also mean pair of letters for KIT or diagraphs
        # feature names could also mean pair of sequence of three letters for trigraphs
        # feature names can be extended to any features that we can extract from keystrokes
        self.pattern1 = p1
        self.pattern2 = p2
        self.pattern1threshold = (
            p1_t  # sort of feature selection, based on the availability
        )
        self.pattern2threshold = (
            p2_t  # sort of feature selection, based on the availability
        )
        with open(os.path.join(os.getcwd(), "classifier_config.json"), "r") as f:
            config = json.load(f)
        self.common_features = []
        if config["use_feature_selection"]:
            for feature in self.pattern1.keys():
                if feature in self.pattern2.keys():
                    if (
                        len(self.pattern1[feature]) >= self.pattern1threshold
                        and len(self.pattern2[feature]) >= self.pattern2threshold
                    ):
                        self.common_features.append(feature)
        else:
            self.common_features = set(self.pattern1.keys()).intersection(
                set(self.pattern2.keys())
            )
        # print(f"comparing {len(self.common_features)} common_features")

    def get_abs_match_score(self):  # A verifier
        if len(self.common_features) == 0:  # if there exist no common features,
            return 0
            # TODO: When running the performance_evaluation with cleaned2.csv, this ValueError gets proced
            raise ValueError("Error: no common features to compare!")
        matches = 0
        for (
            feature
        ) in self.common_features:  # checking for every common feature for match
            # print(f"feature:{feature}")
            # print(f"self.pattern1[feature]:{self.pattern1[feature]}")
            # print(f"self.pattern2[feature]:{self.pattern2[feature]}")

            pattern1_median = statistics.median(self.pattern1[feature])
            pattern2_median = statistics.median(self.pattern2[feature])
            if min(pattern1_median, pattern2_median) == 0:
                return 0  # Must look into and fix this! just a temporary arrangment
                # raise ValueError('min of means is zero, should not happen!')
            else:
                ratio = max(pattern1_median, pattern2_median) / min(
                    pattern1_median, pattern2_median
                )
            # the following threshold is what we thought would be good
            # we have not analyzed it yet!
            # try:
            #     threshold = max(self.pattern1[feature]) / min(self.pattern1[feature])
            # except ZeroDivisionError:
            #     threshold = 0
            threshold = 1.5  # hardcoding the threshold
            if ratio <= threshold:  # basically the current feature matches
                matches += 1
        return matches / len(self.common_features)

    def get_similarity_score(self):  # S verifier, each key same weight
        if len(self.common_features) == 0:  # if there exist no common features,
            return 0
            # raise ValueError("No common features to compare!")
        key_matches, total_features = 0, 0
        for feature in self.common_features:
            pattern1_median = statistics.median(list(self.pattern1[feature]))
            try:
                pattern1_stdev = statistics.stdev(self.pattern1[feature])
            except statistics.StatisticsError:
                # print("In error: ", self.pattern1[feature])
                if len(self.pattern1[feature]) == 1:
                    pattern1_stdev = self.pattern1[feature][0] / 4
                else:
                    pattern1_stdev = (
                        self.pattern1[feature] / 4
                    )  # this will always be one value that is when exception would occur

            value_matches, total_values = 0, 0
            for time in self.pattern2[feature]:
                if (pattern1_median - pattern1_stdev) < time and time < (
                    pattern1_median + pattern1_stdev
                ):
                    value_matches += 1
                total_values += 1
            if value_matches / total_values <= 0.5:
                key_matches += 1
            total_features += 1

        return key_matches / total_features

    def get_weighted_similarity_score(
        self,
    ):  # S verifier, each feature different weights
        if len(self.common_features) == 0:  # if there exist no common features,
            return 0
            # raise ValueError("No common features to compare!")
        matches, total = 0, 0
        for feature in self.common_features:
            enroll_mean = statistics.median(list(self.pattern1[feature]))
            try:
                template_stdev = statistics.stdev(self.pattern1[feature])
            except statistics.StatisticsError:
                # print("In error: ", self.pattern1[feature])
                if len(self.pattern1[feature]) == 1:
                    template_stdev = self.pattern1[feature][0] / 4
                else:
                    template_stdev = self.pattern1[feature] / 4

            for time in self.pattern2[feature]:
                if (enroll_mean - template_stdev) < time and time < (
                    enroll_mean + template_stdev
                ):
                    matches += 1
                total += 1
        return matches / total

    def get_median_of_common_key(self, key):
        if not key in self.common_features:
            raise ValueError(str(key) + " is not in common keys")
        return statistics.median(self.pattern1[key])

    def get_cdf_xi(self, distribution, sample):
        ecdf = ECDF(distribution)
        prob = ecdf(sample)
        # print('prob:', prob)
        return prob

    def itad_similarity(self):  # The new one
        # https://www.scitepress.org/Papers/2023/116841/116841.pdf
        if len(self.common_features) == 0:  # this wont happen at all, but just in case
            # print("dig deeper: there is no common feature to match!")
            return 0
        similarities = []
        for feature in self.common_features:
            M_g_i = statistics.median(self.pattern1[feature])
            for x_i in self.pattern2[feature]:
                if x_i <= M_g_i:
                    similarities.append(self.get_cdf_xi(self.pattern1[feature], x_i))
                else:
                    similarities.append(
                        1 - self.get_cdf_xi(self.pattern1[feature], x_i)
                    )
        return statistics.mean(similarities)

    def scaled_manhattan_distance(self):
        if (
            len(self.common_features) == 0
        ):  # this needs to be checked further when and why and for which users or cases it might hapens at all
            # print("dig deeper: there is no common feature to match!")
            return 0
        grand_sum = 0
        number_of_instances_compared = 0
        for feature in self.common_features:
            # print('comparing the feature:', feature)
            mu_g = statistics.mean(self.pattern1[feature])
            std_g = statistics.stdev(self.pattern1[feature])
            # print(f'mu_g:{mu_g}, and std_g:{std_g}')
            for x_i in self.pattern2[feature]:
                # print('x_i:', x_i)
                current_dist = abs(mu_g - x_i) / std_g
                # print('current_dist:', current_dist)
                grand_sum = grand_sum + current_dist
                # print('grand_sum:', grand_sum)
                number_of_instances_compared = number_of_instances_compared + 1
        # print('number_of_instances_compared', number_of_instances_compared)
        return grand_sum / number_of_instances_compared


if __name__ == "__main__":
    # local testing arrangment
    pattern1 = {
        "W": [210, 220, 200, 230, 210, 220, 200, 230, 210, 220, 200, 230],
        "E": [110, 70, 25, 30, 35, 70, 115, 107, 110, 115, 107, 110, 115, 107],
        "L": [150, 130, 190, 120, 150, 130, 190, 120],
        "C": [25, 30, 35, 70, 25, 30, 35, 70, 25, 30, 35, 70, 25, 30, 35, 70],
        "O": [90, 40, 49, 90, 40, 49, 90, 40, 49, 90, 40, 49],
    }
    pattern2 = {
        "W": [11, 12, 13, 14, 15, 16, 11, 12, 13, 14, 15, 16, 11, 12, 13, 14, 15, 16],
        "E": [
            25,
            30,
            35,
            70,
            25,
            30,
            35,
            70,
            70,
            25,
            30,
            35,
            70,
            70,
            25,
            30,
            35,
            70,
            25,
            30,
            35,
            70,
        ],
        "L": [1, 23, 21, 23, 43, 45, 64, 23, 43],
        "N": [9, 4, 12, 23, 21, 11, 9, 9, 4, 12, 23, 21, 11, 9],
        "S": [512, 621, 234, 257, 289, 512, 621, 234, 257, 289],
    }

    print("----------------local testing results--------------------")
    ExampleVerifier = Verify(pattern2, pattern1)
    print("itad_similarity() for diff patterns:", ExampleVerifier.itad_similarity())
    ExampleVerifier = Verify(pattern1, pattern1)
    print("itad_similarity() for same patterns:", ExampleVerifier.itad_similarity())
