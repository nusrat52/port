from django.db import models

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=20)
    sirName = models.CharField(max_length=20)
    description = models.TextField()
    profession = models.JSONField(default=dict)
    photo = models.ImageField(upload_to='images')


class Testimonials(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    profession = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='testimonialImages')
   

class Tools(models.Model):
    name = models.CharField(max_length=20)
    percent = models.IntegerField()
    photo = models.ImageField(upload_to='toolImages')
   

class Experience(models.Model):
    companyName = models.CharField(max_length=50)
    description = models.TextField()
    position = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
 
 

class Education(models.Model):
    companyName = models.CharField(max_length=50)
    description = models.TextField()
    position = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
 
 





 



class Projects(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    description = models.TextField()
    technologies = models.JSONField(default=list)
    slug = models.SlugField(unique=True)
 
    def __str__(self):
        return self.slug

    @property
    def images_list(self):
        return [img.image.url for img in self.images.all()]  # Fetch all related images


class ProjectImages(models.Model):
    image=models.ImageField(upload_to='projectImages')
    project = models.ForeignKey(Projects, related_name="images", on_delete=models.CASCADE)
 
    def __str__(self):
        return f"Image for {self.image}"
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    subject = models.CharField(max_length=50)
    email = models.EmailField()
 
 