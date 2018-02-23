import socket
from flask import Flask
from datetime import datetime

application = Flask(__name__)

@application.route("/")
def hello():
    log_file = open("/mnt/hello-world-storage/log", "a")
    log_file.write(socket.gethostname() + " " + str(datetime.now()) + "\n")
    log_file.close()
    return "Hello World! Greetings from "+socket.gethostname()+"\n"


if __name__ == "__main__":
    application.run()
