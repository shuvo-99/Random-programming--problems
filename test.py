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

# num = int(input('Enter the value = '))
# def splitfunc(n):
#   money_list = [500,100,50,20,10,5,2,1]
#   for i in range(len(money_list)):
#     note = n//money_list[i]
#     n = n%money_list[i]

#     if note!=0:
#       print(money_list[i],'taka :',note,'notes(s)')


# splitfunc(num)

# ----------------------------------------------------------------------------------------------------------------------------------

# Write a function called show_palindrome that takes a number as an argument and then returns a palindrome string. 

# Example1:
# Input = 5

# Output:
# 123454321

# def show_palindrome(n):
#   for i in range(1,n+1):
#     print(i,end='')
#   for j in range(n-1,0,-1):
#     print(j,end='')

# show_palindrome(5)

# ----------------------------------------------------------------------------------------------------------------------------------

# Write a function called show_palindromic_triangle that takes a number as a argument and prints a Palindromic Triangle in the function.

# Input = 3

# Output:
#     1
#   1 2 1
# 1 2 3 2 1

# def show_palindrome(x):
#   no_digit = 1
#   no_space = x-1

#   for lines in range(1,x+1):
#     values = 0

#     for j in range(1,no_space+1):
#       print(' ',end='')

#     for j in range(1,no_digit + 1):
#       if (j<=lines):
#         values = values + 1

#       else:
#         values = values-1
      
#       print(values,end='')

#     print()
#     no_digit = no_digit + 2
#     no_space = no_space - 1
# show_palindrome(3)

# Takes a list as an argument & Create a new list where each element can be present at max 2 times. 
# Print the number of elements removed from the given list

# Input :
# [1, 2, 3, 3, 3, 3, 4, 5, 8, 8]
# Output:
# Removed: 2
# [1, 2, 3, 3, 4, 5, 8, 8]

# def valid_element(n):
#   remove = 0
#   new_list = []
#   for i in n:
#     if i not in new_list:
#       new_list.append(i)

#     elif i in new_list:
#       repeat_count  = new_list.count(i)
#       if repeat_count< 2 :
#         new_list.append(i)
#       else:
#         remove = remove + 1
#   print('Remove = ', remove)
#   print(new_list)

# valid_element([1, 2, 3, 3, 3, 3, 4, 5, 8, 8])



# num = int(input())
# add = []
# res = 0
# for i in range(num):
#   list1 = [j for j in input().split(" ")]
  
#   print(list1)
#   for i in list1:
#     res += int(i)
#   add.append(res)
#   print(add)
#   max = add[0]
#   for i in range(len(add)):
#     if add[i]>max:
#       index = i

# print(max)
# print(list1[index])

# inp = int(input(''))
# res = 0
# highest = 0
# lst2=[]
# for i in range(inp):
#   lst=input().split(' ')
#   for j in range(len(lst)):
#     res += int(lst[j])
#   if res>highest:
#     highest = res
#     lst2 = lst
#   res = 0
# print(highest)
# print(lst2)

# print(23//4)

# var="ha, hermionea"
# var=var.split(",")
# string=""
# if len(var[0])<len(var[1]):
#   var1=var[0]
#   var2=var[1]
#   for i in var1:
#     if i in var2:
#       string+=i
#   for j in var2:
#     if j in var1:
#       string+=j

# if string=="" :
#   print("Nothing in common.")
# else:
#   print(string)

# else:
#   var1=var[1]
#   var2=var[0]
# print(var1)
# print(var2)
# for j in var2:
#   if j in var1:
#     # if j==i:
#     string+=j

# print('h')

# def capitalized(sen) :
#     res=""
#     for i in range(len(sen)) :
#         if i==0 or (i>1 and (sen[i-2]=="." or sen[i-2]=="!" or sen[i-2]=="?" )) :
#           res+=chr(ord(sen[i])-32)
#         else :
#           res+=str(sen[i])
#     return res
# sen='my favourite animal is a dog. a dog has sharp teeth so that it can eat flesh very easily. do you know my pet dog’s name? i love my pet very much.'
# print(capitalized(sen))

# class Point:
#   def __init__(self, x=0, y=0):
#     self.x = x
#     self.y = y
#   def __str__(self):
#     return "({0},{1})".format(self.x, self.y)
  # def __add__(self, other):
  #   x = self.x + other.x
  #   y = self.y + other.y
  #   return Point(x, y)

# p1 = Point(1, 2)
# p2 = Point(2, 3)
# print(p1+p2)
# print(p1)

# dict_1 = {
# 1:'.,?!:',
# 2:'ABC',
# 3:'DEF',
# 4:'GHI',
# 5:'JKL',
# 6:'MNO',
# 7:'PQRS',
# 8:'TUV',
# 9:'WXYZ',
# 0:' '
# }

# text = input("Please input a text = ").upper()

# for index in range(len(text)):
#     for key,value in dict_1.items():
#         if text[index] in value:
#             l1=list(value)
            
#             for i in range(len(l1)):
#                 if text[index] == l1[i]:
#                     b = str(key)*(i+1)
#                     print(b,end='')

# for i in text:
#   for key,value in dict_1.items():
#     c=0
#     for j in value:
#       c+=1
#       if i in j:
#         print(str(key)*c,end='')

# p = 5
# q = 6
# r = 9
# sum = 0
# if (p < 12):
#     print(r + 2)
# else:
#     print(r + p)
# if (q > 20):
#     print(r + 19)
# elif (q <= 6):
#     print(q + 3)
# else:
#     print(p + q + r)
# if (r > 15):
#     print(r)
# elif (r == 0):
#     print(p + q)
# else:
#     print(p)
# if (sum != 0):
#     print(3)
# else:
#     print(sum + 32)
# if (p>0 and r<10):
#     print(p+r)
# else:
#     print(p-r)

# string = '12'         
# c = 0
# number = '0123456789' 
# for i in string:        
#     # if (i>='A'and i<='Z') or (i>='a'and i<='z'):  
#     #     word += 1            
#     if i in number: 
#         c += 1
# if c == len(string):
#     print('NUMBER')

# elif c==0:
#     print('Word')

# elif c <= len(string):
#     print('Mixed')
# u = 'baNgladEsh'
# indx1=0
# indx2=0
# for i in u:
#   if 65<=ord(i)<=90:
#     break
#   indx1+=1
# for j in u:
#   if 65<=ord(j)<=90:
#     indx3=indx2
#   indx2+=1
# # indx1 = 1
# if indx1==indx2:
#   print('blank')
# else:
#   print(u[indx1+1:indx3])
# lst1 = []
# while True:
#   user_imp = input("Enter the list:")
#   if user_imp != "STOP":
#       lst1= user_imp.split(' ')
#   else:
#       break
#   list2=[]
#   sum=0
#   for i in range(1,len(lst1)):
#     diff=int(lst1[i-1])-int(lst1[i])
#     list2.append(abs(diff))
#   for j in list2:
#     sum+=j

#   if (len(lst1)*(len(lst1)-1))/2 == sum:
#     print('UB')
#   else:
#     print('no')

# class Easy:
#   def __init__(self, x, y ):
#     self.m = y 
#     self.n = x 
#     self.a = []

#   def methodA(self, *args):
#     if len(args) == 0:
#       self.m += self.n
#       self.a.append(True)
#       print(self.a[0], self.m)
#     else:
#       self.a.append(args[0])
#       self.methodB(self.m)

#   def methodB(self,a):
#     print(self.a[-1], a)


#   def methodC(self):
#     print(self.a[len(self.a)-1])

# obj1 = Easy(2 , 3)
# obj1.methodA(1)
# obj1.methodB()
# obj1.methodC()

# string = 'HOusE'
# upper = 0
# lower = 0 
# up= ''
# l = ''
# for i in string:        
#     if (i>='A'and i<='Z'): 
#       upper += 1    
#       up+=i 
#     else:
#       up+=i.upper()    
#     if (i>='a'and i<='z'): 
#       lower += 1
#       l+=i 
#     else:
#       l+=i.lower() 
# if upper > lower :
#     print(up)
# else:
#     print(l)

