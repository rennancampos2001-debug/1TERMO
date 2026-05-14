# Portal de Conteúdo: Curso de Tecnologia e Engenharia de Software

Este repositório centraliza todos os materiais didáticos, planos de aula, códigos-fonte e diretrizes de projetos para as quatro disciplinas principais do curso.

---

## Organização Geral do Repositório

*   `/iot` - Códigos C++/Python, esquemas de circuitos e notas sobre Arduino.
*   `/requisitos` - Modelos de SRS, atas de reuniões e arquivos de protótipo.
*   `/logica-programação` - Exercícios práticos e scripts iniciais em Python.
*   `/sistemas-operacionais` - Guias de laboratório e scripts de terminal (Bash/PowerShell).

---

## 1. Internet das Coisas (IoT)
**Ementa:** Conectividade de dispositivos físicos, eletrônica básica, automação de processos e transmissão de dados em tempo real.

*   **Fundamentos Teóricos:**
    *   Definição e arquitetura física/lógica da internet das coisas.
    *   Fluxo de dados: Sensores -> Microcontroladores -> Gateways -> Nuvem.
    *   Protocolos de rede aplicados: MQTT (padrão M2M), HTTP/REST e WebSockets.
*   **Hardware e Hardware Hacking:**
    *   Placas de desenvolvimento: Arduino Uno, Nano e módulos ESP32 (Wi-Fi integrado).
    *   Eletrônica e pinagem: GPIOs digitais, entradas analógicas (ADC), modulação PWM e barramentos (I2C, SPI).
    *   Componentes de medição: Sensores de temperatura/umidade, presença (PIR) e relés de acionamento.
*   **Abordagem de Programação:**
    *   **C++ (Arduino SDK):** Estruturas `setup()` e `loop()`, manipulação de registradores, interrupções de hardware e eficiência de memória.
    *   **Python (MicroPython):** Interpretador em microcontroladores, controle de tarefas paralelas e integração nativa com Web APIs.

---

## 2. Engenharia de Software: Levantamento de Requisitos
**Ementa:** Métodos, técnicas e ferramentas para descobrir, documentar, analisar e validar as necessidades reais dos usuários do sistema.

*   **Engenharia de Requisitos:**
    *   O ciclo de vida dos requisitos: Elicitação, Análise, Especificação e Gestão de Mudanças.
    *   Diferenciação crítica de escopo:
        *   *Requisitos Funcionais (RF):* Regras de negócio, cálculos, telas e dados do sistema.
        *   *Requisitos Não Funcionais (RNF):* Critérios de performance, segurança (LGPD), usabilidade e portabilidade.
*   **Técnicas de Elicitação e Descoberta:**
    *   *Entrevistas:* Técnicas de condução aberta, fechada e criação de roteiros de perguntas.
    *   *Brainstorming:* Dinâmicas de grupo para extração de ideias sem barreiras iniciais.
    *   *Prototipagem:* Criação de wireframes de baixa fidelidade no papel e protótipos navegáveis de alta fidelidade via Figma.
*   **Documentação e Modelagem Visual:**
    *   Diagramas de Caso de Uso UML (Atores, Casos de Uso, Inclusões e Extensões).
    *   Modelagem de Processos com Diagramas de Fluxo de Dados (DFD).
    *   Escrita técnica: Criação do documento de Especificação de Requisitos de Software (padrão IEEE 830).
    *   Mapeamento ágil: Redação de Histórias de Usuário e Critérios de Aceite.

---

## 3. Lógica de Programação e Versionamento
**Ementa:** Desenvolvimento do raciocínio algorítmico básico usando a linguagem Python e introdução à cultura de controle de versão.

*   **Lógica com Python:**
    *   Sintaxe básica, tipagem dinâmica, entrada (`input`) e saída (`print`) de dados.
    *   Operações matemáticas básicas, operadores lógicos (`and`, `or`, `not`) e relacionais.
    *   Estruturas condicionais aninhadas (`if`, `elif`, `else`).
    *   Estruturas de repetição controladas por loops condicionais e por contagem (`while` e `for`).
    *   Estruturas de dados nativas: Listas, Tuplas e Dicionários.
*   **Versionamento com Git & GitHub:**
    *   Conceitos fundamentais de controle de versão descentralizado.
    *   O ciclo do arquivo no Git: *Untracked*, *Staged*, *Modified* e *Committed*.
    *   **Comandos do Terminal Prático:**
        *   Inicialização e Configuração: `git init`, `git config`
        *   Gerenciamento Local: `git status`, `git add`, `git commit -m`
        *   Trabalho Remoto: `git remote add`, `git push`, `git pull`, `git clone`

---

## 4. Sistemas Operacionais
**Ementa:** Gerenciamento dos recursos de hardware do computador e análise comparativa de usabilidade e arquitetura de mercado.

*   **Conceitos de Kernel e Subsistemas:**
    *   Funções do SO: Gerência de CPU (escalonamento), paginação de memória virtual e sistemas de arquivos.
*   **Microsoft Windows:**
    *   Histórico e Kernel NT, sistema de arquivos padrão NTFS.
    *   Configurações de segurança, permissões de usuário e diretórios de sistema.
    *   Laboratório: Introdução a scripts utilitários com PowerShell e Prompt de Comando.
*   **GNU/Linux:**
    *   O Kernel open-source, filosofia de software livre e ecossistema de distribuições (Debian, Ubuntu).
    *   Sistema de arquivos EXT4, montagem de discos e hierarquia `/bin`, `/etc`, `/var`, `/home`.
    *   Laboratório: Linha de comando avançada (CLI) usando Shell/Bash e comandos `ls`, `cd`, `chmod`, `grep`.
*   **Apple iOS:**
    *   Arquitetura de dispositivos móveis, Kernel XNU e sistema APFS.
    *   O concept estrito de *Sandboxing* para isolamento e segurança de aplicativos.
    *   Otimização de hardware dedicada e restrições de instalação do ecossistema Apple.

---

## Pré-requisitos de Instalação para as Aulas

Antes do início das aulas, certifique-se de instalar as seguintes ferramentas em seu computador:
1.  **Git:** [Instalar Git](https://git-scm.com)
2.  **Python 3.x:** [Instalar Python](https://python.org)
3.  **VS Code:** [Instalar VS Code](https://visualstudio.com)
4.  **Arduino IDE:** [Instalar Arduino IDE](https://arduino.cc)
