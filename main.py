# # #المطلوب الاول والثاني
# name = input("Enter Your Name:")
# print('"Name:'+(name)+"\"")
# age =int(input('Enter your Age:'))
# #print('"Age: '+age+"\"")
# address=input('Enter your Address(steet,city,country):')
# print('"Address: ' +address+"\"")

# #المطلوب الثالث
name='Ali'
age=22
street=142
city='Gaza'
country='Palestine'
new_age= age-5
output=  f"Hello {({name})}Your age is {new_age} Years Old, Your Address is {street,city,country}"
#print(output)

# #المطلوب الرابع
# print(type(name))
# print(type(age))
# print(type(street))
# print(type(city))
# print(type(country))
#
# #المطلوب الخامس
# output2=f'Hello \'{name}\' , How Are You? \ """Your Age Is \"{new_age}\" + And Your Country Is: {country}'
# print(output2)

# #المطلوب السادس
# output3 = f'"Hello \'{name}\',How Are You? \
# """ Your Age Is \"{new_age}\"  +And Your City Is:{city}'
# print(output3)

#المطلوب السايع
# full_name = 'Doaa Reem'
# output4 = f' "{full_name[0]}"'
# print('First Letter Is :'+output4)
# output4=f'"{full_name[2]}"'
# print('Third Letter Is : '+output4)
# output4=f'"{full_name[-1]}"'
# print('Last  Letter Is : '+output4)

#المطلوب الثامن
# name='Doaa Reem'
# print(name[6:])
# print(name[0:4])
# capetal= name[2:3].upper()+(name[3:7])
#
# print(capetal) # انتبهي هنا في فراغ
# print(name[:-5:-1])
# x1= name[0:2]
# x2=name[5:7]
# print(x1,x2)

#المطلوب التاسع

# name = "$&$&Mohammed$&$&"
# print(name.strip('$&'))

# #المطلوب العاشر
# message= "I %7 Python And Although I %7 GSG with Zakaria"
# print(message.replace('%7','Love'))

# مطلوب 11
# name1 = 'tasneem mosabeh'
# name2 ='i love python with gsg'
# print(name1.capitalize()) # بتعمل كابيتال لاول حرف فقط
# print(name2.title())# بتعمل كابيتال لاول حرف من كل كلمة

#مطلوب 12
# num1 = "4"
# num2 = "56"
# num3 = "963"
# num4 = "385"
# num5 = "8719"
# num6 = "87190"
#
# print(num1.zfill(5))
# print(num2.zfill(5))
# print(num3.zfill(5))
# print(num4.zfill(5))
# print(num5.zfill(5))
# print(num6.zfill(5))

#مطلوب 13
# the_name = "Hadeel"
# print("*" * 11 + the_name )
# print("*" * 11 + the_name  + "*" * 11)
# print(the_name  + "*" * 11)

# مطلوب 14
# name_one = "HaLA"
# name_two = "shaHD"
# print(name_one[0].lower()+name_one[1].upper()+name_one[2].lower()+name_one[3].lower())
# print(name_two[0].upper()+name_two[1].upper()+name_two[2].upper()+name_two[3].lower()+name_two[4].lower())
# print(name_one.upper())
# print(name_one.lower())

#مطلوب 15
# name_one = "HaLA"
# name_two = "shaHD"
# if name_one.isupper():
#     print("yes all the name is upper latter")
# else:
#     print("No")
#
# if name_two.islower():
#     print("yes all the name is lower latter")
# else:
#     print("No")

#مطلوب 16
# name_one = "HaLA"
# name_two = "shaHD"
# if name_one.find('S'):
#     print("yes ")
# else:
#     print("No")
#
# if name_two.find('SH'):
#     print("yes ")
# else:
#     print("No")

#مطلوب 17
# msg = "I Love Python And Although I Love GSG with Zakaria"
# love_count = msg.count("Love")
# print("'Love'", love_count, "times in the string.")
# t_count = msg.count("t")
# print("'t'", t_count, "times in the string.")

#مطلوب 18
# name = "Zakaria"
# position = name.index("r")
# print(position)

#مطلوب 19
message = "I %7 Python And Although I %7 GSG with Zakaria"
modified_msg = message.replace("%7", "Love", 1)
print(modified_msg)