# string_1 = 'harry'
# string_2 = 'hermione'
# final_string_1 = ''
# final_string_2 = ''
# count = 0
# l = ['harry','hermione']
# for i in l:
#   for j in i:
#     if (j in l[0] and j in l[1]):
#       final_string_1+=j
# if (len(final_string_1)>1):
#   print(final_string_1)

# for i in string_1:
    
#     for j in string_2:
#       if i==j:
#         final_string_1 += i 
#         count+=1
    
# for i in string_2:
   
#     if i in string_1:
#         final_string_2 += i
            
# final_string = final_string_1 + final_string_2
            
# if(count==0):
#     print("Nothing in common.")
# else:
#     print(final_string)

# def maxt(n,k,y):
#   y=sorted(y,reverse=True)
#   c=0
#   for i in range(0,n,3):
#     if y[i]>=k:
#       c+=1
#     else:
#       break
#   return c

# y=list(map(int,input().split()))
# print(maxt(5,2,y))
# c=0
# l=[10,20,10,20,30,50,90]
# for i in l:
#   for j in l:
#     if i==j:
#       c+=1
#   print(i,'-',c)
# def janina(line):
#   m=""
#   k= ".!?"
#   m=line[0].upper()
#   for i in range(1,len(line)):
#     if line[i-1] ==" " and line[i-2] in k:
#       m+=line[i].upper()
#     elif line[i-1] ==" " and line[i] =="i" and line[i+1] ==" " :
#       m+= 'I'
#     else:
#       m+=line[i]
#   print(m)
# line='guilty'
# janina(line)
# def vowel(string):
#     vowel_list = ["a", "e", "i", "o", "u"]
#     new_list = 0
#     print_string = 'Vowels:'
#     for i in string:
#         if i in vowel_list:
#             new_list+=1
#     if new_list==0:
#       print("No vowels in the name!")
#     # length = len(new_list)
#     else:
#         print(f'{print_string[0:-1]}.Total number of vowels:',new_list)
    
        

# # name = input('Enter the name = ')
# vowel('Steve Jobs')
# def year_month_day(num):
    
#     # num = int(input("Enter the number of days = "))
    
#     year = num//365
    
#     month = (num-(year*365))//30
    
#     # month = year1//30
    
#     day = (num-(year*365))-(month*30)
    
#     print(year,"years,", month,"months",'and',day,"days ")

# year_month_day(4320)
# def vowel(string):
#     vowel_list = ["a", "e", "i", "o", "u"]
#     new_list = []
#     print_string = ''
#     for i in string:
#         if i in vowel_list:
#             new_list.append(i)
#     for j in new_list:
#         print_string += j
#         print_string += ","
#     length = len(new_list)
#     if length > 0:
#         print("Vowels:", print_string[:len(print_string)-1],"Total number of vowels:",length)
#     else:
#         print("No vowels in the name!")

# # name = input('Enter the name = ')
# vowel('Steve Jobs')

# Python program to demonstrate
# string slicing
 
# String slicing
# String = 'ASTRING'
# # Using slice constructor
# s3 = slice(-1, -12, 2)
# print(String[s3])
# def fraction(num1,num2):
#     # num1 = int(input("Enter the 1st number = "))
#     # num2 = int(input("Enter the 2nd number = "))
    
#     # if num1 == 0:
#     #     print('0')
    
#     if num2 > 0:
#       return (num1%num2)/num2
#     return 0
#     # else:
#     #     a = num1/num2
#     #     b = int(a)
#     #     fraction_part = a-b
#     #     print(fraction_part)
               
# print(fraction(5,2))
# def year_month_day(num):
    
#     # num = int(input("Enter the number of days = "))
    
#     year = int(num/365)
    
#     month = int((num%365)/7)
    
#     # month = year1//30
    
#     day = (num%365)%7
    
#     print(year,"years,", month,"months",'and',day,"days ")

# year_month_day(4320)

# class DataType:
#     def __init__(self,name,value):
#         self.name = name
#         self.value = value

#     # def printDeatails(self):
#     #     print('Interger')
#     def __str__(self):
#         return 'Integer\n1234'

# data_type1 = DataType('Integer', 1234)
# print(data_type1)
# # data_type1.printDeatails()
# # print(data_type1.name)
# # print(data_type1.value)
# # print('=====================')
# data_type2 = DataType('String', 'Hello')
# print(data_type2.name)
# print(data_type2.value) 
# print('=====================')
# data_type3 = DataType('Float', 4.0)
# print(data_type3.name)
# print(data_type3.value)

# class Student:
#   def __init__(self, name, id):
#     self.__name=name # protected attribute
#     self.__id=id # protected attribute
# s1=Student("Kiran",18101)
# print(s1.__id)
# s1.__id=18202
# print(s1.__id)

# num = int(input("Enter the number = "))
# y=0
# x=0
# while(x<num):
#     x=num//10
#     y=num%10
#     print(x, end=", ")
#     num = y

# n='32768'
# res=''
# p = len(n)-1#3
# while True:
#     s = int(n)//pow(10,p) #7
#     n = int(n)%pow(10,p) #68
#     res += str(s)+', ' #3, 2, 7,
#     # print(s,end=', ') 
#     if n==0:
#         break
#     p-=1
# print(res)
# print(res[:-2])
# print(32768//10)

# class StudentDatabase:
#     def __init__(self,name,ID):
#       self.name = name
#       self.ID = ID
#       self.grades= {}
    
#     def calculateGPA(self,course, sem):
#       self.courseList = {}
#       self.course = []
#       self.cgpa = []
#       self.sem = sem

#       for i in course:
#          var = i.split(': ')
#          self.course.append(var[0])
#          self.cgpa.append(float(var[1]))
#       # for i in self.cgpa:
         
#       self.gpa = round(sum(self.cgpa)/len(self.course),2)

#       self.courseList[tuple(self.course)] = self.gpa

#       self.grades[self.sem] = self.courseList
#       # print(self.grades)

#     def printDetails(self):
        
#         print(f'Name: {self.name}\nID: {self.ID}')
#         for k,v in self.grades.items():
#           print(f'Courses Taken in {k}')
#           for m,n in v.items():
#               for i in m:
#                 print(i)
#           print('GPA',n)

         

# s1 = StudentDatabase('Pietro', '10101222')
# s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0', 'MAT110: 4.0'], 'Summer2020')
# s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'], 'Summer2021')
# print(f'Grades for {s1.name}\n{s1.grades}')
# print('------------------------------------------------------')
# s1.printDetails()
# s2 = StudentDatabase('Wanda', '10103332')
# s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7', 'ENG101: 4.0'], 'Summer2022')
# print('------------------------------------------------------')
# print(f'Grades for {s2.name}\n{s2.grades}')
# print('------------------------------------------------------')
# s2.printDetails()

# class Vaccine:
#     def __init__(self,vaccine_type,place,day):
#         self.vaccine_type=vaccine_type
#         self.place=place
#         self.day=day
# class Person:
#     def __init__(self,name,age,x="General Citizen"):
#         self.name=name
#         self.age=age
#         self.proffesion=x
#         self.l=[]

#     def pushVaccine(self,vaccine_name,dose_num="1st dose"):
#         self.vaccine_name = vaccine_name
#         self.dose_num = dose_num
#         if len(self.l)==0:
#             self.l.append(self.vaccine_name)

#         if self.age <25 and self.proffesion !='Student':
#            print(f'Sorry {self.name}, Minimum age for taking vaccines is 25 years now.')
#         else:
#           if self.vaccine_name != self.l[0]:
#               print(f'Sorry {self.name}, you can’t take 2 different vaccines')
#           else:
#             print(f"{self.dose_num} done for {self.name}")

#     def showDetail(self):
#         print("Name:",self.name,"Age:",self.age,"Type:",self.proffesion)
#         print("Vaccine name:",self.vaccine_name.vaccine_type)
#         print("1st dose: Given")
#         if self.dose_num != '2nd Dose':
#           print(f"2nd dose: Please come after {self.vaccine_name.day} days")
#         else:
#           print('2nd dose: Given')

