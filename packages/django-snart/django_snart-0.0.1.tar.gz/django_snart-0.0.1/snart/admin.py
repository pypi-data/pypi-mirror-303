from django.conf import settings
from django.contrib import admin
from django.utils.html import escape
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin

from snart.filters import TranslationStatusFilter

from .models import Constant


def truncate_with_count(value, max_length):
    lv = len(value)
    if lv > max_length:
        return mark_safe("%s... %s" % (escape(value[:max_length]), f"<em>[{lv}]</em>"))
    return value


@admin.register(Constant)
class ConstantAdmin(TranslationAdmin):
    actions_on_top = False
    actions = None
    list_max_show_all = 300
    list_per_page = 100
    ordering = ["key"]
    list_display = ["key_nobr", "get_filled_trans", "truncated_value"]
    readonly_fields = ["key", "context"]
    list_filter = [TranslationStatusFilter]

    # @admin_field(short_description="D. Tr.", admin_order_field="filled_trans")
    def get_filled_trans(self, obj):
        status = []
        for lang in settings.MODELTRANSLATION_LANGUAGES:
            value = (getattr(obj, f"value_{lang}") or "").strip()
            css_class = "yes" if len(value) else "no"
            status.append(f'<span class="snart_lang_badge snart_lang_badge-{css_class}">{lang}</span>')
        return mark_safe("<nobr class='snart_lang_badges'>" + "".join(status) + "</nobr>")

    get_filled_trans.short_description = "Translations"

    def key_nobr(self, obj):
        return mark_safe(f"<nobr>{obj.key}</nobr>")

    key_nobr.short_description = "Key"

    def truncated_value(self, obj):
        return truncate_with_count(obj.value, 100)

    truncated_value.short_description = "Value"
    truncated_value.allow_tags = True

    class Media:
        css = {"all": ("snart/css/style.css", "modeltranslation/css/tabbed_translation_fields.css")}
        js = [
            "snart/js/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
        ]

