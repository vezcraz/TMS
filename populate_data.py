import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TMS.settings')

import django

django.setup()
from transfers.models import UserProfile, PS2TSTransfer, TS2PSTransfer, DeadlineModel

from django.contrib.auth.models import User

import random
from django.utils import timezone as datetime

# choices
campus_choices = [0, 1, 2]
PS2TS_choices = [0, 1]
thesis_locale_choices = [0, 1, 2]
boolean_choices = [True, False]


def fake_number_generator():
    fake_number = 0
    for x in range(10):
        fake_number = fake_number * 10 + random.randint(0, 10)
    return fake_number


def fake_cgpa():
    cgpa = float(random.randrange(0, 1000)) / 100
    return cgpa


def create_super_user():
    try:
        (super_user, created) = User.objects.get_or_create(username="admin", is_superuser=True)
        super_user.set_password('password')
        super_user.is_staff = True
        super_user.is_admin = True
        super_user.is_superuser = True
        super_user.save()

    except:
        print("Error occurred while creating super user")

    try:
        (deadline, created) = DeadlineModel.objects.get_or_create(deadline_PS2TS = datetime.now(), deadline_TS2PS = datetime.now())
        deadline.save()
        print("Deadline created")

    except:
        print("Error occured while creating deadlines")

def create_user(n):
    for i in range(n):
        (user, created) = User.objects.get_or_create(username="user" + str(random.randint(1, 1000)))
        user.set_password('password')
        user.save()


def create_user_profile(i, user_type_name):
    try:

        (mUser, created) = User.objects.get_or_create(
            username=user_type_name + str(i),
            first_name=user_type_name + str(i),
            email=user_type_name + str(i) +"@gmail.com")
        mUser.set_password('password')
        mUser.save()
        fake_phone_number = fake_number_generator()

        if user_type_name == "Student":
            user_type = 0
        elif user_type_name == "Supervisor":
            user_type = 1
        elif user_type_name == "HOD":
            user_type = 2
        elif user_type_name == "AD":
            user_type = 3
        elif user_type_name == "PSD":
            user_type = 4

        UserProfile.objects.filter(
            user=mUser).update(
            campus=random.choice(campus_choices),
            contact=fake_phone_number,
            user_type=user_type
        )

    except Exception as e:
        print(str(e))
        print("Error creating user profile")


def create_ps2tstransfer(n, student_name):
    for i in range(n):
        create_user_profile(i, student_name)
        user = User.objects.get(username=student_name + str(i))
        user_profile = UserProfile.objects.get(user=user)
        new_applicant = user_profile
        fake_name_supervisor = "Supervisor" + str(i)
        fake_name_hod = "HOD" + str(i)
        fake_thesis = "Fake text"
        fake_org = "Org name "+str(random.randint(1, 1000))
        fake_cg = fake_cgpa()
        print(new_applicant.campus)

        try:
            PS2TSTransfer.objects.create(
                applicant=new_applicant,
                supervisor_email=fake_name_supervisor + "@gmail.com",
                hod_email=fake_name_hod + "@gmail.com",
                sub_type=random.choice(PS2TS_choices),
                cgpa=fake_cg,
                thesis_locale=random.choice(thesis_locale_choices),
                thesis_subject=fake_thesis,
                name_of_org=fake_org,
                expected_deliverables=fake_thesis,
                is_supervisor_approved=random.choice(boolean_choices),
                is_hod_approved=random.choice(boolean_choices)
            )
        except Exception as e:
            print(str(e))


def create_ts2pstransfer(n, student_name):
    for i in range(n):
        create_user_profile(i+100, student_name)
        user = User.objects.get(username=student_name + str(i+100))
        user_profile = UserProfile.objects.get(user=user)
        new_applicant = user_profile
        fake_name_hod = "HOD" + str(i)
        fake_org_name = "Org name "+str(random.randint(1, 1000))
        fake_reason = "Reason "+str(random.randint(1, 1000))
        fake_cg = fake_cgpa()

        try:
            TS2PSTransfer.objects.create(
                applicant=new_applicant,
                hod_email=fake_name_hod + "@gmail.com",
                sub_type=random.choice(thesis_locale_choices),
                cgpa=fake_cg,
                reason_for_transfer=fake_reason,
                name_of_org=fake_org_name,
                is_hod_approved=random.choice(boolean_choices)
            )
        except Exception as e:
            print(str(e))


if __name__ == '__main__':

    print("Clearing existing data")
    User.objects.all().delete()
    UserProfile.objects.all().delete()
    PS2TSTransfer.objects.all().delete()
    TS2PSTransfer.objects.all().delete()

    print("Generating the fake data")

    create_super_user()
    print("SuperUser created")

    create_user(5)
    print("Created users without userprofiles")

    for i in range(20):
        create_user_profile(i, "HOD")
    print("Created HOD")

    for i in range(20):
        create_user_profile(i+100, "HOD")
    print("Created HOD pt2")

    for i in range(20):
        create_user_profile(i, "Supervisor")
    print("Created Supervisor")

    for i in range(20):
        create_user_profile(i+100, "Supervisor")
    print("Created Supervisor pt2")

    for i in range(3):
        create_user_profile(i, "AD")
    print("Created AOD")

    create_user_profile(1, "PSD")
    print("Created PSD")

    create_ps2tstransfer(20, "Student")
    print("PS2TS applications created")

    create_ts2pstransfer(20, "Student")
    print("TS2PS applications created")