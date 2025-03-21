from django.shortcuts import render, redirect
from .models import Profile, Workshop, FollowUp, Happiness, EncryptedProfile
from .forms import ProfileForm, WorkshopForm, EditWorkshopParticipantsForm, FollowupForm, ReferralForm, LikesForm, ConcernLevelForm,EditHappinessForm,PersonalPlanForm, DocumentForm
#from .filters import ProfileFilter
from rac.forms import EditConcernForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import pandas as pd
from django.db.models import Q
from django.forms import model_to_dict
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from itertools import chain
from operator import attrgetter
from .utils import getChart
from .models import Profile, Workshop, FollowUp
import datetime
import urllib


def loginPage(request):
    """ Function to render the login page"""

    #If user already logged in, redirect to the home page
    if request.user.is_authenticated:
        return redirect('home')

    #If details entered, attempt login
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')


        try:

            #If details correct, login the user
            user = User.objects.get(username = username)
            user = authenticate(request, username=username, password=password)

            #Login and redirect home
            if user is not None:
                login(request, user)
                return redirect('home')
            
        except:
            
            #display error if combination does not exist
            messages.error(request, "Username or password does not exist")


    #render the login page
    context = {"page":"login"}
    return render(request,'base/signup_login.html',context)

def logoutUser(request,message=None):
    """ Function to deal with a logout request"""

    #logout and redirect to the login
    logout(request)
    return redirect('login')


#TODO I think that instead of using a ProfileFilter, since we are pretty much pulling all of the objects out of memory anyway
    # we can probably do filtering on the objects after they've been retrieved and decrypted.
    # it's a slightly hackier way to do it but i think it can work with the encryption system.

#ensures a user is logged in
@login_required(login_url='/login')
def home(request):
    """ Function to display the main home page"""

    #creates the search bar and filters the profiles
    q = request.GET.get('q')
    c = request.GET.get('concern')
    # Instead of using a ProfileFilter, profiles are filtered after all profiles have been raised from the database
    # This is a performance loss, but will mean that profiles are able to be filtered by name even when the name is encrypted

    all_profiles = list(Profile.objects.all())
    if q != None and q!= "":
        profiles = [profile for profile in all_profiles if q.lower() in profile.person_name.lower()]
    else:
        profiles = all_profiles

    if c != "" and c != None:
        profiles = [profile for profile in profiles if c == profile.concern_level]
    else:
        profiles = profiles

    #render the homepage
    context = {"profiles": profiles}
    return render(request,'base/home.html',context)


@login_required(login_url='/login')
def profile(request,pk):
    """ Function to show a single profile """

    now = datetime.datetime.now()


    #get the id of the profile seleced
    profile = Profile.objects.get(id=pk)
    followups = FollowUp.objects.all().order_by('date').filter(profile=profile)
    pastWorkshops = Workshop.objects.all().order_by('date').filter(date__lt = now,participants=profile)
    futureWorkshops = Workshop.objects.all().order_by('date').filter(date__gt = now,participants=profile)

    timeline = sorted(
        chain(followups, futureWorkshops),
        key=attrgetter('date')
)

    #render the profile page
    context = {'profile':profile,'followups':followups,'pastworkshops':pastWorkshops,'futureworkshops':futureWorkshops,'timeline':timeline}
    return render(request,'base/profile.html',context)


@login_required(login_url='/login')
def createProfile(request):
    """ Function to create a new profile """

    #load the profile form
    form = ProfileForm()

    #if a valid post request, save the new profile
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    #render the form webpage
    context = {'form':form}
    return render(request, 'base/RAC_form.html',context)


@login_required(login_url='/login')
def editProfile(request,pk):
    """ Function to edit an existing profile """

    #get the id of the profile being edited
    profile = Profile.objects.get(id=pk)
    form = EditConcernForm(instance=profile)

    #if the post is valid, save the edit
    if request.method == "POST":
        form = EditConcernForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            return redirect("home")   
        

    #render the form webpage
    context = {'profile':profile,'form':form}
    return render(request,'rac/rac.html',context)


@login_required(login_url='/login')
def deleteProfile(request,pk):
    """ Function to delete a profile """

    #get the profile id
    profile = Profile.objects.get(id=pk)

    #If delete clicked, return to the homepage
    if request.method == "POST":
        profile.delete()
        return redirect("home")
    
    return render(request, 'base/delete_profile.html',{'obj':profile})

