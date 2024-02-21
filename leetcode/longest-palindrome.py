class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = defaultdict(int)
        for i in s:
            hashmap[i] += 1
        length = 0
        for i in hashmap:
            if hashmap[i]%2 == 0:
                length += hashmap[i]
            else:
                length += hashmap[i] - 1
        for i in hashmap:
            if hashmap[i]%2==1:
                length += 1
                break
        return length