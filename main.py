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
my_int_1 = 39
my_int_2 = 35
sum_ints = my_int_1 + my_int_2
print('Sum of integers:', sum_ints)
my_int_1 = 37
my_int_2 = 29
diff_ints = my_int_1 - my_int_2
print('difference of integers:', diff_ints)
my_float_3 = 5.22
print(type(my_float_3))
my_int_1 = 48
my_int_2 = 13
mod_ints = my_int_1 % my_int_2
print('modulus integer:', mod_ints)
my_int_2 = 98
my_int_3 = 45
floor_division = my_int_2 // my_int_3
print('floor_divison' , floor_division)
my_int_2 = 24
my_int_4 = 2
exp_int = my_int_2 ** my_int_4
print('exponential function' , exp_int)
my_float = 3.67
my_int = int(my_float)
print(my_int)
num = 45
num += 45
print(num)
count = 66
count //= 3
print(count)
biii = 'Super Saiyan'
biii += ' Vegeta'
print(biii)



#   Bill Splitter


running_total = 0

num_of_friends = 4

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

tip = running_total * 0.25
print('Tip amount:', tip)

running_total += tip
print('Total with tip:', running_total)

final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

round(final_bill,2)
each_pays = round(final_bill, 2)
print('Each person pays:', each_pays)


Power_Level = 3000000
if Power_Level >= 3000000:
    print('You are a Super Saiyan God')
Pure_Soul = 1000000
if Pure_Soul >= 1000000:
    print('You are a Super Saiyan Blue')
else:
    print('You are a Super Saiyan')
age = 3
if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
elif age >= 2:
    print('You are a child')
else:
    print('You are a young adult')
is_citizen = False
age = 55
print(is_citizen and age)
is_admin = False
if not is_admin:
    print('Access denied')
else:
    print('Access Granted')

        #Build a Movie Ticket Booking Calculator


base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'

if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

is_member = False
is_weekend = False

discount = 0
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)
    final_price = base_price + extra_charges + service_charges - discount 
    print('Final price of ticket:', final_price)
else:
    print('Ticket booking failed due to restrictions')        