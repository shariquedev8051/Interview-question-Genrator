from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from .models import Programms
# Register your models here.
class ProgrammsAdmin(admin.ModelAdmin):
    empty_value_display = '-NA-'
    fields = ('Programms','Tag','Answer','Link','company')
    list_filter = ('Tag',)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }

admin.site.register(Programms,ProgrammsAdmin)