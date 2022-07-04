from ec2_metadata import ec2_metadata as ec2
from flask import Flask
from waitress import serve
app = Flask(__name__)


@app.route("/")
def hello():
    # print(ec2.instance_id)
    return "Hello World! from "+ec2.instance_id + " this is version 2"


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)
