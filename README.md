# OfficeFlow – Internal Office Coordination System

OfficeFlow is a lightweight web-based internal office coordination system designed to simplify everyday office activities such as managing clients, scheduling meetings, and tracking tasks.

## Features

### 📊 Dashboard
- View total number of clients, meetings, and tasks
- Quick access to different modules
- Simple and clean interface

### 👥 Client Management
- Add new client information
- View client records
- Store company and contact details
- Delete client records when required

### 📅 Meeting Management
- Schedule meetings with clients
- Store meeting date and time
- Select meeting type
- Add participants and meeting agenda
- Track meeting status
- Delete meetings

### ✅ Task Management
- Create and manage office tasks
- Assign tasks to team members
- Set due dates
- Set task priority
- Update task status
- Delete tasks

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **Database:** SQLite
- **API:** REST APIs

## Project Structure

```text
OfficeFlow/
│
├── app.py
├── database.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── clients.html
│   ├── meetings.html
│   └── tasks.html
│
└── static/
    ├── css/
    │   └── style.css
    │
    └── js/
        ├── dashboard.js
        ├── clients.js
        ├── meetings.js
        └── tasks.js
How to Run the Project
1. Clone the Repository
git clone https://github.com/YOUR-USERNAME/OfficeFlow.git
2. Open the Project Folder
cd OfficeFlow
3. Create a Virtual Environment
python -m venv venv
4. Activate the Virtual Environment

For Windows:

venv\Scripts\activate
5. Install Dependencies
pip install -r requirements.txt
6. Run the Application
python app.py
7. Open the Application

Open the following address in your browser:

http://127.0.0.1:5000/
Application Workflow
Dashboard
    │
    ├── Client Management
    │       ├── Add Client
    │       ├── View Clients
    │       └── Delete Client
    │
    ├── Meeting Management
    │       ├── Schedule Meeting
    │       ├── View Meetings
    │       └── Delete Meeting
    │
    └── Task Management
            ├── Create Task
            ├── Assign Task
            ├── Update Status
            └── Delete Task
Database

OfficeFlow uses SQLite for storing application data.

The database contains tables for:

Clients
Meetings
Tasks

The database is automatically initialized when the Flask application starts.

REST API

The backend provides REST API endpoints for managing application data.

Client APIs
GET    /api/clients
POST   /api/clients
DELETE /api/clients/<client_id>
Meeting APIs
GET    /api/meetings
POST   /api/meetings
DELETE /api/meetings/<meeting_id>
Task APIs
GET    /api/tasks
POST   /api/tasks
PUT    /api/tasks/<task_id>
DELETE /api/tasks/<task_id>
Purpose

OfficeFlow was developed as a practical full-stack project to demonstrate:

Web application development
Frontend and backend integration
REST API development
SQLite database management
CRUD operations
JavaScript-based API interaction
Basic responsive UI development
Understanding of simple office coordination workflows
Future Improvements

Possible future improvements include:

User authentication and role-based access
Advanced search and filtering
Notifications and reminders
Report generation
Exporting data
Integration with productivity tools
Author

Rajashree Ray

Computer Science & Engineering Student