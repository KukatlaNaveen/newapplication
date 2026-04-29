const user = JSON.parse(localStorage.getItem("user"));

if (!user) {
    window.location.href = "login.html";
}

// Add product
async function addProduct() {
    const name = document.getElementById("pname").value;
    const price = document.getElementById("price").value;

    if (!name || !price) {
        alert("Enter all fields");
        return;
    }

    try {
        await fetch("https://69ee2c129163f839f89290f1.mockapi.io/products", { // replace this
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name,
                price
            })
        });

        alert("Product added!");

        // clear inputs
        document.getElementById("pname").value = "";
        document.getElementById("price").value = "";

    } catch (error) {
        console.error(error);
        alert("Error adding product");
    }
}