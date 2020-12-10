class Matrix:
    
    def __init__(self):
        pass

    def main(self):
        print("1. Add matrices\
        \n2. Multiply matrix by a constant\
        \n3. Multiply matrices\
        \n4. Transpose matrix\
        \n5. Calculate a determinant\
        \n6. Inverse matrix\n0. Exit")
        print("Your choice:", end=' ')
        choice = input()
        while choice != '0':
            # try to use a dict
            if choice == '1':
                return self.matrix_add()
            if choice == '2':
                return self.matrix_add_const()
            if choice == '3':
                return self.matrix_multip()
            if choice == '4':
                return self.matrix_transpose_menu()
            if choice == '5':
            	return self.matrix_determinant()
            if choice == '6':
            	return self.inverse_matrix()
            else:
                print("Sorry, this option will be implemented soon", end='\n\n')
                return self.main()

    def formatting_output(self, answer):
        """ Formatting output for all the methods """
        print("The result is:")
        for i in answer:
            for j in i:
                print(j, end=' ')
            print()
        print()
        return self.main()

    def matrix_add(self):
        """
        Matrix addition
        x: first matrix; b: second matrix
        rows and columns of x must be equal
        to rows and columns of y respectively
        """
        print("Enter size of first matrix: ", end='')
        # if user input > or < than 2 elements (n_rows, n_cols)...
        # ...then give message of error
        n_rows_x, n_cols_x = map(int, input().split())
        print("Enter first matrix:")
        # what if in input 1 x 1 matrix -> not a good answer
        x = [[float(i) for i in input().split()] for _i in range(n_rows_x)]
        print("Enter size of second matrix: ", end='')
        n_rows_y, n_cols_y = map(int, input().split())
        print("Enter second matrix:")
        y = [[float(j) for j in input().split()] for _j in range(n_rows_y)]

        # check if number of columns in user's input of matrix
        # corresponds to size typed in input
        real_cols_x, real_cols_y = len(x[0]), len(y[0])
        if n_cols_x != real_cols_x and n_cols_y != real_cols_y:
            print("You entered more or less of columns than indicate in 'size' section")
            return self.main()

        if n_rows_x != n_rows_y or n_cols_x != n_cols_y:
            print("The operation cannot be performed.", end='\n\n')
            return self.main()
        
        # create a matrix 0 with same dimension than both matrix to add
        s = [[float(0) for _col in range(n_cols_x)] for _row in range(n_rows_x)]
        # addition of two matrix
        for i in range(n_rows_x):
            for j in range(n_cols_x):
                s[i][j] = x[i][j] + y[i][j]
        self.formatting_output(s)

    def matrix_add_const(self):
        print("Enter size of matrix: ", end='')
        # if user input > or < than 2 elements (n_rows, n_cols)...
        # ...then give message of error 
        n_rows, n_cols = [int(k) for k in input().split()]
        print("Enter matrix:")
        x = [[float(k) for k in input().split()] for _row in range(n_rows)]
        print("Enter constant: ", end='')
        constant = float(input())
        s = [[0 for _col in range(n_cols)] for _row in range(n_rows)]
        for i in range(n_rows):
            for j in range(n_cols):
                s[i][j] += x[i][j] * constant
        self.formatting_output(s)

    def matrix_multip(self):
        """
        Matrix multiplication
        The number of columns in the first matrix 
        should equal the number of rows for the second matrix
        The multiplication of X matrix with n rows and m columns 
        and Y matrix with m rows and k columns is Sn,k = Xn,m × Ym,k
        The resulting matrix has n rows and k columns
        """
        print("Enter size of first matrix: ", end='')
        n_rows_x, n_cols_x = map(int, input().split())
        print("Enter first matrix:")
        x = [[float(i) for i in input().split()] for _ in range(n_rows_x)]
        print("Enter size of second matrix: ", end='')
        n_rows_y, n_cols_y = map(int, input().split())
        print("Enter second matrix:")
        y = [[float(j) for j in input().split()] for _ in range(n_rows_y)]

        if n_cols_x != n_rows_y:
            print("This operation cannot be performed.", end='\n\n')
            return self.main()

        # create a matrix 0 with same dimension than both matrix to add
        # (answer's shape = rows of the fist x columns of the second)
        s = [[0 for _col in range(n_cols_y)] for _row in range(n_rows_x)]
        # addition of two matrix
        # i: row; j: i[col]
        for i in range(n_rows_x):
            for j in range(n_cols_y):
                for k in range(n_cols_x):
                    s[i][j] += x[i][k] * y[k][j]
        self.formatting_output(s)

    def matrix_transpose_menu(self):
        """ Transpose matrix menu """
        print()
        print("1. Main diagonal\n2. Side diagonal\
        \n3. Vertical line\n4. Horizontal line")
        print("Your choice: ", end='')
        transp_choice = input()
        if transp_choice == '1':
            return self.transp_main_diag()
        if transp_choice == '2':
            return self.transp_side_diag()
        if transp_choice == '3':
            return self.transp_vert_line()
        if transp_choice == '4':
            return self.transp_horiz_line()
        print("Not a correct choice. Do again", end='\n\n')
        return self.main()

    def transp_main_diag(self):
        print("Enter matrix size: ", end='')
        rows, cols = map(int, input().split())
        print("Enter matrix:")
        x = [[int(i) for i in input().split()] for _i in range(rows)]
        s = [[0 for _col in range(cols)] for _row in range(rows)]
        for i in range(rows):
            for j in range(cols):
                s[i][j] += x[j][i]
        self.formatting_output(s)

    def transp_side_diag(self):
        print("Enter matrix size: ", end='')
        rows, cols = map(int, input().split())
        print("Enter matrix:")
        x = [[int(i) for i in input().split()] for _i in range(rows)]
        s = [[0 for _col in range(cols)] for _row in range(rows)]
        for i in range(rows):
            for j in range(cols):
                s[i][j] = x[cols-j-1][cols-i-1]
        self.formatting_output(s)
    
    def transp_vert_line(self):
        print("Enter matrix size: ", end='')
        rows, cols = map(int, input().split())
        print("Enter matrix:")
        x = [[int(i) for i in input().split()] for _i in range(rows)]
        for i in range(rows):
            for j in range(cols//2):
                x[i][j], x[i][cols-j-1] = x[i][cols-j-1], x[i][j]
        self.formatting_output(x)

    def transp_horiz_line(self):
        print("Enter matrix size: ", end='')
        rows, cols = map(int, input().split())
        print("Enter matrix:")
        x = [[int(i) for i in input().split()] for _i in range(rows)]
        for i in range(rows//2):
            for j in range(cols):
                x[i][j], x[rows-i-1][j] = x[rows-i-1][j], x[i][j]
        self.formatting_output(x)

    def matrix_determinant(self):
    	print("Coming soon")
    	return self.main()

    def inverse_matrix(self):
    	print('Comin soon')
    	return self.main()

    def trace_matrix(self):
        print("Coming soon")
        return self.main()


a = Matrix()
a.main()
