from .models import HotProfile

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