# astra = Vaccine("AstraZeneca", "UK", 60)
# modr = Vaccine("Moderna", "UK", 30)
# sin = Vaccine("Sinopharm", "China", 30)
# p1 = Person("Bob", 21, "Student")
# print("=================================")
# p1.pushVaccine(astra)
# print("=================================")
# p1.showDetail()
# print("=================================")
# p1.pushVaccine(sin, "2nd Dose")
# print("=================================")
# p1.pushVaccine(astra, "2nd Dose")
# print("=================================")
# p1.showDetail()
# print("=================================")
# p2 = Person("Carol", 23, "Actor")
# print("=================================")
# p2.pushVaccine(sin)
# print("=================================")
# p3 = Person("David", 34)
# print("=================================")
# p3.pushVaccine(modr)
# print("=================================")
# p3.showDetail()
# print("=================================")
# p3.pushVaccine(modr, "2nd Dose")


# class  PizzaMachine:
#     def init(self,typei="Regular",size=6):
#         self.alike=typei
#         self.size=size
#     def customizePizza(self,*args):
#         tope=""
#         self.spiceiwant=['Regular','Hot',"Super Naga"]
#         if len(args)==2:
#             self.toping=args[0]
#             self.spicelevel=args[1]
#         if  len(args)==1:
#             if type(args[0])==str:
#                 self.spicelevel=args[0]
#                 self.toping=[] 
#             else:
#                 self.toping=args[0]
#                 self.spicelevel="Regular"
#         # for i in self.spiceiwant:
#         if self.spicelevel not in self.spiceiwant:

#             return "Sorry! Spice level not allowed. Can't bake pizza."
#         if len(self.toping)==0:
#             return "No toppings specified! Can't bake pizza."
#         else:
#             for i in self.toping:
#                 tope+=i+","
#         tope=tope[:-1]
#         return f"Your {self.size} { self.spicelevel} spicy {self.alike} Pizza is ready with {tope}. Enjoy!"

# class Patient:
    
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
    
#     def add_Symptom(self,*symptom):
#         self.symptom = symptom    
    
#     def printPatientDetail(self):
#         print('Name:',self.name)
#         print('Age:',self.age)
#         s = ''
#         for i in self.symptom:
#             s = s + i + ', '
            
#         print('Symptoms:', s[:-2])
        
# p1 = Patient('Thomas', 23)
# p1.add_Symptom('Headache')
# p2 = Patient('Carol', 20)
# p2.add_Symptom('Vomiting', 'Coughing')
# p3 = Patient('Mike', 25)
# p3.add_Symptom('Fever', 'Headache', 'Coughing')
# print("=========================")
# p1.printPatientDetail()
# print("=========================")
# p2.printPatientDetail()
# print("=========================")
# p3.printPatientDetail()
# print("=========================")

# class Match:
#     def __init__(self,teams):
#         self.team1,self.team2 = teams.split('-')
#         self.run=0
#         self.over = 0
#         print('5..4..3..2..1.. Play !!!')

#     def add(self,run):
#         self.run +=run


# match1 = Match("Rangpur Riders-Cumilla Victorians")
# print("=========================")
# match1.add_run(4)
# match1.add_run(6)
# match1.add_over(1)
# print(match1.print_scoreboard())
# print("=========================")
# match1.add_over(5)
# print("=========================")
# match1.add_wicket(1)
# print(match1.print_scoreboard())
# s='Ppython'
# res = ''
# value = 0
# for i in s:
#   asc = ord(i)
#   # print(asc)
#   res = str(asc)
#   value += int(res[0])
# print(value)
# class Snapchat:
#     def __init__(self,name,horoscope,gender="Female",score=0):
#         self.name = name
#         self.horoscope = horoscope
#         self.gender = gender
#         self.score = score
#         self.friendno = 0
#         self.friend = []
#         self.msg = {}
#         self.msgno = 0
#     def QuickAdd(self,*args):
#         for user in args:
#             if user.name in self.friend:
#                 pass
#             else:
#                 self.friendno += 1
#                 self.friend.append(user.name)
#                 user.friendno += 1
#                 user.friend.append(self.name)
#     def sendSnap(self,user):
#         if user.name in self.friend:
#             self.score += 1
#             print("Snap sent.")
#         else:
#             print(f"Sorry,{user.name} is not in your friend list.")
#     def sendMessage(self,user,message):
#         if user.name in self.friend:
#             #for key,val in user.msg.items():
#             if self.name in user.msg:
#                 # print('yes')
#                 user.msg[self.name].append(message)
                
#             else:
#                 user.msg[self.name] = [message]
#             print("Message sent.")
#             user.msgno += 1
#             # print(user.msg)
#         else:
#             print(f"Sorry,{user.name} is not in your friend list.")
#     def printDetails(self):
#         print(f"User Name:{self.name} Score:{self.score}\n Horoscope:{self.horoscope} Gender:{self.gender}")
#         frnd = ""
#         for i in self.friend:
#             frnd += i + ", "
#         print(f"Friends({self.friendno}):{frnd[0:len(frnd)-2]}")
#     def showInbox(self):
#         # print(self.msg)
#         if self.msgno != 0:
#             print(f"Messages:You have {self.msgno} new message(s).")
#             print("Here is your inbox:")
#             for key,val in self.msg.items():
#                 print(f"From {key}")
#                 # print(val)
#                 for i in val:
#                     print(i)
#         else:
#             print("You have no message(s)")
# user1 = Snapchat("Jaime","Leo","Male",123)
# user2 = Snapchat("Bran","Virgo","Male")
# user3 = Snapchat("John","Aries","Male",234)
# user4 = Snapchat("Sansa","Scorpio")
# print("1----------------------------")
# user1.QuickAdd(user3)
# user1.QuickAdd(user2,user4)
# user2.QuickAdd(user3)
# user2.QuickAdd(user4)
# print("2----------------------------")
# user1.sendSnap(user2)
# print("3----------------------------")
# user1.sendSnap(user2)
# print("4----------------------------")
# user1.sendMessage(user2,"Hii")
# print("5----------------------------")
# user1.sendMessage(user2,"Can you help me with question 1?")
# print("6----------------------------")
# user2.sendSnap(user1)
# print("7----------------------------")
# user2.sendMessage(user1,"Hello")
# print("8----------------------------")
# user2.sendMessage(user1,"Sorry Bro.")
# print("9----------------------------")
# user3.sendSnap(user2)
# print("10----------------------------")
# user3.sendMessage(user2,"Hii there. Do you know when is our CSE111 Lab mid?")
# print("11----------------------------")
# user2.printDetails()
# print("12----------------------------")
# user2.showInbox()
# print("13----------------------------")
# user1.printDetails()
# user1.showInbox()
# print("14----------------------------")
# user1.sendMessage(user3,"Hey. You are giving it right now.")
# print("15----------------------------")
# user3.printDetails()
# print("16----------------------------")
# user3.showInbox()
# print("17----------------------------")
# user3.sendSnap(user4)
# print("18----------------------------")
# user4.sendMessage(user3,"Hi")
# print("19----------------------------")
# user4.printDetails()
# print("20----------------------------")
# user4.showInbox()

# class Student:   def init(self,name,id,dep):     self.name=name     self.id=id     self.dep=dep     self.email=None     self.password=None     self.login=None     print("Student object is created!")   class Usis:   def init(self):      print("USIS is ready to use!")   def login(self,name2):     if name2.email!=None and name2.password!=None and name2.login!=None:       print("Login successful!")     elif(name2.email!=None and name2.password!=None):       print("Email and password need to be set.")      def advising(self,name1,*course):     self.name1=name1     self.course='course'      if len(course)==0:       print("You haven't selected any courses.")     else:       if len(course)>3:         print("You need special approval to take more than 3 courses.")       else:         for i in course:           self.course+=i         print("Advising successful!")   def individualDetails(self,x):     print("Name:",x.name)     print("Id:",x.id)     print("Department:",x.dep)     # print("
# class Student:
#   def __init__(self,name,id,dep):
#     self.name=name
#     self.id=id
#     self.dep=dep
#     self.email=None
#     self.password=None
#     self.login=False
#     print("Student object is created!")

# class Usis:
#   def __init__(self):

#     print("USIS is ready to use!")

