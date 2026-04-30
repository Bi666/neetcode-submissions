class MyHashSet:

    def __init__(self):
        self.array = [[] for _ in range(1000)]

    def add(self, key: int) -> None:
        if key not in self.array[key % 1000]:
            self.array[key % 1000].append(key)

    def remove(self, key: int) -> None:
        if key in self.array[key % 1000]:
            self.array[key % 1000].remove(key)
        
    def contains(self, key: int) -> bool:
        if key in self.array[key % 1000]:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)