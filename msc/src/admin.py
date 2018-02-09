from django.contrib import admin
from .models import *
# Register your models here.
class core_team_model(admin.ModelAdmin):
    list_display=["name","post","fb_link","git_link","linkedin_link"]
    class Meta:
        model=Secretarie
class about_us_model(admin.ModelAdmin):
    list_1=["text","img"]
    class Meta:
        model=About_us
class event_model(admin.ModelAdmin):
    list_2=["logo","heading","description"]
    class Meta:
        model=Events

class team_model(admin.ModelAdmin):
	list_display=["name","department"]
	list_filter=["department"]
	class Meta:
		model=Team

class post_model(admin.ModelAdmin):
	list_display=["title","timestamp"]
	date_hierarchy = 'timestamp'
	search_fields = ['title','content']
	class Meta:
		model=Post

class msweek_event_model(admin.ModelAdmin):
	list_display=["title","date"]
	date_hierarchy = 'date'
	search_fields = ['title','description']
	class Meta:
		model=MSWeek_Event

class inspirus_event_model(admin.ModelAdmin):
	list_display=["title","date"]
	date_hierarchy = 'date'
	search_fields = ['title','description']
	class Meta:
		model=Inspirus_Event

class rumble_event_model(admin.ModelAdmin):
	list_display=["title","date"]
	date_hierarchy = 'date'
	search_fields = ['title','description']
	class Meta:
		model=Rumble_Event




admin.site.register(Secretarie,core_team_model)
admin.site.register(About_us,about_us_model)
admin.site.register(About_us_content)
admin.site.register(Events,event_model)
admin.site.register(Post,post_model)
admin.site.register(Team,team_model)
admin.site.register(MSWeek_Event,msweek_event_model)
admin.site.register(Inspirus_Event,inspirus_event_model)
admin.site.register(Rumble_Event,rumble_event_model)

admin.site.register(index_gallery)
admin.site.register(MSWEEK_gallery)
admin.site.register(INSPIRUSUS_gallery)
admin.site.register(RUMBLE_gallery)
