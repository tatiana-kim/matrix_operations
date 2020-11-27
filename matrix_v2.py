class Matrix:
    
    def __init__(self):
        pass

    
    def main(self):
        print("1. Add matrices\
        \n2. Multiply matrix by a constant\
        \n3. Multiply matrices\n0. Exit")
        print("Your choice:", end=' ')
        choice = input()
        while choice != '0':
            if choice == '1':
                return self.matrix_add()
            if choice == '2':
                return self.matrix_add_const()
            if choice == '3':
                return self.matrix_multip()
            else:
                print("Sorry, this option will be implemented soon", end='\n\n')
                return self.main()
        return 0
    
    
    def matrix_add(self):
        '''
        Matrix addition
        x: first matrix; b: second matrix
        rows and columns of x must be equal
        to rows and columns of y respectively
        '''
        print("Enter size of first matrix: ", end='')
        n_rows_x, n_cols_x = map(int, input().split())
        print("Enter first matrix:")
        x = [[int(i) for i in input().split()] for i in range(n_rows_x)]
        print("Enter size of second matrix: ", end='')
        n_rows_y, n_cols_y = map(int, input().split())
        print("Enter second matrix:")
        y = [[int(j) for j in input().split()] for j in range(n_rows_y)]
        
        if n_rows_x != n_rows_y or n_cols_x != n_cols_y:
            print("The operation cannot be performed.", end='\n\n')
            return self.main()
        
        # create a matrix 0 with same dimension than both matrix to add
        s = [[0 for col in range(n_cols_x)] for row in range(n_rows_x)]
        # addition of two matrix
        for i in range(n_rows_x):
            for j in range(n_cols_x):
                s[i][j] = x[i][j] + y[i][j]
        # formating output:
        print('The result is:')
        for k in s:
            for r in k:
                print(r, end=' ')
            print()
        print()
        return self.main()
    
    
    def matrix_add_const(self):
        print("Enter size of matrix: ", end='')
        n_rows, n_cols = [int(k) for k in input().split()]
        print("Enter matrix:")
        x = [[int(k) for k in input().split()] for row in range(n_rows)]
        print("Enter constant: ", end='')
        constant = int(input())
        s = [[0 for col in range(n_cols)] for row in range(n_rows)]
        for i in range(n_rows):
            for j in range(n_cols):
                s[i][j] += x[i][j] * constant
        print('The result is:')
        for k in s:
            for r in k:
                print(r, end=' ')
            print()
        print()
        return self.main()
    
    
    def matrix_multip(self):
        print("Sorry, this option will be implemented soon", end='\n\n')
        return self.main()


a = Matrix()
a.main()
