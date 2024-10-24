// NxLU custom JavaScript

document.addEventListener('DOMContentLoaded', function () {
    // Add custom functionality here
    console.log('NxLU documentation loaded');

    // Example: Add a click event to all buttons with class 'nxlu-button'
    const buttons = document.querySelectorAll('.nxlu-button');
    buttons.forEach(button => {
        button.addEventListener('click', function (event) {
            event.preventDefault();
            console.log('NxLU button clicked:', this.href);
            window.open(this.href, '_blank');
        });
    });
});
