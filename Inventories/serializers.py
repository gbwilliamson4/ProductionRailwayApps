from rest_framework import serializers
from .models import IncomeDetail, IncomeMaster


class IncomeMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeMaster
        fields = ['id', 'daterange']


class IncomeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeDetail
        fields = ['id', 'daterange', 'location', 'transactions', 'net_amnt', 'type']