# def cap(para):
#   new =''
#   for i in range(len(para)):
#     if para[i]=='i' and para[i-1]==' ' and para[i+1]==' ':
#       new+=para[i]
#     else:
#       new+=para[i]  
#   return new     
# a = 'my favourite animal is a dog. a dog has sharp teeth so that it can eat flesh very easily. do you know my pet dog’s name? i love my pet very much.' 
# print(cap(a))

# string = 'ApplE'
# upper = 0
# lower = 0 
# for i in string:        
#     if ord(i)>=65 and ord(i)<=90:
#         upper += 1            
#     if ord(i)>=97 and ord(i)<=122: 
#         lower += 1 
# if upper > lower :
#     print(string.upper())
# else:
#     print(string.lower())

# s1 = "coDIng"
# upper = 0
# lower = 0 
# for i in range(len(s1)-1,0,-1):        
#     if ord('A')<=ord(s1[i])<=ord('Z'):
#         upper= i
#         break
# print(upper)
# for i in s1:
#     if i>= 'A' and i<= 'Z':
        
#         if not inBetween:
            
#             inBetween = True
#             continue
        
#         else:
            
#             inBetween = False
#             break
#     if inBetween:
#         s2 += i

# if len(s2) == 0:
#     print('BLANK')

# else:    
#     print(s2)
# l1=[]
# for i in range(1):
#     n = input('e = ')
#     k= n.split(' ')
# print(k)
# lst1 = []
# while True:
#     user_imp = input("Enter the list:")
#     if user_imp != "STOP":
#         lst1.append(user_imp)
#     else:
#       var =user_imp.split(' ')
# lst1=['1','4','2','3']
# lst2=[]
# for j in range(0,len(lst1)-1):
#   m = abs(int(lst1[j])-int(lst1[j+1]))
#   lst2.append(m)
#   for x in lst2:
#     if all(x<=(len(lst1)-1)):
#       print('Ub')
#     else:
#       print('no')      

# dict1 = {}
# user_inp = input("key:value pairs :").split(",")
# for i in user_inp:
#     k, v = i.split(":")
#     dict1[k] = v
# my_dict = {}
# for k, v in dict1.items():
#     if v not in my_dict:
#         my_dict[v] = [k]
#     else:
#         my_dict[v]+=[k]
# print(my_dict)
# dict1 = {
#     '1': ['.', ',', '?', '!', ':'],
#     '2': ['A', 'B', 'C'],
#     '3': ['D', 'E', 'F'],
#     '4': ['G', 'H', 'I'],
#     '5': ['J', 'K', 'L'],
#     '6': ['M', 'N', 'O'],
#     '7': ['P', 'Q', 'R', 'S'],
#     '8': ['T', 'U', 'V'],
#     '9': ['W', 'X', 'Y', 'Z'],
#     '0': [' ']}
# user_imp = input('Enter a message:')
# for i in user_imp.upper():
#     for k, v in dict1.items():
#         if i in v:
#           print(k*(v.index(i)+1),end='')

# sum=0
# new_sum=0
# m=5
# n=10
# diff=n-m
# for i in range(1,diff+1):
#   sum=0
#   # prev_sum = new_sum
#   for j in range(1,5):
#     sum+=j
#   sum+=i*(m)+(m+i)
#   print(sum,end=' ')
# sum=0
# for j in range(1,5):
#   sum+=j
# print(sum)
# dict1={'a': 100, 'b': 100, 'c': 200, 'd': 300}
# dict2={'a': 300, 'b': 200, 'd': 400, 'e': 200}
# d= {}
# s = 0
# for keys,values in dict1.items():
#   if keys in dict2.keys(): 
#         s = dict1[keys] + dict2[keys]
#         d[keys]=s
#   else:
#     d[keys]=dict1[keys]
# for keys,values in dict2.items():
#   if keys in dict1.keys(): 
#         s = dict1[keys] + dict2[keys]
#         d[keys]=s
#   else:
#     d[keys]=dict2[keys]
# print(d)
# m=[]
# for i in range(2):
#   lst =input('enter = ').split(' ')
#   lst = [int(item) for item in lst]
#   m.append(lst)
# lar = sum(m[0])
# larlst = m[0]
# print(lar)
# print(larlst)

