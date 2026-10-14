from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    # Honeypot field: hidden from humans, bots tend to fill it in.
    website = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        label="",
    )

    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Your name"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "you@example.com"}
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your message…",
                    "rows": 5,
                }
            ),
        }

    def clean_website(self):
        value = self.cleaned_data.get("website")
        if value:
            raise forms.ValidationError("Spam detected.")
        return value
