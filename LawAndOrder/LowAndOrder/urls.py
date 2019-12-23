"""LowAndOrder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView,DeleteView
from app.models import Police,Detective,Citizen,Station,Complent,Criminal,Status
from app import views
from django.conf.urls.static import static
from LowAndOrder import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',TemplateView.as_view(template_name='index.html')),
    path('adminlogin/', TemplateView.as_view(template_name="adminlogin.html")),
    path('adminlog/',views.adminLog),
    path('policelogin/',TemplateView.as_view(template_name="policelogin.html")),
    path('policelog/',views.policeLog),
    path('detectivelogin/',TemplateView.as_view(template_name="detectivelogin.html")),
    path('detectivelog/',views.detectiveLog),
    path('citizenlogin/',ListView.as_view(template_name="citizenlogin.html",model=Citizen)),
    path('citizenlog/',views.citizenLog),
    path('addpolice/',TemplateView.as_view(template_name="addpolice.html")),
    path('savepolice/',views.savePolice),
    path('viewpolice/',ListView.as_view(template_name="viewPolice.html",model=Police)),
    path('updatepolice/',ListView.as_view(template_name="updatepolice.html",model=Police)),
    path('updatePolice/',views.updatePolice),
    path('deletepolice/',ListView.as_view(template_name="deletepolice.html",model=Police)),
    path('deletePolice/',views.deletePolice),
    path('adddetective/',TemplateView.as_view(template_name="adddetective.html")),
    path('savedetective/',views.saveDetective),
    path('viewdetective/',ListView.as_view(template_name="viewdetective.html",model=Detective)),
    path('updatedetective/',ListView.as_view(template_name="updatedetective.html",model=Detective)),
    path('detectiveUpdate/',views.detectiveUpdate),
    path('deletedetective/',ListView.as_view(template_name="deletedetective.html",model=Detective)),
    path('deleteDetective/',views.deleteDetective),
    path('addstations/',TemplateView.as_view(template_name="addstations.html")),
    path('savestation/',views.saveStations),
    path('viwestation/',ListView.as_view(template_name="viwestation.html",model=Station)),
    path('updatestation/',ListView.as_view(template_name="updatestation.html",model=Station)),
    path('updateStation/',views.updateStation),
    path('deletestation/',ListView.as_view(template_name="deletestation.html",model=Station)),
    path('deleteStation/',views.deleteStation),
    path('citizenRegister/',views.addCitizen),
    path('savecitizen/',views.saveCitizen),
    path('viewcitizen/',ListView.as_view(template_name="viewCitizen.html",model=Citizen)),
    path('deletecitizen/',ListView.as_view(template_name="deletecitizen.html",model=Citizen)),
    path('deleteCitizen/',views.deleteCitizen),
    path('addcomplients/',ListView.as_view(template_name='addcomplients.html',model=Station)),
    path('savecomplent/',views.saveComplent),
    path('viewcomplients/',ListView.as_view(template_name="viewcomplent.html",model=Complent)),
    path('updatecomplients/',ListView.as_view(template_name="updatecomplients.html",model=Complent)),
    path('updatecomp/',views.updateComp),
    path('viewcitizencomplet/',ListView.as_view(template_name="viewcitizencomplet.html",model=Complent)),
    path('detectiveviewcomplients/',ListView.as_view(template_name="detectiveviewcomplients.html",model=Complent)),
    path('addcriminal/',TemplateView.as_view(template_name="addcriminal.html")),
    path('savecriminal/',views.savecriminal),
    path('viewcriminal/',ListView.as_view(template_name="viewcriminal.html",model=Criminal)),
    path('deletecriminal/',ListView.as_view(template_name="deletecriminal.html",model=Criminal)),
    path('deletecri/',views.deletecriminal),
    path('addcrim/', TemplateView.as_view(template_name="addcrim.html")),
    path('savecri/',views.savecri),
    path('viewcrim/',ListView.as_view(template_name="viewcri.html",model=Criminal)),
    path('delcrim/',ListView.as_view(template_name="deletecrim.html",model=Criminal)),
    path('deletecrim/',views.deletecrim),
    path('viewDetec/',ListView.as_view(template_name="viewDetec.html",model=Detective)),
    path('addcom/', TemplateView.as_view(template_name="addcom.html")),
    path('savecom/',views.savecom),
    path('viewcomp/',ListView.as_view(template_name="viewcomp.html",model=Complent)),
    path('addstatus/',ListView.as_view(template_name="statusAdd.html",model=Complent)),
    path('statusadd/',views.statusadd),
    path('savestatus/',views.savestatus),
    path('statusDetec/',ListView.as_view(template_name="statusDetec.html",model=Status),),
    path('viewstatus/',ListView.as_view(template_name="viewstatus.html",model=Status)),
    path('updatestatus/',ListView.as_view(template_name="statusUpdate.html",model=Complent)),
    path('viewstat/',ListView.as_view(template_name="viewstat.html",model=Status)),
    path('viewstatcit/',ListView.as_view(template_name="viewstatcit.html",model=Status)),
    path('report/',views.report),
    path('findreport/',views.findReport),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

