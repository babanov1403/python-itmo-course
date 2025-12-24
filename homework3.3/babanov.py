import numpy as np

class Matrix:
    _cache = {}

    def __init__(self, data):
        self.data = np.array(data, dtype=int)
        self.rows = self.data.shape[0]
        self.cols = self.data.shape[1]
    
    def __str__(self):
        result = []
        for i in range(self.data.shape[0]):
            row_str = " ".join(f"{self.data[i][j]:.4f}" for j in range(self.data.shape[1]))
            result.append(f"[{row_str}]")
        return "\n".join(result)

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
        
        # if other in self._cache:
        #     return self._cache[other]

        result_data = np.zeros((self.rows, other.cols))
        
        for i in range(self.rows):
            for j in range(other.cols):
                sum_val = 0
                for k in range(self.cols):
                    sum_val += self.data[i][k] * other.data[k][j]
                result_data[i][j] = sum_val
        # self._cache[other] = Matrix(result_data)
        return Matrix(result_data)
    
    def __eq__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return False
        
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False
        
        return True

    def __hash__(self) -> int:
        return int(self.data[0][0]) % 2
    
if __name__ == "__main__":
    np.random.seed(0)
    t = 0
    while True:
        print(t)
        t+= 1
        a = Matrix(np.random.randint(0, 20, (3, 3)))
        b = Matrix(np.random.randint(0, 20, (3, 3)))
        c = Matrix(np.random.randint(0, 20, (3, 3)))
        d = b
        if hash(a) == hash(c) and (a != c) and (b == d) and (a @ b != c @ d):
            print(a)
            print()
            print(b)
            print()
            print(c)
            print()
            print(d)
            print()
            print(a @ b)
            print()
            print(c @ d)
            print()
            print(hash(a @ b), hash(c @ d))
            break
    