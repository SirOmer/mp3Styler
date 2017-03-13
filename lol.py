from flask import *
from flask_socketio import *
import console
import edit


# Create a Console log instance
log = console.Console()

app = Flask(__name__)
app.config['DEBUG'] = True
socketio = SocketIO(app)


@app.route("/upload", methods=['POST'])
def update():
    content = request.files['file']
    remote_address = request.remote_addr
    log.good("Data Added by " + remote_address)
    socketio.emit(event='song_added', data=edit.fix_song(content), namespace="/sock_connect")
    return "0"

@app.route("/")
def index():
    return render_template("index.html")


@socketio.on('connect', namespace="/sock_connect")
def user_connect():
    log.good("User connected")
    send("Connected to the stream")


@socketio.on('message', namespace="/sock_connect")
def on_message(msg):
    send(msg, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=8080)

