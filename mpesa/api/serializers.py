from dataclasses import field


from rest_framework import serializers

from mpesa.models import LNMOnline,C2BPayments


class LNMOnlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = LNMOnline
        fields = ("id",)

class C2BPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = C2BPayments
        fields = ("id",)



