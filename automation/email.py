import re


with open ('automation/potential-contacts.txt','w') as f:
    contant_file=f.read()

match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', contant_file)
print(match)

