class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        indxs = deque()
        for i in range(len(deck)):
            indxs.append(i)
        ans = [0]*len(deck)
        deck.sort()

        for i in range(len(deck)):
            val = indxs.popleft()
            ans[val] = deck[i]
            if indxs:   
                indxs.append(indxs.popleft())
        return ans