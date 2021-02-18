class Ressizable_array(object):
    def __init__(self):
        self.pointer = 0
        self.i = 0
        self.size = 1        #Initial Size of the Array

        self.array = [None for i in range(self.size)]   #Initial Array


    #Add element at the desire index
    def insert(self, index, value):
        counter = len(self.array)
        if self.i == self.size:   #checking that the Array is Full or not
            self.Resize()
        if index > len(self.array):
            self.array[counter] = value
        elif self.array[index] == None:
            self.array[index] = value
        else:
            for i in range(self.size - 1, index, -1): #Reverse Loop
                self.array[i] = self.array[i - 1]  #Push the Element to make the room for new one
            self.array[index] = value
        self.pointer += 1
        self.i += 1



    #Return teh reduced by 1 size of the Array use in SHrink Function
    def size_call(self):
        return self.size - 1

    #Remove the Element from the desire Index
    def Remove(self, index):

        if index >= self.pointer:
            print('array index out of range')
        else:
            self.array[index] = None

            for i in range(index, self.pointer - 1): #Reverse Loop
                self.array[i] = self.array[i + 1] #Pushing the ELement Backword After removing
                # print(i)

            self.array[self.pointer - 1] = None
            self.pointer -= 1
            self.i -= 1
            self.shrink()

    #Increase the size of the Array means increase presvious size + 1
    def Resize(self):
        self.size += 1
        new_array = [None] * self.size     #Creating new Array double the size of previous one
        i = 0
        j = 0

        while j < self.i:
            new_array[i] = self.array[j]  #Adding the Element of the previous Array into the new Array
            i += 1
            j += 1
        self.array = None
        self.array = new_array


    def shrink(self):
        self.size = self.size_call()
        new_array = [None] * self.size   #Creating new Array
        i = 0
        j = 0
        while j < self.i:
            new_array[i] = self.array[j]  #Adding the Element of the previous Array into the new Array
            i += 1
            j += 1
        self.array = None
        self.array = new_array

    #Set the ELement At the Given index
    def set(self,index,value):
        if index<=self.size:
            if self.array[index]==None:
                self.array[index]=value
                self.pointer+=1
            else:
                self.array[index]=value
        else:
            print("Your index is not present")

    #Get the Value of the given Index
    def Get(self, i):

        if self.array[i]==None:
            print("index out of range")

        else:
            print(self.array[i])


    #Total Count of the Element
    def Count(self):
        print(self.pointer)

    #This function return the max element in the array
    def maxElement(self):
        lst = [-1]
        # first loop is run only for fisrt element in the array
        for i in range(len(self.array)):
            # second loop is run for all element in the array
            for j in range(len(self.array) - 1, -1, -1):
                # this condition check that all elements in array is greater or equal to first element in the array
                if self.array[i] <= self.array[j]:
                    # this condition check that the fisrt if condtion give element is greater then or not the element present in lst1 list
                    # if not then check other element in array
                    if lst[-1] < self.array[j]:
                        # if True then pop the element and append the array element
                        lst.pop(0)
                        lst.append(self.array[j])
                        break

        return lst[-1]
    #This function return the min element in the array
    def minElement(self):

        lst1 = [float('inf')]
        # first loop is run only for fisrt element in the array
        for i in range(len(self.array)):
            # second loop is run for all element in the array
            for j in range(len(self.array)-1, -1, -1):
                # this condition check that all elements in array is less or equal to first element in the array
                if self.array[i] >= self.array[j]:
                    # this condition check that the fisrt if condtion give element is less then or not the element present in lst1 list
                    # if not then check other element in array
                    if self.array[j] < lst1[-1]:
                        # if True then pop the element and append the array element
                        lst1.pop(0)
                        lst1.append(self.array[j])
                        break

        return lst1[-1]


a=Ressizable_array()
# -------------insert-----------------------
a.insert(0,5)
a.insert(10,7)
a.insert(0,5)
a.insert(0,5)
a.insert(0,5)


#--------------Set-----------------
a.set(4,9)
a.set(3,9)
#--------------Get---------------
a.Get(2)
a.Get(3)
a.Get(4)
a.Get(1)

#-------------Remove-----------
# a.Remove(2)
# a.Remove(2)
# a.Remove(2)
# a.Remove(1)

#--------------Printing Array--------
print(a.array)
#-------------print max element-------------------
print(a.maxElement())
#-------------print min element-------------------
print(a.minElement())




#This project is done by Syed Abdul Ali and Muhammad Zeeshan Khan
