from collections import Counter

def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    res = []
    pCounter = Counter(p)
    sCounter = Counter(s[:len(p)-1])
    for i in range(len(p)-1,len(s)):
        sCounter[s[i]] += 1   # include a new char in the window
        if sCounter == pCounter:    # This step is O(1), since there are at most 26 English letters
            res.append(i-len(p)+1)   # append the starting index
        sCounter[s[i-len(p)+1]] -= 1   # decrease the count of oldest char in the window
        if sCounter[s[i-len(p)+1]] == 0:
            del sCounter[s[i-len(p)+1]]   # remove the count if it is 0
    return res

def findAnagrams_1(s, p):  #basic idea, need to understand
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    hash = {}  # hash stores the list of characters we need to cross-off. Initially has all of p in it
    for c in p:
        if c in hash:
            hash[c] += 1
        else:
            hash[c] = 1
    count = len(p)  # number of characters still to be crossed-off

    # initialize
    result = []
    left = 0  # the current candidate is s[left:right+1]
    right = 0
    while right < len(s):
        # for every iteration, check if current character is a desired char. if so, cross it off.
        # otherwise, move on to the next character
        if s[right] in hash:
            hash[s[right]] -= 1
            # If we have a negative hash value(meaning more than enough of that particular character),
            # it means we are not getting any closer to the solution, so, count should not change
            if hash[s[right]] >= 0:
                count -= 1

        # print 'left=', left, 'right=', right, 'count=', count, 'hash=', hash, 'cur_window=',
        # s[left:right+1]
        # if all items are crossed-off, add to result list
        if count == 0:
            result.append(left)

        # Move window only if the minimum size is met.
        if right == left + len(p) - 1:
            # If the char we are getting rid of is already in the hash, increment the hash
            # (add to the items that we need to cross-off)
            if s[left] in hash:
                # If the hash (number of items we need to cross-off) is negative(i.e we have had
                # double chars in out current window), do not increment the required count
                if hash[s[left]] >= 0:
                    count += 1
                hash[s[left]] += 1
            left += 1
        right += 1

    return result


findAnagrams_1('cbaebabacd', 'abc')
# findAnagrams('abab', 'ab')