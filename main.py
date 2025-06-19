from flask import Flask, request, jsonify
import openai
import os

openai.api_key = os.getenv("SUA_CHAVE_DA_OPENAI")
app = Flask(__name__)

@app.route('/zapbot', methods=['GET', 'POST'])
def zapbot():
    msg = request.args.get('msg') or request.json.get('message')
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": msg}]
    )
    return jsonify({"reply": resposta['choices'][0]['message']['content']})

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
