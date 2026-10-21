<?php
// Practical 7: Session Handling for Login System (login page)
session_start();

// already logged in? go to dashboard
if (isset($_SESSION["username"])) {
    header("Location: dashboard.php");
    exit;
}

$error = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];

    // demo credentials (in a real project, check the database)
    if ($username == "admin" && $password == "1234") {
        $_SESSION["username"] = $username;   // store data in session
        header("Location: dashboard.php");
        exit;
    } else {
        $error = "Invalid username or password";
    }
}
?>
<!DOCTYPE html>
<html>
<body>
    <h3>Login</h3>
    <p style="color:red;"><?php echo $error; ?></p>
    <form method="post">
        Username: <input type="text" name="username" required><br><br>
        Password: <input type="password" name="password" required><br><br>
        <button type="submit">Login</button>
    </form>
    <p>Demo: admin / 1234</p>
</body>
</html>
