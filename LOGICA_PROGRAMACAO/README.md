# Notas de Aula: Lógica de Programação com Python e Versionamento

## 1. Introdução à Lógica com Python
*   **O que é Lógica:** Organização coerente de instruções para resolver problemas através de algoritmos.
*   **Por que Python:** Sintaxe limpa, parecida com inglês, ideal para iniciantes focarem na lógica, não nas regras da linguagem.
*   **Variáveis e Tipos:** Espaços na memória para guardar textos (`str`), inteiros (`int`), decimais (`float`) e booleanos (`bool`).
*   **Operadores:** Matemáticos (`+`, `-`, `*`, `/`) e Comparativos (`>`, `<`, `==`, `!=`).

---

## 2. Estruturas Fundamentais em Python

### Condicionais (Tomada de Decisão)
*   Permitem que o programa siga caminhos diferentes com base em uma condição verdadeira ou falsa.

```python
# Exemplo de Condicional (IF/ELSE)
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

### Repetição (Loops)
*   Evitam a repetição manual de código executando blocos de instruções várias vezes.

```python
# Exemplo de Repetição (FOR) para contar até 3
for contador in range(1, 4):
    print(f"Número: {contador}")
```

---

## 3. Versionamento com Git e GitHub

### O que é o Git?
*   Sistema de controle de versão para rastrear modificações no histórico do código fonte.
*   Funciona localmente no computador do desenvolvedor.

### O que é o GitHub?
*   Plataforma online que hospeda repositórios Git na nuvem.
*   Permite o trabalho em equipe, compartilhamento de códigos e criação de portfólio.

---

## 4. Fluxo de Trabalho Essencial (Terminal)

### Configuração Inicial
*   `git init`: Transforma a pasta atual em um repositório Git local.
*   `git remote add origin [URL]`: Vincula o repositório local ao projeto criado no GitHub.

### Ciclo de Envio de Código
*   `git status`: Verifica quais arquivos foram alterados ou criados.
*   `git add .`: Salva as modificações na área de preparação (Stage).
*   `git commit -m "Mensagem"`: Grava as alterações localmente com uma justificativa.
*   `git push origin main`: Envia os commits locais para o servidor do GitHub.
