from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/zapbot", methods=["POST"])
def zapbot():
    user_msg = request.json.get("message")

    if not user_msg:
        return jsonify({"reply": "Nenhuma mensagem recebida."})

    try:
        # Chamada ao GPT gratuito via proxy (modelo openrouter gratuito)
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": "Bearer sk-demo",  # token demo gratuito
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-3.5-turbo",
                "messages": [{"role": "user", "content": user_msg}]
            }
        )
        result = response.json()
        reply = result["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"Erro ao consultar GPT: {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
