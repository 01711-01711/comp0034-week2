
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
@app.route("/<name>")
def hello(name='Mateusz'):
    return f"Hello, {escape(name)}!"


# Run the app
if __name__ == '__main__':
    app.run()