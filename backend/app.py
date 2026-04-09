from flask import Flask, request, jsonify, send_from_directory
from openai import OpenAI
from dotenv import load_dotenv
import json, os, time

load_dotenv()  # loads .env from project root

BASE_DIR  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND  = os.path.join(BASE_DIR, "frontend")

app = Flask(__name__, static_folder=FRONTEND)

@app.route("/")
def index():
    return send_from_directory(FRONTEND, "index.html")

@app.route("/summarize", methods=["POST"])
def summarize():
    body    = request.get_json()
    text    = (body.get("text") or "").strip()
    api_key = os.getenv("OPENAI_API_KEY", "")  # only from .env now
    model   = body.get("model", "gpt-4o-mini")
    style   = body.get("style", "concise")

    if len(text) < 30:
        return jsonify({"success": False, "error": "Text too short."})
    if not api_key:
        return jsonify({"success": False, "error": "No API key provided."})

    style_map = {
        "concise":  "Write a concise 2-3 sentence summary.",
        "detailed": "Write a detailed 4-6 sentence summary.",
        "bullets":  "Set summary to empty string. Give at least 5 key_points.",
    }

    prompt = f"""Analyze this text and return ONLY valid JSON — no markdown, no extra text:
{{
  "summary": "<paragraph or empty string>",
  "key_points": ["point 1", "point 2", "point 3"],
  "topics": ["topic1", "topic2"],
  "sentiment": "positive" | "neutral" | "negative",
  "word_count": <int>,
  "reading_time": "<N> min read"
}}
Style: {style_map.get(style, style_map["concise"])}

Text:
{text}"""

    try:
        client = OpenAI(api_key=api_key)
        t0     = time.monotonic()
        resp   = client.chat.completions.create(
            model=model,
            temperature=0.3,
            max_tokens=800,
            response_format={"type": "json_object"},
            messages=[{"role": "user", "content": prompt}]
        )
        elapsed_ms = int((time.monotonic() - t0) * 1000)
        data = json.loads(resp.choices[0].message.content)

        return jsonify({
            "success": True,
            "data": {
                "summary":      data.get("summary", ""),
                "key_points":   data.get("key_points", []),
                "topics":       data.get("topics", []),
                "sentiment":    data.get("sentiment", "neutral"),
                "word_count":   data.get("word_count", len(text.split())),
                "reading_time": data.get("reading_time", "—"),
            },
            "model_used": model,
            "elapsed_ms": elapsed_ms,
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


if __name__ == "__main__":
    import webbrowser
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True, port=5000)