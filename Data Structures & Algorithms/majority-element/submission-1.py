class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        lista = {}
        for num in nums:
            lista[num] = lista.get(num, 0) + 1
        major = max(lista, key=lista.get)
        return major