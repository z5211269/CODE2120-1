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
def Fibonacci_series(Number):
nterms = int(10)
n1 = 0
n2 = 1
count = 2
if nterms <= 0:
   print(2)
elif nterms == 1:
   print("Fibonacci")
   print(n1)
else:
   print("Fibonacci")
   print(n1,",",n2,end=" , ")
   while count < nterms:
       nth = n1 + n2
       print(nth,end=" , ")
       n1 = n2
       n2 = nth
       count += 1
	   
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return HttpResponse("<h1>ONLY POST REQUESTS</h1>")
