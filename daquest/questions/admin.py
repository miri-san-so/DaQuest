from django.contrib import admin

from .models import Questions, Comments, Solutions

admin.site.site_header = "DaQuest Admin"
admin.site.site_title = "DaQuest Admin Area"
admin.site.index_title = "Welcome Admin to DaQuests Heart"


class CommentsInline(admin.TabularInline):
    model = Comments


class SolutionsInline(admin.TabularInline):
    model = Solutions
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_title']}),
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': [
         'published_date'], 'classes': ['collapse']}),
    ]
    readonly_fields = ('published_date',)
    inlines = [CommentsInline, SolutionsInline]


# admin.site.register(Questions)
# admin.site.register(Comments)
admin.site.register(Questions, QuestionAdmin,)
