<?php
// Practical 14: Login endpoint, returns a JWT token
// Test: POST login.php with JSON body {"username":"admin","password":"1234"}
require "jwt_helper.php";

header("Content-Type: application/json");

$input = json_decode(file_get_contents("php://input"), true);
$username = $input["username"] ?? "";
$password = $input["password"] ?? "";

// demo credentials (use database in a real project)
if ($username == "admin" && $password == "1234") {
    $payload = [
        "user" => $username,
        "iat" => time(),
        "exp" => time() + 3600   // valid for 1 hour
    ];
    $token = createJWT($payload, $secret);
    echo json_encode(["token" => $token]);
} else {
    http_response_code(401);
    echo json_encode(["message" => "Invalid username or password"]);
}
