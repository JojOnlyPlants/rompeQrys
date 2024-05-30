from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Page

class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'content': CKEditorWidget(attrs={'class':'form-control'}),
            'order': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Orden  '}),
        }
        labels = {
            'title':'', 'order':'', 'content': ''
        }

def page_create(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            # redirige a donde quieras ir después de guardar la página
    else:
        form = PageForm()

    return render(request, 'nombre_del_template.html', {'form': form})