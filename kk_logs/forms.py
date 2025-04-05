from django import forms
from .models import Topic, Entry

# define topic form for topic adding.
class TopicForm(forms.ModelForm):
    
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

# define entry form for entry adding
class EntryForm(forms.ModelForm):
    
    class Meta:
        model = Entry
        fields = ['content']
        labels = {'content': ''}
        widgets = {'content': forms.Textarea()}
        #widgets = {'content': forms.Textarea(attrs={'id': 'id_content','cols': 80, 'required': False})}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].required = False 
        
        