from faker import Faker
import re
fake=Faker('en_us')

potential_txt=""

for i in range(100):

    email = fake.email()
    phone_number = fake.phone_number()
    potential_txt += fake.paragraph()
    potential_txt += " " + email + " "
    potential_txt += fake.paragraph()
    potential_txt += fake.sentence()
    potential_txt += phone_number
    potential_txt += fake.paragraph()

with open ('automation/potential-contacts.txt','w') as f:
    f.write(potential_txt)
# print(fake.phone_number())
# print(potential_txt)

match_email = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', potential_txt)
email_format=""
for i in match_email:
    email_format += f'{i}\n'
# print (email_format)
with open ('automation/email.txt','w+') as f:
    f.write(email_format)

# match_email = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', potential_txt)
# print(match_email)

#==================phone========================

match_phone = re.findall("(\d{3}\D{0,3}\d{3}\D{0,3}\d{4})", potential_txt)
format_phone1=""
for i in match_phone:
    # phone = re.search(r'(\d+-?){1,2}$', addr_str)
    format_phone1 +=f'{i} '
last_num=re.sub(r"[)-.]", "-",str(format_phone1))
x_num=re.sub(r"[(]", "",last_num)
x_num= x_num.split(" ")
list_item=[]
for num in x_num:
    if len(num) < 11:
        list_item.append(f"{num[:3]}-{num[3:5]}-{num[5:]}")
    else:
        list_item.append(num)
list='' 
for i in list_item:
    list += f'{i}\n'
print (list)
with open ('automation/phone_number.txt','w+') as f:
    f.write(list)
# # nl='\n'
# print (phone_format)