#   def login(self,name2):
#     if name2.email!=None and name2.password!=None:
#       name2.login = True
#       print("Login successful!")
#     elif(name2.email==None and name2.password==None):
      
#       print("Email and password need to be set.")

#   def advising(self,name1,*course):

#     self.name1=name1
#     self.course=''

#     if name1.login == False:
#       print('Please login to advise courses!')
#     else:
#       if len(course)==0:
#         print("You haven't selected any courses.")
#       else:
#         if len(course)>3:
#           print("You need special approval to take more than 3 courses.")
#         else:
#           for i in course:
#             self.course+=i+', '
#           print("Advising successful!")
#   def individualDetails(self,x):
#     print("Name:",x.name)
#     print("Id:",x.id)
#     print("Department:",x.dep)
#     return f'Advised courses: {self.course[:-2]}'

# rakib = Student("Rakib", 12301455, "CSE")
# print("1***********************")
# usis_obj = Usis()
# print("2***********************")
# usis_obj.login(rakib)
# print("3***********************")
# usis_obj.advising(rakib)
# print("4***********************")
# rakib.email = "rakib@hotmail.com"
# rakib.password = "1234"
# print("5***********************")
# usis_obj.login(rakib)
# print("6***********************")
# usis_obj.advising(rakib)
# print("7***********************")
# usis_obj.advising(rakib, "CSE110", "PHY111", "MAT110", "CSE260")
# print("8***********************")
# usis_obj.advising(rakib, "CSE110", "PHY111", "MAT110")
# print("9***********************")
# print(usis_obj.individualDetails(rakib))

# ind_diff = 2
# fare = (ind_diff)*100


# class Train:
#   def __init__(self,nam,*t):
#     self.train=nam
#     self.location=t
#     self.count=0
#     self.name=[]
#     self.start=[]
#     self.exit=[]
#     self.diff=[]
#     print('Welcome aboard on',self.train)
#     print('Start:',self.location[0])
#     print('Destination:',self.location[-1])
#   def addPassenger(self,*n):
#     self.count+=1
    
#     for i in n:
#       print(i.name,'welcome aboard')
#       self.name.append(i.name)
#       # self.start.append(i.place1)
      
#       if (i.place1==None):
#         i.place1=self.location[0]
#         self.start.append(i.place1)
#       else:
#         self.start.append(i.place1)

#       if (i.place2==None):
#         i.place2=self.location[-1]
#         self.exit.append(i.place2)
#       else:
#         self.exit.append(i.place2)
      
#       diff = self.location.index(i.place2)-self.location.index(i.place1)
#       self.diff.append(diff)
#   def allPassengerDetails(self):
#     for i in range(len(self.name)): 
#       print(f'Name: {self.name[i]},Start: {self.start[i]}, Destination: {self.exit[i]}, Fair: ${self.diff[i]*100}')

# class Passenger:
#   def __init__(self,nam,enter=None,exit=None):
#     self.name=nam
#     self.place1=enter
#     self.place2=exit


# t1 = Train('T1-Express','New York','Manhattan','Brooklyn','Boston')
# print("1========================")
# p1 =Passenger("Naruto")
# t1.addPassenger(p1)
# p2 = Passenger("Sasuke","Manhattan")
# p3 = Passenger("Hinata","Manhattan","Brooklyn")
# print("2========================")
# t1.addPassenger(p2,p3)
# print("3========================")
# t1.allPassengerDetails()
# print("4========================")
# t2 = Train('Europe-Express','London','Paris','Brussels','Turkey')
# print("5========================")
# p4 =Passenger("Max","London","Brussels")
# p5 = Passenger("Eleven","Paris")
# p6 = Passenger("Mike","Brussels")
# t2.addPassenger(p4,p5,p6)
# print("6========================")
# t2.allPassengerDetails()

# class BracuStudent:
#     def __init__(self,name, live_in):
#       self.name = name
#       self.home = live_in
#       self.bus_pass = False
    
#     def show_details(self):
#       print(f'Student Name: {self.name}\nLives in {self.home}\nHave Bus Pass? {self.bus_pass}')
    
#     def get_pass(self):
#       self.bus_pass = True
# class BracuBus:
#     def __init__(self,route, max = 2):
#       self.route = route
#       self.max = max
#       self.on_board = []
#       self.passenger=[]
      

#     def show_details(self):
#       print(f'Bus Route: {self.route}\nPassengers Count: {len(self.on_board)} (Max: {self.max})\nPassengers On Board: {self.on_board}')

#     def board(self, *args):
#       if len(args)==0:
#         print('No passenger!')
#       else:
#         for i in args:
#           if i.bus_pass == False:
#             print("You don't have bus pass!")
#           else:
#             if self.route != i.home:
#               print('You got on wrong bus!')
#             else:
#               self.passenger.append(i.name)
#         count=0
#         for i in self.passenger:
#           count+=1 
#           if count > self.max:
#             print('Bus is full!') 
#             return 
#           else:
#             self.on_board.append(i)
#             print(i,'boarded the bus')
      

# st1 = BracuStudent("Afif", "Mirpur")
# print("1===========================")
# st2 = BracuStudent("Shanto", "Motijheel")
# st3 = BracuStudent("Taskin", "Mirpur")
# st1.show_details()
# st2.show_details()
# print("2===========================")
# st3.show_details()
# print("3===========================")
# bus1 = BracuBus("Mirpur")
# bus2 = BracuBus("Azimpur", 5)
# bus1.show_details()
# bus2.show_details()
# print("4===========================")
# st2.get_pass()
# st3.get_pass()
# print("5===========================")
# st2.show_details()
# st3.show_details()
# print("6===========================")
# bus1.board()
# print("7===========================")
# bus1.board(st1, st2)
# print("8===========================")
# st1.get_pass()
# st2.home = "Mirpur"
# st1.show_details()
# st2.show_details()
# print("9===========================")
# bus1.board(st1, st2, st3)
# print("10===========================")
# bus1.show_details()


# class BracuStudent:
#   def __init__(self,name,area,bpass=False):
#     self.name=name
#     self.area=area
#     self.bpass=bpass
#   def show_details(self):
#     print("Student Name:",self.name)
#     print("Lives in",self.area)
#     print("Have Bus Pass?",self.bpass)
#   def get_pass(self):
#     self.bpass=True

# class BracuBus:
#   def __init__(self,route,max=2):
#     self.route =route
#     self.max=max
#     self.count=0
#     self.board1=[]
#     # if board!=None:
#     #   self.board1.append(board)
#   def show_details(self):
#     print("Bus Route:",self.route)
#     print(f"Passengers Count:{self.count}(Max:{self.max})")
#     print("Passengers On Board:",self.board1)
#   def board(self,*x):
#     if len(x)==0:
#       print("No passenger!")
#     else:
#       if bpass.x[0]!=True and x[-1].area==self.route:
#         print("You don't have bus pass!")
#       elif x.bpass[0]==True and x[-1]!=self.route:
#         print("You got on wrong bus!")
# st1 = BracuStudent("Afif", "Mirpur")
# print("1===========================")
# st2 = BracuStudent("Shanto", "Motijheel")
# st3 = BracuStudent("Taskin", "Mirpur")
# st1.show_details()
# st2.show_details()
# print("2===========================")
# st3.show_details()
# print("3===========================")
# bus1 = BracuBus("Mirpur")
# bus2 = BracuBus("Azimpur", 5)
# bus1.show_details()
# bus2.show_details()
# print("4===========================")
# st2.get_pass()
# st3.get_pass()
# print("5===========================")
# st2.show_details()
# st3.show_details()
# print("6===========================")
# bus1.board()
# print("7===========================")
# bus1.board(st1, st2)
# print("8===========================")
# st1.get_pass()
# st2.home = "Mirpur"
# st1.show_details()
# st2.show_details()
# print("9===========================")
# bus1.board(st1, st2, st3)
# print("10===========================")
# bus1.show_details()

# class Library:
#     def __init__(self,city, dict1):
#       self.city = city
#       self.book = dict1
#       self.borrower_detail = {}


