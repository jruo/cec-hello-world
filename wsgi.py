import socket
from flask import Flask
from datetime import datetime

application = Flask(__name__)

@application.route("/")
def hello():
    log_file = open("/mnt/hello-world-storage/log", "a")
    log_file.write(socket.gethostname() + " " + str(datetime.now()) + "\n")
    log_file.close()
    
    log_file = open("/mnt/hello-world-storage/log", "r")
    log_content = log_file.read()
    log_file.close()
    
    return log_content


if __name__ == "__main__":
    application.run()
