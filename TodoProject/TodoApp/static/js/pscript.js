
function loadContent(url) {
    fetch('/ajax/load_content/', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
        // You can include additional options as needed
    })
    .then(response => response.text())
    .then(data => {
        // Insert the loaded content into the tabcontents div
        document.getElementById('tabcontents').innerHTML = data;
    })
    .catch(error => console.error('Error:', error));
}
    