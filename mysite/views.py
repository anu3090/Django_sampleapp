from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from sites_coll.models import collectionofsites
from django.db import connection
from django.shortcuts import render_to_response
from django.db.models.aggregates import Avg,Sum,Count


import datetime

def home(request):
    now = datetime.datetime.now()
    t = get_template('home.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def sites(request):
    now = datetime.datetime.now()
    t= get_template('sites.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def abcsite(request):
    abcsites_list = collectionofsites.objects.filter(site_name__exact = 'ABC Site')
    t= get_template('abcsite.html')
    c= Context({'sites_list': abcsites_list})
    return HttpResponse(t.render(c))

def xyzsite(request):
    cursor = connection.cursor()
    cursor.execute("SELECT date,Avalue,Bvalue from sites_coll_collectionofsites where site_name = 'XYZ Site'")
    results = cursor.fetchall()
    return render_to_response('xyzsite.html',{'results': results})

def demosite(request):
    demosites_list = collectionofsites.objects.filter(site_name__exact = 'Demo Site')
    t= get_template('demosite.html')
    c= Context({'sites_list': demosites_list})
    return HttpResponse(t.render(c))

def summary(request):
    demosite_Avalue = collectionofsites.objects.filter(site_name__exact = 'Demo Site').aggregate(Sum('Avalue'))
    demosite_Bvalue = collectionofsites.objects.filter(site_name__exact = 'Demo Site').aggregate(Sum('Bvalue'))
    abcsite_Avalue = collectionofsites.objects.filter(site_name__exact = 'ABC Site').aggregate(Sum('Avalue'))
    abcsite_Bvalue = collectionofsites.objects.filter(site_name__exact = 'ABC Site').aggregate(Sum('Bvalue'))
    xyzsite_Avalue = collectionofsites.objects.filter(site_name__exact = 'XYZ Site').aggregate(Sum('Avalue'))
    xyzsite_Bvalue = collectionofsites.objects.filter(site_name__exact = 'XYZ Site').aggregate(Sum('Bvalue'))
    t= get_template('summary.html')
    c= Context({'abcsite_Avalue': abcsite_Avalue,'abcsite_Bvalue': abcsite_Bvalue,'xyzsite_Avalue': xyzsite_Avalue,'xyzsite_Bvalue': xyzsite_Bvalue,'demosite_Avalue': demosite_Avalue,'demosite_Bvalue': demosite_Bvalue})
    return HttpResponse(t.render(c))

def summary_average(request):
    demosite_Avalue = collectionofsites.objects.filter(site_name__exact = 'Demo Site').aggregate(Avg('Avalue'))
    demosite_Bvalue = collectionofsites.objects.filter(site_name__exact = 'Demo Site').aggregate(Avg('Bvalue'))
    abcsite_Avalue = collectionofsites.objects.filter(site_name__exact = 'ABC Site').aggregate(Avg('Avalue'))
    abcsite_Bvalue = collectionofsites.objects.filter(site_name__exact = 'ABC Site').aggregate(Avg('Bvalue'))
    xyzsite_Avalue = collectionofsites.objects.filter(site_name__exact = 'XYZ Site').aggregate(Avg('Avalue'))
    xyzsite_Bvalue = collectionofsites.objects.filter(site_name__exact = 'XYZ Site').aggregate(Avg('Bvalue'))
    t= get_template('summary_average.html')
    c= Context({'abcsite_Avalue': abcsite_Avalue,'abcsite_Bvalue': abcsite_Bvalue,'xyzsite_Avalue': xyzsite_Avalue,'xyzsite_Bvalue': xyzsite_Bvalue,'demosite_Avalue': demosite_Avalue,'demosite_Bvalue': demosite_Bvalue})
    return HttpResponse(t.render(c))


