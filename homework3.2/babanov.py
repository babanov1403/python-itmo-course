import numpy as np

class KostblLMixin:
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value) -> None:
        self._data = value
    
    @property
    def shape(self) -> tuple:
        return self._data.shape
    
    @property
    def dtype(self) -> type:
        return type(self._data)

class Matrix(np.lib.mixins.NDArrayOperatorsMixin, KostblLMixin):
    def __init__(self, data):
        self.data = data
    
    def __str__(self):
        result = []
        for i in range(self._data.shape[0]):
            row_str = " ".join(f"{self.data[i][j]:.4f}" for j in range(self._data.shape[1]))
            result.append(f"[{row_str}]")
        return "\n".join(result)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        inputs = tuple(
            x.data if isinstance(x, Matrix) else x 
            for x in inputs
        )
        
        if kwargs.get('out'):
            kwargs['out'] = tuple(
                x.data if isinstance(x, Matrix) else x 
                for x in kwargs['out']
            )
        
        result = getattr(ufunc, method)(*inputs, **kwargs)
        return type(self)(result)

if __name__ == "__main__":
    np.random.seed(0)
    m1 = Matrix(np.random.randint(0, 10, (10, 10)))
    m2 = Matrix(np.random.randint(0, 10, (10, 10)))
    print("a+b:")
    print (m1 + m2)
    print()
    print("a*b")
    print (m1 * m2)
    print()
    print("a@b")
    print (m1 @ m2)