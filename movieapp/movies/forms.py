from django import forms
from .models import Comment



class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        # fields =["full_name", "email","review","stars"]
        exclude = ["film","creating_at"]
        
        choi = (
            ( 1,"1 ulduz"),
            ( 2,"2 ulduz"),
            ( 3,"3 ulduz"),
            ( 4,"4 ulduz"),
            ( 5,"5 ulduz"),
        )
        
        labels = {
            "full_name":"Ad Soyad",
            "email":"Mailinzi",
            "review":"Yorumunuz",
            "stars":"Yildiz"
        }
        
        widgets = {
            "full_name": forms.TextInput(attrs={"class":"form-control"}),
            "email": forms.EmailInput(attrs={"class":"form-control"}),
            "review": forms.Textarea(attrs={"class":"form-control"}),
            "stars": forms.Select(attrs={"class":"form-control costum-select"}, choices=choi)
        }
        