#!/usr/bin/env python
from flask import Flask, render_template, session, request, copy_current_request_context, jsonify
from flask_socketio import SocketIO, emit, disconnect

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/broadcast", methods=["POST"])
def broadcast():
    print(f"Flask app received {request.form}")
    emit("my_response", {"data": request.form["message"]}, broadcast=True, namespace="")
    return jsonify({"success": True}), 200


@socketio.on("connect")
def test_connect():
    emit("my_response", {"data": "Connected"})


@socketio.on("disconnect_request", namespace="/test")
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
