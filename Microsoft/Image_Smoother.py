class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        ans = [[0] * n for _ in range(m)] 

        for i in range(m):
            for j in range(n):
                total = 0  
                count = 0

                for x in (i-1,i,i+1):
                    for y in (j-1,j,j+1):
                        if 0 <= x < m and 0 <= y < n:
                            total += img[x][y]
                            count += 1

                ans[i][j] = total // count  
        return ans
