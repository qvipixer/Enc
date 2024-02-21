from django import forms

from .models import ASLog


class AsLogAddForm(forms.ModelForm):
    class Meta:
        model = ASLog
        fields = (
            "record_text_title",
            "record_text_full",
            # "record_author",
            "record_change_location_plc",
            "record_change_location_hmi",
            # "record_data_create",
            "record_object",
            "record_electrical_room",
            "record_project",
            "record_mechanism",
        )
