from django.forms import ModelForm
from MyRent.models import Operation, Image


class OperationAgreementForm(ModelForm):
    class Meta:
        model = Operation
        exclude = ["agreement"]


class ImageFlatForm(ModelForm):
    class Meta:
        model = Image
        exclude = ["flat"]
