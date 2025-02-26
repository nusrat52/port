from django.shortcuts import render
from .models import Owner, Projects, ProjectImages, Testimonials, Tools, Education, Experience, Contact
# Create your views here.

def index(response): 


     #     {"image":"", "description":"Nusret is a highly skilled Full-Stack React & Django developer who consistently delivers clean, efficient, and scalable code. He has a keen eye for UI/UX, ensuring that every project is both visually appealing and user-friendly. Beyond coding, he's always eager to learn and optimize deployments, making our development workflow smoother and more efficient.", 'name':"Semedbeyli Ilkin", "profession":"Senior Mobile Developer"},
     


    testimonials=Testimonials.objects.all()
    mainDetail= Owner.objects.first()

    images=ProjectImages.objects.all()
    tools=Tools.objects.all()


    for image in images:
        print(image.project.__dict__, "image")

    return render(response, "index.html", {"detail":mainDetail, "testimonials": testimonials, "tools":tools})





def resume(response):
    def split_experience_list(exp_list):
                mid = (len(exp_list) + 1) // 2  # Ensures first half is larger when odd
                return exp_list[:mid], exp_list[mid:]
    

    education=Education.objects.all()[::-1]
    experience=Experience.objects.all()[::-1]
    tools = Tools.objects.all()
 
    tool1, tool2 = split_experience_list(tools)
    
    return render(response, 'resume.html', { "experience":experience, "education":education, "tool1":tool1, "tool2":tool2})



def contact(request):
 
    if request.method=="POST":
          
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        subject=request.POST['subject']
        try:
            contact=Contact(name=name, subject=subject, description=message, email=email)
            contact.save()
            return render(request, 'contact.html', {"name":name})
        except Exception as e:
            return render(request, 'contact.html', {"error":e})
    else:
      return render(request, 'contact.html')



def portfolio(request):
     projects=Projects.objects.all()

     return render(request, 'portfolio.html', {"projects":projects})
 



def detailed(request, slug):
     project=Projects.objects.get(slug=slug)


     return render(request, 'detail.html', {"project":project})
 