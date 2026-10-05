class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset=set()
        colset=set()
        boxset=set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]!=".":
                    
                    if (i,board[i][j]) not in rowset and (j,board[i][j]) not in colset and (i//3,j//3,board[i][j]) not in boxset:
                        
                        rowset.add((i,board[i][j]))
                        colset.add((j,board[i][j]))
                        boxset.add((i//3,j//3,board[i][j]))
                        # print(i,j,rowset,colset,boxset)
                    else:
                        print(i,j)
                        return False
        return True