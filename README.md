# simulador-fila-torre-controle

## Descrição do Problema

Simular o processamento de pedidos de pouso e decolagem no controle aéreo, aplicando regras de prioridade para emergências e limites de capacidade da pista.

## Requisitos

- Processar uma fila de solicitações com tipo de operação.
- Pedidos de emergência têm prioridade máxima sobre os demais.
- Máximo de 3 aeronaves podem ser atendidas simultaneamente.
- Gerar relatório final com ordem de atendimento e aeronaves recusadas.

## Exemplo de Uso

Entrada: [('F1', 'pouso'), ('F2', 'emergencia'), ('F3', 'decolagem'), ('F4', 'pouso'), ('F5', 'emergencia')]

Saída:

Fila inicial: [('F1', 'pouso'), ('F2', 'emergencia'), ('F3', 'decolagem'), ('F4', 'pouso'), ('F5', 'emergencia')]
Atendido: F2
Atendido: F1
Atendido: F3
Recusado: F4
Recusado: F5