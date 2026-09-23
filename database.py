import sqlite3


def get_db_connection():
    connection = sqlite3.connect("officeflow.db")
    connection.row_factory = sqlite3.Row
    return connection


def create_tables():
    connection = get_db_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            company TEXT NOT NULL,
            country TEXT,
            email TEXT,
            phone TEXT,
            status TEXT DEFAULT 'Active'
        )
    """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS meetings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER,
            title TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            meeting_type TEXT,
            participants TEXT,
            agenda TEXT,
            status TEXT DEFAULT 'Upcoming',
            FOREIGN KEY (client_id) REFERENCES clients(id)
        )
    """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            assigned_to TEXT,
            due_date TEXT,
            priority TEXT DEFAULT 'Medium',
            status TEXT DEFAULT 'Pending'
        )
    """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS test_cases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            test_name TEXT NOT NULL,
            module TEXT,
            expected_result TEXT,
            actual_result TEXT,
            tester TEXT,
            status TEXT DEFAULT 'PASS',
            bug_description TEXT
        )
    """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            location TEXT,
            participants TEXT,
            description TEXT
        )
    """)

    connection.commit()
    connection.close()