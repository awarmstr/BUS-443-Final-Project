from django.contrib import admin
from Student.models import Studentdetails
from Student.models import Coursedetails
from Student.models import Enrollment

admin.site.register(Studentdetails)
admin.site.register(Coursedetails)
admin.site.register(Enrollment)

# Register your models here.
