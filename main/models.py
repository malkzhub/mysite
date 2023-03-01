from django.db import models

# Create your models here.

### App

'''
    01 March, 2023

    Install Pillow for ImageField 
        pip install Pillow

'''

# Home Section

class Home(models.Model):
    name = models.CharField(max_length=120)
    greeting_1 = models.CharField(max_length=15)
    greeting_2 = models.CharField(max_length=15)
    picture = models.ImageField(upload_to='images/')

    recent_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# About Section

class About(models.Model):
    heading = models.CharField(max_length=120)
    career = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    profile_pic = models.ImageField(upload_to='profile')

    recent_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career
    
class Social_Media(models.Model):
    fk_about = models.ForeignKey(About, on_delete=models.CASCADE)
    sm_name = models.CharField(max_length=15)
    sm_link = models.URLField(max_length=250)


class Education(models.Model):
    fk_about = models.ForeignKey(About, on_delete=models.CASCADE)
    institution = models.CharField(max_length=250)
    course = models.CharField(max_length=120)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()


# Work Experience Section
class Job_Title(models.Model):
    title = models.CharField(max_length=50)
    dt_start = models.DateField()
    dt_end = models.DateField()

    def __str__(self):
        return self.title

class Job_Description(models.Model):
    fk_job_title = models.ForeignKey(Job_Title, on_delete=models.CASCADE)
    tasks = models.CharField(max_length=225)

    recent_update = models.DateTimeField(auto_now=True)

# Skills Section
class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name
    
class Skills(models.Model):
    fk_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skill = models.CharField(max_length=50)

# Portfolio Section (To be followed)

class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=250)



# Work Section

# Contact Section
