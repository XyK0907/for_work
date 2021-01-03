class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B) or A == '' or B == '':
            return False
        if A == B and len(A) == len(set(A)):
            return False

        count = 0
        diff_a = []
        diff_b = []
        for i in range(len(A)):
            if A[i] != B[i]:
                count += 1
                diff_a.append(A[i])
                diff_b.append(B[i])
            if count > 2:
                return False
        if count == 1:
            return False
        else:
            if count == 0:
                return True
            else:
                return set(diff_b) == set(diff_a)

    def buddyStrings_brute_force(self, A, B):
        import itertools
        if len(A) != len(B): return False
        if A == B:
            seen = set()
            for a in A:
                if a in seen:
                    return True
                seen.add(a)
            return False
        else:
            pairs = []
            for a, b in itertools.izip(A, B):
                if a != b:
                    pairs.append((a, b))
                if len(pairs) >= 3: return False
            return len(pairs) == 2 and pairs[0] == pairs[1][::-1]

    def buddyStrings_cool_solution(self, A, B):
        if len(A) != len(B): return False
        if A == B and len(set(A)) < len(A): return True
        dif = [(a, b) for a, b in zip(A, B) if a != b]
        return len(dif) == 2 and dif[0] == dif[1][::-1]



if __name__ == '__main__':
    solution = Solution()
    print(solution.buddyStrings('ab', 'ba')) #true
    print(solution.buddyStrings('ab', 'ab')) #false
    print(solution.buddyStrings('aa', 'aa')) #true
    print(solution.buddyStrings('aaaaaaabc', 'aaaaaaacb')) #true
    print(solution.buddyStrings('', 'aa')) #false
    print(solution.buddyStrings('','')) #false
