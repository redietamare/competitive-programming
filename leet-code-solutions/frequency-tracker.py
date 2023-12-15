class FrequencyTracker:

    def __init__(self):
        self.count=defaultdict(int)
        self.freqhold=defaultdict(int)
    def add(self, number: int) -> None:
        prev=self.count[number]
        self.count[number]+=1
        self.freqhold[prev]-=1
        self.freqhold[self.count[number]]+=1
    def deleteOne(self, number: int) -> None:
        if self.count[number]:
            prev=self.count[number]
            self.freqhold[prev]-=1
            self.count[number]-=1
            self.freqhold[self.count[number]]+=1
    def hasFrequency(self, frequency: int) -> bool:
        if self.freqhold[frequency]>=1:
            return True
        return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)