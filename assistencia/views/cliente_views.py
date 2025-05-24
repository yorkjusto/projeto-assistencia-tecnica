from django.http import HttpRequest
from django.shortcuts import redirect, render, get_object_or_404
from assistencia.models.cliente import Cliente
from django.contrib import messages

def lista_clientes(request:HttpRequest):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/lista_clientes.html', {'clientes':clientes} )

def adicionar_cliente(request:HttpRequest):
    if request.method == 'POST':
        # Coletando dos do formulário
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        morada = request.POST.get('morada')
        email = request.POST.get('email')

        # Criar o cliente
        Cliente.objects.create(
            nome=nome,
            telefone=telefone,
            morada=morada,
            email=email,
        )
        return redirect('assistencia:clientes')
    return render(request, 'cliente/cadastrar.html')

def editar_cliente(request:HttpRequest, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        # Coletando dados do formulário
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        morada = request.POST.get('morada')
        email = request.POST.get('email')

        # Atualizando
        cliente.nome = nome
        cliente.telefone = telefone
        cliente.morada = morada
        cliente.email = email
        cliente.save()
        return redirect('assistencia:clientes')
    return render(request, 'cliente/editar.html', {'cliente': cliente} )

def excluir_cliente(request: HttpRequest, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('assistencia:clientes')
    return render(request, 'cliente/excluir.html', {'cliente': cliente} )