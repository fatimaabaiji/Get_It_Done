const deleteTaskUrl = "{% url 'delete_task' 'TASK_ID' %}";

function confirmDelete(taskId) {
    const url = deleteTaskBaseUrl + taskId + '/';
    document.getElementById('confirmDeleteBtn').href = url;
    $('#deleteModal').modal('show');
}

$(document).ready(function() {
    $('input[type="date"]').datepicker({
        dateFormat: 'dd/mm/yy'
    });

    document.addEventListener('DOMContentLoaded', function () {
        var deleteButtons = document.querySelectorAll('.delete-button');
        deleteButtons.forEach(function(button) {
            button.addEventListener('click', function() {
                var taskId = button.getAttribute('data-task-id');
                if (taskId) {
                    window.location.href = '/tasks/delete/' + taskId + '/';
                } else {
                    console.error('Task ID not found on delete button');
                }
            });
        });
    });

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
});

function showDeleteModal(taskId) {
    var deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
    deleteModal.show();
    document.getElementById('confirmDeleteBtn').setAttribute('data-task-id', taskId);
}
document.addEventListener('DOMContentLoaded', function() {
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