# print(char)
# c=0
# par = [0,4,5,1,0]

# n = 6
# g = 5
# t =0
# player = input('Par = ').split()
# team = [int(i) for i in player]
# for i in range (len(team)-1):
#   if team[i]==5:
#     team.pop(i)
# for i in team:
#   sum = i+g
#   if sum<=5:
#     t +=1
# print(t//3)
# d = {
#     1: ['.', ',', '?', '!', ':'],
#     2: ['A', 'B', 'C'],
#     3: ['D', 'E', 'F'],
#     4: ['G', 'H', 'I'],
#     '5': ['J', 'K', 'L'],
#     '6': ['M', 'N', 'O'],
#     '7': ['P', 'Q', 'R', 'S'],
#     '8': ['T', 'U', 'V'],
#     '9': ['W', 'X', 'Y', 'Z'],
#     '0': [' ']}
# s='Hello, World!'
# for i in s.upper():
#   for j in d.values():
#     if i in j:
#       c = 0
#       for x in j:
#         if i==j:
#           c+=1
#           break

#         else:
#           c+=1
#       print(d[j]*c,end='')
# n='madam'
# def fun(n):
#   s=''
#   for i in n:
#     if i!='':
#       s+=i
#   if s[::-1] ==s:
#     print('pa')
#   else:
#     print('no')
# fun(n)
# from curses.ascii import islower

# n=''
# v='h,'
# for i in range(len(v)):
#     if v[i]>='A' and v[i]<='Z':
#       n+=v[i+1::len(v)]
# print(len(v))
# li=[1,2,1]
# l=[]
# l = list(dict.fromkeys(li))
# print(l)

# class UberEats():
#     def __init__ (self,name,num,loc):
#         self.name=name
#         self.num=num
#         self.loc=loc
#         print(f"{self.name} welcome to UberEats!")
#         print('=========================')
#     def add_items(self,ord1,ord2,price1,price2):
#         self.ord1=ord1
#         self.ord2=ord2
#         self.price1=price1
#         self.price2=price2
#         print(f'user details: Name:{self.name},Phone: {self.num},Address:{self.loc},Orders:{dict({self.ord1:self.price1,self.ord2:self.price2})}')
# order1 = UberEats("Shakib", "01719658xxx", "Mohakhali")
# print("=========================")
# order1.add_items("Burger", "Coca Cola", 220, 50)
# print("=========================")
# print(order1.print_order_detail())
# print("=========================")
# order2 = UberEats ("Siam", "01719659xxx", "Uttara")
# print("=========================")
# order2.add_items("Pineapple", "Dairy Milk", 80, 70)
# print("=========================")
# print(order2.print_order_detail())

# {dict((self.ord1,self.price1),dict{(self.ord2,self.price2)})}')
# a='h'
# b='e'
# j=dict(a='h',b='e')
# print(j)

# l=[10,20,10]
# li={}
# for i in l:
#   if i not in li:
#     li[i]=1
#   else:
#     li[i]=li[i]+1
    
#     # li.append(i)
#     # y = l.count(i)
#     # # l.append(y)
# print(li)
# d1={'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value1'}
# d2={}
# for v in d1.values():
#   if v not in d2:
#     l=[]
#     for k in d1:
#       if d1[k]==v:
#         l.append(k)
#     d2[v]=l
# print(d2)
# class Human:

#   def __init__(self):
#     self.age = 0
#     self.height = 0.0

# h1 = Human()
# h2 = Human()
# h1.age = 21
# h1.height = 5.5
# print(h1.age)
# print(h1.height)
# h2.height = h1.height - 3
# print(h2.height)
# h2.age = h1.age
# h1.age += h1.age
# print(h1.age)
# h2 = h1
# print(h2.age)
# print(h2.height)
# h1.age += h1.age
# h2.height += h2.height
# print(h1.age)
# print(h1.height)
# h2.age += h2.age
# h1.age = h2.age
# print(h2.age)
# import math
# # using pi
# a = math.sin(math.pi/2)
# print(a)
# # using radians
# b = math.sin(math.radians(90))
# print(b)
# d = {
#     1: ['.', ',', '?', '!', ':'],
#     2: ['A', 'B', 'C'],
#     3: ['D', 'E', 'F'],
#     4: ['G', 'H', 'I'],
#     5: ['J', 'K', 'L'],
#     6: ['M', 'N', 'O'],
#     7: ['P', 'Q', 'R', 'S'],
#     8: ['T', 'U', 'V'],
#     9: ['W', 'X', 'Y', 'Z'],
#     0: [' ']}
# s='Hello, World!'
# s= s.upper()
# r=''
# for i in s:
#   l=''
#   for k,v in d.items():
#     for j in range(0,len(v)):
#         if i==v[j]:
#           l=str(k)*(j+1)
#   r+=l
# print(r)
# b='baNgladEsh'
# f=''
# o=''
# for i in range(len(b)):
#   if b[i]>='A' and b[i]<='Z':
#     f+=b[i+1:i:len(b)]
#     break

