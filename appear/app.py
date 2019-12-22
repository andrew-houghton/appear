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
    session["receive_count"] = session.get("receive_count", 0) + 1
    emit(
        "my_response",
        {"data": request.form["message"], "count": session["receive_count"]},
        broadcast=True,
        namespace="/test",
    )
    return jsonify({"success": True}), 200


@socketio.on("connect", namespace="/test")
def test_connect():
    emit("my_response", {"data": "Connected", "count": 0})


@socketio.on("disconnect", namespace="/test")
def test_disconnect():
    print("Client disconnected", request.sid)


if __name__ == "__main__":
    socketio.run(app, debug=True)
