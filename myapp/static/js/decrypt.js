const decryptionForm = document.getElementById("decryptionForm")
const keyInput = document.getElementById('key')

decryptionForm.addEventListener("submit", function(event) {
    event.preventDefault();

    keyInput.type = "password"; 
    const formData = new FormData(this);

   // Send a POST request to the encrypt_view endpoint
   fetch(this.action, {
    method: "POST",
    body: formData,
    headers: {
        "X-CSRFToken": getCookie("csrftoken")
    }
})
    .then(response => {
    if (!response.ok) {
        throw new Error('Key not compatible');
    }
    return response.json();
    })
    .then(data => {
        swal({
            title: "Decrypted Text",
            text: data.decrypted_text,  
            icon: "success",
        })
    })
    .catch(error => {
        swal({
            title: "Error",
            text: error.message,
            icon: "error",
        });
    });
});

// Function to get the CSRF token from the cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";").map(cookie => cookie.trim());
        for (const cookie of cookies) {
            if (cookie.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
