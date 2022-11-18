from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demo(request):
	return HttpResponse("Good Afternoon!!Welcome to the django course ....")

def sample(r):
	return HttpResponse("<h2>Good Afternoon!!Welcome to the django course ....</h2>")

def hrf(self,aq):
	return HttpResponse("<h3>Welcome to Django... {}!!</h3>".format(aq))

def student(request,y,r,t):
	return HttpResponse("Student Roll Number:{} </br> Branch:{} <br/> Year:{}".format(y,r,t))

def wg(g):
	return HttpResponse("<html><head><title></title><body><h2>Django Workshop</h2></br><h3>Sample Response By Using Html Structure</h3></body></head></html>")

def af(q,qw):
	return HttpResponse("<html><head><title></title><body style='background-color:	#339999'><h2 style='text-align:center'>Hii..Welcome <span style='color:	#3399FF'> {} </span></h2><h3 style='text-align:center'>This is internal css.</h3></body></head></html>".format(qw))

def ae(t,nm):
	return HttpResponse("<html><head><title>Django</title><style>span{color:yellow}</style></head><body><h3>Hii..Welcome<span>"+nm+"</h3></body></html>")

def cy(request,k):
	return HttpResponse("<html><head><title>Demo For JS</title><script>alert('Welcome to this site {}')</script></head><body><h3>Hi User {}</h3></body></html>".format(k,k))

def hk(request):
	return render(request,'sample.html')

def vy(request,qy):
	return render(request,'demo.html',{'p':qy})


def std(request):
	return render(request,'strg.html')

def emp(request):
	return render(request,'employee.html')

def me(request):
	if request.method == "POST":
		name=request.POST['en']
		eid=request.POST['ei']
		eg=request.POST['a']
		return render(request,'edetails.html',{'ename':name,'empid':eid,'eage':eg})
	return render(request,'employee.html')

	