def lcs_length_table_formulation(X, Y):
    m = len(X)
    n = len(Y)

    # Initialize tables C and B
    C = [[0] * (n + 1) for _ in range(m + 1)]
    B = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                C[i][j] = C[i - 1][j - 1] + 1
                B[i][j] = 'D'
            else:
                if C[i - 1][j] >= C[i][j - 1]:
                    C[i][j] = C[i - 1][j]
                    B[i][j] = 'U'
                else:
                    C[i][j] = C[i][j - 1]
                    B[i][j] = 'L'

    return C, B

def print_lcs(B, X, i, j):
    if i == 0 or j == 0:
        return
    if B[i][j] == 'D':
        print_lcs(B, X, i - 1, j - 1)
        print(X[i - 1], end=' ')
    elif B[i][j] == 'U':
        print_lcs(B, X, i - 1, j)
    else:
        print_lcs(B, X, i, j - 1)

# Example usage:
X = input("Enter the first sequence: ")
Y = input("Enter the second sequence: ")
 
C, B = lcs_length_table_formulation(X, Y)
print("Length of Longest Common Subsequence:", C[len(X)][len(Y)])

print("Longest Common Subsequence:")
print_lcs(B, X, len(X), len(Y))

