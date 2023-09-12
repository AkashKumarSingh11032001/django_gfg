from django.http import HttpResponse

# Create your views here.
def hiWorld(request):
    return HttpResponse("Hello I am back")