from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import patterns, url
from django.http import QueryDict

@csrf_exempt
def test_view(request):
    # The error will be raised here
    data = QueryDict(request.body)
    print data
    return HttpResponse("Done...")

urlpatterns = patterns('',
    url(r'test_body', test_view)
)