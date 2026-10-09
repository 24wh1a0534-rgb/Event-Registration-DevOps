document.getElementById("registrationForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const phone = document.getElementById("phone").value.trim();
    const selectedEvent = document.getElementById("event").value;
    const message = document.getElementById("message");

    const registration = {
        name: name,
        email: email,
        phone: phone,
        event: selectedEvent
    };

    message.textContent = "Registering...";
    message.style.color = "blue";

    try {
        const response = await fetch("http://localhost:5000/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(registration)
        });

        const result = await response.json();

        if (response.ok) {
            message.textContent = result.message;
            message.style.color = "green";
            document.getElementById("registrationForm").reset();
        } else {
            message.textContent = result.message || "Registration failed!";
            message.style.color = "red";
        }

    } catch (error) {
        message.textContent = "Cannot connect to server!";
        message.style.color = "red";
        console.error(error);
    }
});