@login_required(login_url='/login')
def workshops(request):
    """ Function to the workshops """

    now = datetime.datetime.now()

    pastWorkshops = Workshop.objects.all().order_by('date').filter(date__lt = now)
    futureWorkshops = Workshop.objects.all().order_by('date').filter(date__gt = now)

    #render the workshops page
    context = {"pastworkshops":pastWorkshops,'futureWorkshops':futureWorkshops}
    return render(request,'base/workshops.html',context)

@login_required(login_url='/login')
def createWorkshop(request):
    """ Function to create a workshop """

    #load the workshop form
    form = WorkshopForm()

    #if the post request is valid, save the workshop
    if request.method == "POST":
        form = WorkshopForm(request.POST)
        if form.is_valid():

            #redirect to the workshops page
            form.save()
            return redirect("workshops")

    #render the workshop form webpage
    context = {'form':form}
    return render(request, 'base/workshopForm.html',context)

@login_required(login_url='/login')
def workshop(request,pk):
    """ Function to create a workshop """

    workshop = Workshop.objects.get(id=pk)

    participants = workshop.participants.all()

    levels = Happiness.objects.filter(profile__id__in = participants,workshop=workshop)

    levelProfiles = levels.values_list('profile', flat=True)

    
    #levels = Happiness.objects.filter(profile__id__in = participants,workshop=workshop)
    #levelIDs =levelProfiles.values_list('id', flat=True)

    #print(levelIDs)

   

    #render the workshop form webpage
    context = {'workshop':workshop,'participants':participants,'levelProfiles':levelProfiles,'levels':levels}
    return render(request, 'base/workshop.html',context)

@login_required(login_url='/login')
def EditWorkshopParticipants(request,pk):
    """ Function to edit a profile """

    #get the id of the workshop
    workshop = Workshop.objects.get(id=pk)
    form = WorkshopForm(instance=workshop)


    #if the post is valid, save and redirect to the workshops
    if request.method == "POST":
        form = WorkshopForm(request.POST,instance=workshop)
        if form.is_valid():
            form.save()
            return redirect("workshops")

    #render the edit page
    context = {'form':form}
    return render(request,'base/workshopForm.html',context)

@login_required(login_url='/login')
def addProfiletoWorkshop(request,pk):
    """ Function to edit a profile """

    now = datetime.datetime.now()
    profile = Profile.objects.get(id=pk)

    #get all the workshops
    workshops = Workshop.objects.all().order_by('date').filter(date__gt = now).exclude(participants__in = [profile])

    if (len(workshops) <= 0):
        context = {"profile":profile,"workshops":workshops,'nonZero':False}
    else:
        context = {"profile":profile,"workshops":workshops,'nonZero':True}

    return render(request,'base/profileWorkshop.html',context)


@login_required(login_url='/login')
def confirmAdd(request,profileId,workshopId):
    """ Function to delete a workshop """

    #get the profile id
    profile = Profile.objects.get(id=profileId)
    workshop = Workshop.objects.get(id=workshopId)

    #If delete clicked, return to the homepage
    if request.method == "POST":
        workshop.participants.add(profile)
        
        return redirect("profile", pk=profile.id)
    
    #render the workshops page
    context = {"profile":profile,"workshop":workshop}
    
    return render(request, 'base/addProfile.html',context)


@login_required(login_url='/login')
def deleteWorkshop(request,pk):
    """ Function to delete a workshop """

    #get the profile id
    workshop = Workshop.objects.get(id=pk)

    #If delete clicked, return to the homepage
    if request.method == "POST":
        workshop.delete()
        return redirect("workshops")
    
    return render(request, 'base/delete_workshop.html',{'obj':workshop})

@login_required(login_url='/login')
def addFollowUp(request,pk):
    """ Function to add a followup metting"""

    #get the profile to have a meeting added to
    profile = Profile.objects.get(id=pk)

     #load the followup form
    form = FollowupForm()

    #if the post request is valid, save the followup
    if request.method == "POST":
        form = FollowupForm(request.POST)
        form.profile = profile.id
        if form.is_valid():
            
            obj = form.save(commit=False)
            obj.profile = profile


            #redirect to the user's profile
            obj.save()
            return redirect("profile",pk=profile.id)
        
        else:
            print(form.errors)


    #render the followup form
    context = {'form':form}
    return render(request,'base/add_followup.html',context)


