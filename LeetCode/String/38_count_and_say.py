class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        else:
            sequence =  self.digui("1")
            for i in range(2,n):
                sequence = self.digui(sequence)
            return sequence

    def digui(self, sequence):
        new_string = ""
        count = 1
        coutinuious = False
        for i in range(len(sequence)):
            if i != len(sequence) - 1:
                if sequence[i] == sequence[i+1]:
                    count +=1
                    coutinuious = True
                else:
                    new_string = new_string + str(count) + sequence[i]
                    coutinuious = False
                    count = 1
            else:
                if coutinuious == False:
                    new_string = new_string + "1" + sequence[len(sequence)-1]
                else:
                    new_string = new_string + str(count) + sequence[i]
        return new_string

    def countAndSay_1(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return str(n)
        former = ['1']
        for i in range(1, n):
            left, right = 0, len(former) - 1
            length = 1
            while left <= right:
                if left == len(former) - 1 or former[left] != former[left + 1]:
                    former.insert(left, str(length))
                    length = 1
                    left, right = left + 2, right + 1
                else:
                    length += 1
                    former.pop(left + 1)
                    right -= 1
        return ''.join(former)






if __name__=="__main__":
    solution = Solution()
    print(solution.countAndSay_1(6))
