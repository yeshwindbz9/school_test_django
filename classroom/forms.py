from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "id": "exampleFormControlInput1", "placeholder":"mail: name@example.com"}
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": "3",
                "id": "exampleFormControlTextarea1",
                "placeholder":"message: sample message"
            }
        )
    )
