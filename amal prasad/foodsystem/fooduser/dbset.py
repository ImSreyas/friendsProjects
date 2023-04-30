from .models import HotProfile,cmuser,items,tempcart,orders,userregs
from django.core.files.storage import FileSystemStorage
from django.utils.crypto import get_random_string
def upatehotelinf(request):
    hotProfile=HotProfile()
    hotProfile.adrss=request.POST.get('hadrs')
    hotProfile.hname=request.POST.get('hname')
    hotProfile.place=request.POST.get('hplace')
    hotProfile.email=request.POST.get('hemail')
    hotProfile.mobs=request.POST.get('hcnt')
    hotProfile.hid=request.session.get('hotids')
    suss= hotProfile.save()
    return suss

def usrreg(request):
    UserProfile=cmuser()
    UserProfile.unames=request.POST.get('Username')
    UserProfile.upass=request.POST.get('Password')
    UserProfile.umail=request.POST.get('Email')
    UserProfile.uphone=request.POST.get('Phone')
    suss= UserProfile.save()
    return 1
def hotelereg(request):
    hotProfile=HotProfile()
    hotProfile.email=request.POST.get('username')
    hotProfile.password=request.POST.get('password1')
    suss= hotProfile.save()
    return 1
def additemsdb(request):
    additm=items()
    additm.items=request.POST.get('iname')
    additm.price=request.POST.get('iprice')
    additm.qtys=request.POST.get('istock')
    additm.description=request.POST.get('idsicp')
    additm.catsgry=request.POST.get('icat')
    upload = request.FILES['iimg']
    fss = FileSystemStorage()
    file = fss.save(upload.name, upload)
    file_url = fss.url(file)
    additm.imgs=file_url
    additm.hotid= request.session.get('hotuser')
    suss= additm.save()
    return 1
def addtempcart(request):
    addtmp=tempcart()
    addtmp.cattempid=request.session.get('cartids')
    addtmp.cathots=request.POST.get('hotl')
    addtmp.catprice=request.POST.get('price')
    addtmp.catitm=request.POST.get('item_name')
    addtmp.catqty=request.POST.get('quantz')
    addtmp.catitids=request.POST.get('item_id')
    addtmp.catimng=request.POST.get('img')
    addtmp.catstatus=1
    suss= addtmp.save()
    return 1

def addorder(request):
    ordersids=get_random_string(length=15)
    addodr=orders()
    addodr.odrid=ordersids
    addodr.odrrcart=request.session.get('cartids')
    addodr.odruser=""
    addodr.odrdanam=request.POST.get('dname')
    addodr.oddrmob=request.POST.get('dmob')
    addodr.odrland=request.POST.get('dland')
    addodr.odrcity=request.POST.get('dcity')
    addodr.odrdlvey="Processing"
    addodr.odrpaymet=1
    addodr.odrstatus=1
    suss= addodr.save()
    return 1
def reguser(request):
    adduser=userregs()
    adduser.useremail=request.POST.get('email')
    adduser.userpass=request.POST.get('Password')
    adduser.username=request.POST.get('Username')
    adduser.userphone=request.POST.get('Phone')
    adduser.usersts=1
    suss= adduser.save()
    return 1