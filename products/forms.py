from django import forms
from .models import *

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ('name','brand','category','cost','release_date','description','photo')


# class ReviewForm(forms.ModelForm):  
#     class Meta:  
#         model = Review  
#         fields = ('rating','comment')  