from django.shortcuts import render,redirect,HttpResponse
from .models import Department,Role,Person,Year
from django.db.models import Q
from .forms import Personform,PersonSearchform
# Create your views here.
def index(request):
    return render(request,"index.html")

def all_stud(request):
    form = PersonSearchform(request.POST or None)
    stud = Person.objects.all()
    context = {
      'stud':stud
    }
    print(context)    
    if request.method == "POST":
            stud = Person.objects.filter(first_name__icontains=form['first_name'].value(),         
            role=form['role'].value()
            )            
    context = {
                    'form':form,
                    'stud':stud
        

        }

    return render(request,"all_stud.html",context)

def remove_stud(request,st_id=0):
      if st_id:
         try:
             
             st_remove =Person.objects.get(id=st_id)
             st_remove.delete()
             return HttpResponse("Student removed successfully" )
             
         except:
             return HttpResponse("please enter a valid id")
              
      
      
      
      
      
      
      
      stud = Person.objects.all()
      context = {
      'stud':stud

    }
      

      return render(request,"remove_stud.html",context)

def add_stud(request):
    form = Personform(request.POST or None)
    if form.is_valid():
	        form.save() 
           
                 
    context = {
		        "form": form,
		         "title": "Add Stud",
	    }
    return render(request, "add_stud.html", context)


def filter_stud(request):
    queryset = Person.objects.all()
    context = {
               'queryset':queryset
    }
    print(context)
    return render(request,"all_stud.html",context)
    
     

    