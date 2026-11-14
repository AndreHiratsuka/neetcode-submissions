class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        step = 0
        count = 0
        for child in g:
            while step < len(s):
                if s[step] >= child:
                    count += 1
                    step += 1
                    print(f"deu {child}")
                    break
                else:
                    step += 1 
        return count