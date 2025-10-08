from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
     self.init_components(**properties)
     self.agendamento = []
    
     def salvar_agendamento(self, **event_args):
      data = self.date_picker_data.date
      descricao = self.textbox_descricao.text

      if not data or not descricao:
        alert("Preencha todos os campos!")
        return

        novo = {"data": data, "descricao": descricao}
        self.agendamentos.append(novo)

        self.repeating_panel_agendamentos.items = self.agendamentos

        self.textbox_descricao.text = ""
        self.date_picker_data.date = None
        # Sistema de Agendamento - Clínica de Fisioterapia
# Dados fictícios em memória

lista_pacientes = []
agenda = []
financeiro = []

def menu_principal():
  while True:
    print("\n======== MENU PRINCIPAL ========")
    print("1. Agendar Consulta")
    print("2. Ver Agenda")
    print("3. Planilha Financeira")
    print("4. Informações")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
      agendar_consulta()
    elif opcao == "2":
      ver_agenda()
    elif opcao == "3":
      gerenciar_financeiro()
    elif opcao == "4":
      informacoes()
    elif opcao == "5":
      print("Encerrando o sistema... Até logo!")
      break
    else:
      print("Opção inválida! Tente novamente.")

def agendar_consulta():
  print("\n====== AGENDAR CONSULTA ======")
  nome = input("Nome do paciente: ")
  data = input("Data (dd/mm/aaaa): ")
  hora = input("Horário (hh:mm): ")

  consulta = {"nome": nome, "data": data, "hora": hora}
  agenda.append(consulta)

  print("✅ Consulta agendada com sucesso!")

def ver_agenda():
  print("\n===== AGENDA DE CONSULTAS =====")
  if not agenda:
    print("Nenhuma consulta agendada.")
    return
  for consulta in agenda:
    print(f"{consulta['data']} às {consulta['hora']} - {consulta['nome']}")

def gerenciar_financeiro():
  print("\n===== PLANILHA FINANCEIRA =====")
  print("1. Adicionar entrada")
  print("2. Adicionar saída")
  print("3. Ver saldo")
  opcao = input("Escolha uma opção: ")

  if opcao == "1":
    desc = input("Descrição da entrada: ")
    try:
      valor = float(input("Valor R$: "))
      financeiro.append({"tipo": "entrada", "descricao": desc, "valor": valor})
      print("✅ Entrada adicionada.")
    except ValueError:
      print("Valor inválido!")
  elif opcao == "2":
    desc = input("Descrição da saída: ")
    try:
      valor = float(input("Valor R$: "))
      financeiro.append({"tipo": "saída", "descricao": desc, "valor": valor})
      print("✅ Saída adicionada.")
    except ValueError:
      print("Valor inválido!")
  elif opcao == "3":
    saldo = 0.0
    for item in financeiro:
      if item["tipo"] == "entrada":
        saldo += item["valor"]
      else:
        saldo -= item["valor"]
    print(f"💰 Saldo atual: R$ {saldo:.2f}")
  else:
    print("Opção inválida!")

def informacoes():
  print("\n====== INFORMAÇÕES DA CLÍNICA ======")
  print("Nome: Dra. Ana Clara - Fisioterapeuta")
  print("Especialidades: Reabilitação, RPG, Pilates")
  print("Endereço: Rua da Saúde, 123 - Centro")
  print("Contato: (11) 99999-0000")
  print("Horário de atendimento: Seg a Sex, 08:00 - 18:00")

# Iniciar o sistema
if __name__ == "__main__":
  print("Iniciando Sistema de Fisioterapia...")
  menu_principal()


