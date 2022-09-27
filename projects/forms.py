from django import forms
from .models import Project 

##  3)   add page to create the project =>create form to establish

attrs = {'class': 'form-control'}
class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('category','title','description')
        # define decorate of fields by bootstrap
        labels = {
            'category': ('Category'),
            'title': ('Title'),
            'description': ('Description'),
        }
        widgets = {
            'category': forms.Select(attrs=attrs),
            'title': forms.TextInput(attrs=attrs),
            'description': forms.Textarea(attrs=attrs)
        }


## 5) = add page to manage the project =>creat form to update

class ProjectupdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('category','title','status')
        # define decorate of fields by bootstrap
        widgets = {
            'category':forms.Select(attrs=attrs),
            'title':forms.TextInput(attrs=attrs),
            'status':forms.Select(attrs=attrs),

        }