# for j in range(len(f)):
#   if f[j]>='A' and f[j]<='Z':
#     o+=f[:j:]
#     break
# if o=='':
#   print('blank')
# else:
#   print(o)

# class Programmer:
#   def __init__(self,info,salary='Pending for HR approval'):
#     # if '_' in info:
#     details = info.split("-")
#     self.name = details[0]
#     self.designation = details[1]
#     self.salary = salary
#     print('Programmer created successfully.')
  
#   def extraDuty(self,time):
#     if time =='Day':
#       return f"Sorry, salary won't increase for {self.name}"
#     elif  time =='Night':
#       self.salary = self.salary + 100

#   def setSkill(self, *args):
#     self.setSkill = args

#   def showInfo(self):
#     print('Name: ', self.name)
#     print('Designation: ', self.designation)
#     print('Salary: ', self.salary)
#     skills=''
#     for i in self.setSkill:
#       skills+=i+','
#     print('Skills:',skills[:-1])
#   def setSalary(self,value):
#     self.salary = value


# programmer_info = []
# joy = Programmer("Joy-junior Software Engineer", 50000)
# print(joy.extraDuty("Day"))
# joy.setSkill("c++", "java")
# print("1====================")
# joy.showInfo()
# print("2====================")
# anik = Programmer("anik-Software Engineer", 60000)
# print("3====================")
# anik.extraDuty("Night")
# anik.setSkill("c++", "java", "python")
# anik.showInfo()
# print("4====================")
# programmer_info.append(Programmer("luna-Senior Software Engineer"))
# programmer_info[0].setSkill("c++", "java", "python", "ruby")
# programmer_info[0].showInfo()
# print("5====================")
# programmer_info[0].setSalary(70000)
# print("6====================")
# programmer_info[0].showInfo()

# class Player:
#   def __init__(self,info,sal="Information not found"):
#     self.info_list = info.split(",")
#     if len(self.info_list)==1:
#       self.name=self.info_list[0]
#     if len(self.info_list)==2:
#       self.name=self.info_list[0]
#       self.club=self.info_list[1]
#     if len(self.info_list)==3:
#       self.name=self.info_list[0]
#       self.club=self.info_list[1]
#       self.country=self.info_list[1]

#     self.sal = sal
#     print("Player created successfully.")

#   def signAdvertisement(self, brand=None):
#     if brand == 'Nike':
#       self.sal = self.sal + 200
#       return f"Hooray! Salary updated for {self.name}."
#     elif brand == 'Adidas':
#       self.sal = self.sal + 100
#       return f"Hooray! Salary updated for {self.name}."
#     elif brand == None:
#       self.sal = self.sal

#   def setSkill(self, *skills):
#     self.skills = skills
#     self.dict1 = {}
#     if len(skills) == 3:
#       self.dict1[1] = skills[0]
#       self.dict1[2] = skills[1]
#       self.dict1[3] = skills[2]
#     elif len(skills) == 2:
#       self.dict1[1] = skills[0]
#       self.dict1[2] = skills[1]
#     elif len(skills) == 1:
#       self.dict1[1] = skills[0]

#   def playerInfo(self):
#     print(f"Name: {self.name}\nClub: {self.club}\nCountry: {self.country}\nSalary: {self.sal}\nSkills: {self.dict1}")
  
#   def setSalary(self, newsal):
#     self.sal = newsal

