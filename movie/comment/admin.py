from django.contrib import admin

# Register your models here.
from comment.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "content", "date"]
    list_filter = ["active", "date"]
    search_fields = ['user', 'date', 'content']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Comment, CommentAdmin)
