import webbrowser
from flask import Flask, render_template, request, jsonify
from g4f.client import Client
import threading

app = Flask(__name__)
client = Client()

bot_name = ""
company_name = ""

def set_bot_name(name):
    global bot_name
    bot_name = name

def set_company_name(name):
    global company_name
    company_name = name

@app.route('/')
def index():
    return render_template('index.html', bot_name=bot_name)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    behaviour = request.json.get('behaviour')

    if not user_message or not behaviour:
        return jsonify({"response": "Invalid input."}), 400

    content = (
        f"Follow the below commands strictly {user_message} "
        f"and behave very strongly like {behaviour} "
        f"as I am a/an {behaviour} type person. If asked questions about yourself, "
        f"introduce yourself as {bot_name} from {company_name}, "
        f"which is in a developing stage."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": content}],
        )
        bot_response = response.choices[0].message.content if response.choices else "Sorry, I couldn't process your request."
    except Exception:
        bot_response = "An error occurred while processing your request."

    return jsonify({"response": bot_response})

def main():
    threading.Timer(1, open_browser).start()
    app.run(debug=True)

def open_browser():
    webbrowser.open("http://127.0.0.1:5000")