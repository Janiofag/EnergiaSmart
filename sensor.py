import time
import random
import paho.mqtt.client as mqtt

# Configurações do MQTT
broker = "localhost"  # Endereço do broker MQTT
port = 1883           # Porta do broker MQTT
topic = "fabrica/energia"

# Função para enviar dados para o broker MQTT
def publish_data(client):
    while True:
        # Simula a leitura de dados do sensor
        consumo_energia = random.uniform(10.0, 100.0)
        # Publica o dado no tópico MQTT
        client.publish(topic, f"Consumo de energia: {consumo_energia:.2f} kWh")
        print(f"Enviado: {consumo_energia:.2f} kWh")
        time.sleep(5)  # Espera 5 segundos antes de enviar o próximo dado

# Configura o cliente MQTT
client = mqtt.Client()
client.connect(broker, port, 60)

# Publica dados continuamente
publish_data(client)
