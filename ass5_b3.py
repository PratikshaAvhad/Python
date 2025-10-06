#Write a Python Program to Create a Class Set and Get All Possible Subsets 
#from a Set of Distinct Integers.

class MySet:
    def __init__(self, elements):
        self.elements = elements

    
    def get_subsets(self, current=[], index=0):
        if index == len(self.elements):
            print(current)
            return
       
        self.get_subsets(current + [self.elements[index]], index + 1)
       
        self.get_subsets(current, index + 1)



nums = list(map(int, input("Enter distinct integers: ").split()))
myset = MySet(nums)

print("All possible subsets are:")
myset.get_subsets()
