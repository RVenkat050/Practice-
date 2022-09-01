# a=100
# b=10.55
# c="venkat"
# print(a)
# print(b)
# print(c)
# print(type(b))
# print(type(a))
# print(type(c))


# for i in range (0,100):
#     if i%3==0:
#         print("FIZZ")
#     if i%5==0:
#         print("buzz")
#     if i%3==0 and i%5==0:
#         print("fizz buzz")
#     else:
#         print(i)


# a=3
# b=4
# print('The value of 3+4 is',3+4)
# print('The value of 3-4 is',3-4)
# print('The value of 3*4 is',3*4)
# print('The value of 3/4 is',3/4)

# a=34
# a-=12
# print(a)
# a=34
# a+=12
# print(a)
# a=34
# a*=12
# print(a)
# a=34
# a/=12
# print(a)



# b=(4>5)
# print(b)
# b=(14<7)
# print(b)
# b=(14>7)
# print(b)
# b=(14==7)
# print(b)
# b=(14!=7)
# print(b)



# b1=True
# b2=False
# print("The value of b1 and b2 is ",(b1 and b2))
# print("The value of b1 or b2 is ",(b1 or b2))
# print("The value of  not b2 is ",(not b2))


# a=10
# b=20.2022
# c='venkat'
# print(type(a))
# print(type(b))
# print(type(c))


# a='7411'
# b=int(a)
# print(b+5)
# a='7411'
# print(a+5)
# for i in range(0,10):
#     if i%3==0:
#         print(i)
#     elif i%5==0:
#         print(i)
#     elif i%3==0 and i%5==0:
#         print(i)
#     else:
#         print(i)

# a=input("enter your name: ")
# a=int(a)
# print(type(a))
# a=input("enter your phone no: ")
# a=str(a)
# print(type(a))


# def functionname(Email):
#     print(Email)

# a=input("enter your name: ")

# functionname(a)

# class Mobile:
#     def __init__(self, battery,brand,camera,price):
#         self.battery=battery
#         self.brand=brand
#         self.camera=camera
#         self.price=price
#     def display(self):
#         print("battery:", self.battery)
#         print("brand:", self.brand)
#         print("camera:", self.camera)
#         print("price",self.price)

#         print("-----------------------------")
# obj=Mobile("5000mah","OPPO","60mp",30000)
# obj.display()
# obj=Mobile("4000mah","MI","50mp",20000)
# obj.display()



# a=60
# if (a>4):
#     print("the value is greater than 4")
# if(a>15):
#     print("the value is greater than 15")
# if(a>30):
#     print("the value is greater than 30")
# if(a<40):
#     print("the value is less than 40")
# else :
#     print("The value is not greater than 50")

#     print("Done")


# a=60
# if (a<10):
#     print("the value is less than 10")
# if(a>25):
#     print("the value is greater than 25")
# if(a>30):
#     print("the value is greater than 30")
# if(a<40):
#     print("the value is less than 40")
# else :
#     print("The value is not greater than 50")

#     print("Done")

# age=int(input("Enter your age: "))
# if age>18:
#     print("yes")
# else:
#     print("no")

# Age=int(input("Enter your Age: "))
# if (Age>25) and (Age<40):
#     print("you can work with us")
# else:
#     print("you are not work us")


# amount=50000
# enter_Pin=int(input("Enter your atm pin: "))
# enter_Cash=int(input("Enter your cash: "))
# remaing_Balance=(amount-enter_Cash)

# print("Take your cash: ", enter_Cash, )
# print("Remaining Balance is: ",remaing_Balance)
# print("Thankyou")

# a=None
# if (a is None):
#     print("yes")
# else:
#     print("no")

# a=[45,25,10]
# print(25 in a)

# for i in range(0,100):
#     if (i%3==0):
#         print("fuzzy")
#     if (i%5==0):
#         print("buzzy")

#     if (i%3==0) and (i%5==0):
#         print("fuzzybuzzy")
#     else:
#         print(i)
# from operator import truediv
# from unicodedata import name


1
# num1=(input("Enter number1 :"))
# num2=(input("Enter number2 :"))
# num3=(input("Enter number3 :"))
# num4=(input("Enter number4 :"))

# if(num1>num4):
#     F1=num1
# else:
#     F1=num4

# if(num2>num3):
#     F2=num2
# else:
#     F2=num3
# if (F1>F2):
#     print((F1) +"is Greatest")
# else:
#     print((F2) + "is Greatest")

# sub1=int(input("Enter first subject marks\n"))
# sub2 =int(input("Enter first subject marks\n"))
# sub3=int(input("Enter first subject marks\n"))
 
# if(sub1<33 or sub2<33 or sub3<33 ):
#     print("You are fail because you get marks less than 33")
# elif(sub1+sub2+sub3)/3<40:
#     print("you are fail because your total percentage is less than 40%")
# else:
#     print("congralutations you are pass")

# Text=input("Enter your text ")
# spam=False


# if ("Make a lot of money" in Text):
#     spam=True
# elif("buy now" in Text):
#     spam=True
# elif("subscribe this" in Text):
#     spam=False
# else:
#     spam=False
# if(spam):
#     print("this text is spam")
# else:
#     print("this text isnot spam")

# Username=input("Enter your name")
# if(len(Username))<10:
#     print("username contains less than 10 char")
# else:
#     print("Username contains more than 10 char")


# Names=["Aruna","venkat","pavan","Rupesh","Manju"]
# name=input("Enter name to check")
# if (name in Names):
#     print("Name is found")
# else:
#     print("Name is not found")

num1 = int(input("Please Enter the First Number  = "))
num2 = int(input("Please Enter the second number = "))

sub = num1 - num2
print('The Result of subtracting {0} from {1} = {2}'.format(num2,num1,sub)