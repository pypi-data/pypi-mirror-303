window.addEventListener('DOMContentLoaded', function () {
    var errorStore = document.getElementById('error-store'); // Select the error store directly
    var observer = new MutationObserver(function (mutationsList) {
        mutationsList.forEach(function (mutation) {
            var errorMessage = mutation.target.textContent || "";
            if (errorMessage && errorMessage !== '""') { // Check if error message is not empty
                alert("Error: " + errorMessage);  // Display the error popup
            }
        });
    });

    // Observe changes to the error store's child list or text content
    var config = { childList: true, subtree: true, characterData: true };
    observer.observe(errorStore, config);  // Start observing
});
