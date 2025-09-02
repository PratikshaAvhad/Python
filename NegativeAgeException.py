class NegativeAgeException(RuntimeError):
    def _init_(self,msg):
        self.msg=msg

try:
    n=int(input("enter age"))
    if(n<0):
        raise negativeAgeException("invalid age")
    print("valid age=",n)
except NegativeAgeException as e:
    print("error=",e)
