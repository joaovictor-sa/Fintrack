from rest_framework import serializers
from categories.models import Category
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ('user',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        request = self.context.get('request')
        if request:
            self.fields['category'].queryset = Category.objects.filter(user=request.user)
