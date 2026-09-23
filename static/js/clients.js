const API_URL = "/api/clients";


// Load clients
async function loadClients() {

    const response = await fetch(API_URL);

    const clients = await response.json();

    const tableBody = document.getElementById("clientTableBody");

    tableBody.innerHTML = "";

    clients.forEach(client => {

        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${client.name}</td>
            <td>${client.company}</td>
            <td>${client.country || "-"}</td>
            <td>${client.email || "-"}</td>
            <td>${client.status}</td>
            <td>
                <button onclick="deleteClient(${client.id})">
                    Delete
                </button>
            </td>
        `;

        tableBody.appendChild(row);
    });
}


// Add client
document.getElementById("clientForm").addEventListener(
    "submit",
    async function(event) {

        event.preventDefault();

        const client = {

            name: document.getElementById("name").value,

            company: document.getElementById("company").value,

            country: document.getElementById("country").value,

            email: document.getElementById("email").value,

            phone: document.getElementById("phone").value,

            status: document.getElementById("status").value
        };


        const response = await fetch(API_URL, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(client)
        });


        if (response.ok) {

            alert("Client added successfully!");

            document.getElementById("clientForm").reset();

            loadClients();

        } else {

            alert("Failed to add client.");

        }

    }
);


// Delete client
async function deleteClient(id) {

    if (!confirm("Are you sure you want to delete this client?")) {
        return;
    }

    await fetch(`${API_URL}/${id}`, {
        method: "DELETE"
    });

    loadClients();
}


// Load clients when page opens
loadClients();