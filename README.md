# OfficeFlow – Office Administration & Management System

OfficeFlow is a web-based office administration and management system designed to organize and monitor day-to-day administrative activities in one place.

The system helps manage client records, meetings, tasks, and administrative reports through a centralized dashboard.

## Features

### 📊 Dashboard
- Centralized overview of office activities
- Total clients, meetings, and tasks
- Quick access to different management sections

### 👥 Client Management
- Add and manage client records
- Store client contact and company information
- Track client status
- Delete outdated records
- Export client data to Excel

### 📅 Meeting Management
- Schedule and manage meetings
- Store meeting details and client information
- Track meeting status
- Export meeting records to Excel

### ✅ Task Management
- Create and manage office tasks
- Track task status and priority
- Monitor pending, in-progress, and completed tasks
- Export task records to Excel

### 📈 Reports & Analytics
- View administrative activity summaries
- Monitor client, meeting, and task statistics
- Visualize data using charts
- Track task and meeting status

### 📑 Administrative Excel Reporting
- Export individual client, meeting, and task records
- Generate a consolidated Administrative Report
- Separate Summary, Clients, Meetings, and Tasks sheets
- Excel filters for structured data analysis
- Frozen headers for easier navigation
- Automatic column sizing

## Technology Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **Database:** SQLite
- **Data & Reporting:** Microsoft Excel, OpenPyXL
- **Charts:** Chart.js
- **Version Control:** Git & GitHub

## Project Structure

```text
OfficeFlow/
│
├── app.py
├── database.py
├── officeflow.db
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   ├── clients.html
│   ├── meetings.html
│   ├── tasks.html
│   └── reports.html
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
How to Run
1. Clone the repository
git clone https://github.com/Rajashree185/OfficeFlow.git
2. Navigate to the project
cd OfficeFlow
3. Install dependencies
pip install -r requirements.txt
4. Run the application
python app.py
5. Open in browser
http://127.0.0.1:5000
Administrative Use Cases

OfficeFlow can be used for:

Maintaining client records
Scheduling and tracking meetings
Managing daily office tasks
Monitoring task progress
Preparing administrative reports
Exporting structured records to Excel
Reviewing office activity through charts and summaries
Project Objective

The objective of OfficeFlow is to provide a simple centralized system for organizing office information and reducing manual effort in maintaining administrative records.

Future Improvements
User authentication and role-based access
Automated email notifications
Advanced monthly and yearly reports
Cloud database integration
Automated backup and restore
Author

Rajashree Ray