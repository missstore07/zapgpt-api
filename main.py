from flask import Flask, request, jsonify
import openai
import os

openai.api_key = os.getenv("SUA_CHAVE_DA_OPENAI")

app = Flask(__name__)

@app.route('/zapbot', methods=['POST'])
def zapbot():
    mensagem = request.json.get('message')
    print("Mensagem recebida:", mensagem)

    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": mensagem}]
    )

    conteudo = resposta['choices'][0]['message']['content']
    print("Resposta gerada:", conteudo)

    return jsonify({"reply": conteudo})

app.run(host="0.0.0.0", port=8080)
