<?php
// Practical 5: Prepared Statements to Prevent SQL Injection
require "db.php";

$message = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["name"];
    $email = $_POST["email"];

    // Prepared statement: user input is NOT added directly into the SQL
    $stmt = $pdo->prepare("INSERT INTO users (name, email) VALUES (:name, :email)");
    $stmt->execute([
        ":name" => $name,
        ":email" => $email
    ]);
    $message = "User inserted safely!";
}
?>
<!DOCTYPE html>
<html>
<body>
    <h3>Insert User (Prepared Statement)</h3>
    <p style="color:green;"><?php echo $message; ?></p>
    <form method="post">
        Name: <input type="text" name="name" required><br><br>
        Email: <input type="email" name="email" required><br><br>
        <button type="submit">Save</button>
    </form>
    <p>Try typing <code>'); DROP TABLE users; --</code> in the name box. It will be saved as plain text, not executed.</p>
</body>
</html>
