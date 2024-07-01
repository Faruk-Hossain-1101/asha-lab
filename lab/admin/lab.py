from django.contrib import admin
from lab.models.lab import Discount, Lab, TestGroup, Test

admin.site.register(Discount)
admin.site.register(Lab)
admin.site.register(TestGroup)
admin.site.register(Test)