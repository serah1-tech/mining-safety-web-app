// This code runs when the window loads
window.onload = function() {
    var successMessage = document.querySelector('.success-message');
    if (successMessage) {
        successMessage.classList.add('show'); // Make the message visible

        // Hide the success message after 5 seconds
        setTimeout(function() {
            successMessage.classList.remove('show');
        }, 5000);
    }
};
