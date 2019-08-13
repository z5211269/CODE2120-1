from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import *

# Create your views here.

def example_get(request, var_a, var_b):
	try:
		returnob = {
		"data": "%s: %s" %(var_a, var_b),
		}
		return JsonResponse(returnob)
	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		other = sys.exc_info()[0].__name__
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		errorType = str(exc_type)
		return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})

@csrf_exempt
def example_post(request):
    jsob={"startnumber":0, "length":10}
    log=[]
    if request.method == "POST":
        try:
	    data = request.POST["data"]
	    received = json.loads(data)
	    jsob.update(received)

	    startnumber = int(jsob["startnumber"])
	    length = int(jsob["length"])

	    loop = range(length)
	    numarray = []
	    fibno = startnumber
	    addno = 1
	    for l in loop:
	    numarray.append(fibno)
	    fibno = fibno + addno
	    addno = fibno - addno
	    return JsonResponse({"fib number":numarray})
		
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return HttpResponse("<h1>ONLY POST REQUESTS</h1>")

@csrf_exempt
def Teresa(request):
    jsob={}
log=[]
if request.method == "POST":
   try:
	data = request.POST["data"]
	received = json.loads(data)
	jsob.update(received)
        first = 0
        second = 1
        result = [0]
        print('Fibonacci series is')
        for i in range(0,num):
        third = first + second
        #print(second)
        result.append(second)
        first = second
        second = third
        print(result)
        return
fibo(7)

		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return HttpResponse("<h1>ONLY POST REQUESTS</h1>")
