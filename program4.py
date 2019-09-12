class admit():
    def __init__(self):
       self.__studentid=None
       self.__age=None
       self.__marks=None
    def validate_age(self):
        if self.__age>20:
            return True
        else:
            return False
    def validate_marks(self):
        if self.__marks in range(1,101):
            return True
        else:
            return False               
    def check_qualification(self):
         if self.validate_age() and self.validate_marks():
              if self.__marks>60:
                 return True
              else:
                 return False
         else:
             return False                
    def setter_method(self):
        self.__studentid=input('Enter the student id')
        self.__age=int(input('Enter the age'))
        self.__marks=int(input('Enter the marks'))
    def getter_method(self):
        print('STUDENT-ID:',self.__studentid)
        print('AGE:',self.__age)
        print('MARKS',self.__marks)
        if self.check_qualification():
            print('QUALIFIED FOR ADMISSION')
        else:
            print('NOT ELIGIBLE')
n=int(input('Enter the number of students:'))
stlist=[admit() for j in range(n)]
for i in  range(n):
    print('Enter details of student',(i+1))    
    stlist[i].setter_method()   
for i in  range(n):    
    stlist[i].getter_method()                      
