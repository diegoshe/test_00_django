from django import forms


class InputForm(forms.Form):
    name = forms.CharField(max_length=200)
    msg  = forms.CharField(max_length=2000)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'