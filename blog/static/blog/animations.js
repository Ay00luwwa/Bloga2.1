document.addEventListener("DOMContentLoaded", function(){
    setTimeout(() => {
        const introContainer = document.querySelector('.intro-container');
        introContainer.style.opacity = '0';

        setTimeout(() => {
            // Redirect to home.html after the fade-out animation
            window.location.href = "home/";
        }, 2000);  // Redirect after 2 seconds (or the duration of your fade-out animation)

    }, 4000);  // Start the fade-out animation after 4 seconds
});
