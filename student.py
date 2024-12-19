class Student:
  def get(self,rlno,name,totalmark):
      self.rlno=rlno
      self.name=name
      self.totalmark=totalmark
  def disp(self):
      print(f"roll number:{self.rlno}")
      print(f"name:{self.name}")
      print(f"totalmark:{self.totalmark}")
stud1=Student()
stud1.get()
stud1.disp()
      
    
