""" Assignment 1 uses temperatures"""
import webbrowser

url = "https://www.google.com/"

temp_1_string = float(input('Enter 1st temperature in Celsius:'))
temp_2_string = float(input('Enter 2nd temperature in Celsius:'))
temp_3_string = float(input('Enter 3rd temperature in Celsius:'))

if(temp_3_string<0):
    print("It's below freezing in Florida!")
if(temp_3_string==0):
    print("It's freezing in Florida!")
if(temp_3_string>0):
    print("It's above freezing in Florida!") 

print(temp_1_string, 'first temperature')
print(temp_2_string, 'second temperature')
print(temp_3_string, 'third temperature')

sum_of_temp = temp_1_string+temp_2_string+temp_3_string
print('Sum of 3 temperatures is :' , sum_of_temp)
avg_of_temp = round(sum_of_temp/3,2)
print('Average of 3 temperatures is:', avg_of_temp)
prd_of_temp = (temp_1_string*temp_2_string*temp_3_string)
print('Product of 3 temperatures:', prd_of_temp)
sml_of_temp = min(temp_1_string,temp_2_string,temp_3_string)
print('smallest temperature is:',sml_of_temp)
lgt_of_temp = max(temp_1_string,temp_2_string,temp_3_string)
print('Largest temperature is:',lgt_of_temp)
print('Range:',min(temp_1_string,temp_2_string,temp_3_string),'-',max(temp_1_string,temp_2_string,temp_3_string))

more_details = input("Want more details about weather? Yes or No")

if(more_details == "Yes"):
  webbrowser.open(url)