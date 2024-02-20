from django import forms

from .models import ElcLog


class ElcLogAddForm(forms.ModelForm):
    class Meta:
        model = ElcLog
        fields = (
            "record_text_title",
            "record_text_full",
            # "record_author",
            # "record_data_create",
            "record_object",
            "record_electrical_room",
            "record_mechanism",
        )
