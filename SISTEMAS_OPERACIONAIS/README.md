# Notas de Aula: Sistemas Operacionais (SO)

## 1. Introdução aos Sistemas Operacionais
*   **Definição:** Software que gerencia o hardware e atua como intermediário entre o usuário e as aplicações.
*   **Funções Principais:** Gerenciamento de processos, administração de memória, controle de arquivos e segurança de dados.

---

## 2. Microsoft Windows (Foco em Desktop e Mercado Corporativo)
*   **Arquitetura:** Baseada no núcleo (kernel) NT, utilizando sistemas de arquivos como **NTFS** e **FAT32**.
*   **Modelo de Código:** Código fechado (proprietário), mantido e licenciado exclusivamente pela Microsoft.
*   **Interface e Usabilidade:** Interface Gráfica do Usuário (GUI) padronizada e forte compatibilidade com softwares de terceiros e jogos.
*   **Gerenciamento de Linha de Comando:** Uso do *Prompt de Comando* (CMD) clássico e do *PowerShell* para automação avançada.

---

## 3. Linux (Foco em Servidores, Desenvolvimento e Customização)
*   **Arquitetura:** Baseada no kernel Linux, utilizando sistemas de arquivos como **EXT4**.
*   **Modelo de Código:** Código aberto (*open-source*), permitindo modificação, auditoria e distribuição livre.
*   **Distribuições (Distros):** Variações criadas para públicos específicos, como **Ubuntu** (iniciantes), **Debian** (servidores) e **Arch Linux** (usuários avançados).
*   **Terminal e Shell:** Centralizado na CLI (Interface de Linha de Comando). Uso extensivo do interpretador *Bash* para administração de sistemas.
*   **Comandos Essenciais:**
    *   `ls`: Lista arquivos do diretório.
    *   `cd`: Altera a pasta atual.
    *   `mkdir`: Cria novas pastas.

---

## 4. Apple iOS (Foco em Dispositivos Móveis e Ecossistema Fechado)
*   **Arquitetura:** Baseada no kernel *XNU* (derivado do Unix/BSD), utilizando o sistema de arquivos **APFS**.
*   **Modelo de Código:** Código fechado, projetado estritamente para funcionar no hardware proprietário da Apple (iPhone).
*   **Segurança e Sandboxing:** Cada aplicativo roda isolado em seu próprio ambiente protegido para evitar vírus e vazamento de dados.
*   **Otimização:** Integração vertical profunda entre hardware e software, garantindo alto desempenho com menor consumo de bateria.

---

## 5. Matriz Comparativa de Arquiteturas


| Característica | Microsoft Windows | Linux | Apple iOS |
| :--- | :--- | :--- | :--- |
| **Tipo de Kernel** | Híbrido (NT) | Monolítico | Híbrido (XNU) |
| **Licença** | Proprietária | Código Aberto | Proprietária |
| **Plataforma Alvo** | Desktops e Servidores | Servidores e Sistemas Embarcados | Dispositivos Móveis (iPhone) |
| **Interface Padrão** | GUI Gráfica | CLI Terminal / GUI Opcional | Multi-touch GUI |
