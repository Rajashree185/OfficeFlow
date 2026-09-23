async function loadDashboardData() {

    try {

        // Get clients
        const clientResponse = await fetch("/api/clients");
        const clients = await clientResponse.json();

        // Get meetings
        const meetingResponse = await fetch("/api/meetings");
        const meetings = await meetingResponse.json();

        // Get tasks
        const taskResponse = await fetch("/api/tasks");
        const tasks = await taskResponse.json();


        // Update dashboard counts
        document.getElementById("clientCount").textContent = clients.length;

        document.getElementById("meetingCount").textContent = meetings.length;

        document.getElementById("taskCount").textContent = tasks.length;

    }

    catch (error) {

        console.error("Error loading dashboard data:", error);

    }
}


// Load data when dashboard opens
loadDashboardData();