# messi = Player("Messi,PSG,Argentina",60000)
# print(messi.signAdvertisement("Nike"))
# messi.setSkill("Dribble","Body Faint","Shooting")
# print("1====================")
# messi.playerInfo()
# print("2====================")
# neymar = Player("Neymar,PSG,Brazil",50000)
# print("3====================")
# neymar.signAdvertisement("Adidas")
# neymar.setSkill("Neymar turn", "Rollover")
# neymar.playerInfo()
# print("4====================")
# haaland = Player("Haaland,ManCity,Norway")
# haaland.setSkill("Acrobatic moves")
# haaland.playerInfo()
# print("5====================")
# haaland.setSalary(40000)
# print("6====================")
# haaland.playerInfo()
# s = input("")
# l = len(s)
# c = ""
# a = ""
# d = ""
# for i in s:
#   if 97<=ord(i)<=122:
#     c+=i
#   elif 65<=ord(i)<=90:
#     c+=i
#   elif (48<=ord(i)<=57):
#     d += i
#   elif (33<=ord(i)<=47):
#     a += i
#   else:
#     continue

# print("Character:", c)
# print("Digit:", d)
# print("Alphabet:", a)

# s = 'This-is-CSE110'
# s1=''
# for i in s:

#   if i!='-':
#     s1= s1 + i#cse110
  
#   elif i =='-':
#     print(s1)
#     s1=''
# print(s1)

# s=0
# for i in range(1,6):
#   s = s+i 
# print(s)

# s= 'CSE110'
# n = 3
# s1=''
# # if n%2==0:
# #   print(s*(n*2))
# # else:
# #   print(s*(n*3))
# for i in range(n):
#   if n%2==0:
#     s1 += s*2
#   else:
#     s1 += s*3
# print(s1)

# n= 11
# r=''
# while n!=0:
#   r+= str((n)%2)
#   n = n//2 
# print(r[::-1])
# print(14//2)

# s = '0, 0, 1, 2, 3, 4,      4, 5, 6, 6, 6,      7, 8, 9, 4,         4'
# print(s.strip( ))
# def remove(string):
#     return "".join(string.split())
     
# print(remove(s))
# snew = s.split()
# print(snew)



# if self.power>m2.power:
#             print(f'Attack successful. {self.name} defeated {m2.name}.')
#             Monster.monsterCount-=1
#             m2.alive=False
#           else:
#             print(f'Attack unsuccessful. {self.name} was defeated by {m2.name}.')
# class Monster:
#   monsterCount = 0
#   def __init__(self,name, power):
#     self.name = name
#     self.power = power
#     self.alive = True
#     Monster.monsterCount+=1
#   def get_details(self):
#     return f"Name: {self.name}\nPower: {self.power}\nAlive: {self.alive}"

#   def check(self,second):
#     if self.power>second.power:
#       print(f'Attack successful. {self.name} defeated {second.name}.')
#       Monster.monsterCount-=1
#       second.alive=False
#     else:
#       print(f'Attack unsuccessful. {self.name} was defeated by {second.name}.')
#       Monster.monsterCount-=1
#       self.alive=False

#   def attack(self,*args):

#     if self.alive == True:
#       if len(args) == 0:
#         print('No monsters to attack')

#       elif len(args) == 1:

#         m2 = args[0]
#         if m2.alive == True:
#           self.check(m2)
#         else:
#           print(f"Cannot attack {m2.name}. It's not alive.")

#       elif len(args)==2:
#         m2=args[0]
#         m3=args[1]
#         if m2.alive == True:
#           self.check(m2)

#         else:
#           print(f"Cannot attack {m2.name}. It's not alive.")
        
#         if self.alive == True:
#           if m3.alive == True:
#             self.check(m3)

#           else:
#             print(f"Cannot attack {m3.name}. It's not alive.")
#         else:
#           print(f'{self.name} is not alive to attack.')
#     else:
#       print(f'{self.name} is not alive to attack.')



