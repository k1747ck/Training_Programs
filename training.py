# fruits = ['apple' , 'banana' , 'cherry']

# print(fruits.index('banana'))
# print(fruits.count('apple'))
# num = [1,2,3,4,5,6,7,8,9,10]
# num.sort()
# print(num)

# num1 = [10,9,8,7,6,5,4,3,2,1]
# num1.sort()
# print(num1)
# my_tuple = (1,2,3)
# print("tuple:" , my_tuple)
# print(type(my_tuple))
# list=((1,2,3),1,2,3,(1,2,3),True,(5,8),"Khushi",True)
# print(list)

# my_set2 = set ([1,2,2,3])
# print ("my_set2", my_set2)

# print(type(my_set2))

# a = list(my_set2)
# print(type(a))
# # methods
# # diffrence
# my_set = ({1,2,3})
# print(my_set)
# s = set ({1,2,3,4,4,3})
# print(s)
# # membership testing
# lst = [1,2,3,3,4,4,2,5]
# num = set(lst)
# print("original list:", lst)
# print("List to set:", num)
# fs = frozenset([1,2,2,3])
# print("frozenset fs :", fs)
# my_dic = {
#     "name" : "khushi",
#     "age" : 20,
#     "country" :"India"
# }
# print(my_dic)
# # operations
# grading

# while True:
#     print("Khushi")


# for i in range(6):
#     if i == 6:
#         continue
#     print(i)


# user = True
# while (user):
#     n =int(input("Enter the value :"))
#     for i in range (1, 11):
#         print (f"{n}*{i}={n*i}")
        
#     n = int(input("you want to print next table :"))
#     if (n == 1): user= True
#     elif(n ==0): user= False
            
    
# def print_hello():
#     print("hello world") 
# # print_hello()


# def add(a,b):
#     return a+b
# print (add(2,6))    



# class college :
#     colleges = "ITM University"
#     def __init__(self, name):
#         self.name = name
        
#     def info(self):
#         print(f"The name of the student is {self.name} and she studies in {self.colleges}")
        
# coll = college("Khushi")

# # print (coll.name)
# # print (coll.colleges)

# coll.info()        


class bankaccount:
    def __init__(self, balance):
        self.balance = balance
        
    def deposit (self,amount):
        self.balance+=amount
        
    def show_balance(self):
        print (f"Total balance: {self.balance}")
        
    def withdraw_balance (self,with_amount):
        self.balance-=with_amount
        
acc= bankaccount(2000)
acc.show_balance()
acc.deposit(500)
acc.show_balance()
acc.withdraw_balance(2000)
acc.show_balance()
