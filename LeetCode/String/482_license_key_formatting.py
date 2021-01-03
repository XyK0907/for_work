class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        attached = ''.join(S.split('-')).upper()[::-1]
        ll = [attached[i: i+K] for i in range(len(attached)) if i % K == 0]

        return '-'.join(ll)[::-1]

    def licenseKeyFormatting_cool_solution(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace("-", "").upper()[::-1]
        return '-'.join(S[i:i+K] for i in range(0, len(S), K))[::-1]

if __name__ == '__main__':
    solution = Solution()
    print(solution.licenseKeyFormatting('5F3Z-2e-9-w', 3))