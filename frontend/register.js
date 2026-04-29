// document.getElementById("registerForm").addEventListener("submit", async function(e) {
//     e.preventDefault();

//     const username = document.getElementById("username").value;
//     const password = document.getElementById("password").value;
//     const role = document.getElementById("role").value;

//     try {
//         const response = await fetch("https://69ee2c129163f839f89290f1.mockapi.io/users", {
//             method: "POST",
//             headers: {
//                 "Content-Type": "application/json"
//             },
//             body: JSON.stringify({
//                 username: username,
//                 password: password,
//                 role: role
//             })
//         });

//         if (response.ok) {
//             alert("Registered successfully!");
//             window.location.href = "login.html";
//         } else {
//             alert("Registration failed");
//         }

//     } catch (error) {
//         console.error(error);
//         alert("Error connecting to server");
//     }
// });
document.getElementById("registerForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const role = document.getElementById("role").value;

    if (!role) {
        alert("Please select a role");
        return;
    }

    try {
        const response = await fetch("https://69ee2c129163f839f89290f1.mockapi.io/users", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username,
                password,
                role
            })
        });

        if (response.ok) {
            alert("Registered successfully!");
            window.location.href = "login.html";
        } else {
            alert("Registration failed");
        }

    } catch (error) {
        console.error(error);
        alert("Error connecting to API");
    }
});