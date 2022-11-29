from django.shortcuts import render,redirect
import uuid
from django.http import HttpResponse
from .models import Url
# Create your views here.

def index_view(request):
    return render(request,'shortner/index.html')


def create_view(request):
    if request.method == 'POST':
        if request.POST['link'].strip() == "":
            return HttpResponse(uid)


        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link,uuid=uid)
        new_url.save()
        return HttpResponse(uid)
    


def go_view(request,pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(url_details.link)