# monster1 = Monster('Godzilla', 40)
# monster2 = Monster('Hydra', 30)
# monster3 = Monster('KingKong', 50)
# print(f"Number of monsters alive:{Monster.monsterCount}")
# print('1--------------------------------')
# print(monster1.get_details())
# print('2--------------------------------')
# print(monster2.get_details())
# print('3--------------------------------')
# print(monster3.get_details())
# print('4--------------------------------')
# monster1.attack()
# print('5--------------------------------')
# monster1.attack(monster2)
# print('6--------------------------------')
# monster1.attack(monster2, monster3)
# print('7--------------------------------')
# print(f"Number of monsters alive:{Monster.monsterCount}")
# print('8--------------------------------')
# print(monster2.get_details())
# print('9--------------------------------')
# monster2.attack(monster1)

# class User:
#   activities = ["Post", "Like", "Comment"]
#   def __init__(self, name,email):
#     self.name = name
#     self.email = email
#   def UserActivity(self, activityType):
#     if activityType in User.activities:
#       return True
#     else:
#       return False
#   def userDetail(self):
#     return f"User Detail:\nName:{self.name}\nEmail: {self.email}"

# class BracbookUser(User):
#   activity =['No recent activity.']
#   tasks=''
#   def __init__(self,name,email,phn='Not set'):
#     super().__init__(name,email)
#     self.phn = phn
#     self.task=''

#   def userDetail(self):
#     return f"User Detail:\nName:{self.name}\nEmail: {self.email}\nPhone: {self.phn}\nActivity Log: {BracbookUser.activity[0]}"

#   def UserActivity(self, activityType):
#     self.activityType = activityType
#     if super().UserActivity(activityType) == True:
#       print(f'{self.name} has {self.activityType}(d/ed) succesfully.')
#       self.tasks +=self.activityType +','
#       BracbookUser.activity[0] = self.tasks[:-1]

#     else:
#       print(f'No activities found like {self.activityType}')

# user1 = BracbookUser("Rakait","xyz@gmail.com")
# print("1===========================")
# print(user1.userDetail())
# print("2===========================")
# user2 = BracbookUser("Sazzad","abc@gmail.com","01727xxxxxx")
# print("3===========================")
# print(user2.userDetail())
# print("4===========================")
# user1.UserActivity("Like")
# print("5===========================")
# user1.UserActivity("Comment")
# print("6===========================")
# print(user1.userDetail())
# print("7===========================")
# user2.UserActivity("Share")
# print("8===========================")
# user2.UserActivity("Comment")
# print("9===========================")
# print(user2.userDetail())
# ------------------------------------------------------------------------------------------------------------
# import numpy as np
# # import pandas as pd
# cnf_mat = np.array([[15,1,12,18,4],[ 1 ,44,  4,  0 , 1],[ 6,  2, 33,  6,  3],[ 7 , 2 , 6, 33,  2],[10,  5, 11, 16,  8]])
# print(cnf_mat)

# def calc(cnf_matrix):
#   FP = cnf_matrix.sum(axis=0) - np.diag(cnf_matrix) 
#   FN = cnf_matrix.sum(axis=1) - np.diag(cnf_matrix)
#   TP = np.diag(cnf_matrix)
#   TN = cnf_matrix.sum() - (FP + FN + TP)
#   FP = FP.astype(float)
#   FN = FN.astype(float)
#   TP = TP.astype(float)
#   TN = TN.astype(float)
#   print('FP = ',FP)
#   print('FN = ',FN)
#   print('TP = ',TP)
#   print('TN = ',TN)
  # Sensitivity, hit rate, recall, or true positive rate
  # TPR = TP/(TP+FN)

  # Specificity or true negative rate
  # TNR = TN/(TN+FP) 

  # Precision or positive predictive value
  # PPV = TP/(TP+FP)

  # # Negative predictive value
  # NPV = TN/(TN+FN)

  # # F1 Score
  # F1 = 2*((PPV)*(TPR)/(PPV + TPR))  

  # # Overall accuracy for each class
  # ACC = (TP+TN)/(TP+FP+FN+TN)
  # print('Sensitivity = ',TPR)
  # print('Specificity = ',TNR)
  # print('PPV = ',PPV)
  # print('NPV = ',NPV)
  # print('F1 Score = ',F1)
  # print('Accuray = ',ACC)
#   return TPR, TNR, PPV, NPV, F1
#   # print('Sensitivity = ',TPR)
#   # print('Specificity = ',TNR)
#   # print('PPV = ',PPV)
#   # print('NPV = ',NPV)
#   # print('F1 Score = ',F1)
#   # print('Accuray = ',ACC)
# TPR, TNR, PPV, NPV, F1= calc(cnf_mat)

