def mm(p,n):
    m=[[0 for i in range(n)] for x in range(n)]
    s=[[0 for i in range(n)] for x in range(n)]
    for i in range(1,n):
        m[i][i]=0
    for l in range(2,n):
        for i in range(1,n-l+1):
            j=i+l-1
            m[i][j]=float('inf')
            for k in range(i,j):
                q=m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
                if q<m[i][j]:
                    m[i][j]=q
                    s[i][j]=k
    return m,s

def printmat(s,i,j):
    if i==j:
        print('A'+str(i),end=' ')
    else:
        print('(',end=' ')
        printmat(s,i,s[i][j])
        printmat(s,s[i][j]+1,j)
        print(')',end=' ')
arr = [0, 1, 2, 3, 4, 5, 6]
size = len(arr)

m, s = mm(arr, size)
printmat(s, 1, size - 1)
print("")