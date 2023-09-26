from rest_framework import serializers

from cadastre.models import CadastreData, Result


class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "cadastre_number",
            "latitude",
            "longitude",
            "create_date"
        )
        model = CadastreData


class ResultSerializer(serializers.ModelSerializer):
    cadastre_number = serializers.SlugRelatedField(
        queryset=CadastreData.objects.all(),
        slug_field="cadastre_number"
    )

    class Meta:
        fields = (
            "cadastre_number",
            "result"
        )
        model = Result
