from django.shortcuts import render

def sum(request):
    if request.method=="POST":
        num1=request.POST.get("txt_num1")
        num2=request.POST.get("txt_num2")
        result=int(num1)+int(num2)
        return render(request,"Basics/sum.html",{'sum':result})
    else:
        return render(request,"Basics/sum.html")


def Calculator(request):
    if request.method=="POST":
        num1=request.POST.get("txt_num1")
        num2=request.POST.get("txt_num2")
        btn=request.POST.get("btn_submit")
        if btn=="+":
           result=int(num1)+int(num2)
        elif btn=="-":
           result=int(num1)-int(num2)
        elif btn=="*":
           result=int(num1)*int(num2) 
        elif btn=="/":
           result=int(num1)/int(num2)    
        return render(request,"Basics/Calculator.html",{'result':result})
    else:
        return render(request,"Basics/Calculator.html")
        
def Largest(request):
    if request.method=="POST":
        num1=int(request.POST.get("txt_num1"))
        num2=int(request.POST.get("txt_num2"))
        if num1 > num2:
            largest=num1
            smallest=num2
        else:
            largest=num2
            smallest=num1
        return render(request,"Basics/Largest.html",{'largest':largest,'smallest':smallest})
    else:
        return render(request,"Basics/Largest.html")        