@login_required(login_url='/login')
def addReferall(request,pk):
    """ Function to add a referral"""

   #get the id of the profile being edited
    profile = Profile.objects.get(id=pk)
    form = ReferralForm(instance=profile)

    #if the post is valid, save the edit
    if request.method == "POST":
        form = ReferralForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile",pk=profile.id)

    #render the form webpage
    context = {'profile':profile,'form':form}
    return render(request, 'base/add_referral.html',context)

@login_required(login_url='/login')
def document_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():

            instance = form.save()
            file_path = instance.upload.path
            print(file_path)
            df = pd.read_excel(file_path)

            # Selects the relevant columns
            df = df[['RAC date:',
                     'Concern raised by:',
                     'Issue',
                     'Initials:',
                     'Walk In?',
                     'Gender',
                     'Issue',
                     'Consent to share?',
                     'Referred to:',
                     'Refeered to 2:',
                     'Type of support needed',
                     'Support service accessed',
                     'Initial decision ',
                     ]]

            for index, row in df.iterrows():

                # Clean RACdate
                if not pd.isna(row["RAC date:"]):
                    rac_date = row["RAC date:"]
                else:
                    rac_date = datetime.date.today()

                # Get person name
                person_name = row["Initials:"]

                # Clean walk-in data
                walk_in_str = str(row["Walk In?"]).lower()
                if "w" in walk_in_str or "y" in walk_in_str:
                    walk_in = True
                else:
                    walk_in = False

                # Clean gender data
                gender = str(row["Gender"]).lower()

                # Get concern description
                if not row["Issue"].isnull:
                    concern_description = str(row["Issue"])
                else:
                    concern_description = None

                # Clean consent to share value
                consent_to_share_str = str(row["Consent to share?"]).lower()
                if consent_to_share_str == "yes" or consent_to_share_str == "y":
                    consent_to_share = True
                else:
                    consent_to_share = False

                # Get referred to
                # TODO handle other agencies
                if not row["Referred to:"]:
                    referred_to = str(row["Referred to:"])
                else:
                    referred_to = None

                # Get support needed
                if not pd.isna(row["Type of support needed"]) and not row["Type of support needed"] == "N/A":
                    support_needed = str(row["Type of support needed"])
                else:
                    support_needed = None

                # Get support accessed
                if not pd.isna(row["Support service accessed"]):
                    support_accessed = str(row["Support service accessed"])
                else:
                    support_accessed = None

                # Get initial decision
                if not row["Initial decision "]:
                    initial_decision = str(row["Initial decision "])
                else:
                    initial_decision = None

                newProfile = Profile(RACdate=rac_date,
                                     person_name=person_name,
                                     walk_in=walk_in,
                                     gender=gender,
                                     concern_description=concern_description,
                                     consent_to_share=consent_to_share,
                                     referredTo=referred_to,
                                     support_needed=support_needed,
                                     support_accessed=support_accessed,
                                     initialDecision=initial_decision
                                     )

                newProfile.save()

            return redirect('/')
    else:
        form = DocumentForm()
    return render(request, 'base/upload.html', {'form': form})

@login_required(login_url="/login")
def dataTransfer(request):

    # Loads data file
    #file_name = "C:\Users\joshp\OneDrive - University of Exeter\Year 4\mental-health\mh\data.xlsx"
    df = pd.read_excel("../media/xlsx")

    # Selects the relevant columns
    df = df[['RAC date:',
             'Concern raised by:',
             'Issue',
             'Initials:',
             'Walk In?',
             'Gender',
             'Issue',
             'Consent to share?',
             'Referred to:',
             'Refeered to 2:',
             'Type of support needed',
             'Support service accessed',
             'Initial decision ',
             ]]

    for index, row in df.iterrows():


        # Clean RACdate
        if not pd.isna(row["RAC date:"]):
            rac_date = row["RAC date:"]
        else:
            rac_date = datetime.date.today()

        # Get person name
        person_name = row["Initials:"]

        # Clean walk-in data
        walk_in_str = str(row["Walk In?"]).lower()
        if "w" in walk_in_str or "y" in walk_in_str:
            walk_in = True
        else:
            walk_in = False

        # Clean gender data
        gender = str(row["Gender"]).lower()

        # Get concern description
        if not row["Issue"].isnull:
            concern_description = str(row["Issue"])
        else:
            concern_description = None

        # Clean consent to share value
        consent_to_share_str = str(row["Consent to share?"]).lower()
        if consent_to_share_str == "yes" or consent_to_share_str == "y":
            consent_to_share = True
        else:
            consent_to_share = False

        # Get referred to
        # TODO handle other agencies
        if not row["Referred to:"]:
            referred_to = str(row["Referred to:"])
        else:
            referred_to = None

        # Get support needed
        if not pd.isna(row["Type of support needed"]) and not row["Type of support needed"] == "N/A":
            support_needed = str(row["Type of support needed"])
        else:
            support_needed = None

        # Get support accessed
        if not pd.isna(row["Support service accessed"]):
            support_accessed = str(row["Support service accessed"])
        else:
            support_accessed = None

        # Get initial decision
        if not row["Initial decision "]:
            initial_decision = str(row["Initial decision "])
        else:
            initial_decision = None


        newProfile = Profile(RACdate=rac_date,
                             person_name=person_name,
                             walk_in=walk_in,
                             gender=gender,
                             concern_description=concern_description,
                             consent_to_share=consent_to_share,
                             referredTo=referred_to,
                             support_needed=support_needed,
                             support_accessed=support_accessed,
                             initialDecision=initial_decision
                             )

        newProfile.save()


    return render(request, 'base/data_transfer.html')

