# Notas de Aula: Engenharia de Software - Levantamento de Requisitos

## 1. Conteúdo da Aula
*   **Definição:** Processo de descobrir, analisar, documentar e verificar os serviços e restrições de um sistema.
*   **Importância:** Minimizar falhas no escopo, reduzir custos de retrabalho e alinhar expectativas com o cliente.
*   **Etapas Principais:** Elicitação (descoberta), Análise, Especificação (documentação) e Validação.

---

## 2. Tipos de Requisitos

### Requisitos Funcionais (RF)
*   **O que são:** Declarações de serviços que o sistema deve fornecer ou como ele deve reagir a entradas específicas.
*   **Foco:** Comportamento, funcionalidades e recursos diretos do software.
*   **Exemplos:** 
    *   O sistema deve permitir o cadastro de novos clientes.
    *   O sistema deve emitir um comprovante após a confirmação do pagamento.

### Requisitos Não Funcionais (RNF)
*   **O que são:** Restrições aos serviços ou funções oferecidos pelo sistema.
*   **Foco:** Qualidade, desempenho, segurança, confiabilidade, portabilidade e usabilidade.
*   **Exemplos:**
    *   A página de login deve carregar em menos de 2 segundos.
    *   O sistema deve criptografar todas as senhas dos usuários utilizando SHA-256.

---

## 3. Técnicas de Elicitação de Requisitos

### Entrevistas
*   **Objetivo:** Coleta direta de informações conversando com as partes interessadas (stakeholders).
*   **Tipos:** Estruturadas (perguntas fixas) ou não estruturadas (discussão aberta e flexível).
*   **Vantagem:** Permite entender o contexto geral e a visão individual do usuário sobre o problema.

### Brainstorm
*   **Objetivo:** Reuniões de tempestade de ideias para gerar soluções e identificar necessidades ocultas.
*   **Dinâmica:** Estimular a participação livre de críticas na fase inicial para mapear ideias inovadoras.
*   **Vantagem:** Excelente para definição de escopo inicial e alinhamento de equipes multidisciplinares.

### Prototipagem
*   **Objetivo:** Construir maquetes visuais do software para que os usuários validem o fluxo antes do código.
*   **Níveis de Fidelidade:**
    *   **Baixa Fidelidade:** Desenhos em papel (wireframes) para validar ideias rapidamente.
    *   **Alta Fidelidade:** Telas interativas (Figma, Adobe XD) simulando o comportamento real do app.
*   **Vantagem:** Reduz erros de interpretação visual e lógica entre cliente e desenvolvedor.

---

## 4. Documentação e Modelagem

### Diagramas (Modelagem Visual)
*   **Diagrama de Casos de Uso (UML):** Mostra as interações entre os atores (usuários/sistemas externos) e as funcionalidades principais.
*   **Diagrama de Fluxo de Dados (DFD):** Mapeia o caminho e as transformações que os dados sofrem dentro do sistema.
*   **Histórias de Usuário (User Stories):** Abordagem ágil no formato: *"Como [tipo de usuário], eu quero [objetivo] para que possa [benefício]"*.

### Relatórios Técnicos
*   **Documento de Especificação de Requisitos de Software (SRS):** O contrato técnico oficial contendo a descrição detalhada do sistema.
*   **Estrutura Padrão:**
    1.  Introdução (Escopo e Objetivos).
    2.  Descrição Geral (Perspectiva do produto e restrições).
    3.  Requisitos Específicos (Listagem codificada de RFs e RNFs).
*   **Matriz de Rastreabilidade:** Tabela que conecta cada requisito à sua origem, código e caso de teste correspondente.
