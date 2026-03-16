from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Привет, мир! Мое приложение теперь на Hugging Face! 🚀"

# Убедись, что приложение слушает порт 7860, который ожидает Hugging Face [citation:5]
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)