@login_required(login_url="/login")
def data_output(request):

    # Outputs all data into a csv file

    # For each profile
    profiles = Profile.objects.all()



    model_dicts = []

    for profile in profiles:
        model_dict = model_to_dict(profile)
        model_dicts.append(model_dict)

    print(model_dicts)

    df = pd.DataFrame.from_dict(model_dicts)
    print(df.info)

    # Prepare the response object with the right CSV headers
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="profiles.csv"'

    # Write the DataFrame to the response object
    df.to_csv(path_or_buf=response, index=False)

    return response

@login_required(login_url="/login")
def pdf_output(request, pk):

    field_names_description={
        "cr_name":"Concern raiser name",
        "cr_contact":"Concern raiser contact",
        "cr_org":"Concern raiser organisation",
        "cr_team":"Concern raiser team",
        "cr_risk":"Risk identified",
        "person_name":"Name",
        "person_contact":"Your contact details:",
        "gp_surgery":"GP Surgery",
        "nhs_number":"NHS Number",
        "address":"Address",
        "walk_in":"Walk in?",
        "email":"Email",
        "dob": "Date of Birth",
        "gender":"Gender",
        "concern_description":"Concern Description",
        "consent_to_share":"Consent to share information",
        "signature":"Signature",
        "signature_date":"Signature Date",
        "support_needed":"Support Needed",
        "support_accessed":"Support Accessed",
        "initialDecision":"Initial Decision",
        "personal_plan":"Personal Plan"
    }


    # Get data
    # Get data from Profile model
    print(pk)
    profile = Profile.objects.get(id=pk)

    width, height = letter
    print(width)
    print(height)

    filename = profile.person_name.replace(" ", "") + ".pdf"
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    my_canvas = canvas.Canvas(response, pagesize=letter)
    my_canvas.drawImage("colab.png", width/2-50, 650, width=100, height=100)
    add_centered_text(my_canvas, "Your data stored by Colab Exeter:", 600, 25)
    add_centered_text(my_canvas, profile.person_name, 570, 25)

    height = 500
    for field in Profile._meta.fields:
        field_name = field.name
        field_value = getattr(profile, field_name)

        print(field_name)
        print(field_value)

        try:
            field_name = field_names_description[field_name]
        except:
            print("Field name not found")

        my_canvas.setFont("Helvetica", 10)
        if field_value is not None and field_name not in ["id","updated","created","RACdate","is_homeless","is_alcoholic","using_drugs","taking_medication"]:

            output_text = field_name + ": " + str(field_value)

            my_canvas.drawString(50, height, output_text)
            #add_centered_text(my_canvas, output_text, height, 15)

            height -= 22

    my_canvas.save()

    return response

def add_centered_text(canvas, text, y_position,font_size=12):

    # Build the PDF
    width, height = letter
    text_width = canvas.stringWidth(text, 'Helvetica', font_size)
    x_position = (width - text_width) / 2

    canvas.setFont("Helvetica", font_size)
    canvas.drawString(x_position, y_position, text)


