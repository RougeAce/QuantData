// Function to handle the search input
function searchStock(event) {
    if (event.keyCode === 13) {
        var input = document.getElementById("searchInput");
        var query = input.value;

        // Redirect to the search route for the entered query
        window.location.href = "/" + query;
    }
}



