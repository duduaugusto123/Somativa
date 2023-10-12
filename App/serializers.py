from rest_framework import serializers
#importa todos os models que criamos
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        many = True
class CustomUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = CustomUser
        fields = '__all__'
        many = True

class Categoria_ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria_Servico
        fields = '__all__'
        many = True

class Produtos_ManutencaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos_Manutencao
        fields = '__all__'
        many = True

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
        many = True


class Auto_CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Auto_Category
        fields = '__all__'
        many = True
        
class Auto_registerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auto_register
        fields = '__all__'
        many = True
        
class ManutencionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manutencion
        fields = '__all__'
        many = True
        
class Payment_CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_Category
        fields = '__all__'
        many = True
        
class Payment_StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_Status
        fields = '__all__'
        many = True

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        many = True
        