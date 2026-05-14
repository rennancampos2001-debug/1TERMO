# Notas de Aula: Introdução à Internet das Coisas (IoT)

## 1. Conteúdo da Aula
*   **Conceito de IoT:** Conexão de objetos físicos à internet para coleta e troca de dados.
*   **Arquitetura Básica:** Sensores (coleta), Atuadores (ação), Microcontroladores (processamento) e Nuvem (armazenamento).
*   **Protocolos de Comunicação:** Introdução ao MQTT, HTTP e WebSockets para transmissão de dados.
*   **Aplicações Práticas:** Automação residencial, cidades inteligentes e monitoramento industrial.

---

## 2. Ecossistema Arduino
*   **Hardware:** Placa de prototipagem eletrônica de código aberto com pinos digitais e analógicos.
*   **Componentes Essenciais:** Sensores (presença, temperatura, luz) e Atuadores (LEDs, relés, motores).
*   **Ambiente de Desenvolvimento:** Uso da Arduino IDE para escrever, compilar e transferir o código para a placa.
*   **Fluxo de Trabalho:** Conexão via USB, configuração da porta COM e upload do firmware.

---

## 3. Programação para IoT: C++ vs. Python

### Linguagem C++ (Foco em Hardware e Performance)
*   **Uso principal:** Programação direta no microcontrolador (Arduino).
*   **Vantagens:** Alta velocidade, baixo consumo de memória e controle total dos pinos de hardware.
*   **Estrutura do Código:** Dividido estritamente em duas funções principais:
    *   `setup()`: Executa uma vez para configurar os pinos.
    *   `loop()`: Executa repetidamente para rodar a lógica do circuito.

```cpp
// Exemplo de código C++ para Arduino (Piscar LED)
const int ledPin = 13;

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  digitalWrite(ledPin, HIGH);
  delay(1000);
  digitalWrite(ledPin, LOW);
  delay(1000);
}
```

### Linguagem Python (Foco em Integração e Análise de Dados)
*   **Uso principal:** Execução em microcomputadores (Raspberry Pi) ou gateways de IoT.
*   **MicroPython:** Versão otimizada do Python para rodar diretamente em microcontroladores modernos como ESP32.
*   **Vantagens:** Sintaxe limpa, desenvolvimento rápido e bibliotecas prontas para conectar com servidores e APIs.

```python
# Exemplo de código Python/MicroPython (Piscar LED)
import machine
import time

led = machine.Pin(2, machine.Pin.OUT)

while True:
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)
```

---

## 4. Comparativo de Papéis no Projeto IoT
*   **C++:** Coleta os dados do sensor bruto e controla os componentes físicos localmente.
*   **Python:** Recebe esses dados, processa, gera gráficos e envia para bancos de dados na nuvem.
