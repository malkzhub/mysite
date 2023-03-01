from django.contrib import admin
from .models import Home, About, Social_Media, Education, Job_Title, Job_Description, Category, Skills, Portfolio

# Register your models here.

# App


# Home
admin.site.register(Home)

# About
class Social_Media_Inline(admin.TabularInline):
    model = Social_Media
    extra = 2

class Education_Inline(admin.TabularInline):
    model = Education
    extra = 1

@admin.register(About)
class About_Admin(admin.ModelAdmin):
    inlines = [
        Social_Media_Inline,
        Education_Inline,
    ]


# Work Experience
class Job_Description_Inline(admin.TabularInline):
    model = Job_Description
    extra = 5

@admin.register(Job_Title)
class Job_Title_Admin(admin.ModelAdmin):
    inlines = [
        Job_Description_Inline
    ]
    

# Skills
class Skills_Inline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class Category_Admin(admin.ModelAdmin):
    inlines = [
        Skills_Inline
    ]


# Portfolio
admin.site.register(Portfolio)