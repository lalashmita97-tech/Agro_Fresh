from django.contrib import admin
from.models import Contact,Feedback,Farmer,Product

class Contact_Admin(admin.ModelAdmin):
    list_display=["name","email","phone","query","date"]


class Feedback_Admin(admin.ModelAdmin):
    list_display=["name","email","rating","remarks","date"]









admin.site.register(Contact,Contact_Admin)
admin.site.register(Feedback,Feedback_Admin)
admin.site.register(Farmer)
admin.site.register(Product)


admin.site.site_header="Famers Portal Admin Dasboard"

admin.site.site_title="your fam"
admin.site.index_title="AgroFresh"
