<?php
// Practical 8: Form Validation and Sanitization in PHP
$errors = [];
$name = $email = $password = "";
$success = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // sanitize input
    $name = htmlspecialchars(trim($_POST["name"]));
    $email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);
    $password = $_POST["password"];

    // validate name
    if ($name == "") {
        $errors[] = "Name is required";
    } elseif (!preg_match("/^[a-zA-Z ]+$/", $name)) {
        $errors[] = "Name can contain only letters and spaces";
    }

    // validate email
    if ($email == "") {
        $errors[] = "Email is required";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = "Invalid email format";
    }

    // validate password
    if (strlen($password) < 6) {
        $errors[] = "Password must be at least 6 characters";
    }

    if (empty($errors)) {
        $success = "Form submitted successfully!";
    }
}
?>
<!DOCTYPE html>
<html>
<body>
    <h3>Registration Form</h3>

    <?php foreach ($errors as $e) { echo "<p style='color:red;'>$e</p>"; } ?>
    <p style="color:green;"><?php echo $success; ?></p>

    <form method="post">
        Name: <input type="text" name="name" value="<?php echo $name; ?>"><br><br>
        Email: <input type="text" name="email" value="<?php echo htmlspecialchars($email); ?>"><br><br>
        Password: <input type="password" name="password"><br><br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
