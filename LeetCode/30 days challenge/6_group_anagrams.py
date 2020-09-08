class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for each in strs:
            new_key = ''.join(sorted(each))
            if new_key not in dic.keys():
                dic[new_key] = [each]
            else:
                dic[new_key].append(each)
        return dic.values()


if __name__ == '__main__':
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))