document.addEventListener('DOMContentLoaded', function() {
    const updateForms = document.querySelectorAll('.update-form');
    updateForms.forEach(form => {
        form.addEventListener('change', function(event) {
            event.preventDefault(); // Prevent the default form submission
            const formData = new FormData(form);
            fetch(form.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': formData.get('csrfmiddlewaretoken')
                }
            })
            .then(response => response.json())
            .then(data => {
                if (!data.success) {
                    alert('Failed to update task: ' + JSON.stringify(data.errors));
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred while updating the task.');
            });
        });
    });

    const deleteButtons = document.querySelectorAll('.delete-button');
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            const taskId = button.getAttribute('data-task-id');
            if (taskId) {
                window.location.href = '/tasks/delete/' + taskId + '/';
            } else {
                console.error('Task ID not found on delete button');
            }
        });
    });

    $('input[type="date"]').datepicker({
        dateFormat: 'dd/mm/yy'
    });
});

function submitForm(selectElement) {
    const form = selectElement.closest('form');
    const formData = new FormData(form);
    fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': formData.get('csrfmiddlewaretoken')
        }
    })
    .then(response => response.json())
    .then(data => {
        if (!data.success) {
            alert('Failed to update task: ' + JSON.stringify(data.errors));
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while updating the task.');
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function displaySuccessMessage(message) {
    const messageContainer = document.createElement('div');
    messageContainer.className = 'alert alert-success';
    messageContainer.textContent = message;
    document.body.appendChild(messageContainer);

    setTimeout(() => {
        messageContainer.remove();
    }, 3000);
}