#     def details(self):
#       print(f'{self.city} Library details\nBorrower details:\n{self.borrower_detail}\nBooks availability:\n{self.book}')
        
# class Reader:
#     def __init__(self,name):
#       self.name = name
#       self.borrow_no = []
#       self.borrower = {}
#     def borrow(self,*args):
#       self.obj = args[0]
      
#       for i in range(1,len(args)):
#          for k,v in self.obj.book.items():
#             if args[i] == k:
#               if v==0:
#                 print(f'{args[i]} books are not available at the moment.')
              
#               elif len(self.borrow_no)>=5:
#                 print('You cannot borrow more than 5 books.')
                
#               else:
#                 self.obj.book[k]-=1
#                 print(f'{args[i]} book is borrowed successfully.')
#                 self.borrow_no.append(args[i])
#                 if k in self.borrower:
#                   self.borrower[k] += 1
#                 else:
#                   self.borrower[k]=1
#       self.obj.borrower_detail[self.name] = len(self.borrow_no)
#     def readerInfo(self,*topic):
#       self.topic = topic
#       print(f'{self.name} you have {len(self.borrow_no)} book(s) with you')
#       if self.topic != '':
#         for k,v in self.borrower.items():
#           print(f'Books on {k}: {v}')
#       else:
#         for k,v in self.borrower.items():
#           for i in self.topic:
#             if i == k:
#               print(f'{self.name}, you have {v} {i} book(s) with you.')
#             # if self.topic == k:
#             #   print(f'{self.name}, you have {v} {self.topic} book(s) with you.')


# L1=Library('Dhaka',{'Arts':15,'Fiction':135,'Politics':2,'Science':11,'Poetry':15})
# L1.details()
# print("1----------------------")
# r1=Reader('Aladdin')
# r1.borrow(L1,'Arts','Fiction','Fiction','Politics')
# print("2----------------------")
# r1.borrow(L1,'Politics','Fiction')
# print("3----------------------")
# r1.readerInfo()
# print("4----------------------")
# r1.readerInfo('Fiction')
# print("5----------------------")
# L1.details()
# print("6----------------------")
# r2=Reader('Jasmine')
# r2.borrow(L1,'Politics','Poetry')
# print("7----------------------")
# r2.readerInfo()
# print("8----------------------")
# L1.details()

# class BracuStudent:
#   def __init__(self,name,home,bpass=False):
#     self.name=name
#     self.home=home
#     self.bpass=bpass
#   def show_details(self):
#     print("Student Name:",self.name)
#     print("Lives in",self.home)
#     print("Have Bus Pass?",self.bpass)
#   def get_pass(self):
#     self.bpass=True

# class BracuBus:
#   def __init__(self,route,max=2):
#     self.route =route
#     self.max=max
#     self.count=0
#     self.board1=[]
#     self.board2=[]
#   def show_details(self):
#     print("Bus Route:",self.route)
#     print(f"Passengers Count:{self.count}(Max:{self.max})")
#     print("Passengers On Board:",self.board2)
#   def board(self,*x):
#     for i in x:
#       # self.board1.append(i)
#       if i.bpass!=True:
#           print("You don't have bus pass!")
#       else:
#         if self.route!=i.home:
#           print("You got on wrong bus!")
#         else:
#           self.board1.append(i.name)
#     for i in self.board1:
#       self.count+=1
#       if self.count>self.max:
#         print("Bus is full!")
#         return
#       else:
#         self.board2.append(i)
#         print(i,"boarded the bus")
        

# st1 = BracuStudent("Afif", "Mirpur")
# print("1===========================")
# st2 = BracuStudent("Shanto", "Motijheel")
# st3 = BracuStudent("Taskin", "Mirpur")
# st1.show_details()
# st2.show_details()
# print("2===========================")
# st3.show_details()
# print("3===========================")
# bus1 = BracuBus("Mirpur")
# bus2 = BracuBus("Azimpur", 5)
# bus1.show_details()
# bus2.show_details()
# print("4===========================")
# st2.get_pass()
# st3.get_pass()
# print("5===========================")
# st2.show_details()
# st3.show_details()
# print("6===========================")
# bus1.board()
# print("7===========================")
# bus1.board(st1, st2)
# print("8===========================")
# st1.get_pass()
# st2.home = "Mirpur"
# st1.show_details()
# st2.show_details()
# print("9===========================")
# bus1.board(st1, st2, st3)
# print("10===========================")
# bus1.show_details()


# class Hashing:
#   def __init__(self,a):
#     self.a=a
#     self.l=[0]*9
#     self.ac=0
#     self.calculate(a)
#     print("==============Task 2==============")
#     print("Initial array:",arr)
#     print("Hash table:",self.l)
#   def calculate(self, a):
#     if a!=[]:
#       self.hashTable(strng(a[0],c=0))
#       return self.calculate(a[1:])
#   def hashTable(self,idx):
#     if self.l[idx]==0:
#       self.l[idx]=arr[self.ac]
#     else:
#       return self.hashTable((idx+1)%9)
#     self.ac+=1

# def strng(s,c=0):
#   if s!='':
#     if ord(s[0])>=65 and ord(s[0])<=90:
#       return strng(s[1:],c+24)
#     elif ord(s[0])>=48 and ord(s[0])<=57:
#       return strng(s[1:],c+int(s[0]))
#   return c%9

# arr = ["ST1E89B8A32",'7','7','8','9','85127H']
# Hashing(arr)

# class Train:
#   def __init__(self,train_name,*locations):
#     self.train_name=train_name
#     self.locations=locations
#     self.name_list=[]
#     self.start_list=[]
#     self.destination_list=[]
#     self.diff=[]
#     print(f"Welcome aboard on {self.train_name}")
#     print(f"Start: {self.locations[0]}")
#     print(f"Destination: {self.locations[-1]}")

#   def addPassenger(self,*arg):
#     for i in arg:
#       print(i.name,'welcome aboard')
#       self.name_list.append(i.name)
#       if i.start==None:
#         i.start=self.locations[0]
#         self.start_list.append(i.start)
#       else:
#         self.start_list.append(i.start)
      
#       if i.destination==None:
#         i.destination=self.locations[-1]
#         self.destination_list.append(i.destination)
#       else:
#         self.destination_list.append(i.destination)

      
#       # print(self.locations)
#       # print('i = ',i.start)
#       # print('s = ',i.destination)
#       diff=self.locations.index(i.destination)-self.locations.index(i.start)
#       self.diff.append(diff)

#   def allPassengerDetails(self):
#     for i in range(len(self.name_list)):
#       print(f"Name: {self.name_list[i]},Start: {self.start_list[i]},Destination: {self.destination_list[i]},Fair: {self.diff[i]*100}")

# class Passenger:
#   def __init__(self,name,start=None,destination=None):
#     self.name=name
#     self.start=start
#     self.destination=destination
    

# t1 = Train('T1-Express','New York','Manhattan','Brooklyn','Boston')
# print("1========================")
# p1 =Passenger("Naruto")
# t1.addPassenger(p1)
# p2 = Passenger("Sasuke","Manhattan")
# p3 = Passenger("Hinata","Manhattan","Brooklyn")
# print("2========================")
# t1.addPassenger(p2,p3)
# print("3========================")
# t1.allPassengerDetails()
# print("4========================")
# t2 = Train('Europe-Express','London','Paris','Brussels','Turkey')
# print("5========================")
# p4 =Passenger("Max","London","Brussels")
# p5 = Passenger("Eleven","Paris")
# p6 = Passenger("Mike","Brussels")
# t2.addPassenger(p4,p5,p6)
# print("6========================")
# t2.allPassengerDetails()


# class SportsPerson:
#   def __init__(self, team_name, name, role):
#     self.__team = team_name
#     self.__name = name
#     self.role = role
#     self.earning_per_match = 0
#   def get_name_team(self):
#     return 'Name: '+self.__name+', Team Name: ' +self.__team
# class Player(SportsPerson):
#   def __init__(self,team_name,name,role,totalgoal,totalmatch):
#     super().__init__(team_name,name,role)
#     self.totalgoal=totalgoal
#     self.totalmatch=totalmatch
#   def calculate_ratio(self):
#     self.earning_per_match=(self.totalgoal*1000)+(self.totalmatch*10)
#   def print_details(self):
#     print( f"{super().get_name_team()}\nTeam Role: {self.role}\nTotal Goal : {self.totalgoal}, Total played : {self.totalmatch}\nGoal ratio : {self.totalgoal/self.totalmatch}\nMatch earning : {self.earning_per_match}K")
# class Manager(SportsPerson):
#   def __init__(self, team_name, name, role,win):
#      super().__init__(team_name, name, role)
#      self.win=win
     
