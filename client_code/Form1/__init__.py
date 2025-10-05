from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.   
  INICIAR
SistemaFisioterapia
Bancodedadosfictício
ListaPacientes = []
Agenda = []
Financeiro = []

ENQUANTOsistemaestiverrodandoFAÇA
EXIBIRMenuPrincipal()
FIMENQUANTO

MENUPRINCIPAL
FUNÇÃOMenuPrincipal()
EXIBIR 
"======== MENU PRINCIPAL ========"
EXIBIR
"1. Agendar Consulta"
EXIBIR
"2. Ver Agenda"
EXIBIR
"3. Planilha Financeira"
EXIBIR
"4. Informações"
EXIBIR
"5. Sair"

OPÇÃO = LER_INPUT()

ESCOLHAOPÇÃO
CASO1:CHAMARAgendarConsulta()
CASO2:CHAMARVerAgenda()
CASO3:CHAMARGerenciarFinanceiro()
CASO4:CHAMARInformacoes()
CASO5:ENCERRARsistema

EXIBIR
"Opção inválida!"
FIMESCOLHA
FIMFUNÇÃO

AGENDAMENTODECONSULTAS
FUNÇÃOAgendarConsulta()
EXIBIR 
"Nome do paciente:"
nome = LER_INPUT()

EXIBIR 
"Data (dd/mm/aaaa):"
data = LER_INPUT()

EXIBIR
"Horário (hh:mm):"
hora = LER_INPUT()

ADICIONAR
{nome: nome, data: data, hora: hora};ÀAgenda
EXIBIR
"Consulta agendada com sucesso!"
FIMFUNÇÃO

FUNÇÃOVerAgenda()
EXIBIR
"===== AGENDA ====="
PARAcadaconsultaEMAgendaFAÇA
EXIBIR
consulta["data"] + " às " + consulta["hora"] + " - " + consulta["nome"]
FIMPARA
FIMFUNÇÃO

PLANILHAFINANCEIRA
FUNÇÃOGerenciarFinanceiro()
EXIBIR 
"1. Adicionar entrada"
EXIBIR 
"2. Adicionar saída"
EXIBIR
"3. Ver saldo"
OPÇÃO = LER_INPUT()

ESCOLHAOPÇÃO
CASO1:EXIBIR
"Descrição da entrada:"
desc = LER_INPUT()
EXIBIR
"Valor R$:"
valor = LER_INPUT()
ADICIONAR
{tipo: "entrada", descricao: desc, valor: valor}; ÀFinanceiro
EXIBIR
"Entrada adicionada."
CASO2:EXIBIR
"Descrição da saída:"
desc = LER_INPUT()
EXIBIR 
"Valor R$:"
valor = LER_INPUT()
ADICIONAR
{tipo: "saída", descricao: desc, valor: valor}; ÀFinanceiro
EXIBIR
"Saída adicionada."
CASO3:saldo = 0
PARAcadaitemEMFinanceiroFAÇA
SEitem["tipo"] == "entrada" 
ENTÃO
saldo += item["valor"]
SENÃO
saldo -= item["valor"]
FIMPARA
EXIBIR 
"Saldo atual: R$" + saldo
FIMESCOLHA
FIMFUNÇÃO

MENUDEINFORMAÇÕES
FUNÇÃOInformacoes()
EXIBIR
"====== INFORMAÇÕES ======"
EXIBIR
"Nome: Dra. Ana Clara - Fisioterapeuta"
EXIBIR
"Especialidades: Reabilitação, RPG, Pilates"
EXIBIR
"Endereço: Rua da Saúde, 123 - Centro"
EXIBIR
"Contato: (11) 99999-0000"
EXIBIR
"Horário de atendimento: Seg a Sex, 08:00 - 18:00"
FIMFUNÇÃO
