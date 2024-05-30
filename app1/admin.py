from django.contrib import admin
from.models import Blog,Author,userregister,image
# Register your models here.


admin.site.register(Blog)
#admin.site.register(Author)

class author_(admin.ModelAdmin):
    list_display = ['name','email']
    list_filter = ['name','email']
    search_fields= ['name','email']

admin.site.register(Author,author_)    

class user_(admin.ModelAdmin):
    list_display=['name','email','address','password']

admin.site.register(userregister,user_)     

admin.site.register(image)

    