#   def print_details(self):
#     print( f"{super().get_name_team()}\nTeam Role: {self.role}\nTotal win : {self.win}\nMatch earning : {self.win*1000}K")
# #write your code here
# player_one = Player('Juventus', 'Ronaldo', 'Striker', 25, 32)
# player_one.calculate_ratio()
# player_one.print_details()
# print('------------------------------------------')
# manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
# manager_one.print_details()


# class Library:
#     Total_book = 1000
#     borrow_data = {}
#     book_list=[]
    
#     def __init__(self,n,id):
#         self.student_name = n
#         self.student_id = id     
    
#     def borrowbook(self):
#         print("A book is borrowed!")
        
#     def __str__(self):
#         return "Library: XYZ"

# class Student(Library):
#     def __init__(self,n,id):
#         super().__init__(n,id) 
#         self.dictionary={}
#     def borrowbook(self,name,uniqueid=None):
#         if uniqueid==None:
#             self.name=name 
#             self.uniqueid=""
#         else:
#             self.name=name 
#             self.uniqueid=uniqueid
        
    
#         if Library.Total_book>0:
#             if self.name in Library.borrow_data:
#                 print(f"Sorry {self.student_name}! '{self.name}' book is already borrowed by {Library.borrow_data[name][0]}")
#             else:
#                 Library.borrow_data[self.name]=[self.student_name]
#                 Library.book_list.append(self.name)
#                 Library.Total_book-=1 
#                 super().borrowbook()
#                 print(f"{self.name} book with the unique id {self.uniqueid} is borrowed by by {self.student_name}({self.student_id})\nNumber of books available for borrowing={Library.Total_book}")
       

#     def returnAllBooks(self):
#         # if Library.Total_book<999:
#         #     print(f"All the books have been returned by {self.student_name}")
#         borrow_dict2 = Library.borrow_data.copy()
#         for k,v in borrow_dict2.items():
#             for i in v:
#               # print(i)
#               # print(self.student_name)
#               if self.student_name == i:
#                   # print('yes')
#                   del Library.borrow_data[k]
#         print('All Books are returned by Alice.')

              
            

#     def __str__(self):
#         return(f"{super().__str__()}\nStudent Name:{self.student_name} ID:{self.student_id}\nBooks borrowed:{','.join(Library.book_list)}")
# #driver code
# s1 = Student("Alice",18101259)
# s1.borrowbook("The Alchemist", "Hdw652")
# print("1===============")
# print(s1)
# print("2===============")
# print(Library.borrow_data)
# print("3===============")
# s1.borrowbook("Wuthering Heights")
# print("4===============")
# print(s1)
# print("5===============")
# s2= Student("David",18141777)
# s2.borrowbook("The Alchemist", "Hdw652")
# print("6===============")
# s2.borrowbook("The Vampyre")
# print("7===============")
# print(Library.borrow_data)
# print("8===============")
# s1.returnAllBooks()
# print("9===============")
# print(Library.borrow_data)

# class Mobile:
#   countryCodes = {"880": "Bangladesh", "966": "India", "455": "USA"}
#   def __init__(self, model, simCardStatus):
#     self.model = model
#     self.__simCardStatus = simCardStatus
#     print(f"Model {model} is manufactured.")
#   def setSimCardStatus(self,status):
#     self.__simCardStatus = status
#     print("SIM card status updated successfully.")
#   def getSimCardStatus(self):
#     return self.__simCardStatus
#   def __str__(self):
#     return f"Mobile Phone Detail:\nModel: {self.model}\nSIM Card Status: {self.__simCardStatus}"
# class Nokia(Mobile):
#   def __init__(self, model, simCardStatus, balance=0):
#     self.balance=balance
#     self.dialCallHistory=[]
#     super().__init__(model, simCardStatus)
#     print(self.model)
     
#   def __str__(self):
#     return(f"Mobile Phone Detail:\nModel: {self.model}\nSIM Card Status: {self.getSimCardStatus()}\nBalance: {self.balance} TK")
  
#   def rechargeSIMCard(self,new_b):
#     self.balance+=new_b
#     print(f"Recharge successful! Current balance: {self.balance} TK")
  
#   def changeSIMCardStatus(self):
#     self.setSimCardStatus(not self.getSimCardStatus())
#     return('SIM card status updated successfully.')
#   def dialCall(self, num):
#     if self.getSimCardStatus()==False:
#       return('No SIM card available!')
#     elif self.balance==0:
#       return('Insufficient balance!')
#     elif num[0:3] in Mobile.countryCodes:
#       self.dialCallHistory.append(num)
#       return(f"Dialing the number {num} to {Mobile.countryCodes[num[:3]]} region")
#     elif num[0:3]!='880' or num[0:3]!='966' or num[0:3]!='455':
#       return(f"Dialing is not allowed in this region.")
# N3110 = Nokia("N3110", False)
# print("#######################################")
# print(N3110)
# print("1======================================")
# N1100 = Nokia("N1100", True,100)
# print("#######################################")
# print(N1100)
# print("2======================================")
# print(N3110.dialCall("88017196xxxx"))
# print("3======================================")
# N3110.changeSIMCardStatus()
# print("4======================================")
# print(N3110.dialCall("88017196xxxx"))
# print("5======================================")
# N3110.rechargeSIMCard(200)
# print("6======================================")
# print(N3110.dialCall("88017196xxxx"))
# print("7======================================")
# print(N1100.dialCall("45617196xxxx"))
# print("8======================================")
# print(N1100.dialCall("45517196xxxx"))
# print(N1100.dialCall("96617196xxxx"))
# print("9======================================")
# print(f"Dial call history for {N1100.model}: {N1100.dialCallHistory}")
# print(f"Dial call history for {N3110.model}: {N3110.dialCallHistory}")

# class Mobile:
#   countryCodes = {"880": "Bangladesh", "966": "India","455": "USA"}
#   def __init__(self, model, simCardStatus):
#     self.model = model
#     self.__simCardStatus = simCardStatus
#     print(f"Model {model} is manufactured.")
#   def setSimCardStatus(self,status):
#     self.__simCardStatus = status
#     print("SIM card status updated successfully.")
#   def getSimCardStatus(self):
#     return self.__simCardStatus
#   def __str__(self):
#     return f"Mobile Phone Detail:\nModel:{self.model}\nSIM Card Status: {self.__simCardStatus}"
# #Write your code here
# class Nokia(Mobile):
#   def __init__(self,model,status,balance=0):
#     super().__init__(model,status)
#     self.balance=balance
#   def __str__(self):
#     return f"Mobile Phone Detail:\nModel:{self.model}\nSIM Card Status: {self.getSimCardStatus()}\nBalance:{self.balance}"
#     # print(super().__str__())
#     # print(f"Balance:",self.balance)
#   def dialCall(self,number):
#     self.code=number[:3]
#     # print(self.code)
#     if self.getSimCardStatus()==False:
#       return "No SIM card available!"
      
#     elif(self.balance==0):
#       return "Insufficient balance!"
#     else:
   
#       if self.code in Mobile.countryCodes:
#         for k,v in Mobile.countryCodes.items():
#           if self.code==k:
#             return f"Dialing the number {number} to {v} region."
#       else:
#         return "Dialing is not allowed in this region."
        
