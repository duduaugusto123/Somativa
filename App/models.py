from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class CustomUser(models.Model):
    Type_User = [
        ("FUNCIONARIO","FUNCIONARIO"),
        ("CLIENTE","CLIENTE"),
    ]
    type = models.CharField(choices=Type_User, max_length=200)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    data_nasc = models.DateField(null=True,blank=True)
    cpf = models.IntegerField(null=True,blank=True)
        
    def __str__(self):
        return self.user.email

@receiver(post_save, sender=User)
def create_user_custom(sender, instance, created, **kwargs):
    if created:
        CustomUser.objects.create(user=instance)
        

class Categoria_Servico(models.Model):
    Type_Category = [
        ("Troca de Oleo","Troca de Oleo"),
        ("Troca de Velas","Troca de Velas"),
        ("Rodizio Pneus","Rodizio Pneus"),
        ("Troca Farol","Troca Farol"),        
        ]
    tipo = models.CharField(max_length=50,choices=Type_Category,null=False,blank=False)
    Valor_Servico = models.IntegerField(null=False,blank=False)
    
    def __str__(self):
        return self.tipo

class Produtos_Manutencao(models.Model):
    product_name = models.CharField(max_length=250,null=False,blank=False)
    qt_Stock = models.IntegerField(null=False,blank=False)
    producer_name = models.CharField(max_length=200,null=False,blank=False)
    producer_code = models.CharField(max_length=200,null=False,blank=False)
    Buy_price = models.IntegerField(null=False,blank=False)
    Sell_price = models.IntegerField(null=False,blank=False)
    
    def __str__(self):
        return self.product_name
    
class Auto_Category(models.Model):
    Auto_Type = [
        ("Carro","Carro"),
        ("Moto","Moto"),
        ("Trem","Trem"),
        ("Caminhão","Caminhão")
    ]
    type = models.CharField(max_length=200,choices=Auto_Type,null=False,blank=False)
    
    def __str__(self):
        return self.type
    
class Auto_register(models.Model):
    category = models.ForeignKey(Auto_Category, related_name="type_auto_category", on_delete=models.CASCADE)
    marca = models.CharField(max_length=200,null=False, blank=False)
    modelo = models.CharField(max_length=200,null=False, blank=False)
    ano = models.IntegerField(null=False, blank=False)
    
    def __str__(self):
        return self.category
    
class Reserva(models.Model):

    Cliente = models.ForeignKey(CustomUser, related_name="Cliente_Rquester",on_delete=models.CASCADE)
    carro = models.ForeignKey(Auto_register, related_name="Car_Client",on_delete=models.CASCADE)
    data_reserva = models.DateField(default=timezone.now)
    
    def __str__(self):
        return str(self.data_reserva)
    
    def save(self, *args, **kwargs):
        # Verifique se já existem 2 reservas para a mesma data
        count_reservas = Reserva.objects.filter(data_reserva=self.data_reserva).count()        
        if count_reservas >= 2:
            raise ValueError('Já existem 2 reservas para esta data.')
        
        super().save(*args, **kwargs)

   


class Manutencion(models.Model):
    dados_auto = models.ForeignKey(Auto_register, related_name="Dados_Auto",on_delete=models.CASCADE)
    Service_Category = models.ManyToManyField(Categoria_Servico,related_name="Category_Service")
    Used_Product = models.ManyToManyField(Produtos_Manutencao,related_name="Used_Products")
    Price_total = models.IntegerField(null=True,blank=True)
    funcionario_id = models.ForeignKey(CustomUser,related_name="Service_Relized_Employee",on_delete=models.CASCADE)
    Cliente_id = models.ForeignKey(CustomUser, related_name="Service_Requester",on_delete=models.CASCADE)
    Reserva_id = models.ForeignKey(Reserva, related_name="Reserva",on_delete=models.CASCADE, null = True, blank=True)

    def __str__(self):
        return self.category



class Payment_Category(models.Model):
    Payment_Type = [
        ("PIX","PIX"),
        ("Boleto","Boleto"),
        ("Cartão Credito","Cartão Credito"),
        ("Cartão Debito","Cartão Debito"),
    ]
    Payment_type = models.CharField(max_length=50,choices=Payment_Type,null=False,blank=False)
    
    def __str__(self):
        return self.Payment_type

class Payment_Status(models.Model):
    Status_Type = [
        ("Pendente","Pendente"),
        ("Aprovado","Aprovado"),
        ("Cancelada","Cancelada"),
    ]
    status = models.CharField(max_length=50,choices=Status_Type,null=False,blank=False)
    
    def __str__(self):
        return self.status

class Payment(models.Model):
    category = models.ForeignKey(Payment_Category, related_name="Payment_Category",on_delete=models.CASCADE)
    descrition = models.CharField(max_length=200,null=False,blank=False)
    manutention_id = models.ForeignKey(Manutencion,related_name="Manutencion",on_delete=models.CASCADE)
    status = models.ForeignKey(Payment_Status, related_name="Payment_Status",on_delete=models.CASCADE)
    discount_value = models.IntegerField(null=True,blank=True)
    Valor_Final = models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.category
    
    