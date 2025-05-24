from django.shortcuts import render, redirect, get_object_or_404
from assistencia.models.ordem import OrdemDeServico
from django.http import HttpRequest
from django.contrib import messages
from assistencia.models.cliente import Cliente

def lista_servicos(request: HttpRequest):
    ordens = OrdemDeServico.objects.all()
    return render(request, 'servico/lista_servicos.html', {'ordens': ordens} )

def cadastrar(request: HttpRequest):
    if request.method == 'POST':
        try:
            # Validação básica dos campos obrigatórios
            if not request.POST.get('cliente'):
                messages.error(request, 'Selecione um cliente!')
                return render(request, 'servico/cadastrar.html')
            
            # Obter dados do formulário
            cliente_id = request.POST.get('cliente')
            equipamento = request.POST.get('equipamento', '').strip()
            servico = request.POST.get('servico', '').strip()
            defeito = request.POST.get('defeito', '').strip()
            valor = request.POST.get('valor', '0').replace(',', '.')  # Formata decimal
            tecnico = request.POST.get('tecnico', '').strip()
            situacao = request.POST.get('situacao','na_bancada')

            # Verificar se cliente existe
            try:
                cliente = Cliente.objects.get(id=cliente_id)
            except Cliente.DoesNotExist:
                messages.error(request, 'Cliente não encontrado!')
                return render(request, 'servico/cadastrar.html')

            # Criar a ordem de serviço
            OrdemDeServico.objects.create(
                cliente=cliente,
                equipamento=equipamento,
                servico=servico,
                defeito=defeito,
                valor=float(valor) if valor else 0.0,  # Converter para float
                tecnico=tecnico,
                situacao=situacao
            )

            
            return redirect('assistencia:servicos')

        except Exception as e:
            messages.error(request, f'Erro ao cadastrar: {str(e)}')
            return render(request, 'servico/cadastrar.html')

    # GET request - mostrar formulário vazio
    clientes = Cliente.objects.all().order_by('nome')
    situacoes = OrdemDeServico._meta.get_field('situacao').choices
    
    context = {
        'clientes': clientes,
        'situacoes': situacoes,
    }
    return render(request, 'servico/cadastrar.html', context)

def editar(request: HttpRequest, id):
    # Obter a ordem de serviço ou mostrar erro 404
    ordem = get_object_or_404(OrdemDeServico, id=id)
    
    if request.method == 'POST':
        try:
            # Validação básica dos campos obrigatórios
            if not request.POST.get('cliente'):
                messages.error(request, 'Selecione um cliente!')
                return render(request, 'servico/editar.html', {'ordem': ordem, 'clientes': Cliente.objects.all()})
            
            # Obter dados do formulário
            cliente_id = request.POST.get('cliente')
            equipamento = request.POST.get('equipamento', '').strip()
            servico = request.POST.get('servico', '').strip()
            defeito = request.POST.get('defeito', '').strip()
            valor = request.POST.get('valor', '0').replace(',', '.')  # Formata decimal
            tecnico = request.POST.get('tecnico', '').strip()
            situacao = request.POST.get('situacao', 'na_bancada')

            # Verificar se o cliente existe
            try:
                cliente = Cliente.objects.get(id=cliente_id)
            except (Cliente.DoesNotExist, ValueError):
                messages.error(request, 'Cliente inválido!')
                return render(request, 'servico/editar.html', {'ordem': ordem, 'clientes': Cliente.objects.all()})

            # Atualizar os campos
            ordem.cliente = cliente
            ordem.equipamento = equipamento
            ordem.servico = servico
            ordem.defeito = defeito
            ordem.tecnico = tecnico
            ordem.situacao = situacao
            
            # Converter e validar o valor
            try:
                ordem.valor = float(valor) if valor else 0.0
            except ValueError:
                messages.error(request, 'Valor inválido!')
                return render(request, 'servico/editar.html', {'ordem': ordem, 'clientes': Cliente.objects.all()})

            # Salvar as alterações
            ordem.save()
            
            return redirect('assistencia:servicos')

        except Exception as e:
            messages.error(request, f'Erro ao atualizar: {str(e)}')
    
    # GET request - mostrar formulário de edição
    clientes = Cliente.objects.all().order_by('nome')
    situacoes = OrdemDeServico._meta.get_field('situacao').choices
    
    return render(request, 'servico/editar.html', {
        'ordem': ordem,
        'clientes': clientes,
        'situacoes': situacoes
    })

def excluir(request: HttpRequest, id):
    servico = OrdemDeServico.objects.get(id=id)
    if request.method == 'POST':
        servico.delete()
        return redirect('assistencia:servicos')
    return render(request, 'servico/excluir.html', {'servico': servico} )