<?php
// Practical 11: AJAX Data Fetching (PHP side, returns JSON)
require "../db.php";

header("Content-Type: application/json");

$stmt = $pdo->query("SELECT id, name, email FROM users");
echo json_encode($stmt->fetchAll(PDO::FETCH_ASSOC));
