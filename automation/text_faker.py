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
    phone = re.search(r'(\d+-?){1,2}$', addr_str)
    format_phone1 +=f'{i} \n'
last_num=re.sub(r"[)-.]", "-",format_phone1)
x_num=re.sub(r"[(]", "",last_num)


for num in x_num:
    if len(num) == 10:
        num=f"{num[:3]} - {num[3:5]} - {num[5:]}"
    # print(num)
    x_num += num
print (x_num)
# with open ('automation/phone_number.txt','w+') as f:
#     f.write(phone_format)
# # nl='\n'
# print (phone_format)