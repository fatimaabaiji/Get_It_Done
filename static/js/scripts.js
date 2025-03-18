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

    const dueDateInputs = document.querySelectorAll('.due-date-input');
    dueDateInputs.forEach(function(input) {
        input.addEventListener('change', function() {
            const taskId = input.getAttribute('data-task-id');
            const dueDate = input.value;
            const csrfToken = getCookie('csrftoken');

            fetch(`/tasks/update-due-date/${taskId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify({ due_date: dueDate })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    displaySuccessMessage('Due date updated successfully.');
                } else {
                    alert('Failed to update due date: ' + JSON.stringify(data.errors));
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred while updating the due date.');
            });
        });
    });

    const prioritySelects = document.querySelectorAll('.priority-select');
    prioritySelects.forEach(function(select) {
        select.addEventListener('change', function() {
            const taskId = select.getAttribute('data-task-id');
            const priority = select.value;
            const csrfToken = getCookie('csrftoken');

            fetch(`/tasks/update-priority/${taskId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify({ priority: priority })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    displaySuccessMessage('Priority updated successfully.');
                } else {
                    alert('Failed to update priority: ' + JSON.stringify(data.errors));
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred while updating the priority.');
            });
        });
    });

    // Ensure only one date picker is initialized
    $('input[type="date"]').datepicker('destroy');

    const dueDateInput = document.querySelector('input[name="due_date"]');
    
    // Retrieve the due date from localStorage
    const savedDueDate = localStorage.getItem('due_date');
    if (savedDueDate) {
        dueDateInput.value = savedDueDate;
    }

    // Save the due date to localStorage on change
    dueDateInput.addEventListener('change', function() {
        localStorage.setItem('due_date', dueDateInput.value);
    });

    // Clear the due date from localStorage on form submission
    const form = document.getElementById('create-task-form');
    form.addEventListener('submit', function() {
        localStorage.removeItem('due_date');
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

function updatePriority(selectElement) {
    const taskId = selectElement.getAttribute('data-task-id');
    const priority = selectElement.value;
    const csrfToken = getCookie('csrftoken');

    fetch(`/tasks/update-priority/${taskId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({ priority: priority })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            displaySuccessMessage('Priority updated successfully.');
        } else {
            alert('Failed to update priority: ' + JSON.stringify(data.errors));
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while updating the priority.');
    });
}
