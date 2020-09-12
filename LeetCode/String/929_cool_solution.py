class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        seen = set()
        for email in emails:
            name, domain = email.split('@')
            local = name.split('+')[0].replace('.', '')
            #local = "".join(local.split('+')[0].split('.'))
            seen.add(local + '@' + domain)
        return len(seen)


if __name__ == '__main__':
    solution = Solution()
    print(solution.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))