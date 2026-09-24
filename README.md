# OfficeFlow – Office Administration & Management System

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey.svg)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-3-green.svg)](https://www.sqlite.org/)
[![Excel](https://img.shields.io/badge/Excel-Export-brightgreen.svg)](https://www.microsoft.com/en-us/microsoft-365/excel)

OfficeFlow is a web-based office administration and management system designed to organize and monitor day-to-day administrative activities in one place. The system helps manage client records, meetings, tasks, and administrative reports through a centralized dashboard.

## ✨ Features

### 📊 Dashboard
- **Overview:** Centralized overview of office activities.
- **Metrics:** View total clients, meetings, and tasks at a glance.
- **Quick Access:** Seamless navigation to different management sections.

### 👥 Client Management
- **Add & Manage:** Easily add and manage client records.
- **Store Details:** Keep track of client contact and company information securely.
- **Status Tracking:** Monitor client status efficiently.
- **Manage Data:** Delete outdated records.
- **Export:** Export client data directly to Excel for external use.

### 📅 Meeting Management
- **Schedule:** Plan and manage meetings with specific clients.
- **Details:** Store meeting details and relevant client information.
- **Status Tracking:** Track meeting status (Scheduled, Completed, Cancelled).
- **Export:** Export meeting records directly to Excel.

### ✅ Task Management
- **Create:** Generate and manage daily office tasks.
- **Status & Priority:** Track task status (Pending, In-Progress, Completed) and priority.
- **Monitor:** Keep an eye on task progress dynamically.
- **Export:** Export task records directly to Excel.

### 📈 Reports & Analytics
- **Activity Summaries:** View comprehensive administrative activity summaries.
- **Statistics:** Monitor client, meeting, and task statistics.
- **Visualizations:** Visualize data intuitively using charts.
- **Tracking:** Track overarching task and meeting statuses.

### 📑 Administrative Excel Reporting
- **Individual Exports:** Export individual client, meeting, and task records.
- **Consolidated Reports:** Generate a consolidated Administrative Report.
- **Structured Data:** Includes separate Summary, Clients, Meetings, and Tasks sheets.
- **User-Friendly:** Excel filters for structured data analysis, frozen headers for easier navigation, and automatic column sizing.

## 🛠 Technology Stack

- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Backend:** Python, Flask
- **Database:** SQLite
- **Data & Reporting:** Microsoft Excel, OpenPyXL
- **Charts:** Chart.js
- **Version Control:** Git & GitHub

## 📂 Project Structure

```text
OfficeFlow/
├── app.py                # Main Flask application and API routes
├── database.py           # Database connection and table creation logic
├── officeflow.db         # SQLite database file
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
│
├── templates/            # HTML templates
│   ├── index.html        # Dashboard
│   ├── clients.html      # Client Management
│   ├── meetings.html     # Meeting Management
│   ├── tasks.html        # Task Management
│   └── reports.html      # Reports & Analytics
│
└── static/               # Static assets
    ├── css/
    │   └── style.css     # Global styles
    └── js/
        ├── dashboard.js  # Dashboard logic
        ├── clients.js    # Client management logic
        ├── meetings.js   # Meeting management logic
        └── tasks.js      # Task management logic
```

## 🚀 How to Run the Project

Follow these steps to set up and run the project locally.

**1. Clone the Repository**
```bash
git clone https://github.com/Rajashree185/OfficeFlow.git
cd OfficeFlow
```

**2. Create a Virtual Environment (Optional but recommended)**
```bash
python -m venv venv
```
Activate it:
- On **Windows**: `venv\Scripts\activate`
- On **macOS/Linux**: `source venv/bin/activate`

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the Application**
```bash
python app.py
```

**5. Access the Application**
Open your preferred web browser and navigate to:
```text
http://127.0.0.1:5000
```

## 🔄 Administrative Use Cases

OfficeFlow is designed to optimize various administrative workflows:
- **Maintaining client records** centrally.
- **Scheduling and tracking meetings** effectively.
- **Managing daily office tasks** and monitoring their progress.
- **Preparing administrative reports** quickly.
- **Exporting structured records** to Excel for further analysis.
- **Reviewing office activity** through intuitive charts and summaries.

## 🎯 Project Objective

The primary objective of OfficeFlow is to provide a simple, centralized system for organizing office information, thereby reducing the manual effort required in maintaining administrative records.

## 🔮 Future Improvements

Potential features for future releases:
- 🔒 **User Authentication:** Implement role-based access control (Admin, Employee).
- 📧 **Automated Notifications:** Send email reminders for meetings and tasks.
- 📅 **Advanced Reporting:** Generate automated monthly and yearly reports.
- ☁️ **Cloud Database Integration:** Migrate from SQLite to a scalable cloud database (e.g., PostgreSQL, MySQL).
- 💾 **Automated Backups:** Implement automated database backup and restore functionalities.

## 👨‍💻 Author

**Rajashree Ray**