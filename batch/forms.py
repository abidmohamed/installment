from django.forms import ModelForm, modelformset_factory
from django import forms

from batch.models import OriginalBatch, OngoinglBatch


class OriginalBatchFrom(ModelForm):
    class Meta:
        model = OriginalBatch

        fields = ['amount', 'period']


class OngoingBatchFrom(ModelForm):
    class Meta:
        model = OngoinglBatch

        fields = ['amount', 'period']