# N3110 = Nokia("N3110", False)
# print("#######################################")
# print(N3110)
# print("1======================================")
# N1100 = Nokia("N1100", True,100)
# print("#######################################")
# print(N1100)
# print("2======================================")
# print(N3110.dialCall("88017196xxxx"))
# print("3======================================")
# # N3110.changeSIMCardStatus()
# print("4======================================")
# print(N3110.dialCall("88017196xxxx"))
# print("5======================================")
# # N3110.rechargeSIMCard(200)
# print("6======================================")
# print(N3110.dialCall("88017196xxxx"))
# print("7======================================")
# print(N1100.dialCall("45617196xxxx"))
# print("8======================================")
# print(N1100.dialCall("45517196xxxx"))
# print(N1100.dialCall("96617196xxxx"))
# print("9======================================")
# print(f"Dial call history for {N1100.model}:{N1100.dialCallHistory}")
# print(f"Dial call history for {N3110.model}:{N3110.dialCallHistory}")

# class SportsPerson:
#   def __init__(self, team_name, name, role):
#     self.__team = team_name
#     self.__name = name
#     self.role = role
#     self.earning_per_match = 0
#   def get_name_team(self):
#     return 'Name: '+self.__name+', Team Name: ' +self.__team
# class Player(SportsPerson):
#     def __init__(self, team_name, name, role, goal, played):
#         super().__init__(team_name, name, role)
#         self.goal = goal
#         self.played = played
#     def calculate_ratio(self):
#         self.ratio = self.goal / self.played
#     def print_details(self):
#         earning = (self.goal * 1000) + (self.played * 10)
#         print(super().get_name_team())
#         print(f"Team Role: {self.role}")
#         print(f"Total Goal: {self.goal}, Total Played: {self.played}")
#         print(f"Goal Ratio: {self.ratio}")
#         print(f"Match Earning: {earning}K")
# class Manager(SportsPerson):
#     def __init__(self, team_name, name, role, win):
#         super().__init__(team_name, name, role)
#         self.win = win
#     def print_details(self):
#         earning = self.win * 1000
#         print(super().get_name_team())
#         print(f"Team Role: {self.role}")
#         print(f"Win: {self.win}")
#         print(f"Match Earning: {earning}K")
# player_one = Player('Juventus', 'Ronaldo', 'Striker', 25, 32)
# player_one.calculate_ratio()
# player_one.print_details()
# print('------------------------------------------')
# manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
# manager_one.print_details()

# class A:
#     temp = 7
#     def __init__(self):
#         self.y = A.temp - 3
#         self.sum = self.temp + 2
#         A.temp += 3
#     def methodA(self, m, n, x=0):
#         self.y = self.y + m + (A.temp)
#         x = x + 2 + n
#         self.sum = self.sum + x + self.temp
#         print(x, self.y, self.sum)
# class B(A):
#     temp = 1
#     def __init__(self, obj=None):
#         super().__init__()
#         self.temp = self.temp + B.temp
#         self.sum = 3 + B.temp + A.temp
#         if obj != None:
#             obj.methodB(3, 6)
#         else:
#             self.methodB(1, 4)
#     def methodB(self, m, n):
#         y = self.temp + self.y + n
#         B.temp = m + self.y + n
#         self.methodA(n, m)
#         self.sum = self.y + y + A.temp
#         print(self.temp , y, self.sum)
# b1 = B()
# b2 = B(b1)


# Summer final 2022
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
#   activity=['No recent acitivity.']
  
#   def __init__(self, name, email, phn='No set'):
#     super().__init__(name, email)
#     self.phn = phn
#     self.task=''

#   def userDetail(self):
#     return f"User Detail:\nName:{self.name}\nEmail: {self.email}\nPhone: {self.phn}\nActivity Log: {BracbookUser.activity[0]}"

#   def UserActivity(self, activityType):
#     self.activityType = activityType
#     if super().UserActivity(activityType) == True:
#       self.task += self.activityType + ', '
#       print(f'{self.name} has {self.activityType}(d/ed) successfully')
#       BracbookUser.activity[0] = self.task[:-2]
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

#fall22
# class Mobile:
#   countryCodes = {"880": "Bangladesh", "966": "India","455": "USA"}
#   def __init__(self, model, simCardStatus):
#     self.model = model
#     self.__simCardStatus = simCardStatus
#     print(f"Model {model} is manufactured.")
#   def setSimCardStatus(self,status):
#     self.__simCardStatus = status
#     print("SIM card status updated successfully.")
#   def getSimCardStatus(self):
#      return self.__simCardStatus
#   def __str__(self):
#     return f"Mobile Phone Detail:\nModel:{self.model}\nSIM Card Status: {self.__simCardStatus}"

# class Nokia(Mobile):
#   dialCallHistory=[]
#   def __init__(self,model,sim,bal=0):
#     super().__init__(model,sim)
#     self.bal=bal
    

#   def __str__(self):
#     return (f"{super().__str__()}\nBalance:{self.bal}")

#   def dialCall(self,s):
#     i=s[0:3]
#     if self.getSimCardStatus():
#       if self.bal!=0 :
#         if i in Mobile.countryCodes:
#           Nokia.dialCallHistory.append(s)
#           return(f"Dialing the number {s} to {Mobile.countryCodes[i]} region.")
          
#         else:
#           return("Dialing is not allowed in this region.")
#       else:
#         return("Insufficient balance!")
#     else:
#       return("No SIM card available!")

#   def changeSIMCardStatus(self):
#     status=super().getSimCardStatus()
#     if status :
#       super().setSimCardStatus(False)
#     else:
#       super().setSimCardStatus(True)

#   def rechargeSIMCard(self,amount):
#     self.bal+=amount
#     print(f"""Recharge successful! Current balance {self.bal} TK.""")
    
#   # def dialCallHistory(self):
#   #   return Nokia.history

# N3110 = Nokia("N3110", False)
# print("#######################################")
# print(N3110)
# print("1======================================")
# N1100 = Nokia("N1100", True,100)
# print("#######################################")
# print(N1100)
# print("2======================================")
# print(N3110.dialCall("88017196xxxx"))
# print("3======================================")
# N3110.changeSIMCardStatus()
# print("4======================================")
# print(N3110.dialCall("88017196xxxx"))
# print("5======================================")
# N3110.rechargeSIMCard(200)
# print("6======================================")
# print(N3110.dialCall("88017196xxxx"))
# print("7======================================")
# print(N1100.dialCall("45617196xxxx"))
# print("8======================================")
# print(N1100.dialCall("45517196xxxx"))
# print(N1100.dialCall("96617196xxxx"))
# print("9======================================")
# print(f"Dial call history for {N1100.model}:{N1100.dialCallHistory}")
# print(f"Dial call history for {N3110.model}:{N3110.dialCallHistory}")

# class SportsPerson:
#   def __init__(self, team_name, name, role):
#     self.__team = team_name
#     self.__name = name
#     self.role = role
#     self.earning_per_match = 0
#   def get_name_team(self):
#     return 'Name: '+self.__name+', Team Name: ' +self.__team
# class Player(SportsPerson):
#     def __init__(self, team_name, name, role, goal, played):
#         super().__init__(team_name, name, role)
#         self.goal = goal
#         self.played = played
#     def calculate_ratio(self):
#         self.ratio = self.goal / self.played
#     def print_details(self):
#         earning = (self.goal * 1000) + (self.played * 10)
#         print(super().get_name_team())
#         print(f"Team Role: {self.role}")
#         print(f"Total Goal: {self.goal}, Total Played: {self.played}")
#         print(f"Goal Ratio: {self.ratio}")
#         print(f"Match Earning: {earning}K")
# class Manager(SportsPerson):
#     def __init__(self, team_name, name, role, win):
#         super().__init__(team_name, name, role)
#         self.win = win
#     def print_details(self):
#         earning = self.win * 1000
#         print(super().get_name_team())
#         print(f"Team Role: {self.role}")
#         print(f"Win: {self.win}")
#         print(f"Match Earning: {earning}K")
# player_one = Player('Juventus', 'Ronaldo', 'Striker', 25, 32)
# player_one.calculate_ratio()
# player_one.print_details()
# print('------------------------------------------')
# manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
# manager_one.print_details()

