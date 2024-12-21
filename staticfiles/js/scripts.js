document.addEventListener("DOMContentLoaded", function() {
    const successMessage = document.getElementById('success-message');
    const form = document.querySelector('form');
    
    // If the form exists and there is a success message, show it after a registration success
    if (form) {
        form.addEventListener('submit', function(event) {
            // Prevent form from submitting immediately (for testing purposes)
            event.preventDefault();
            
            // Show the success message
            if (successMessage) {
                successMessage.style.display = 'block'; // Show message
                setTimeout(function() {
                    successMessage.style.display = 'none'; // Hide message after 2 seconds
                }, 2000);
            }

            // Simulate form submission after 2 seconds (you can remove this in actual use)
            setTimeout(function() {
                form.submit();  // Uncomment if you want the form to submit after showing the success message
            }, 2000);
        });
    }
});
