const encryptionForm = document.getElementById("encryptionForm");
const keyInput = document.getElementById('key');


encryptionForm.addEventListener("submit", function(e) {
    e.preventDefault();
  
    const key = keyInput.value;
  
    if (key.length !== 32) { 
        alertify.set('notifier', 'position', 'top-left'); 
        alertify.error('Key must be exactly 32 characters long.');
        return;
    }
    
    // Get the form data
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
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        const encryptedText = data.encrypted_text;
        const swalContent = document.createElement('div');
        swalContent.innerHTML = `<div id="copyText">${encryptedText}</div><button id="copyButton"  onclick="copyText()">Copy</button>`;
        
        swal({
            title: "Encrypted Text",
            content: swalContent,
            icon: "success",
        }).then(() => {
            window.location.href = "/decrypt/";
        });
    })
    .catch(error => {
        swal({
            title: "Error",
            text: "An error occurred. Please try again later.",
            icon: "error",
        });
    });
});

    
// Function to copy the encrypted text
function copyText() {
    const copyText = document.getElementById("copyText");
    const encryptedText = copyText.textContent;

    
    navigator.clipboard.writeText(encryptedText)
        .then(() => {
            alertify.success("Encrypted text copied to clipboard");
        })
        .catch(err => {
            console.error("Failed to copy text: ", err);
            alertify.error("Failed to copy encrypted text");
        });
}

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
