from django.contrib import admin
from django.forms import ModelForm

# Models
from webservicedoc.models import Webservicedoc

# Utilities
import pyxb  # For catching the exceptions
from .wadl import CreateFromDocument  # The Python-version WADL XSD validator


class WebservicedocAdminForm(ModelForm):
    """
    Custom Validation For DWML
    """
    class Meta:
        model = Webservicedoc
        fields = ['wadl_raw', ]

    def clean_wadl_raw(self):
        # Custom WADL validation
        wadl_raw = self.cleaned_data['wadl_raw']
        try:
            this_wadl = CreateFromDocument(wadl_raw)
        except pyxb.UnrecognizedContentError as e:
            raise forms.ValidationError(
                "Error validating response: %s" % e.details())
        except Exception as e:
            forms.ValidationError("Unknown validation error: %s" % e)
        return wadl_raw
