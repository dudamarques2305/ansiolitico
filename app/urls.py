from django.urls import path
from . import views

urlpatterns = [
    # Página inicial
    path('', views.home, name='home'),

    # Autenticação
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Pessoa
    path('pessoas/', views.lista_pessoas, name='lista_pessoas'),
    path('pessoas/novo/', views.pessoa_create, name='pessoa_create'),
    path('pessoas/<int:pk>/editar/', views.pessoa_edit, name='pessoa_edit'),
    path('pessoas/<int:pk>/excluir/', views.pessoa_delete, name='pessoa_delete'),

    # Sintoma
    path('sintomas/', views.lista_sintomas, name='lista_sintomas'),
    path('sintomas/novo/', views.sintoma_create, name='sintoma_create'),
    path('sintomas/<int:pk>/editar/', views.sintoma_edit, name='sintoma_edit'),
    path('sintomas/<int:pk>/excluir/', views.sintoma_delete, name='sintoma_delete'),

    # Medicamento
    path('medicamentos/', views.lista_medicamentos, name='lista_medicamentos'),
    path('medicamentos/novo/', views.medicamento_create, name='medicamento_create'),
    path('medicamentos/<int:pk>/editar/', views.medicamento_edit, name='medicamento_edit'),
    path('medicamentos/<int:pk>/excluir/', views.medicamento_delete, name='medicamento_delete'),

    # Cargo
    path('cargos/', views.lista_cargos, name='lista_cargos'),
    path('cargos/novo/', views.cargo_create, name='cargo_create'),
    path('cargos/<int:pk>/editar/', views.cargo_edit, name='cargo_edit'),
    path('cargos/<int:pk>/excluir/', views.cargo_delete, name='cargo_delete'),

    # Instituição de Apoio
    path('instituicoes/', views.lista_instituicoes, name='lista_instituicoes'),
    path('instituicoes/novo/', views.instituicao_create, name='instituicao_create'),
    path('instituicoes/<int:pk>/editar/', views.instituicao_edit, name='instituicao_edit'),
    path('instituicoes/<int:pk>/excluir/', views.instituicao_delete, name='instituicao_delete'),

    # Artigo
    path('artigos/', views.lista_artigos, name='lista_artigos'),
    path('artigos/novo/', views.artigo_create, name='artigo_create'),
    path('artigos/<int:pk>/editar/', views.artigo_edit, name='artigo_edit'),
    path('artigos/<int:pk>/excluir/', views.artigo_delete, name='artigo_delete'),

    # Avaliação de Ansiedade
    path('avaliacoes/', views.lista_avaliacoes, name='lista_avaliacoes'),
    path('avaliacoes/novo/', views.avaliacao_create, name='avaliacao_create'),
    path('avaliacoes/<int:pk>/editar/', views.avaliacao_edit, name='avaliacao_edit'),
    path('avaliacoes/<int:pk>/excluir/', views.avaliacao_delete, name='avaliacao_delete'),

    # Autoavaliação
    path('autoavaliacoes/', views.lista_autoavaliacoes, name='lista_autoavaliacoes'),
    path('autoavaliacoes/novo/', views.autoavaliacao_create, name='autoavaliacao_create'),
    path('autoavaliacoes/<int:pk>/editar/', views.autoavaliacao_edit, name='autoavaliacao_edit'),
    path('autoavaliacoes/<int:pk>/excluir/', views.autoavaliacao_delete, name='autoavaliacao_delete'),

    # Alerta
    path('alertas/', views.lista_alertas, name='lista_alertas'),
    path('alertas/novo/', views.alerta_create, name='alerta_create'),
    path('alertas/<int:pk>/editar/', views.alerta_edit, name='alerta_edit'),
    path('alertas/<int:pk>/excluir/', views.alerta_delete, name='alerta_delete'),

    # Depoimento
    path('depoimentos/', views.lista_depoimentos, name='lista_depoimentos'),
    path('depoimentos/novo/', views.depoimento_create, name='depoimento_create'),
    path('depoimentos/<int:pk>/editar/', views.depoimento_edit, name='depoimento_edit'),
    path('depoimentos/<int:pk>/excluir/', views.depoimento_delete, name='depoimento_delete'),
]
