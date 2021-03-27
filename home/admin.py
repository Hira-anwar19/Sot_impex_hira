from django.contrib import admin
from home.models import Contact,Estimate,Subscribe,Blog,Comment
from django.contrib import admin

class CommentInline(admin.TabularInline): # new
    model = Comment


class NewsfeedAdmin(admin.ModelAdmin): # new
    inlines = [
        CommentInline,
    ]


# Register your models here.
admin.site.register(Contact)
admin.site.register(Estimate)
admin.site.register(Subscribe)
admin.site.register(Blog)
admin.site.register(Comment)





