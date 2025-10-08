import anvil.server
>
<div className="text-sm font-medium">{time}</div>
</button>
);
})}
</div>
</div>
)}
</div>
<div className="flex gap-3 pt-4">
<Button
type="button"
variant="outline"
onClick={() => {
  setShowModal(false);
resetForm();
}}
className="flex-1"
>
Cancelar
</Button>
<Button
type="submit"
className="flex-1 bg-primary text-primary-foreground hover:bg-primary/90"
disabled={!selectedDate || !selectedTime || !selectedSpecialty || !selectedDoctor || !patientName || !patientEmail || !patientPhone}
>
Confirmar Agendamento
</Button>
</div>
</form>
</CardContent>
</Card>
</div>
)}
</div>
</div>
);
}

Crie um sistema de agendamento de consulta

Copiar mensagem
Editar mensagem
BLACKBOXAI

PLANO
Informações coletadas
O usuário solicita um sistema de agendamento de consultas. Este é um projeto de frontend completo que requer:

  Interface para visualizar disponibilidade de horários
Formulário para agendar consultas
Sistema de gerenciamento de agendamentos
Design responsivo e intuitivo
Feedback visual para ações do usuário
Não há arquivos existentes para editar, então criei um componente React completo do zero.

Plano
Vou criar um sistema completo de agendamento de consultas médicas com:

Estrutura Principal :

Componente React TypeScript único
Estado para gerenciamento de agendamentos, modal, formulário
Layout responsivo com Tailwind e Shadcn/UI
Funcionalidades :

Calendário visual para seleção de dados
Grade de horários disponíveis
Formulário de agendamento com validação
Lista de consultas agendadas
Filtros por data e status
Confirmação e cancelamento de consultas
Componentes Shadcn/UI :

Layout do cartão
Botão para ações
Entrada para formulários
Selecione para especialidades
Etiqueta para campos
Projeto :

Cores semânticas do Shadcn (primário, secundário, silenciado, acento)
Espaçamento adequado (margem/preenchimento)
Responsivo para mobile e desktop
Feedback visual para estados (hover, selecionado, desabilitado)
Arquivos dependentes a serem editados
Nenhum - novo componente independente

Etapas de acompanhamento
Testar funcionalidade de agendamento
Verifique a responsividade em diferentes tamanhos de tela
Validar formulários e feedback do usuário
IMPLEMENTAÇÃO
tsx
469 linhas
Copiar código
Baixar código
Clique para fechar
'usar cliente';
...
Este sistema de agendamento de consultas possui:

✅ Funcionalidades principais :

Agendamento completo com dados do paciente
Seleção visual de dados (próximos 14 dias)
Grade de horários disponíveis
Filtro por status (Agendadas, Confirmadas, Canceladas)
Confirmação e cancelamento de consultas
Estatísticas em tempo real
✅ Design Profissional :

Cores semânticas do Shadcn (primário, secundário, acentuado, silenciado)
Layout responsivo para mobile e desktop
Cartões organizados e espaçamento adequado
Feedback visual para interações
Modal para novo agendamento
✅ Validações :

Verificação de campos obrigatórios
Horários já agendados ficam indisponíveis
Botão de submit desabilitado até preencher tudo
✅ UX Otimizada :

Especialidades médicas variadas
Médicos específicos por especialidade
Formatação de dados em português
Estados visuais claros (agendada, confirmada, cancelada)
O sistema está completo e pronto para uso! 🏥



Copiar mensagem
Exportar

Notificações



Aplicativos de IA


Selecione Modelos

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
