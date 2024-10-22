def common_prefix_length(list1: list, list2: list):
    i = 0
    while i < len(list1) and i < len(list2) and list1[i] == list2[i]:
        i += 1
    return i
