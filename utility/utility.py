import math
def find_pairs(list1, list2):
    # Sort the lists to optimize the algorithm
    list1.sort()
    list2.sort()

    result = []

    # Find the smaller list and its length
    if len(list1) >= len(list2):
        smaller_list = list2.copy()
        larger_list = list1.copy()
        larger_list.append(math.inf)

        ind_s = 0
        ind_l = 0

        while ind_s < len(smaller_list):
            if float(larger_list[ind_l]) <= float(smaller_list[ind_s]) and ind_l < len(larger_list) - 1:
                ind_l += 1

            else:
                # print(larger_list[ind_l-1])
                if (larger_list[ind_l - 1] != math.inf):
                    result.append((int(larger_list[ind_l - 1]), int(smaller_list[ind_s])))
                    smaller_list.remove((smaller_list[ind_s]))
                    larger_list.remove((larger_list[ind_l - 1]))
                ind_s += 1

            if ind_l == len(larger_list):
                break

        return result, larger_list, smaller_list

    else:
        smaller_list = list1.copy()
        larger_list = list2.copy()

        ind_s = 0
        ind_l = 0

        while ind_s < len(smaller_list):
            if float(larger_list[ind_l]) <= float(smaller_list[ind_s]) and ind_l < len(larger_list) - 1:
                ind_l += 1

            else:
                result.append((int(smaller_list[ind_s]), int(larger_list[ind_l])))
                smaller_list.remove((smaller_list[ind_s]))
                larger_list.remove((larger_list[ind_l]))
                ind_s += 1

            if ind_l == len(larger_list):
                break
        return result, smaller_list, larger_list