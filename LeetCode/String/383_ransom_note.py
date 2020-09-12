import collections
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for item in set(ransomNote):
            if magazine.count(item) < ransomNote.count(item):
                return False

        return True

    def canConstruct1(self, ransomNote, magazine):
        print(collections.Counter(ransomNote))
        print(collections.Counter(magazine))
        print(collections.Counter(ransomNote) - collections.Counter(magazine))
        return not collections.Counter(ransomNote) - collections.Counter(magazine)

    def canConstruct2(self, ransomNote, magazine):
        return all(ransomNote.count(char) <= magazine.count(char)
                   for char in set(ransomNote))


if __name__ == '__main__':
    solution = Solution()
    print(solution.canConstruct1('aaabc', 'aabc'))