<?php
// Shared PDO connection (used by practicals 4, 5, 6, 13)
// Change user/password if your MySQL is different (XAMPP default is root with empty password)
$host = "localhost";
$dbname = "awd_practical";
$user = "root";
$pass = "";

try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Connection failed: " . $e->getMessage());
}
