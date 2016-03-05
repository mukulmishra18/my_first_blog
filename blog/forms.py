from django import forms #importing django form
from .models import Post #importing Post model

class PostForm(forms.ModelForm): #telling django that this is a ModelForm

	class Meta:
		model = Post    # telling which model is used to create this form
		fields = ('title', 'text',)  #feild end up in this form