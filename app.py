from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from database import create_tables, get_db_connection

app = Flask(__name__)
CORS(app)

create_tables()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/clients")
def clients_page():
    return render_template("clients.html")

@app.route("/meetings")
def meetings_page():
    return render_template("meetings.html")


# Get all clients
@app.route("/api/clients", methods=["GET"])
def get_clients():
    connection = get_db_connection()

    clients = connection.execute(
        "SELECT * FROM clients ORDER BY id DESC"
    ).fetchall()

    connection.close()

    return jsonify([dict(client) for client in clients])


# Add a new client
@app.route("/api/clients", methods=["POST"])
def add_client():
    data = request.get_json()

    name = data.get("name")
    company = data.get("company")
    country = data.get("country")
    email = data.get("email")
    phone = data.get("phone")
    status = data.get("status", "Active")

    if not name or not company:
        return jsonify({
            "error": "Name and company are required"
        }), 400

    connection = get_db_connection()

    cursor = connection.execute("""
        INSERT INTO clients
        (name, company, country, email, phone, status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, company, country, email, phone, status))

    connection.commit()

    client_id = cursor.lastrowid

    connection.close()

    return jsonify({
        "message": "Client added successfully",
        "id": client_id
    }), 201


# Delete a client
@app.route("/api/clients/<int:client_id>", methods=["DELETE"])
def delete_client(client_id):
    connection = get_db_connection()

    connection.execute(
        "DELETE FROM clients WHERE id = ?",
        (client_id,)
    )

    connection.commit()
    connection.close()

    return jsonify({
        "message": "Client deleted successfully"
    })

# Get all meetings
@app.route("/api/meetings", methods=["GET"])
def get_meetings():
    connection = get_db_connection()

    meetings = connection.execute("""
        SELECT meetings.*, clients.name AS client_name,
               clients.company AS client_company
        FROM meetings
        LEFT JOIN clients ON meetings.client_id = clients.id
        ORDER BY meetings.date ASC, meetings.time ASC
    """).fetchall()

    connection.close()

    return jsonify([dict(meeting) for meeting in meetings])


# Add a new meeting
@app.route("/api/meetings", methods=["POST"])
def add_meeting():
    data = request.get_json()

    client_id = data.get("client_id")
    title = data.get("title")
    date = data.get("date")
    time = data.get("time")
    meeting_type = data.get("meeting_type")
    participants = data.get("participants")
    agenda = data.get("agenda")
    status = data.get("status", "Upcoming")

    if not client_id or not title or not date or not time:
        return jsonify({
            "error": "Client, title, date and time are required"
        }), 400

    connection = get_db_connection()

    cursor = connection.execute("""
        INSERT INTO meetings
        (client_id, title, date, time, meeting_type,
         participants, agenda, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        client_id,
        title,
        date,
        time,
        meeting_type,
        participants,
        agenda,
        status
    ))

    connection.commit()

    meeting_id = cursor.lastrowid

    connection.close()

    return jsonify({
        "message": "Meeting scheduled successfully",
        "id": meeting_id
    }), 201


# Delete a meeting
@app.route("/api/meetings/<int:meeting_id>", methods=["DELETE"])
def delete_meeting(meeting_id):
    connection = get_db_connection()

    connection.execute(
        "DELETE FROM meetings WHERE id = ?",
        (meeting_id,)
    )

    connection.commit()
    connection.close()

    return jsonify({
        "message": "Meeting deleted successfully"
    })

@app.route("/tasks")
def tasks_page():
    return render_template("tasks.html")


@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    connection = get_db_connection()

    tasks = connection.execute("""
        SELECT * FROM tasks
        ORDER BY due_date ASC
    """).fetchall()

    connection.close()

    return jsonify([dict(task) for task in tasks])


@app.route("/api/tasks", methods=["POST"])
def add_task():
    data = request.get_json()

    title = data.get("title")
    description = data.get("description")
    assigned_to = data.get("assigned_to")
    due_date = data.get("due_date")
    priority = data.get("priority", "Medium")
    status = data.get("status", "Pending")

    if not title:
        return jsonify({
            "error": "Task title is required"
        }), 400

    connection = get_db_connection()

    cursor = connection.execute("""
        INSERT INTO tasks
        (title, description, assigned_to, due_date, priority, status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        title,
        description,
        assigned_to,
        due_date,
        priority,
        status
    ))

    connection.commit()

    task_id = cursor.lastrowid

    connection.close()

    return jsonify({
        "message": "Task added successfully",
        "id": task_id
    }), 201


@app.route("/api/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()

    status = data.get("status")

    if not status:
        return jsonify({
            "error": "Status is required"
        }), 400

    connection = get_db_connection()

    connection.execute("""
        UPDATE tasks
        SET status = ?
        WHERE id = ?
    """, (status, task_id))

    connection.commit()
    connection.close()

    return jsonify({
        "message": "Task updated successfully"
    })


@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    connection = get_db_connection()

    connection.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    connection.commit()
    connection.close()

    return jsonify({
        "message": "Task deleted successfully"
    })

if __name__ == "__main__":
    app.run(debug=True)