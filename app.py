from flask import Flask, render_template
import paho.mqtt.client as mqtt

app = Flask(__name__)

# Variável global para armazenar o último valor recebido
latest_data = "Nenhum dado recebido ainda."

# Função callback quando uma nova mensagem chega
def on_message(client, userdata, message):
    global latest_data
    latest_data = message.payload.decode()

# Configura o cliente MQTT
mqtt_client = mqtt.Client()
mqtt_client.on_message = on_message
mqtt_client.connect("localhost", 1883, 60)
mqtt_client.subscribe("fabrica/energia")
mqtt_client.loop_start()

@app.route('/')
def index():
    return render_template('index.html', data=latest_data)

if __name__ == '__main__':
    app.run(debug=True)
