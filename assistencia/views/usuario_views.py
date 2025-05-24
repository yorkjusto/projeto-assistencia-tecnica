from django.http import HttpRequest
from django.shortcuts import redirect, render, get_object_or_404
from assistencia.models.usuario import Usuario
from django.contrib import messages
from django.db import IntegrityError


# Listar usuários
def lista_usuarios(request: HttpRequest):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/lista_usuarios.html', {'usuarios': usuarios} )

# Cadastrar usuário

def cadastrar(request: HttpRequest):
    context = {} 
    if request.method == 'POST':
        # Coletando dados do formulário
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        login = request.POST.get('login')
        perfil = request.POST.get('perfil')
        senha = request.POST.get('senha')

        try:
            # Cria o usuário
            Usuario.objects.create(
                    nome=nome,
                    telefone=telefone,
                    login=login,
                    perfil=perfil,
                    senha=senha)
            return redirect('assistencia:usuarios')
        except IntegrityError:
            messages.error(request, 'Este login já está  em uso. Por favor escolha outro.')

            # Mantém os dados no formulário para não perder o que o usuário digitou
        context = {
                'nome': nome,
                'telefone': telefone,
                'login': login,
                'perfil': perfil,
                'senha': senha,
            }
        return render(request, 'usuario/cadastrar.html', {'context': context} )
    
    # Se for GET ou se houver erro de validação
    return render(request, 'usuario/cadastrar.html')

# Editar usuário
def editar(request: HttpRequest, id):
    usuario = get_object_or_404(Usuario, id=id)
    
    if request.method == 'POST':
        # Coleta dados do formulário
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        login = request.POST.get('login')
        perfil = request.POST.get('perfil')
        senha = request.POST.get('senha')
        
        try:
            # Atualiza os dados
            usuario.nome = nome
            usuario.telefone = telefone
            usuario.login = login
            usuario.perfil = perfil
            usuario.senha = senha
            usuario.save()    
            return redirect('assistencia:usuarios')
        
        except IntegrityError:
            messages.error(request, 'Este login já está em uso por outro usuário.')
            # Retorna para a página de edição com os dados
            context = {
                'usuario': usuario,
                'error': True
            }
            return render(request, 'usuario/editar.html', context)
    
    # Se for GET
    return render(request, 'usuario/editar.html', {'usuario': usuario})

# Excluir usuário
def eliminar(request:HttpRequest, id):
    usuario = Usuario.objects.get(id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('assistencia:usuarios')
    
    return render(request, 'usuario/excluir.html', {'usuario': usuario})