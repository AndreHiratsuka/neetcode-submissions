class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # take the value of the last one to the loop
        greater = arr[-1]
        for i in range(len(arr)-1, -1, -1):
            # take the value of the current position
            curr = arr[i]
            # then, update the current value
            arr[i] = greater
            # if the current value is greater, update the greater value
            if curr > greater:
                greater = curr
        arr[-1] = -1
        return arr
