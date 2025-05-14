// Optional enhancement: confirmation alert on submit
document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('soilForm');
    form.addEventListener('submit', function () {
        alert("Submitting soil data... please wait.");
    });
});
