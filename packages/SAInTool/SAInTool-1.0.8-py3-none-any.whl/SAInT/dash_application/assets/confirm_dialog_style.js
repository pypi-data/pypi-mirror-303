window.addEventListener('DOMContentLoaded', function () {
    // Function to apply the custom styling to the ConfirmDialog
    function styleConfirmDialog() {
        var confirmDialogBody = document.querySelector('.dash-confirm-dialog .dash-confirm-dialog-body');
        if (confirmDialogBody) {
            // Apply the custom styles
            print("RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRr")
            confirmDialogBody.style.color = 'red'; // Set text color to red
            confirmDialogBody.style.fontWeight = 'bold'; // Make the text bold
            confirmDialogBody.style.fontSize = '16px'; // Increase the font size
        }
    }

    // MutationObserver to detect when the ConfirmDialog is added to the DOM
    var observer = new MutationObserver(function (mutationsList, observer) {
        for (var mutation of mutationsList) {
            if (mutation.addedNodes.length) {
                // Check if the ConfirmDialog was added
                var dialogAdded = Array.from(mutation.addedNodes).some(node => node.classList && node.classList.contains('dash-confirm-dialog'));
                if (dialogAdded) {
                    styleConfirmDialog();
                }
            }
        }
    });

    // Observe changes in the document body for the appearance of the ConfirmDialog
    observer.observe(document.body, { childList: true, subtree: true });
});
