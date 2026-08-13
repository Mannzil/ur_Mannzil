my_tuple_var = (88, 0.5,'Yuta')
print( 'Tuple: ', my_tuple_var)
my_integer_var = 10
print( 'integer:' , my_integer_var)
my_float_var = 99.9
print( 'float:' , my_float_var)
my_string_var = 'Luffy x Ace'
print( 'string:' , my_string_var)
my_boolean_var = True
print( 'boolean:' , my_boolean_var)
my_set_var = {7, 3.5, 'Sukuna'}
print( 'set:' , my_set_var)
my_dictionary_var = {4, 3.5, 'Zoro', 'Saturo Gojo'}
print( 'dictionary:' , my_dictionary_var)
my_range_var = range(7)
print( 'range:', my_range_var)
my_list_var = [8, 9.9, 'jjk']
print( 'list:' , my_list_var)
my_none_var = None
print( 'None:' , my_none_var)
my_integer_var = 10
print(type(my_integer_var))
developer = 'Mannzil'
print(type(developer))

#     String Practice

my_str = 'Hello World'
print('World' in my_str) 
print('z' in my_str)
my_str = 'One Piece'
print(len(my_str))
print(my_str[4])
my_str_1 = "Luffy is "
my_str_2 = 'King of the Pirates'
str_plus_str = my_str_1 + '' +my_str_2 
print(str_plus_str)
sound = 'Arrrgh'
repeated_sound = sound * 4
print(repeated_sound)
name = 'Ace'
Age = 20
name_and_Age = name + str (Age)
print(name_and_Age)
name = 'Kaneki'
age = 19
name_and_age = f'My name is {name} and I am {age} years old.'
print(name_and_age)
str = 'Bankai'
print(str[::-1])
my_str = 'idle transfiguration'
uppercase_my_str = my_str.upper()
print(uppercase_my_str)
my_str = 'mui tempen'
replace_my_str = my_str.replace('mui' , 'mugen')
print(replace_my_str)
my_str = 'Muzan Kibutsuji'
world_index = my_str.find('Kibutsuji')
print(world_index)
my_str = 'Ayanokoji senpai'
title_case_my_str = my_str.title()
print(title_case_my_str)
first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
address = '123 Main Street'
address += ', Apartment 4B'
employee_age = 28
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)
experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)
position = 'Data Analyst'
salary = 75000
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)
employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3]
print(department)
year_code = employee_code[4:8]
print(year_code)
initials = employee_code[9:11]
print(initials)
last_three = (employee_code[-3:])
print(last_three)


