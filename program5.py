class CallDetail:
    def __init__(self):
       self.calling_num=None
       self.called_num=None
       self.duration=None
       self.type=None
class Util:
     def __init__(self):
         self.list_of_call_objects=[]
         self.std=0
         self.isd=0
         self.local=0
     def parse_customer(self,list_of_call_string):
          for i in range(len(list_of_call_string)):
              obj=CallDetail()
              l=list_of_call_string[i].split(',')
              obj.calling_num=l[0]
              obj.called_num=l[1]
              obj.duration=l[2]
              obj.type=l[3]
              self.list_of_call_objects.append(obj)
     def display(self):
          for i in range(len(self.list_of_call_objects)):
               print('Calling number:',self.list_of_call_objects[i].calling_num)
               print('Called number:',self.list_of_call_objects[i].called_num)
               print('Duration:',self.list_of_call_objects[i].duration)
               print('Type:',self.list_of_call_objects[i].type,end='\n\n')
               if self.list_of_call_objects[i].type=='STD':
                    self.std+=1
               elif self.list_of_call_objects[i].type=='ISD':
                    self.isd+=1 
               elif self.list_of_call_objects[i].type=='Local':
                    self.local+=1 
               print('Number of STD calls:',self.std)
               print('Number of Local calls:',self.local)
               print('Number of ISD calls:',self.isd)            
     def person_details(self):
           p=input('Enter the phone number whose detail is needed:') 
           for i in range(len(self.list_of_call_objects)):        
                 if self.list_of_call_objects[i].calling_num==p:
                     print('Called number:',self.list_of_call_objects[i].called_num)
                     print('Duration:',self.list_of_call_objects[i].duration)
                     print('Type:',self.list_of_call_objects[i].type)
                     print('---------------------------')
'''call='9990000001,9330000001,23,STD'
call2='9990000003,9330000002,54,Local'
call3='9990000001,9330000003,6,STD'''
n=int(input('Enter the number of calls:'))
list_of_call_string=[]
print('Enter call details[calling number,called number,duration,type]')
for _ in range(n):
   c=input()
   list_of_call_string.append(c)
Util_obj=Util()
Util_obj.parse_customer(list_of_call_string)                    
Util_obj.display()
Util_obj.person_details()
