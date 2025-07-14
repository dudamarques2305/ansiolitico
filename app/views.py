from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib import messages

from .models import *
from .forms import *
from .forms import PessoaForm, UsuarioForm

# ------------------------
# Página inicial
# ------------------------

@login_required
def home(request):
    return render(request, 'home.html', {
        'num_pessoas': Pessoa.objects.count(),
        'num_sintomas': Sintoma.objects.count(),
        'num_medicamentos': Medicamento.objects.count(),
        'num_cargos': Cargo.objects.count(),
        'num_instituicoes': InstituicaoApoio.objects.count(),
        'num_artigos': Artigo.objects.count(),
        'num_avaliacoes': AvaliacaoAnsiedade.objects.count(),
        'num_autoavaliacoes': AutoAvaliacao.objects.count(),
        'num_alertas': Alerta.objects.count(),
        'num_depoimentos': Depoimento.objects.count(),
    })

# ------------------------
# Autenticação
# ------------------------

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(request.GET.get('next', 'home'))
        else:
            messages.error(request, 'Usuário ou senha inválidos')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# ------------------------
# CRUD Pessoa
# ------------------------

@login_required
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoas.html', {'pessoas': pessoas})

@login_required
def pessoa_create(request):
    if request.method == 'POST':
        u_form = UsuarioForm(request.POST)
        p_form = PessoaForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            usuario = u_form.save(commit=False)
            usuario.set_password(u_form.cleaned_data['password'])
            usuario.save()

            pessoa = p_form.save(commit=False)
            pessoa.usuario = usuario
            pessoa.save()

            return redirect('lista_pessoas')
    else:
        u_form = UsuarioForm()
        p_form = PessoaForm()
    return render(request, 'pessoa_form.html', {
        'u_form': u_form,
        'form': p_form,
        'acao': 'Cadastrar'
    })
