const MEETING_API = "/api/meetings";
const CLIENT_API = "/api/clients";


// Load clients into dropdown
async function loadClients() {

    const response = await fetch(CLIENT_API);

    const clients = await response.json();

    const clientDropdown =
        document.getElementById("client_id");

    clientDropdown.innerHTML =
        '<option value="">Select Client</option>';

    clients.forEach(client => {

        const option = document.createElement("option");

        option.value = client.id;

        option.textContent =
            `${client.name} - ${client.company}`;

        clientDropdown.appendChild(option);

    });
}


// Load meetings
async function loadMeetings() {

    const response = await fetch(MEETING_API);

    const meetings = await response.json();

    const tableBody =
        document.getElementById("meetingTableBody");

    tableBody.innerHTML = "";

    meetings.forEach(meeting => {

        const row = document.createElement("tr");

        row.innerHTML = `
            <td>
                ${meeting.client_name || "-"}
            </td>

            <td>
                ${meeting.title}
            </td>

            <td>
                ${meeting.date}
            </td>

            <td>
                ${meeting.time}
            </td>

            <td>
                ${meeting.meeting_type || "-"}
            </td>

            <td>
                ${meeting.status}
            </td>

            <td>
                <button
                    onclick="deleteMeeting(${meeting.id})">
                    Delete
                </button>
            </td>
        `;

        tableBody.appendChild(row);

    });
}


// Add meeting
document
    .getElementById("meetingForm")
    .addEventListener("submit", async function(event) {

        event.preventDefault();

        const meeting = {

            client_id:
                document.getElementById("client_id").value,

            title:
                document.getElementById("title").value,

            date:
                document.getElementById("date").value,

            time:
                document.getElementById("time").value,

            meeting_type:
                document.getElementById("meeting_type").value,

            participants:
                document.getElementById("participants").value,

            agenda:
                document.getElementById("agenda").value,

            status:
                document.getElementById("status").value
        };


        const response = await fetch(MEETING_API, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(meeting)

        });


        if (response.ok) {

            alert("Meeting scheduled successfully!");

            document
                .getElementById("meetingForm")
                .reset();

            loadMeetings();

        } else {

            const error = await response.json();

            alert(error.error || "Failed to schedule meeting.");

        }

    });


// Delete meeting
async function deleteMeeting(id) {

    if (!confirm(
        "Are you sure you want to delete this meeting?"
    )) {
        return;
    }


    await fetch(`${MEETING_API}/${id}`, {
        method: "DELETE"
    });


    loadMeetings();
}


// Initial loading
loadClients();
loadMeetings();