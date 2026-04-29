document.getElementById("loginForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    try {
        const res = await fetch("https://69ee2c129163f839f89290f1.mockapi.io/users");
        const users = await res.json();

        const user = users.find(u => 
            u.username === username && u.password === password
        );

        if (user) {
            // save user (like session)
            localStorage.setItem("user", JSON.stringify(user));

            //  redirect based on role
            if (user.role === "admin") {
                window.location.href = "/frontend/admin.html";
            } else if (user.role === "dealer") {
                window.location.href = "/frontend/dealerdashboard.html";
            } else {
                window.location.href = "/frontend/user.html";
            }

        } else {
            alert("Invalid username or password");
        }

    } catch (error) {
        console.error(error);
        alert("Error connecting to server");
    }
});