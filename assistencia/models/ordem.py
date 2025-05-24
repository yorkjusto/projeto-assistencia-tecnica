from django.db import models
from .geral import Geral
from .cliente import Cliente

class OrdemDeServico(Geral):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    equipamento = models.CharField(max_length=100)
    defeito = models.TextField()
    # Serviço a ser feito
    servico = models.TextField()
    # Data de emissão da ordem de serviço
    data = models.DateTimeField(auto_now_add=True)
    # Valor a ser pago
    valor = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    tecnico = models.CharField(max_length=50)
    situacao = models.CharField(
        max_length=50,
        choices=[
            ('na_bancada', 'Na Bancada'),
            ('aguardando_pecas', 'Aguardando Peças'),
            ('aguardando_aprovacao', 'Aguardando Aprovação'),
            ('abandonado', 'Abandonado pelo Cliente'),
            ('retornou', 'Retornou'),
            ('orcamento_reprovado', 'Orçamento Reprovado'),
        ]
    )

    def __str__(self):
        return f"OS #{self.id} - {self.cliente.nome} "
    