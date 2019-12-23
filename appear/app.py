#!/usr/bin/env python
from flask import Flask, render_template, session, request, copy_current_request_context, jsonify
from flask_socketio import SocketIO, emit, disconnect
import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("You must include a second argument, a path to the template_folder. This folder must contain a file named index.html")
    sys.exit()

app = Flask(__name__, template_folder=Path(sys.argv[1]).absolute())
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/broadcast", methods=["POST"])
def broadcast():
    data = request.get_json()
    print(f"Flask app received {data}")
    emit("my_response", data, broadcast=True, namespace="")
    return jsonify({"success": True}), 200


@socketio.on("disconnect_request", namespace="")
def disconnect_request():
    @copy_current_request_context
    def can_disconnect():
        disconnect()
    emit("my_response", {"data": "Disconnected!"}, callback=can_disconnect)


@socketio.on("disconnect")
def test_disconnect():
    print("Client disconnected", request.sid)


if __name__ == "__main__":
    socketio.run(app, debug=True)
