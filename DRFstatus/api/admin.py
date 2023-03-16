from django.contrib import admin

from .models import Order, TitleJob, Status, Workers

admin.site.register(Order)
admin.site.register(Workers)
admin.site.register(Status)
admin.site.register(TitleJob)
