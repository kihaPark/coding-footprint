from flask import Flask
from khp772_controller import khp772

app = Flask(__name__)

app.register_blueprint(khp772)

@app.errorhandler(404)
def server_error(error):
    # print(str(error) + '-----')
    return str("error"), 404