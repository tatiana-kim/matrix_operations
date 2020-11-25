print("What operation with matrix?")
print("Addition: 1\nScalar multiplication: 2\nMultiplication: 3\
Transpose: 4\nFinde the trace: 5\nIvertible: 6\nDeterminant: 7\
Substraction: 8")
print("Please, input the code of operation:")
code = input()


def matrix_add(x, y):
    '''
       Matrix addition
       x: first matrix; b: second matrix
       rows and columns of x must be equal
       to rows and columns of y respectively
    '''
    n_rows_x, n_cols_x = len(x), len(x[0])
    n_rows_y, n_cols_y = len(y), len(y[0])
    if (n_rows_x == n_rows_y) and (n_cols_x == n_cols_y):
        # create a matrix 0 with same dimension than both matrix to add
        s = [[0 for col in range(n_cols_x)] for row in range(n_rows_x)]
        # addition of two matrix
        for i in range(n_rows_x):
            for j in range(n_cols_x):
                s[i][j] = x[i][j] + y[i][j]
        return s
    else:
        return "ERROR"


def matrix_subst(x, y):
    '''
       Matrix substraction
       x: first matrix; b: second matrix
       rows and columns of x must be equal
       to rows and columns of y respectively
    '''
    pass



def matrix_scalar_mult(x, scalar, n_rows, n_cols):
    s = [[0 for col in range(n_cols)] for row in range(n_rows)]
    for i in range(n_rows):
        for j in range(n_cols):
            s[i][j] += x[i][j] * scalar
    return f'A * scalar = , {s}'


def matrix_mult(x, y):
    '''
       Multiplication of two matrices
       x: first matrix with will be multiplicated by y
       y: second matrix
    '''
    pass


def matrix_transp(x):
    '''
       Transpose matrix
       x: matrix to transpose
    '''
    pass


def matrix_trace(x):
    '''
       Calculate trace of the matrix
       x: matrix
    '''
    pass


def matrix_invertible(x):
    '''
       Invert matrix
       x: matrix to invert
    '''
    pass


def matrix_determinant(x):
    '''
       Calculate the matrix' determinant
    '''
    pass


def main(code):
    if code == '1':
        # number of rows and columns for 1st matrix and create 1sr matrix
        print("Number of rows and columns for first matrix:")
        n_rows_x, n_cols_x = [int(k) for k in input().split()]
        print("Input the first matrix A:")
        x = [[int(k) for k in input().split()] for row in range(n_rows_x)]

        print("Number of rows and columns for second matrix:")
        # number of rows and columns for 2nd matrix and create 2nd matrix
        n_rows_y, n_cols_y = [int(k) for k in input().split()]
        print("Input the second matrix B:")
        y = [[int(k) for k in input().split()] for row in range(n_rows_y)]

        print("A + B =", matrix_add(x, y))

    elif code == '2':
        print("Number of rows and cols for matrix: ")
        n_rows, n_cols = [int(k) for k in input().split()]
        print("Input matrix:")
        a = [[int(k) for k in input().split()] for row in range(n_rows)]
        print("Scalar:")
        scalar = int(input())
        print(matrix_scalar_mult(a, scalar, n_rows, n_cols))

    else
        print("Sorry, this function is not available yet")


main(code)
