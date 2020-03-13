from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from transfers.models import UserProfile, PS2TSTransfer as psts, TS2PSTransfer as tsps
import pandas as pd
import re

objectCode={'01':psts.objects.filter(sub_type=0),
    '10':tsps.objects.filter(sub_type=0),
    '0100':tsps.objects.filter(sub_type=1) ,
    '1110':tsps.objects.filter(sub_type= 2), 
    'xx11':psts.objects.filter(sub_type=1)}

count=1
final=pd.DataFrame(columns=['Sr.No', 'Name', 'Stream'])
def getFile(request, choice):
    global count
    global final
    def send(x):
        for data in x:
            global count
            global final
            if data.is_hod_approved==1:
                print(data.is_hod_approved)
                temp={'Sr.No':count, 'Name':data.applicant.user.first_name+' '+ data.applicant.user.last_name, 'Stream':data.get_sub_type_display()} 
                final=final.append(temp,ignore_index=True)
                count=count+1  
    if choice==1:
        filename="PS To TS"
        send(objectCode['01'])
    elif choice==2:
        filename="TS To PS"
        send(objectCode['10'])
    elif choice==3:
        filename="PS-TS or TS-PS to TS-TS"
        send(objectCode['xx11'])
    elif choice==4:
        filename="PS-TS to PS-PS"
        send(objectCode['0100'])
    elif choice==5:
        filename="TS-TS to TS-PS"
        send(objectCode['1110'])


    print(filename)    
    print(final)
    final.to_csv(f'transfers/tools/export_data/{filename}.csv', index=False)


    count=1
    final=pd.DataFrame(columns=['Sr.No', 'Name', 'Stream'])
    return HttpResponse("Done")