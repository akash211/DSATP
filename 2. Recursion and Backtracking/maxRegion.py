def getval(A, i, j, L, H):
    if (i < 0 or i >= L or j >= H):
        return 0
    else:
        return A[i][j]

def findMaxBlock(A, r, c, L, H, size):
    global max_size_result
    global cntarr
    if (r >= L or c >= H):
        return
    cntarr[r][c] = 1
    size += 1
    if (size > max_size_result):
        max_size_result = size
    #search in eight directions
    direction = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]    
    for i in range(7):
        newi = r + direction[i][0]
        newj = c + direction[i][1]
        val = getval(A, newi, newj, L, H)
        if (val > 0 and (cntarr[newi][newj] == 0)):
            findMaxBlock(A, newi, newj, L, H, size)
    cntarr[r][c] = ()    

def getMaxOnes(A, rmax, colmax):
    global max_size_result
    global size
    global cntarr
    for i in range(rmax):
        for j in range(colmax):
            if (A[i][j] == 1):
                findMaxBlock(A, i, j, rmax, colmax, 0)       
    return max_size_result

zarr = [[1,1,0,0,0],[0,1,1,0,1],[0,0,0,0,0],[1,0,0,1,1],[0,1,0,1,1]]
print("zarr: ",zarr)
rmax = 5
colmax = 5
max_size_result = 0
size = 0
cntarr = rmax*[colmax*[0]]
print("\nNumber of maximum 1s are ",getMaxOnes(zarr, rmax, colmax))