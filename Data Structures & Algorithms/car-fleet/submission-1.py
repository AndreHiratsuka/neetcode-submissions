class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        # now its sorted by the position of the car
        count = 0
        before = 0
        for p, s in pair:
            steps = ((target-p))/s
            if steps > before:
                count += 1
                before = steps
        return count