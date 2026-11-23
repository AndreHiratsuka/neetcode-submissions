class Solution:
    def searchMatrix(
        self,
        matrix: List[List[int]],
        target: int
    ) -> bool:


        rows = len(matrix)
        columns = len(matrix[0])

        # Use zero-based positions.
        low = 0
        high = rows * columns - 1

        while low <= high:
            mid = (low + high) // 2

            # Convert the virtual 1-D position into:
            # row = quotient
            # column = remainder
            row = mid // columns
            column = mid % columns

            value = matrix[row][column]

            if value == target:
                return True

            elif value > target:
                high = mid - 1

            else:
                low = mid + 1

        return False