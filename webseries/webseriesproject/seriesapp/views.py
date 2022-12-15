from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import series
from . forms import SeriesForm

# Create your views here.
def index(request):
    series_list=series.objects.all()
    context={
        'series_list':series_list
    }
    return render(request,"index.html",context)
def detail(request,series_id):
    series1=series.objects.get(id=series_id)
    return render(request,"detail.html",{'series1':series1})
    #return HttpResponse("Series Id %s" % series_id)

def add_series(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year = request.POST.get('year')
        Language = request.POST.get('Language')
        image=request.FILES['image']
        Series=series(name=name,desc=desc,year=year,Language=Language,image=image)
        Series.save()
        return redirect('/')
    return render(request, 'add.html')


def update_series(request, id):
    series1=series.objects.get(id=id)
    form=SeriesForm(request.POST or None, request.FILES, instance=series1)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form':form, 'series':series1})

def delete(request,id):
    if request.method=='POST':
        Series=series.objects.get(id=id)
        Series.delete()
        return redirect('/')
    return render(request, 'delete.html')

