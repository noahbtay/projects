"""welcome to noahArray"""
"""lab2 cmsy257"""

class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fillValue = None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self.items = list()
        for count in range(capacity):
            self.items.append(fillValue)
        self.logicalSize = 0
        self.fillValue = fillValue
        
    def size(self):
        """returns size of array"""
        return self.logicalSize

    def grow(self):
        newCapacity = len(self.items) * 2
        for count in range(len(self.items), newCapacity):
            self.items.append(self.fillValue)

    def shrink(self):
        if self.logicalSize <= len(self.items) // 4:
            newCapacity = len(self.items) // 2
            self.items = self.items[:newCapacity]

    def insert(self, index, value):
        if self.logicalSize == len(self.items):
            self.grow()
        self.items.insert(index, value)
        self.logicalSize += 1
        
    def pop(self, index):
        if 0<= index < self.logicalSize:
            value = self.items.pop(index)
            self.items.append(self.fillValue)
            self.logicalSize -= 1
            if self.logicalSize <= len(self.items) //4:
                self.shrink()
            return value
        else:
            raise IndexError("Out of range")

    def __eq__(self, other):
        if isinstance(other, Array):
            return self.items == other.items and self.logicalSize == other.logicalSize
        return False

    def __len__(self):
        """-> The capacity of the array."""
        return len(self.items)

    def __str__(self):
        """-> The string representation of the array."""
        return str(self.items)

    def __iter__(self):
        """Supports iteration over a view of an array."""
        return iter(self.items)

    def __getitem__(self, index):
        """Subscript operator for access at index."""
        return self.items[index]

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index."""
        self.items[index] = newItem

noahArray = Array(6)
noahArrayWithFill = Array(21,10)

print(noahArray)
print(noahArrayWithFill)
