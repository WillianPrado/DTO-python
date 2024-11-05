from flask import Flask
from controllers.user_controller import user_controller

app = Flask(__name__)

# Registrar o controlador
app.register_blueprint(user_controller)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
