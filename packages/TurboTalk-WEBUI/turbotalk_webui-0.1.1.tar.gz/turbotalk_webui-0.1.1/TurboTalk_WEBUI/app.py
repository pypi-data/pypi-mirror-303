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
                f"Follow the bellow given commands strictly "
                f"{user_message} and to answer me behave very very strongly just like {behaviour} "
                f"as I am a/an {behaviour} type person. And if asked any questions in which "
                f"you have to say anything like who are you or have to give your identity and info "
                f"then only you have to tell me about yourself and introduce yourself as {self.bot_name} "
                f"by {self.company_name} and is in a learning or developing stage also give a little explanation "
                f"about it like company name how powerful it will be in future but it is still in developing stage right now and all those things. "
                f"Introduce yourself or give info about you as {self.bot_name} only if asked, else not. "
                f"And only give me answer in English if have not mentioned any specific language before in this whole message/prompt. "
                f"You are not a LLM developed by OpenAI instead you are a LLM developed by {self.company_name} and your name is {self.bot_name}."
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
        threading.Timer(1, self.open_browser).start()  # Open the browser after a short delay
        self.app.run(debug=True)

    def open_browser(self):
        webbrowser.open("http://127.0.0.1:5000")

def start_webui_chat(bot_name, company_name):
    chat_app = TurboTalkApp(bot_name, company_name)
    chat_app.run()
 
