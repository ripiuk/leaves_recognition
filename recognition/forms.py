from django import forms

class RecignitionImageForm(forms.Form):
    image = forms.FileField(label = 'Select an image:')
    """
    name = forms.CharField(label='Name Of Your Image', widget=forms.TextInput(attrs={'class': 'form-control', }))
    photo = forms.ImageField(label='Select a file', )
    Certification = forms.BooleanField(label='I certify that this is my original work')
    description = forms.CharField(label='Describe Your Image',
                                  widget=forms.TextInput(attrs={'class': 'form-control', }))
    Image_Keyword = forms.CharField(label='Keyword Of Image', widget=forms.TextInput(attrs={'class': 'form-control', }))

    def clean_photo(self):
        image_file = self.cleaned_data.get('photo')
        if not image_file.name.endswith(".jpg"):
            raise forms.ValidationError("Only .jpg image accepted")
        return image_file
    """


    def clean_image(self):
        image_file = self.cleaned_data.get('image')
        if not image_file.name.endswith(".jpg"):
            raise forms.ValidationError("Only .jpg image accepted")
        return image_file