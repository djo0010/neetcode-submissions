class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.checkRows(board) and self.checkCols(board) and self.checkSquares(board)
            
    def checkRows(self, board: List[List[str]]) -> bool:
        for row in board:
            nums = defaultdict(int)
            for num in row:
                if num in nums:
                    return False
                self.placeNum(nums, num)
        return True

    
    def checkCols(self, board: List[List[str]]) -> bool:
        for i in range(9):
            nums = defaultdict(int)
            for j in range(9):
                if board[j][i] in nums:
                    return False
                self.placeNum(nums, board[j][i])
        return True

    def checkSquares(self, board: List[List[str]]) -> bool:
        for i in range(0, 6, 3):
            for j in range(0,6,3):
                if not self.checkSquare(board, i, j):
                    return False
        return True
    
    def checkSquare(self, board: List[List[str]], x: int, y: int) -> bool:
        nums = defaultdict(int)
        for i in range(3):
            for j in range(3):
                if board[x + i][y + j] in nums:
                    return False
                self.placeNum(nums, board[x + i][y + j])
        return True

    def placeNum(self, nums: defaultdict, element: int):
        if element == ".":
            return
        nums[element] = element
