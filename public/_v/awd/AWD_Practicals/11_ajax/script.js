// Practical 11: AJAX Data Fetching (JavaScript file)
function loadUsers() {
    // fetch data from PHP without reloading the page
    fetch("get_users.php")
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            var html = "<table border='1' cellpadding='8'>";
            html += "<tr><th>ID</th><th>Name</th><th>Email</th></tr>";

            data.forEach(function (user) {
                html += "<tr><td>" + user.id + "</td><td>" + user.name + "</td><td>" + user.email + "</td></tr>";
            });

            html += "</table>";
            document.getElementById("result").innerHTML = html;
        })
        .catch(function (error) {
            document.getElementById("result").innerHTML = "Error loading data";
        });
}
