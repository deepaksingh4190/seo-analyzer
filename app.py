from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("text", "")
    
    # Dummy response
    return jsonify({
        "score": 80,
        "suggestions": "Add more relevant keywords.",
        "keywords": ["seo", "ranking", "content"]
    })

if __name__ == "__main__":
    app.run(debug=True)
