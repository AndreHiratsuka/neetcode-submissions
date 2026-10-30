class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        lista = {}
        count = 1
        # base case
        max_count = 1
        for num in nums:
            lista[num] = lista.get(num, 0) + 1
        for index, numb in enumerate(lista):
            aux = numb
            # if it has a number below, we dont even consider
            if numb-1 in lista:
                continue
            while aux+1 in lista:
                aux += 1
                count += 1
            if count > max_count:
                max_count = count
            count = 1
        return max_count