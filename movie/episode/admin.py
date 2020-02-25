from django.contrib import admin
from .models import Episode, Comment

# Register your models here.
admin.site.register(Episode)


class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "content", "date", "active"]
    list_filter = ["active", "date"]
    search_fields = ['user', 'date', 'content']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Comment, CommentAdmin)
