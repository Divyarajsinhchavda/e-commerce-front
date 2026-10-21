<?php
// Practical 7: Dashboard (only for logged in users)
session_start();

if (!isset($_SESSION["username"])) {
    header("Location: login.php");
    exit;
}
?>
<!DOCTYPE html>
<html>
<body>
    <h3>Welcome, <?php echo htmlspecialchars($_SESSION["username"]); ?>!</h3>
    <p>You are logged in.</p>
    <a href="logout.php">Logout</a>
</body>
</html>
