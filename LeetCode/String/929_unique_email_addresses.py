class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        for i in range(len(emails)):
            each = list(emails[i])
            new_each = []
            index = each.index('@')
            j = 0
            while each[j] != '@':
                if each[j] == '.':
                    j += 1
                elif each[j] == '+':
                    break
                else:
                    new_each.append(each[j])
                    j += 1
            new_each.extend(each[index:])
            emails[i] = ''.join(new_each)


        return len(set(emails))

if __name__ == '__main__':
    solution = Solution()
    print(solution.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))