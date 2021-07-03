def merge(nums1, nums2):
    merged = [0] * (len(nums1) + len(nums2))
    first1 = first2 = 0
    for i in range(len(nums1) + len(nums2)):
        if first1 != len(nums1) and (first1 == len(nums2)) or nums1[first1] < nums2[first2]:
            merged[i] = nums1[first1]
            first1 += 1
        else:
            merged[i] = nums2[first2]
            first2 += 1
    return merged
