import pandas as pd
import json

f=open("C:\\Users\\HP PC\\OneDrive\\Desktop\\JSONProj\\ComplexJSON.json","r")
file=json.load(f)

employees=file['Employees']
#print(employees)

row=[]

for data in employees:
    name=data['name']
    desg=data.get('desg','null')
    city=data.get('city','null')
    salary=data.get('salary','null')

    experience=data['Experience']
    for x in experience:
        primaryskill=x['skills'].get("primary",'null')
        secondaryskill=x['skills'].get('secondary','null')
        projects=x.get('projects','null')

    contact = data.get('Contact', {})
    emergency_phone = contact.get('emergency_phone', 'null')

    primary_phone = contact.get('primary_phone', [])
    for phone in primary_phone:
        phoneType = phone.get('PhoneType', 'null')
        number = phone.get('Number', 'null')
        row.append([name, desg, city, salary, "Phone", phoneType, number, 'null', 'null',emergency_phone,primaryskill,secondaryskill,projects])

    email = contact.get('email', [])
    for mail in email:
        mailtype = mail.get('MailType', 'null')
        emailID = mail.get('EmailID', 'null')
        row.append([name, desg, city, salary, "Email", 'null', 'null', mailtype, emailID, emergency_phone, primaryskill,
                    secondaryskill, projects])

    if (contact == {}):
        row.append([name, desg, city, salary, 'null','null' ,'null','null','null','null',  primaryskill,
                    secondaryskill, projects])

df = pd.DataFrame(row, columns=["name", "desg", "city", "salary", "ContactType", "PhoneType", "Number", "MailType",
                                    "EmailID", 'EmergencyContact' ,'Skill1' ,'Skill2' ,'Project'])

# print(df.to_string())

#df.to_csv("C:\\Users\\HP PC\\OneDrive\\Desktop\\JSONProj\\Converted\\Emp.csv")






