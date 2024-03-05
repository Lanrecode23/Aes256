const Form = document.querySelector('form');
const Email = document.getElementById('Email');
const Password = document.getElementById('Password');

Form.addEventListener('submit', (e) => {
    e.preventDefault();

    if (Email.value !== '' && Password.value !== '') {
        const formData = new FormData();
        formData.append('email', Email.value);
        formData.append('password', Password.value);

        fetch('/login/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken') 
            }
        })
        .then(response => {
            if (response.ok) {
                // Form submission successful, show success message
                swal({
                    title: "Congratulations",
                    text: 'You have successfully logged in',
                    icon: "success",
                });
            } else {
                // Form submission failed, show error message
                swal({
                    title: "Error",
                    text: 'Email or password already exist..',
                    icon: "error",
                });
            }
        })
        .catch(error => {
            console.error('Error:', error);
            // Show error message if request fails
            swal({
                title: "Error",
                text: 'Email or password already exist.',
                icon: "error",
            });
        });
    }
});

// Function to get CSRF token from cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
