from django import forms
g=[('male','MALE'),('female','FEMALE')]
c=[('python','PYTHON'),('java','JAVA'),['sql','SQL']]
class StudentForms(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    address=forms.CharField(max_length=300,widget=forms.Textarea)
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    course=forms.ChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)