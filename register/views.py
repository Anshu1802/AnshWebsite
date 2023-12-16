from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from register.models import Register
from django.http import HttpResponse
from django.http import FileResponse

def login(request):
    if request.method=='POST':
        data=request.POST
        email=data.get('email')
        pwd=data.get('pwd')
        
        if Register.objects.filter(email=email,password=pwd).exists():
            
            return redirect('/home')
        else:
            return HttpResponse("Invalid login credentials")
            
                
        
    return render(request,'login.html')


def home(request):
    # Path to the file you want to make available for download
    file_path = "C:/Users/Administrator/Downloads/Anshresume.pdf"

    # Open the file in binary mode
    with open(file_path, 'rb') as file:
        # Use FileResponse to handle the file download
        response = FileResponse(file)
        # Set the content type for the response
        response['Content-Type'] = 'application/pdf'  # Set the appropriate content type for a PDF file
        # Set the Content-Disposition header to force download
        response['Content-Disposition'] = 'attachment; filename="Anshresume.pdf"'
    return render(request,'home.html')




def register(request):
    if request.method=='POST':
        data=request.POST
        email=data.get('email')
        company_name=data.get('cname')
        contact=data.get('contact')
        password=data.get('pwd')
        Register.objects.create(email=email,company_name=company_name,contact=contact,password=password)
        return redirect('/home')
    return render(request,'register.html')