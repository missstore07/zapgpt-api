from flask import Flask, request, jsonify
import openai
import os

openai.api_key = os.getenv("SUA_CHAVE_DA_OPENAI")

app = Flask(__name__)

@app.route('/zapbot', methods=['POST'])
def zapbot():
    mensagem = request.json.get('message')
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": mensagem}]
    )
    return jsonify({"reply": resposta['choices'][0]['message']['content']})

app.run(host="0.0.0.0", port=8080)
