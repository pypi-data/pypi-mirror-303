class Array:
    def __init__(self, list_):
        if not all(isinstance(item, (int, float)) for item in list_):
            raise ValueError("All elements must be integers or floats.")
        self.list_ = list_

    def __add__(self, other):
        if isinstance(other, Array):
            if len(self.list_) != len(other.list_):
                raise ValueError("Arrays must have the same length for addition.")
            return Array([x + y for x, y in zip(self.list_, other.list_)])
        elif isinstance(other, (int, float)):
            return Array([x + other for x in self.list_])
        else:
            raise TypeError("Unsupported type for addition.")

    def __sub__(self, other):
        if isinstance(other, Array):
            if len(self.list_) != len(other.list_):
                raise ValueError("Arrays must have the same length for subtraction.")
            return Array([x - y for x, y in zip(self.list_, other.list_)])
        elif isinstance(other, (int, float)):
            return Array([x - other for x in self.list_])
        else:
            raise TypeError("Unsupported type for subtraction.")

    def __mul__(self, other):
        if isinstance(other, Array):
            if len(self.list_) != len(other.list_):
                raise ValueError("Arrays must have the same length for multiplication.")
            return Array([x * y for x, y in zip(self.list_, other.list_)])
        elif isinstance(other, (int, float)):
            return Array([x * other for x in self.list_])
        else:
            raise TypeError("Unsupported type for multiplication.")

    def __truediv__(self, other):
        if isinstance(other, Array):
            if len(self.list_) != len(other.list_):
                raise ValueError("Arrays must have the same length for division.")
            return Array([x / y for x, y in zip(self.list_, other.list_)])
        elif isinstance(other, (int, float)):
            return Array([x / other for x in self.list_])
        else:
            raise TypeError("Unsupported type for division.")

    def __repr__(self):
        return f"Array({self.list_})"

    def __str__(self):
        return str(self.list_)