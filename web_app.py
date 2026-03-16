from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Привет, мир! Мое приложение работает в интернете! 🚀"

if __name__ == '__main__':
    # Запускаем на всех интерфейсах (0.0.0.0) и порту 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
