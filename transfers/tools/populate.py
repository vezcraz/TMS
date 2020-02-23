from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from transfers.models import UserProfile
from transfers.constants import CampusType, TransferType, UserType
import pandas as pd
import re

campusCode = {'Goa': CampusType.GOA.value, 
'Hyderabad': CampusType.HYD.value, 
'Pilani':CampusType.PILANI.value}

def populate(request):
#Student Populate
    def stu_populate():
        credentials=pd.DataFrame()
        stu=pd.read_excel('transfers/tools/data/student.xlsx')
        for index, row in stu.iterrows():
            cid = row['Campus ID']
            username=cid
            # contact = row['contact']
            name = row['Name'].split()
            fname = name[0]
            lname=""
            for i in range(1,len(name)):
                if(name[i]!='.'):
                    lname=lname+name[i]+" " 
            print(fname, lname)
            start = 'f'
            if cid[4]=='H':
                start = 'h'
            email = start+cid[0:4] + cid[8:-1] + "@" + row['Campus'].lower()+".bits-pilani.ac.in"
            # break
            password = User.objects.make_random_password()
            temp={'Username': username, 'Password': password}
            credentials=credentials.append(temp, ignore_index=True)
            
            try:
                user = User.objects.create_user(username,email,password
                    , first_name=fname, last_name=lname)
                user.is_active = True
                profile = UserProfile(
                    user=user,
                    campus=campusCode[row['Campus']],
                    user_type=UserType.STUDENT.value
                     )
                profile.save()
            except:
                print("(Fail Username)")
            # break        
        credentials.to_csv('transfers/tools/creds/stu_details.csv', index=False)
#Faculty Populate
    def fac_populate():
        credentials=pd.DataFrame()
        fac = pd.read_excel('transfers/tools/data/faculty.xlsx')
        for index, row in fac.iterrows():
            eid = row['Employee ID']
            username=eid
            c = str(row['Contact No. - Mobile'])
            contact = int(re.sub('[^0-9]','',c))
            name = row['Full Name'].split()
            fname = name[0]
            lname=""
            for i in range(1,len(name)):
                lname=lname+name[i]+" " 
            print(fname, lname)
            email = row['Official Email ID']
            password = User.objects.make_random_password()
            temp={'Username': email, 'Password': password}
            credentials=credentials.append(temp, ignore_index=True)
            campus=email.split("@")[1]
            campus=campus.split(".")[0]
            campus=str(campus[0]).upper() + campus[1:]
            try:
                user = User.objects.create_user(email,email,password
                    , first_name=fname, last_name=lname)
                user.is_active = True
                profile = UserProfile(
                    user=user,
                    campus=campusCode[campus],
                    user_type=UserType.SUPERVISOR.value,
                    contact=contact
                     )
                profile.save()
            except:
                print("(Fail Username)")
            # break
        credentials.to_csv('transfers/tools/creds/fac_details.csv', index=False)
#HOD Populate
    def hod_populate():
        credentials=pd.DataFrame()
        hod = pd.read_csv('transfers/tools/data/hod.csv')
        for index, row in hod.iterrows():
            email = row['email']
            password = User.objects.make_random_password()
            temp={'Username': email, 'Password': password}
            credentials=credentials.append(temp, ignore_index=True)
            campus=email.split("@")[1]
            campus=campus.split(".")[0]
            campus=str(campus[0]).upper() + campus[1:]
            print(email)
            try:
                user = User.objects.create_user(email,email,password)
                user.is_active = True
                profile = UserProfile(
                    user=user,
                    campus=campusCode[campus],
                    user_type=UserType.HOD.value,
                     )
                profile.save()
            except:
                print("(Fail Username)")
            # break
        credentials.to_csv('transfers/tools/creds/hod_details.csv', index=False)

    stu_populate()
    fac_populate()
    hod_populate()
    return HttpResponse("Done")