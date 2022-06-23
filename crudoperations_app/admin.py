from django.contrib import admin
from crudoperations_app.models import ParentData, ChildData

# Register your models here.
admin.site.register(ParentData)
admin.site.register(ChildData)
