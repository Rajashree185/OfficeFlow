const TASK_API = "/api/tasks";


// Load all tasks
async function loadTasks() {

    const response = await fetch(TASK_API);
    const tasks = await response.json();

    const tableBody = document.getElementById("taskTableBody");

    tableBody.innerHTML = "";

    tasks.forEach(task => {

        const row = document.createElement("tr");

        row.innerHTML = `
            <td>
                <strong>${task.title}</strong>
                <br>
                <small>${task.description || ""}</small>
            </td>

            <td>${task.assigned_to || "-"}</td>

            <td>${task.due_date || "-"}</td>

            <td>${task.priority}</td>

            <td>
                <select onchange="updateTask(${task.id}, this.value)">

                    <option value="Pending"
                        ${task.status === "Pending" ? "selected" : ""}>
                        Pending
                    </option>

                    <option value="In Progress"
                        ${task.status === "In Progress" ? "selected" : ""}>
                        In Progress
                    </option>

                    <option value="Completed"
                        ${task.status === "Completed" ? "selected" : ""}>
                        Completed
                    </option>

                </select>
            </td>

            <td>
                <button onclick="deleteTask(${task.id})">
                    Delete
                </button>
            </td>
        `;

        tableBody.appendChild(row);
    });
}


// Add a new task
document.getElementById("taskForm").addEventListener("submit", async function(event) {

    event.preventDefault();

    const taskData = {

        title: document.getElementById("title").value,

        description: document.getElementById("description").value,

        assigned_to: document.getElementById("assigned_to").value,

        due_date: document.getElementById("due_date").value,

        priority: document.getElementById("priority").value,

        status: document.getElementById("status").value
    };


    const response = await fetch(TASK_API, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(taskData)
    });


    const result = await response.json();


    if (response.ok) {

        alert(result.message);

        document.getElementById("taskForm").reset();

        loadTasks();

    } else {

        alert(result.error);
    }

});


// Update task status
async function updateTask(taskId, newStatus) {

    const response = await fetch(`${TASK_API}/${taskId}`, {

        method: "PUT",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            status: newStatus
        })
    });


    const result = await response.json();

    if (response.ok) {

        alert(result.message);

        loadTasks();

    } else {

        alert(result.error);
    }
}


// Delete task
async function deleteTask(taskId) {

    const confirmed = confirm(
        "Are you sure you want to delete this task?"
    );

    if (!confirmed) {
        return;
    }


    const response = await fetch(`${TASK_API}/${taskId}`, {

        method: "DELETE"
    });


    const result = await response.json();


    if (response.ok) {

        alert(result.message);

        loadTasks();

    } else {

        alert(result.error);
    }
}


// Load tasks when page opens
loadTasks();