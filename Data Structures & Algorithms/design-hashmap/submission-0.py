class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.hashmap = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        bucket = self.hashmap[self._hash(key)]

        for i, kv in enumerate(bucket):
            if kv[0] == key:
                bucket[i][1] = value
                return
        bucket.append([key, value])


    def get(self, key: int) -> int:
        bucket = self.hashmap[self._hash(key)]

        for kv in bucket:
            if kv[0] == key:
                return kv[1]
        return -1

    def remove(self, key: int) -> None:
        bucket = self.hashmap[self._hash(key)]

        for i, kv in enumerate(bucket):
            if kv[0] == key:
                del bucket[i]
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)