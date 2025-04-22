from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("question", "")

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Sei l’assistente di Stefano Malossini e rispondi come un professionista gentile e preparato."},
            {"role": "user", "content": question}
        ],
        max_tokens=100,
        temperature=0.3
    )

    return jsonify({"answer": completion.choices[0].message.content})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
