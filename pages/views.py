from django.shortcuts import render

def home_view(request):
    context = {'name':'Sajjad','lastname':'Ahmadi'}
    return render(request,'pages/index.html',context)

def about_view(request):
    context = {'age':'29','Birthday':'1997 May 21','email':'sajjadahmadi4sa@gmail.com','city':'saveh & tehran'}
    return render(request,'pages/about.html',context)

def resume_view(request):
    context = {'education':'Associate Degree in Accounting' ,'Graduation Year':'2019','age':'29','Birthday':'1997 May 21','email':'sajjadahmadi4sa@gmail.com','city':'saveh & tehran'}
    return render(request,'pages/resume.html',context)

def portfolio_view(request):
    return render(request,'pages/portfolio.html')

def contact_view(request):
    context = {'city':'Saveh & Tehran', 'phone':'09300761172','email':'sajjadahmadi4sa@gmail.com'}
    return render(request,'pages/contact.html',context)
# Create your views here.
