class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        bottom=len(matrix)-1
        r=len(matrix[0])-1
        top=l=0
        res=[]
        while(l<=r) and (top<=bottom):
            for i in range(l,r+1):
                res.append(matrix[top][i])
            top+=1
            for i in range(top,bottom+1):
                res.append(matrix[i][r])
            r-=1
            if top<=bottom:
                for i in range(r,l-1,-1):
                    res.append(matrix[bottom][i])
                bottom-=1
            if l<=r:
                for i in range(bottom,top-1,-1):
                    res.append(matrix[i][l])
                l+=1
        return res