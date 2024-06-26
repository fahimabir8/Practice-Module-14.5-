from django import forms 
import datetime

Birth_Year_Choices = ['2003','2004','2005']
Anime = [('saitama','One punch man'), ('Gojo','Jujutsu Kaisen'), ('Kakashi','Naruto'), ('Luffy','One piece'),('Light','Deathnote')]

class SampleForm(forms.Form):
    name = forms.CharField(max_length=30,initial="Your name")
    email = forms.EmailField()
    birth = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}),label="BirthDate")
    comment = forms.CharField(widget=forms.Textarea)
    check = forms.BooleanField(label="I agree to the terms & conditions",initial=True)
    double_check = forms.BooleanField(label="I agree to the terms & conditions")
    Birth_select = forms.DateField(widget=forms.SelectDateWidget(years=Birth_Year_Choices), required=False)
    Age = forms.DecimalField()
    Day = forms.DateField(initial=datetime.date.today)
    Favorite_anime = forms.ChoiceField(choices=Anime)
    Favorite = forms.ChoiceField(choices=Anime,widget=forms.RadioSelect)
    Multi_favorite = forms.MultipleChoiceField(choices=Anime)
    Multi_favorite_anime = forms.MultipleChoiceField(choices=Anime,widget=forms.CheckboxSelectMultiple)
    duration = forms.DurationField()
    file = forms.FileField()
    file_path = forms.FilePathField(path='D:\discrete')
    image = forms.ImageField()
    ip_address = forms.GenericIPAddressField()
    ready = forms.NullBooleanField()
    url = forms.URLField()
    uuid = forms.UUIDField()
    