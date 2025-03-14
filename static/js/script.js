const deleteTaskUrl = "{% url 'delete_task' 'TASK_ID' %}";

function confirmDelete(taskId) {
    const url = deleteTaskBaseUrl + taskId + '/';
    document.getElementById('confirmDeleteBtn').href = url;
    $('#deleteModal').modal('show');
}

document.addEventListener('DOMContentLoaded', function () {
    const deleteTaskBaseUrl = document.getElementById('deleteModal').getAttribute('data-delete-url');
    document.getElementById('deleteModal').addEventListener('show.bs.modal', function (event) {
        const button = event.relatedTarget;
        const taskId = button.getAttribute('data-task-id');
        const confirmDeleteBtn = document.getElementById('confirmDeleteBtn');
        confirmDeleteBtn.href = deleteTaskBaseUrl.replace('0', taskId);
    });
});