from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.   
  INICIAR;
Sistema Fisioterapia
//Banco de dados fictício
ListaPacientes = []
Agenda = []
Financeiro = []

ENQUANTO sistema estiver rodando FAÇA
EXIBIR MenuPrincipal()
FIM ENQUANTO

  // ----------------------
  // MENU PRINCIPAL
  FUNÇÃO MenuPrincipal()
  EXIBIR "======== MENU PRINCIPAL ========"
  EXIBIR "1. Agendar Consulta"
  EXIBIR "2. Ver Agenda"
  EXIBIR "3. Planilha Financeira"
  EXIBIR "4. Informações"
  EXIBIR "5. Sair"

  OPÇÃO = LER_INPUT()

  ESCOLHA OPÇÃO
  CASO 1:
CHAMAR AgendarConsulta()
CASO 2:
  CHAMAR VerAgenda()
  CASO 3:
  CHAMAR GerenciarFinanceiro()
    CASO 4:
    CHAMAR Informacoes()
    CASO 5:
    ENCERRAR sistema
      OUTRO:
      EXIBIR "Opção inválida!"
      FIM ESCOLHA
      FIM FUNÇÃO

      // ----------------------
      // AGENDAMENTO DE CONSULTAS
      FUNÇÃO AgendarConsulta()
      EXIBIR "Nome do paciente:"
      nome = LER_INPUT()

      EXIBIR "Data (dd/mm/aaaa):"
      data = LER_INPUT()

      EXIBIR "Horário (hh:mm):"
      hora = LER_INPUT()

      ADICIONAR {nome: nome, data: data, hora: hora} À Agenda
      EXIBIR "Consulta agendada com sucesso!"
      FIM FUNÇÃO

      FUNÇÃO VerAgenda()
      EXIBIR "===== AGENDA ====="
      PARA cada consulta EM Agenda FAÇA
      EXIBIR consulta["data"] + " às " + consulta["hora"] + " - " + consulta["nome"]
      FIM PARA
      FIM FUNÇÃO

      // ----------------------
      // PLANILHA FINANCEIRA
        FUNÇÃO GerenciarFinanceiro()
        EXIBIR "1. Adicionar entrada"
      EXIBIR "2. Adicionar saída"
      EXIBIR "3. Ver saldo"
      OPÇÃO = LER_INPUT()

      ESCOLHA OPÇÃO
      CASO 1:
      EXIBIR "Descrição da entrada:"
        desc = LER_INPUT()
        EXIBIR "Valor R$:"
        valor = LER_INPUT()
        ADICIONAR {tipo: "entrada", descricao: desc, valor: valor} À Financeiro
        EXIBIR "Entrada adicionada."
        CASO 2:
        EXIBIR "Descrição da saída:"
        desc = LER_INPUT()
        EXIBIR "Valor R$:"
        valor = LER_INPUT()
        ADICIONAR {tipo: "saída", descricao: desc, valor: valor} À Financeiro
        EXIBIR "Saída adicionada."
        CASO 3:
        saldo = 0
        PARA cada item EM Financeiro FAÇA
        SE item["tipo"] == "entrada" ENTÃO
      saldo += item["valor"]
      SENÃO
      saldo -= item["valor"]
      FIM PARA
      EXIBIR "Saldo atual: R$" + saldo
      FIM ESCOLHA
      FIM FUNÇÃO

      // ----------------------
      // MENU DE INFORMAÇÕES
      FUNÇÃO Informacoes()
      EXIBIR "====== INFORMAÇÕES ======"
      EXIBIR "Nome: Dra. Ana Clara - Fisioterapeuta"
      EXIBIR "Especialidades: Reabilitação, RPG, Pilates"
      EXIBIR "Endereço: Rua da Saúde, 123 - Centro"
      EXIBIR "Contato: (11) 99999-0000"
      EXIBIR "Horário de atendimento: Seg a Sex, 08:00 - 18:00"
      FIM FUNÇÃO
