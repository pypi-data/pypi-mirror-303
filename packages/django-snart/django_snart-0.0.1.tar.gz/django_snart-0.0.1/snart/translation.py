from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from .models import Constant


@register(Constant)
class ConstantTranslationOptions(TranslationOptions):
    fields = ("value",)