@login_required
def pessoa_edit(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    form = PessoaForm(request.POST or None, instance=pessoa)
    if form.is_valid():
        pessoa = form.save(commit=False)
        nova_senha = form.cleaned_data['senha']
        if nova_senha != pessoa.senha:
            pessoa.senha = make_password(nova_senha)
        pessoa.save()
        return redirect('lista_pessoas')
    return render(request, 'pessoa_form.html', {'form': form, 'acao': 'Editar'})

@login_required
def pessoa_delete(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('lista_pessoas')
    return render(request, 'pessoa_confirm_delete.html', {'pessoa': pessoa})

# ------------------------
# CRUD Sintoma
# ------------------------

@login_required
def lista_sintomas(request):
    sintomas = Sintoma.objects.all()
    return render(request, 'sintomas.html', {'sintomas': sintomas})

@login_required
def sintoma_create(request):
    form = SintomaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_sintomas')
    return render(request, 'sintoma_form.html', {'form': form, 'acao': 'Cadastrar'})

@login_required
def sintoma_edit(request, pk):
    sintoma = get_object_or_404(Sintoma, pk=pk)
    form = SintomaForm(request.POST or None, instance=sintoma)
    if form.is_valid():
        form.save()
        return redirect('lista_sintomas')
    return render(request, 'sintoma_form.html', {'form': form, 'acao': 'Editar'})

@login_required
def sintoma_delete(request, pk):
    sintoma = get_object_or_404(Sintoma, pk=pk)
    if request.method == 'POST':
        sintoma.delete()
        return redirect('lista_sintomas')
    return render(request, 'sintoma_confirm_delete.html', {'sintoma': sintoma})

# ------------------------
# CRUD Medicamento
# ------------------------

@login_required
def lista_medicamentos(request):
    medicamentos = Medicamento.objects.all()
    return render(request, 'medicamentos.html', {'medicamentos': medicamentos})

@login_required
def medicamento_create(request):
    form = MedicamentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_medicamentos')
    return render(request, 'medicamento_form.html', {'form': form, 'acao': 'Cadastrar'})

@login_required
def medicamento_edit(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    form = MedicamentoForm(request.POST or None, instance=medicamento)
    if form.is_valid():
        form.save()
        return redirect('lista_medicamentos')
    return render(request, 'medicamento_form.html', {'form': form, 'acao': 'Editar'})

@login_required
def medicamento_delete(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    if request.method == 'POST':
        medicamento.delete()
        return redirect('lista_medicamentos')
    return render(request, 'medicamento_confirm_delete.html', {'medicamento': medicamento})

# ------------------------
# CRUD Cargo
# ------------------------

@login_required
def lista_cargos(request):
    cargos = Cargo.objects.all()
    return render(request, 'cargos.html', {'cargos': cargos})

@login_required
def cargo_create(request):
    form = CargoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_cargos')
    return render(request, 'cargo_form.html', {'form': form, 'acao': 'Cadastrar'})

@login_required
def cargo_edit(request, pk):
    cargo = get_object_or_404(Cargo, pk=pk)
    form = CargoForm(request.POST or None, instance=cargo)
    if form.is_valid():
        form.save()
        return redirect('lista_cargos')
    return render(request, 'cargo_form.html', {'form': form, 'acao': 'Editar'})

@login_required
def cargo_delete(request, pk):
    cargo = get_object_or_404(Cargo, pk=pk)
    if request.method == 'POST':
        cargo.delete()
        return redirect('lista_cargos')
    return render(request, 'cargo_confirm_delete.html', {'cargo': cargo})

# ------------------------
# CRUD Instituicao de Apoio
# ------------------------

@login_required
def lista_instituicoes(request):
    instituicoes = InstituicaoApoio.objects.all()
    return render(request, 'instituicoes.html', {'instituicoes': instituicoes})

@login_required
def instituicao_create(request):
    form = InstituicaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_instituicoes')
    return render(request, 'instituicao_form.html', {'form': form, 'acao': 'Cadastrar'})

@login_required
def instituicao_edit(request, pk):
    instituicao = get_object_or_404(InstituicaoApoio, pk=pk)
    form = InstituicaoForm(request.POST or None, instance=instituicao)
    if form.is_valid():
        form.save()
        return redirect('lista_instituicoes')
    return render(request, 'instituicao_form.html', {'form': form, 'acao': 'Editar'})

@login_required
def instituicao_delete(request, pk):
    instituicao = get_object_or_404(InstituicaoApoio, pk=pk)
    if request.method == 'POST':
        instituicao.delete()
        return redirect('lista_instituicoes')
    return render(request, 'instituicao_confirm_delete.html', {'instituicao': instituicao})

# ------------------------
# CRUD Artigo
# ------------------------

@login_required
def lista_artigos(request):
    artigos = Artigo.objects.all()
    return render(request, 'artigos.html', {'artigos': artigos})

@login_required
def artigo_create(request):
    form = ArtigoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_artigos')
    return render(request, 'artigo_form.html', {'form': form, 'acao': 'Cadastrar'})

@login_required
def artigo_edit(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    form = ArtigoForm(request.POST or None, instance=artigo)
    if form.is_valid():
        form.save()
        return redirect('lista_artigos')
    return render(request, 'artigo_form.html', {'form': form, 'acao': 'Editar'})

@login_required
def artigo_delete(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    if request.method == 'POST':
        artigo.delete()
        return redirect('lista_artigos')
    return render(request, 'artigo_confirm_delete.html', {'artigo': artigo})

# ------------------------
# CRUD Avaliacao de Ansiedade
# ------------------------

@login_required
def lista_avaliacoes(request):
    avaliacoes = AvaliacaoAnsiedade.objects.all()
    return render(request, 'avaliacoes.html', {'avaliacoes': avaliacoes})

@login_required
def avaliacao_create(request):
    form = AvaliacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_avaliacoes')
    return render(request, 'avaliacao_form.html', {'form': form, 'acao': 'Cadastrar'})

@login_required
def avaliacao_edit(request, pk):
    avaliacao = get_object_or_404(AvaliacaoAnsiedade, pk=pk)
    form = AvaliacaoForm(request.POST or None, instance=avaliacao)
    if form.is_valid():
        form.save()
        return redirect('lista_avaliacoes')
    return render(request, 'avaliacao_form.html', {'form': form, 'acao': 'Editar'})

@login_required
def avaliacao_delete(request, pk):
    avaliacao = get_object_or_404(AvaliacaoAnsiedade, pk=pk)
    if request.method == 'POST':
        avaliacao.delete()
        return redirect('lista_avaliacoes')
    return render(request, 'avaliacao_confirm_delete.html', {'avaliacao': avaliacao})


@login_required
def lista_autoavaliacoes(request):
    autoavaliacoes = AutoAvaliacao.objects.all()
    return render(request, 'autoavaliacoes.html', {'autoavaliacoes': autoavaliacoes})

@login_required
def autoavaliacao_create(request):
    form = AutoAvaliacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_autoavaliacoes')
    return render(request, 'autoavaliacao_form.html', {'form': form, 'acao': 'Cadastrar'})

@login_required
def autoavaliacao_edit(request, pk):
    autoavaliacao = get_object_or_404(AutoAvaliacao, pk=pk)
    form = AutoAvaliacaoForm(request.POST or None, instance=autoavaliacao)
    if form.is_valid():
        form.save()
        return redirect('lista_autoavaliacoes')
    return render(request, 'autoavaliacao_form.html', {'form': form, 'acao': 'Editar'})

@login_required
def autoavaliacao_delete(request, pk):
    autoavaliacao = get_object_or_404(AutoAvaliacao, pk=pk)
    if request.method == 'POST':
        autoavaliacao.delete()
        return redirect('lista_autoavaliacoes')
    return render(request, 'autoavaliacao_confirm_delete.html', {'autoavaliacao': autoavaliacao})

@login_required
def lista_alertas(request):
    alertas = Alerta.objects.all()
    return render(request, 'alertas.html', {'alertas': alertas})

@login_required
def alerta_create(request):
    form = AlertaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_alertas')
    return render(request, 'alerta_form.html', {'form': form, 'acao': 'Cadastrar'})

@login_required
def alerta_edit(request, pk):
    alerta = get_object_or_404(Alerta, pk=pk)
    form = AlertaForm(request.POST or None, instance=alerta)
    if form.is_valid():
        form.save()
        return redirect('lista_alertas')
    return render(request, 'alerta_form.html', {'form': form, 'acao': 'Editar'})

@login_required
def alerta_delete(request, pk):
    alerta = get_object_or_404(Alerta, pk=pk)
    if request.method == 'POST':
        alerta.delete()
        return redirect('lista_alertas')
    return render(request, 'alerta_confirm_delete.html', {'alerta': alerta})

@login_required
def lista_depoimentos(request):
    depoimentos = Depoimento.objects.all()
    return render(request, 'depoimentos.html', {'depoimentos': depoimentos})

@login_required
def depoimento_create(request):
    form = DepoimentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_depoimentos')
    return render(request, 'depoimento_form.html', {'form': form, 'acao': 'Cadastrar'})

@login_required
def depoimento_edit(request, pk):
    depoimento = get_object_or_404(Depoimento, pk=pk)
    form = DepoimentoForm(request.POST or None, instance=depoimento)
    if form.is_valid():
        form.save()
        return redirect('lista_depoimentos')
    return render(request, 'depoimento_form.html', {'form': form, 'acao': 'Editar'})

@login_required
def depoimento_delete(request, pk):
    depoimento = get_object_or_404(Depoimento, pk=pk)
    if request.method == 'POST':
        depoimento.delete()
        return redirect('lista_depoimentos')
    return render(request, 'depoimento_confirm_delete.html', {'depoimento': depoimento})
