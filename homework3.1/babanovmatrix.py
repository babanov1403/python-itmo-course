import numpy as np

class Matrix:
    def __init__(self, data):
        self.data = np.array(data, dtype=int)
        self.rows = self.data.shape[0]
        self.cols = self.data.shape[1]
    
    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("mismatched dimension")
        
        result_data = np.zeros((self.rows, self.cols))
        for i in range(self.rows):
            for j in range(self.cols):
                result_data[i][j] = self.data[i][j] + other.data[i][j]
        
        return Matrix(result_data)

    def __mul__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("mismatched dimension")

        result_data = np.zeros((self.rows, self.cols))
        for i in range(self.rows):
            for j in range(self.cols):
                result_data[i][j] = self.data[i][j] * other.data[i][j]
        
        return result_data
    
    def __matmul__(self, other):
        if self.cols != other.rows:
            raise ValueError("mismatched dimension multiplication")
        
        result_data = np.zeros((self.rows, other.cols))
        
        for i in range(self.rows):
            for j in range(other.cols):
                sum_val = 0
                for k in range(self.cols):
                    sum_val += self.data[i][k] * other.data[k][j]
                result_data[i][j] = sum_val
        
        return Matrix(result_data)
    
    def __eq__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return False
        
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False
        
        return True
    
if __name__ == "__main__":
    np.random.seed(0)
    m1 = Matrix(np.random.randint(0, 10, (10, 10)))
    m2 = Matrix(np.random.randint(0, 10, (10, 10)))
    print (m1 + m2)
    print (m1 * m2)
    print (m1 @ m2)