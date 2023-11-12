from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect

def homepage(request):
    return render(request,'index.html')

from .forms import usersForm

def Joinnow(request):

    fn = usersForm()
    
    data = {'form': fn} 

    try:  
        if request.method == 'POST':
            n1 = int(request.POST.get('num1')) 
            n2 = int(request.POST.get('num2'))
            finalans = n1 + n2 
            data = {
                'form': fn,  
                'output': finalans
            }

    except Exception as e:
        print("An error occurred:", str(e))  
    

    return render(request,'Joinnow.html',data)



def calculator(request):

    output = ""

    try:
        if request.method == 'POST':
            n1 = int(request.POST.get('num1'))  
            n2 = int(request.POST.get('num2'))   
            opr = request.POST.get('opr')  

            if opr == "+": 
                output = n1+n2

            elif opr == "-":
                output = n1-n2

            elif opr == "*":
                output = n1*n2

            elif opr == "/":
                output = n1/n2
                
    except: 
       output= 'Invalid Input'

    return render(request,'calculator.html',{'op':output})





def evenOdd(request):

    output = ''
    
    try: 
        if request.method == 'POST':
            number = eval(request.POST.get('number')) 

            if number%2 == 0: 
                output = "Even"
            else:
                output = "Odd"

    except: 
        output = 'Invalid Input....'

    return render(request,'evenorodd.html',{'op':output})



def markSheet(request):

    data = {}

    try:
        if request.method == 'POST':

            if request.post.get('sub1') == "":   
                return render(request,'marksheet.html',{"error":True})

            sub1 = int(request.POST.get('sub1'))
            sub2 = int(request.POST.get('sub2'))
            sub3 = int(request.POST.get('sub3'))
            sub4 = int(request.POST.get('sub4'))
            sub5 = int(request.POST.get('sub5'))

            total = int(sub1+sub2+sub3+sub4+sub5)
            percentage = int((total*100)/500)
            
            if (percentage>=60): Division = "FIRST Division"
            elif(percentage>=50): Division = 'SECOND Division'            
            elif(percentage>=35): Division = 'THIRD Division'            
            else: Division = 'FAIL'            

            data = {
                'total':total,
                'percentage': percentage,
                'division': Division   
            }
    except:
        data = {
                'total':"invalid",
                'percentage': "invalid" ,
                'division': "invalid"   
            }      
    return render(request,'marksheet.html',data)



from news.models import newsApp
def client(request):

    fetchednews = newsApp.objects.all().order_by('-id')  
    
    if request.method == 'GET':
        search = request.GET.get("servicename")

        if search!=None:
            fetchednews = newsApp.objects.filter(news_title__icontains=search)  

    data = {
        'NewsData':fetchednews
    }

    return render(request,'client.html',data)




def newsDetails(request,slug):
    newsDetails = newsApp.objects.get(news_slug=slug)

    data ={
        'newsDetails': newsDetails,
    }
            
    return render(request,'newsdetails.html',data)




from django.core.paginator import Paginator
from service.models import service
def services(request):

    serviceData = service.objects.all().order_by('-id')
    paginator = Paginator(serviceData,1)
    page_number=request.GET.get('page')
    serviceDataFinal = paginator.get_page(page_number)
    totalpage = serviceDataFinal.paginator.num_pages
    
    data = {
        'srdata' : serviceDataFinal, 
        "lastPage" : totalpage,
        "totalPageList" : [n+1 for n in range(totalpage)],
     }
    
    return render(request,'services.html',data)



def contact(request): 

    data = {}

    try:
        if (request.method == "POST"):

            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')


            data = {
                'name_rec': name,
                'email_rec': email, 
                'phone_rec': phone,
                'message_rec': message,
            }


            url  = "/contact/?email={}".format(email)
            return HttpResponseRedirect(url)



    except Exception as e:
        print("An error occurred:", str(e))  

    return render(request,'contact.html', data)




from contactenquiry.models import contactenquiry

def saveEnquiry(request):

    result = ''

    try:     
        if (request.method == "POST"):
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')

            en = contactenquiry(name=name,email=email,phone=phone,message=message)
            en.save()

            result = 'Thank You! for submitting the enquiry...'

    except Exception as e:
        print("An error occurred:", str(e))

    return render(request,'contact.html',{'result':result})
    