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
        self.ordered = self.checkIfOrdered()
    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        return_string = ""
        for x in range(self.count):
            return_string += "{}, ".format(self.arr[x])
        return return_string[:-2]

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        if self.count == self.capacity:
            self.resize()
        if self.count == 0:
            self.arr[0] = value
        else:
            for i in range(self.count, 0, -1):
                self.arr[i] = self.arr[i-1]
            self.arr[0] = value
        self.count += 1
            
        
        
    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        if index <= self.count and index >= 0:
            if self.count == self.capacity:
                self.resize()
            
            for i in range(self.count, index, -1):
                self.arr[i] = self.arr[i-1]
            self.count += 1
            self.set_at(value, index)
            
        else:
            raise IndexOutOfBounds()

    #Time complexity: O(1) - constant time
    def append(self, value):
        if self.count == self.capacity:
            self.resize()
        self.arr[self.count] = value
        self.count += 1

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        if self.count > 0 and index < self.count and index >= 0:
            self.arr[index] = value
        else:
            raise IndexOutOfBounds()

    #Time complexity: O(1) - constant time
    def get_first(self):
        if self.count > 0:
            return self.arr[0]
        else:
            raise Empty()

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        if self.count > 0 and index < self.count and index >= 0:
            return self.arr[index]
        else:
            raise IndexOutOfBounds()

    #Time complexity: O(1) - constant time
    def get_last(self):
        if self.count > 0:
            return self.arr[self.count-1]
        else:
            raise Empty()

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        self.capacity = 2*self.capacity
        new_arr = [0]*self.capacity
        for i in range(self.count):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        if 0 <= index and index < self.count:
            self.count -= 1
            for i in range(index, self.count):
                self.set_at(self.arr[i+1], i)            
        else:
            raise IndexOutOfBounds()

    #Time complexity: O(1) - constant time
    def clear(self):
        self.count = 0

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def insert_ordered(self, value):
        if self.checkIfOrdered():
            if value <= self.arr[0]:
                self.prepend(value)
            elif value >= self.arr[self.count-1]:
                self.append(value)
            else:
                for i in range(self.count):
                    if self.arr[i] <= value <= self.arr[i+1]:
                        self.insert(value, i+1)
                        break
        else:
            raise NotOrdered()

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        if self.checkIfOrdered():
            returnVal = self.__binarySearch(0, self.count-1, value)
        else:
            returnVal = self.__linearSearch(value)
        if returnVal != False or type(returnVal).__name__ == "int":
            return returnVal
        else:
            raise NotFound()

    def __linearSearch(self, value, index = 0):
        if index < self.count:
            if value == self.arr[index]:
                return index
            else:
                return self.__linearSearch(value, index+1)
        else:
            return False    

    def __binarySearch(self, start, end, value):
        if end >= start:
            middle = start + ((end-start)//2)
            if self.arr[middle] == value:
                return middle
            elif self.arr[middle] > value:
                return self.__binarySearch(start, middle-1, value)
            else:
                return self.__binarySearch(middle+1, end, value)
        return False

        

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def remove_value(self, value):
        index = self.find(value)
        self.remove_at(index)

    def checkIfOrdered(self, index = 0):
        for x in range(self.count-1):
            if self.arr[x]>self.arr[x+1]:
                return False
        return True
                    
          



if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level
    
    the_list = [10, 11, 12, 13, 13, 13, 14, 15, 15, 16, 18, 18, 18, 19, 22, 22, 23, 24, 24, 25, 27, 28, 28, 28, 29, 29, 29, 29, 30]
    arr_lis = ArrayList()
    for x in the_list:
        arr_lis.append(x)
    arr_lis.remove_value(10)
    # arr_lis = ArrayList()
    # print(arr_lis)
    # arr_lis.prepend(2)
    # arr_lis.prepend(23)
    print(arr_lis)