class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        row=0
        col=0
        row_temp=0
        ans=0
        count=0
        for length in board:
            col_temp=0
            for width in length:
                if width=="R":
                    col=col_temp
                    break
                col_temp+=1
            if col>0:
                row=row_temp
                break
            row_temp+=1
        row_count=0
        for i in board[row]:
            if i=="p" and row_count<col:
                count=1
            elif i=="B" and row_count<col:
                count=0
            elif i=="p" and row_count>col:
                count+=1
                break
            elif i=="B" and row_count>col:
                break
            row_count+=1
        ans+=count
        col_count=0
        count=0
        for i in board:
            if i[col]=="p" and col_count<row:
                count=1
            if i[col]=="B" and col_count<row:
                count=0
            if i[col]=="p" and col_count>row:
                count+=1
                break
            if i[col]=="B" and col_count>row:
                break
            col_count+=1
        ans+=count
        return ans