from django.conf import settings
from django.contrib import admin
from django.db.models import Q


class TranslationStatusFilter(admin.SimpleListFilter):
    title = "Translation"
    parameter_name = "snart"
    fields = ["value"]

    def lookups(self, request, model_admin):
        return [
            ("e", "Empty"),
            ("m", "Missing"),
            ("c", "Complete"),
        ]

    def queryset(self, request, queryset):
        languages = getattr(settings, "MODELTRANSLATION_LANGUAGES", [])

        # Determine which translatable fields exist on this model
        model_fields = [f.name for f in queryset.model._meta.get_fields()]
        applicable_fields = [f for f in self.fields if f in model_fields]

        if not applicable_fields:
            return queryset

        # Build a Q object to check for missing translations in each language
        if self.value() in ["m", "c"]:
            query = Q()

            for field in applicable_fields:
                for lang in languages:
                    field_name = f"{field}_{lang}"
                    if field_name in model_fields:
                        query |= Q(**{f"{field_name}__isnull": True})
                        query |= Q(**{f"{field_name}": ""})

            if self.value() == "m":
                return queryset.filter(query)

            if self.value() == "c":
                return queryset.exclude(query)

        if self.value() == "e":
            for field in applicable_fields:
                for lang in languages:
                    field_name = f"{field}_{lang}"
                    if field_name in model_fields:
                        queryset = queryset.filter(Q(**{f"{field_name}__isnull": True}) | Q(**{f"{field_name}": ""}))
            return queryset

        return queryset