# def formTable(a):
  

# #   for i in range(len(a)):
# #     print(i)
# #   print('',end='')
#   for i in range(len(a)):
#     if i == 0:
#       first.append(round(a[i],2))
#     if i == 1:
#       second.append(round(a[i],2))
#     if i == 2:
#       third.append(round(a[i],2))
#     if i == 3:
#       fourth.append(round(a[i],2))
#     if i == 4:
#       fifth.append(round(a[i],2))

# first=[]
# second = []
# third = []
# fourth = []
# fifth = []
# t=[]

# formTable(TPR)
# formTable(TNR)
# formTable(PPV)
# formTable(NPV)
# formTable(F1)

# t.append(first)
# t.append(second)
# t.append(third)
# t.append(fourth)
# t.append(fifth)
# print(t)

# # df = pd.DataFrame(t, columns = ['Sensitivity', 'Specificity', 'PPV', 'NPV', 'F1 Score', 'Accuray'], index=['0', '1', '2', '3', '4','avg'])
# # print(df)

# slst=[]
# slst_ML2=[]
# slst_ML2_t6 =[]
# def formt(t):
#   s0=0
#   s1=0
#   s2=0
#   s3=0
#   s4=0
#   s5=0

#   for i in range(len(t)+1):
#     for j in range(len(t)):
#       if i!=0:
#         break
#       else:
#         s0+= t[j][i]
#       avg_s0 = s0/len(t)
#     for j in range(len(t)):
#       if i!=1:
#         break
#       else:
#         s1+= t[j][i]
#       avg_s1 = s1/len(t)
#     for j in range(len(t)):
#       if i!=2:
#         break
#       else:
#         s2+= t[j][i]
#       avg_s2 = s2/len(t)
#     for j in range(len(t)):
#       if i!=3:
#         break
#       else:
#         s3+= t[j][i]
#       avg_s3 = s3/len(t)
#     for j in range(len(t)):
#       if i!=4:
#         break
#       else:
#         s4+= t[j][i]
#       avg_s4 = s4/len(t)
#     for j in range(len(t)):
#       if i!=5:
#         break
#       else:
#         s5+= t[j][i]
#       avg_s5 = s5/len(t)
  
#   slst.append(round(avg_s0,2))
#   slst.append(round(avg_s1,2))
#   slst.append(round(avg_s2,2))
#   slst.append(round(avg_s3,2))
#   slst.append(round(avg_s4,2))
#   slst.append(round(avg_s5,2))
#   # print(slst)
#   t.append(slst)
#   return t
# formt(t)

# t1 = np.array(t)
# print(t1)
# t1.transpose()
# print(t1)

# ------------------------------------------------------------------------------------------------------------

# Write a python function that takes the limit as an argument of the Fibonacci series and prints till that limit.

# Function Call:
# fibonacci(10)

# Output:
# 0 1 1 2 3 5 8

# def fibonacci(arg):
#   a= 0
#   b= 1
#   c= a+b
#   while a<=arg:
#     print(a,end=' ')
#     a=b
#     b=c
#     c=a+b
# fibonacci(10)

# ------------------------------------------------------------------------------------------------------------------------

#Take an input and calculate the total number of years, months and days as output.

# Input:
# 4330

# Output:
# 11 years, 10 months and 15 days

# num = int(input('Enter value = '))
# def findYear(n):
#   year = n//365
#   remainder1 = n%365
#   month = remainder1//30
#   day = remainder1%30
#   print(year,'years',month,'months',day,'days')

# findYear(num)

# -------------------------------------------------------------------------------------------------------------------------------

# Take an input and calculate how that can be split into 500, 100, 50, 20, 10, 5, 2, and 1 taka notes.

# Input = 151

# Output =
# 100 Taka: 1 note(s)
# 50 Taka: 1 note(s)
# 1 Taka: 1 note(s)

num = int(input('Enter the value = '))
def splitfunc(n):
  money_list = [500,100,50,20,10,5,2,1]
  for i in range(len(money_list)):
    note = n//money_list[i]
    n = n%money_list[i]

    if note!=0:
      print(money_list[i],'taka :',note,'notes(s)')


splitfunc(num)

