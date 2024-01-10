from django import forms

class schoolForm(forms.Form):
     Sname=forms.CharField()
     Sprinc=forms.CharField()
     Sloc=forms.CharField()
     Semail=forms.EmailField()
     re=forms.EmailField()
     def clean(self):
          Email=self.cleaned_data['Semail']
          remail=self.cleaned_data['re']
          if Email != remail:
               raise forms.ValidationError('enter the eamil correctly')
               