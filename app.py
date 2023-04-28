from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory storage for users, tasks, events, and messages (replace with a real database)
users = []
tasks = []
events = []
messages = []


@app.route('/api/register', methods=['POST'])
def register():
    user_data = request.get_json()
    # TODO: Validate user data and save to the database
    users.append(user_data)
    return jsonify({'message': 'User registered successfully'}), 201


@app.route('/api/login', methods=['POST'])
def login():
    credentials = request.get_json()
    # TODO: Check if the user exists and if the password matches
    return jsonify({'message': 'Logged in successfully'}), 200


@app.route('/api/tasks', methods=['GET', 'POST'])
def handle_tasks():
    if request.method == 'GET':
        return jsonify(tasks)
    elif request.method == 'POST':
        task_data = request.get_json()
        tasks.append(task_data)
        return jsonify({'message': 'Task added successfully'}), 201


@app.route('/api/events', methods=['GET', 'POST'])
def handle_events():
    if request.method == 'GET':
        return jsonify(events)
    elif request.method == 'POST':
        event_data = request.get_json()
        events.append(event_data)
        return jsonify({'message': 'Event added successfully'}), 201


@app.route('/api/messages', methods=['GET', 'POST'])
def handle_messages():
    if request.method == 'GET':
        return jsonify(messages)
    elif request.method == 'POST':
        message_data = request.get_json()
        messages.append(message_data)
        return jsonify({'message': 'Message sent successfully'}), 201


if __name__ == '__main__':
    app.run(debug=True)
