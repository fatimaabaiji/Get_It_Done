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