# class A:
#     temp = 7
#     def __init__(self):
#         self.y = A.temp - 3
#         self.sum = self.temp + 2
#         A.temp += 3
#     def methodA(self, m, n, x=0):
#         self.y = self.y + m + (A.temp)
#         x = x + 2 + n
#         self.sum = self.sum + x + self.temp
#         print(x, self.y, self.sum)
# class B(A):
#     temp = 1
#     def __init__(self, obj=None):
#         super().__init__()
#         self.temp = self.temp + B.temp
#         self.sum = 3 + B.temp + A.temp
#         if obj != None:
#             obj.methodB(3, 6)
#         else:
#             self.methodB(1, 4)
#     def methodB(self, m, n):
#         y = self.temp + self.y + n
#         B.temp = m + self.y + n
#         self.methodA(n, m)
#         self.sum = self.y + y + A.temp
#         print(self.temp , y, self.sum)
# b1 = B()
# b2 = B(b1)


# Summer final 2022
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
#   activity=['No recent acitivity.']
  
#   def __init__(self, name, email, phn='No set'):
#     super().__init__(name, email)
#     self.phn = phn
#     self.task=''

#   def userDetail(self):
#     return f"User Detail:\nName:{self.name}\nEmail: {self.email}\nPhone: {self.phn}\nActivity Log: {BracbookUser.activity[0]}"

#   def UserActivity(self, activityType):
#     self.activityType = activityType
#     if super().UserActivity(activityType) == True:
#       self.task += self.activityType + ', '
#       print(f'{self.name} has {self.activityType}(d/ed) successfully')
#       BracbookUser.activity[0] = self.task[:-2]
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

# -------------------- SUMMER 2023 -----------------------

# Lab 2 Home Task - Tick Tac Toe

# from IPython.display import clear_output
# import time

# # All the variables needed
# board = [[1,2,3],[4,5,6],[7,8,9]] # The players will be placing their characters in this list
# # and the whole game be conducted based on the current status of this list.
# current_player_char = 'X' # The character of the current player
# next_player_char = 'O' # The character of the next player
# totalInputs = 9 # Since there are 9 slots in total in the whole board.
# winner = None

# def checkHorizontal():
#     global winner
#     for row in board:
#         if row[0] == row[1] == row[2]:
#             winner = "Player 1" if row[0] == 'X' else "Player 2"

# def checkVertical():
#     global winner
#     for col in range(3):
#         if board[0][col] == board[1][col] == board[2][col]:
#             winner = "Player 1" if board[0][col] == 'X' else "Player 2"

# def checkDiagonal():
#     global winner
#     if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
#         winner = "Player 1" if board[1][1] == 'X' else "Player 2"

# def checkBoard():
#     checkHorizontal()
#     checkVertical()
#     checkDiagonal()
#     return winner is not None

# def placeCharacterOnBoard(pos):
#     if pos>=1 and pos<=9:
#       row = (pos - 1) // 3
#       col = (pos - 1) % 3

#       if isinstance(board[row][col], int):
#           board[row][col] = current_player_char
#           return 1
#       else:
#           print("Invalid position. Please choose another position.")
#           return 0
#     else:
#       print("Invalid position. Please choose another position.")
#       return 0

# # This function prints the current status of the 'board' list in a particular format.
# def printCurrentBoard():
#     print("-------------")
#     for eachRow in board:
#         print("|",end="")
#         for eachCol in eachRow:
#             print(f" {eachCol} ",end="|")
#         print() #To move to the next row
#         print("-------------")

# # This function will simulate the whole game.
# def runGame():
#     global current_player_char, next_player_char, winner
#     welcome_msg = '''Welcome to the TIC-TAC-TOE game. The first player to place a character on the board will be Player 1 (Character X) and the other player will be Player 2 (Character O).'''
#     print(welcome_msg)
#     inputCount = 0 # This variable is for counting the number of inputs and controlling the loop based on it.
#     while inputCount < totalInputs:
#         printCurrentBoard() # This function prints the current state of the board as a player needs to see it before making the next move.
#         position = int(input(f"Player {(inputCount%2)+1}, enter a position that does not contain any X or O: ")) # The user needs to enter a position that does not contain any X or O.
#         validityOfInput = placeCharacterOnBoard(position) # validityOfInput will be 1 if the user inputs a valid "position"; otherwise, it will be 0.
#         inputCount += validityOfInput # If the player inputs a valid "position", the inputCount will increase by one; otherwise, it will remain as it is.
#         if inputCount >= 5: # There is no need to check the board before 5 valid inputs as there will be no winners before 5 valid inputs.
#             if checkBoard(): # If checkBoard() returns True, then the current player won the game.
#                 winner = "Player 1" if current_player_char == 'X' else "Player 2"
#                 clear_output() # This function clears the output panel.
#                 break
#         if validityOfInput: # Only if the player inputs a valid "position", the player characters will be swapped for the next move.
#             current_player_char, next_player_char = next_player_char, current_player_char # The players will place characters alternatively. So if X is the current player's character, in the next turn O will be the current player's character.
#         clear_output() # This function clears the output panel before printing the current board status for the next player.
#     printCurrentBoard()
#     # After the while loop, if the value of winner is still None, that means the game ended in a draw; otherwise, we have a winner.
#     if winner is not None:
#         print(f"Well done, {winner}. You have won the game.")
#     else:
#         print("The game ended in a draw.")

# runGame()

# Previous theory quiz question solve

# t1=(('D',[12,22,95,43]) ,('e',[44,56,2]),('F',[6,8,22,1]), ('G', [55,15]),('h',[9,0,13,13,51,3]))
# d={}
# for i in t1:
#     if 'A'<= i[0] <='Z':
#         add=0
#         for j in i[1]:
#             add+=j
#         k = 'Sum of '+i[0]
#         d[k]=add
#     else :
#         prod = 1
#         for k in i[1]:
#             prod *= k 
#         k = 'Product of '+i[0]
#         d[k]=prod
# print(d)

# Assignment 2 - 2023

class CellPackage:
    def __init__(self, price, data, talk_time,messages,cashback, validity ):
        self.price = price
        data=data.split(' ')
        self.data = int(data[0])*1024
        self.talk_time = talk_time
        self.messages=messages
        self.cashback=int((self.price*(int(cashback[:-1])/100))//1)
        self.validity=validity
        # self.dict1={'Data =':f'{self.data} MB','Talktime =':f'{self.talk_time} Minutes','SMS/MMS =':f'{self.messages}','Validity =':f'{self.validity} Days','--> Price = ':f'{self.price} tk','Buy now to get':f'{self.cashback} tk cashback.'}

pkg = CellPackage(150, '6 GB', 99, 20, '7%', 7)
print('============= Package 1 =============')
# Subtask 2: Check each attribute and print
if pkg.data:
    print(f"Data = {pkg.data} MB")
if pkg.talk_time:
    print(f"Talktime = {pkg.talk_time} Minutes")
if pkg.messages:
    print(f"SMS/MMS = {pkg.messages}")
print(f"Validity = {pkg.validity} Days")
print(f"--> Price = {pkg.price} tk")
if pkg.cashback:
    print(f"Buy now to get {pkg.cashback} tk cashback.")

pkg2 = CellPackage(700, '35 GB', 700, 0, '10%', 30)
print('============= Package 2 =============')
# Subtask 3: Check each attribute and print
if pkg2.data:
    print(f"Data = {pkg2.data} MB")
if pkg2.talk_time:
    print(f"Talktime = {pkg2.talk_time} Minutes")
if pkg2.messages:
    print(f"SMS/MMS = {pkg2.messages}")
print(f"Validity = {pkg2.validity} Days")
print(f"--> Price = {pkg2.price} tk")
if pkg2.cashback:
    print(f"Buy now to get {pkg2.cashback} tk cashback.")
    
pkg4 = CellPackage(120, '0 GB', 190, 0, '0%', 10)
print('============= Package 3 =============')
# Subtask 4: Check each attribute and print
if pkg4.data:
    print(f"Data = {pkg4.data} MB")
if pkg4.talk_time:
    print(f"Talktime = {pkg4.talk_time} Minutes")
if pkg4.messages:
    print(f"SMS/MMS = {pkg4.messages}")
print(f"Validity = {pkg4.validity} Days")
print(f"--> Price = {pkg4.price} tk")
if pkg4.cashback:
    print(f"Buy now to get {pkg4.cashback} tk cashback.")