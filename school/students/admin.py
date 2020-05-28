from django.contrib import admin
from .models import Student
from profile_maker.models import User_Profile
from post.models import Post, Like

# Register your models here.

admin.site.register(Student)
admin.site.site_header = 'School Management System'
admin.site.register(User_Profile)

admin.site.register(Post)
admin.site.register(Like)