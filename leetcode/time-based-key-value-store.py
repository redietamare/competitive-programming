class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append(str(timestamp) + "_" + value)

    def get(self, key: str, timestamp: int) -> str:
        arr = self.hashmap[key]
        l = 0
        r = len(arr) -1
        ans = ""
    
        while l <= r:
            mid = (l + r)//2
            listt = arr[mid].split("_")
            val = int(listt[0])
            if val <= timestamp:
                ans = listt[1]
                l = mid + 1
            else:
                r = mid - 1
        return ans



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)