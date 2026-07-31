class Value:
    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self.grad = 0.0
        self._backward = lambda: None
        # how to propagate gradient backward
        self._prev = set(_children)
        # parent nodes in the graph
        self._op = _op
        # which operation produced this value
    def __repr__(self):
        return f"Value(data={self.data}, grad={self.grad}))"