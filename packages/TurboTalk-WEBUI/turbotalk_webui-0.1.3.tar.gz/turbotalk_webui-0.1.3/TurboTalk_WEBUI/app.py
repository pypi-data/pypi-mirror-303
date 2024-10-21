import webbrowser
from flask import Flask, render_template, request, jsonify
from g4f.client import Client
import threading

class TurboTalkApp:
    def __init__(self, bot_name, company_name):
        self.app = Flask(__name__)
        self.client = Client()
        self.bot_name = bot_name
        self.company_name = company_name

        @self.app.route('/')
        def index():
            return render_template('index.html', bot_name=self.bot_name)

        @self.app.route('/chat', methods=['POST'])
        def chat():
            user_message = request.json.get('message')
            behaviour = request.json.get('behaviour')

            if not user_message or not behaviour:
                return jsonify({"response": "Invalid input."}), 400

            content = (
                f"Follow the below commands strictly {user_message} "
                f"and behave very strongly like {behaviour} "
                f"as I am a/an {behaviour} type person. If asked questions about yourself, "
                f"introduce yourself as {self.bot_name} from {self.company_name}, "
                f"which is in a developing stage."
            )

            try:
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": content}],
                )
                bot_response = response.choices[0].message.content if response.choices else "Sorry, I couldn't process your request."
            except Exception:
                bot_response = "An error occurred while processing your request."

            return jsonify({"response": bot_response})

    def run(self):
        threading.Timer(1, self.open_browser).start()
        self.app.run(debug=True)

    def open_browser(self):
        webbrowser.open("http://127.0.0.1:5000")

def start_webui_chat(bot_name, company_name):
    chat_app = TurboTalkApp(bot_name, company_name)
    chat_app.run()
