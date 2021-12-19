from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from .models import Questions
# Register your models here.


class QuestionsAdmin(admin.ModelAdmin):
    empty_value_display = '-NA-'
    fields = ('Question', 'Sub_Questions', 'Tag', 'Answer', 'Link', 'company')
    list_filter = ('Tag',)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    }


admin.site.register(Questions, QuestionsAdmin)
