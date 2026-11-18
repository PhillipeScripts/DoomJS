import os
from flask import Flask, request, jsonify
from google import genai

app = Flask(__name__)

# Inicializa o SDK do Gemini usando automaticamente a chave do Render
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

@app.route("/")
def home():
    return "🤖 The Gemini API is online and running perfectly!"

@app.route("/perguntar", methods=["POST"])
def perguntar():
    dados = request.get_json()
    mensagem = dados.get("mensagem", "")
    
    if not mensagem:
        return jsonify({"erro": "No message provided."}), 400

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=mensagem,
        )
        return jsonify({"resposta": response.text})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
  
