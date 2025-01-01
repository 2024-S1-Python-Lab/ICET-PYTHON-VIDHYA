class Rectangle:
  def__init__(self,l,b)
    self.__length=1
    self.__breadth=b
  def getdimensions(self):
   return self.__length,self.__breadth
  def getarea(self):
   return self._length*self.__breadth
  def__it__(self,other):
   ifself.getarea()<other.getarea():
     return"1st rectangle is smaller"
  else:
     return"2nd rectangle is smaller"
length1=int(input("enter the 1st rectangle length:"))
breadth1=int(input("enter the 1st rectangle breadth:"))
ar1=Rectangle(length1,breadth1)
length2=int(input("enter the 2nd rectangle length:"))
breadth2=int(input("enter the 2nd rectangle breadth:"))
ar2=Rectangle(length2,breadth2)
print("area of 1st rectangle={ar1.getarea()}&area of 2nd rectangle={ar2.getarea()}")
print(ar1<ar2)

    
