class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lista = {}
        result = []
        for num in nums:
            lista[num] = lista.get(num, 0) + 1
        for i in range(k):
            maximum = max(lista, key=lista.get)
            result.append(maximum)
            del lista[maximum]
        return result