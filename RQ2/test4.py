def base_case(self):
        nums1 = [1, 3]
        nums2 = [2]
        result = medianSortedArrays(nums1, nums2)
        self.assertEqual(result, 2)