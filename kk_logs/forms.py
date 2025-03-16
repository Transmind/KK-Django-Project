from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    
    class Meta:
        model = Entry

        #fields = ['text']
        #labels = {'text': ''}
        #widgets = {'text': forms.Textarea(attrs={'cols': 80})}

        fields = ['content']
        labels = {'content': ''}
        widgets = {'content': forms.Textarea(attrs={'id': 'id_content','cols': 80, 'required': False})}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].required = False 
        
        