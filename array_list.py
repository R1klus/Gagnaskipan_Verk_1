class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass

class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.count = 0
        self.arr = [0]*self.capacity

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        return_string = ""
        for i in range(self.count-1):
            return_string += str(self.arr[i])+","
        return_string += str(self.arr[self.count-1])
        return return_string

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def append(self, value):
        if self.count == self.capacity:
            self.resize()
        self.arr[self.count] = value
        self.count += 1

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def get_first(self):
        if self.count > 0:
            return self.arr[0]
        else:
            return None

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def get_last(self):
        if self.count > 0:
            return self.arr[self.count-1]
        else:
            return None

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        self.capacity = 2*self.capacity
        new_arr = [0]*self.capacity
        for i in range(self.count):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def clear(self):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def insert_ordered(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def remove_value(self, value):
        # TODO: remove 'pass' and implement functionality
        pass


if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_lis = ArrayList()
    arr_lis.append(1)
    arr_lis.append(2)
    arr_lis.append(3)
    arr_lis.append(4)
    arr_lis.append(5)
    
    print(str(arr_lis))