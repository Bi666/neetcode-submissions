class MyHashMap:

    def __init__(self):
        self.array = [[] for _ in range(2069)]

    def put(self, key: int, value: int) -> None:
        arr = self.array[key % 2069]
        for i in range(len(arr)):
            if arr[i][0] == key:
                arr[i][1] = value
                return
        arr.append([key, value])

    def get(self, key: int) -> int:
        arr = self.array[key % 2069]
        for i in range(len(arr)):
            if arr[i][0] == key:
                return arr[i][1]
        return -1

    def remove(self, key: int) -> None:
        arr = self.array[key % 2069]
        for i in range(len(arr)):
            if arr[i][0] == key:
                arr.pop(i)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)