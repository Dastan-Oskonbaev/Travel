from modeltranslation.translator import register, TranslationOptions

from .models import Culture, CultureCategory


@register(CultureCategory)
class CultureCategoryTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'description',
    )


@register(Culture)
class CultureTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'description',
    )
