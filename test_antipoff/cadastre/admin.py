from django.contrib import admin

from .models import CadastreData, Result


class CadastreDataAdmin(admin.ModelAdmin):
    list_display = (
        "cadastre_number",
        "latitude",
        "longitude",
        "create_date"
    )


class ResultAdmin(admin.ModelAdmin):
    list_display = (
        "cadastre_number",
        "result"
    )
    search_fields = ("cadastre_number",)


admin.site.register(CadastreData, CadastreDataAdmin)
admin.site.register(Result, ResultAdmin)
