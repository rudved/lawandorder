from django.shortcuts import render,redirect
from .models import Police,Detective,Citizen,Station,Complent,Criminal,Status
from django.db.models import Q


def adminLog(request):
    uname=request.POST.get("uname")
    upass=request.POST.get("upass")
    if (uname=="admin" and upass=="admin"):
        return render(request,"adminHome.html",{"msg":"Welcome Admin"})
    else:
        return render(request, "adminlogin.html", {"msg": "Invalid Admin"})

def policeLog(request):
    uname = request.POST.get("uname")
    upass = request.POST.get("upass")
    qs=Police.objects.filter(username=uname,password=upass)
    if qs:
        return render(request, "policeHome.html", {"msg": "Welcome Police"})
    else:
        return render(request, "policelogin.html", {"msg": "Invalid Police"})

def detectiveLog (request):
    uname = request.POST.get("uname")
    upass = request.POST.get("upass")
    qs = Detective.objects.filter(username=uname, password=upass)
    if qs:
        return render(request, "detectiveHome.html", {"msg": "Welcome Detective"})
    else:
        return render(request, "detectivelogin.html", {"msg": "Invalid Detective"})

def citizenLog(request):
    uname = request.POST.get("uname")
    upass = request.POST.get("upass")
    qs = Citizen.objects.filter(username=uname, password=upass)
    if qs:
        return render(request, "citizenHome.html", {"msg": "Welcome Citizen","data":qs})
    else:
        return render(request, "citizenlogin.html",{"msg": "Invalid Citizen","data":qs})

def savePolice(request):
    id=request.POST.get("police_id")
    name=request.POST.get("police_name")
    dob=request.POST.get("date_of_birth")
    add=request.POST.get("address")
    des=request.POST.get("designation")
    mob=request.POST.get("mobile_no")
    sid=request.POST.get("station_id")
    uname=request.POST.get("username")
    upass=request.POST.get("password")
    Police(police_id=id,police_name=name,date_of_birth=dob,address=add,designation=des,mobile_no=mob,station_id=sid,username=uname,password=upass).save()
    return redirect("/viewpolice/")

def updatePolice(request):
    id=request.POST.get("id")
    qs=Police.objects.filter(police_id=id)
    return render(request,"policeupdate.html",{"data":qs})

def deletePolice(request):
    id=request.POST.get("id")
    Police.objects.filter(police_id=id).delete()
    return redirect("/viewpolice/")

def saveDetective(request):
    id=request.POST.get("detective_id")
    name=request.POST.get("detective_name")
    dob=request.POST.get("date_of_birth")
    mob=request.POST.get("mobile_no")
    uname=request.POST.get("username")
    upass=request.POST.get("password")
    Detective(detective_id=id,detective_name=name,date_of_birth=dob,mobile_no=mob,username=uname,password=upass).save()
    return redirect("/viewdetective/")

def detectiveUpdate(request):
        id = request.POST.get("id")
        qs = Detective.objects.filter(detective_id=id)
        return render(request, "detectiveupdate.html", {"data": qs})

def deleteDetective(request):
    id=request.POST.get("id")
    Detective.objects.filter(detective_id=id).delete()
    return redirect("/viewdetective/")

def saveStations(request):
    id = request.POST.get("station_id")
    name = request.POST.get("station_name")
    add = request.POST.get("address")
    city = request.POST.get("city")
    dist = request.POST.get("district")
    cno = request.POST.get("contact_no")
    Station(station_id=id,station_name=name,address=add,city=city,district=dist,contact_no=cno).save()
    return redirect("/viwestation/")

def updateStation(request):
    id = request.POST.get("id")
    qs = Station.objects.filter(station_id=id)
    return render(request, "stationupdate.html", {"data": qs})

def deleteStation(request):
    id=request.POST.get("id")
    Station.objects.filter(station_id=id).delete()
    return redirect("/viwestation/")


def addCitizen(request):
        return render(request,"addcitizen.html")

def saveCitizen(request):
    id = request.POST.get("citizen_id")
    name = request.POST.get("citizen_name")
    dob = request.POST.get("date_of_birth")
    email = request.POST.get("email")
    gen = request.POST.get("gender")
    mob = request.POST.get("mobile_no")
    add = request.POST.get("address")
    uname = request.POST.get("username")
    upass = request.POST.get("password")
    Citizen(citizen_id=id,citizen_name=name,date_of_birth=dob,email_id=email,gender=gen,mobile_no=mob,
            address=add,username=uname,password=upass).save()
    return redirect("/citizenlogin/")


def deleteCitizen(request):
    id = request.POST.get("id")
    Citizen.objects.filter(citizen_id=id).delete()
    return redirect("/viewcitizen/")


def saveComplent(request):
    name=request.POST.get("name")
    date=request.POST.get("date")
    complent_type=request.POST.get("complent_type")
    proof=request.POST.get("proof")
    location=request.POST.get("location")
    s_id=request.POST.get("s_id")
    Complent(complient_name=name,date_of_complent=date,
             complent_type=complent_type,proof=proof,location=location,station_id=s_id).save()
    return redirect("/viewcomplients/")

def updateComp(request):
    id = request.POST.get("id")
    qs = Complent.objects.filter(complent_id=id)
    return render(request, "complentUpdate.html", {"data": qs})

def savecriminal(request):
    name=request.POST.get("name")
    img=request.POST.get("image")
    crime=request.POST.get("crime")
    Criminal(criminal_name=name,crime=crime,img=img).save()
    return redirect("/viewcriminal/")

def deletecriminal(request):
    id = request.POST.get("id")
    Criminal.objects.filter(criminal_id=id).delete()
    return redirect("/viewcriminal/")

def savecri(request):
    name=request.POST.get("name")
    img=request.POST.get("image")
    crime=request.POST.get("crime")
    Criminal(criminal_name=name,crime=crime,img=img).save()
    return redirect("/viewcrim/")

def deletecrim(request):
    id = request.POST.get("id")
    Criminal.objects.filter(criminal_id=id).delete()
    return redirect("/viewcrim/")

def savecom(request):
    name=request.POST.get("name")
    date=request.POST.get("date")
    complent_type=request.POST.get("complent_type")
    proof=request.POST.get("proof")
    location=request.POST.get("location")
    s_id=request.POST.get("s_id")
    Complent(complient_name=name,date_of_complent=date,
             complent_type=complent_type,proof=proof,location=location,station_id=s_id).save()
    return redirect("/viewcomp/")

def statusadd(request):
    id = request.POST.get("id")
    qs = Complent.objects.filter(complent_id=id)
    return render(request, "addstatus.html", {"data": qs})

def savestatus(request):
    id=request.POST.get("id")
    name=request.POST.get("name")
    date=request.POST.get("date")
    complent_type=request.POST.get("complent_type")
    location=request.POST.get("location")
    s_id=request.POST.get("s_id")
    status=request.POST.get("status")
    Status(complent_id=id,complient_name=name,date_of_complent=date,
             complent_type=complent_type,location=location,station_id=s_id,status=status).save()
    return redirect("/viewstatus/")


def report(request):
    return render(request,"Report.html")

def findReport(request):
    status=request.POST.get("status")
    qs= Status.objects.filter(status=status)
    print(status,qs)
    return render(request, "Report.html",{"data":qs})