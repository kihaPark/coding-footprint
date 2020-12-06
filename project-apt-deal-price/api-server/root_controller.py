from flask import Flask
from khp771_controller import khp771

app = Flask(__name__)

app.register_blueprint(khp771)

@app.errorhandler(404)
def server_error(error):
    # print(str(error) + '-----')
    return str("error"), 404