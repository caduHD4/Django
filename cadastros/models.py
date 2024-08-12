from django.db import models


class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.nome}/{self.estado}"

class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=150)
    nascimento = models.DateField(verbose_name="data de nascimento")
    cpf = models.CharField(max_length=14, verbose_name="cpf", unique=True)
    email = models.EmailField(max_length=120, blank=True, null=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome_completo} {self.cpf}"

class Apartamento(models.Model):
    numero = models.IntegerField()
    bloco = models.CharField(max_length=10)

    def __str__(self):
        return f"Apto {self.numero}, Bloco {self.bloco}"

class Carro(models.Model):
    placa = models.CharField(max_length=10)
    modelo = models.CharField(max_length=50)
    cor = models.CharField(max_length=20)
    apartamento = models.ForeignKey(Apartamento, on_delete=models.CASCADE, related_name="carros")

    def __str__(self):
        return f"{self.modelo} ({self.placa})"

class Morador(Pessoa):
    apartamento = models.OneToOneField(Apartamento, on_delete=models.CASCADE, related_name="morador")
    possui_animais = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nome_completo} - Apto {self.apartamento.numero}, Bloco {self.apartamento.bloco}"

class Visita(models.Model):
    pessoa_visita = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='visitas_feitas')
    pessoa_visitada = models.ForeignKey(Morador, on_delete=models.CASCADE, related_name='visitas_recebidas')
    motivo = models.CharField(max_length=255)
    data_hora_entrada = models.DateTimeField()
    data_hora_saida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Visitante {self.pessoa_visita.nome_completo} em Apto {self.pessoa_visitada.apartamento.numero}, {self.pessoa_visitada.nome_completo}, Bloco {self.pessoa_visitada.apartamento.bloco} - Entrada: {self.data_hora_entrada.strftime('%d/%m/%Y %H:%M')}"

class Porteiro(models.Model):
    nome = models.CharField(max_length=150)
    turno = models.CharField(max_length=50)

    def __str__(self):
        return f"Porteiro {self.nome} - Turno {self.turno}"
