from django.shortcuts import render

# Create your views here.
def calci(request):
    field1=request.GET['field1']
    field2=request.GET['field2']
    operation =request.GET['optradio']
    result=0
    if operation == '+':
        result=int(field1)+int(field2)
    elif operation =='-':
        result=int(field1)-int(field2)
    elif operation == '*':
        result=int(field1)*int(field2)   
    else: 
        result=int(field1)/int(field2)
    return render(request,'calci/calci.html',{'result':result})

def home(request) :
    return render(request,'calci/home.html')   