@login_required(login_url='/login')
def addlikesdislikes(request,pk):
    """ Function to add a referral"""

   #get the id of the profile being edited
    profile = Profile.objects.get(id=pk)
    form = LikesForm(instance=profile)

    #if the post is valid, save the edit
    if request.method == "POST":
        form = LikesForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile",pk=profile.id)

    #render the form webpage
    context = {'profile':profile,'form':form}
    return render(request, 'base/likesdislikes.html',context)

@login_required(login_url='/login')
def addConcernLevel(request,pk):
    """ Function to add a referral"""

   #get the id of the profile being edited
    profile = Profile.objects.get(id=pk)
    form = ConcernLevelForm(instance=profile)

    #if the post is valid, save the edit
    if request.method == "POST":
        form = ConcernLevelForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile",pk=profile.id)

    #render the form webpage
    context = {'profile':profile,'form':form}
    return render(request, 'base/concernLevel.html',context)


@login_required(login_url='/login')
def editHappiness(request,profileId,workshopId):
    """ Function to add a followup metting"""

    #get the profile to have a meeting added to
    profile = Profile.objects.get(id=profileId)
    workshop = Workshop.objects.get(id=workshopId)

    happiness = Happiness.objects.filter(profile=profile,workshop=workshop)

    if happiness:
        ins = Happiness.objects.get(profile=profile, workshop=workshop)
        print(ins.before)
        form = EditHappinessForm(request.POST or None, instance=ins)
    else:
        form = EditHappinessForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            obj = form.save(commit=False)
            obj.profile = profile
            obj.workshop = workshop
            obj.save()
            return redirect("workshop", pk=workshop.id)
        else:
            print(form.errors)

    #render the followup form
    context = {'form':form}
    return render(request,'base/editHappiness.html',context)


@login_required(login_url='/login')
def personalPlan(request,pk):
    """ Function to add a referral"""

   #get the id of the profile being edited
    profile = Profile.objects.get(id=pk)
    form = PersonalPlanForm(instance=profile)

    #if the post is valid, save the edit
    if request.method == "POST":
        form = PersonalPlanForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile",pk=profile.id)

    #render the form webpage
    context = {'profile':profile,'form':form}
    return render(request, 'base/personalPlan.html',context)

@login_required(login_url='/login')
def add_encrypted(request):

    profile = EncryptedProfile(
        RACdate=datetime.date.today(),
        walk_in=True,
        dob=datetime.date(1990, 1, 1),
        referredTo='GP',
        likes=['Large Groups', "1o1's"],
        dislikes=['Large Groups'],
        concern_level='Medium',
        cr_name="Encrypted Test CR Name",
        cr_contact="Encrypted Test CR Contact",
        cr_org="Encrypted Test Organization",
        cr_team="Encrypted Test Team",
        cr_risk="Encrypted Low",
        person_name="Encrypted John Doe",
        person_contact="Encrypted 123456789",
        gp_surgery="Encrypted Test Surgery",
        nhs_number="Encrypted 987654321",
        address="Encrypted 123 Test St, Test City",
        email="encryptedjohn.doe@example.com",
        gender="Encrypted M",
        concern_description="Encrypted No immediate concerns.",
        consent_to_share=True,
        signature="Encrypted John Doe",
        signature_date="Encrypted 2023-01-01",
        referredToMore="Encrypted Specialist Service",
        support_needed="Encrypted Counseling",
        support_accessed="Encrypted None",
        initialDecision="Encrypted To be reviewed",
        personal_plan="Encrypted Follow-up in 3 months"
    )

    # Save the instance to the database
    profile.save()

    return redirect("/")


@login_required(login_url='/login')
def dataAnalysis(request):
    """Function to show the data analysis webpage"""

    # Get all profiles from the database
    profiles = Profile.objects.all()

    # Get parameters with which the user wants to create a chart
    paramY = request.GET.get('paramY')
    paramX = request.GET.get('paramX')
    chart_type = request.GET.get('chart_type')
    
    context={}
    # If there are any profiles
    if profiles:
        total_profiles = profiles.count()

        context = {'profiles': profiles, 'total_profiles': total_profiles}
        
        if paramY and paramX:

            # Transform profile from django queryset to pandas dataframe
            df = pd.DataFrame([model_to_dict(profile) for profile in profiles])

            # Generate chart to display
            chart = getChart(df, paramY, paramX, chart_type)

            context = {'profiles': profiles, 'total_profiles': total_profiles, 'chart': chart}

    return render(request, 'base/data_analysis.html', context)