from django.contrib import admin
from yelpvis.models import  YelpvisCommentState


class CommentStateAdmin(admin.ModelAdmin):
	list_display=('content','pub_date','vis_state')
	list_filter=['pub_date']
	search_fields=['content']
	date_hierarchy='pub_date'


admin.site.register(YelpvisCommentState,CommentStateAdmin)


