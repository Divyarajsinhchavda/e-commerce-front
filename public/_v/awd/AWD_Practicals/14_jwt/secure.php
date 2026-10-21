<?php
// Practical 14: Secured endpoint (needs a valid token)
// Test: GET secure.php with header  Authorization: Bearer <token>
require "jwt_helper.php";

header("Content-Type: application/json");

$headers = getallheaders();
$auth = $headers["Authorization"] ?? $headers["authorization"] ?? "";

if (strpos($auth, "Bearer ") !== 0) {
    http_response_code(401);
    echo json_encode(["message" => "Token missing"]);
    exit;
}

$token = substr($auth, 7);
$payload = verifyJWT($token, $secret);

if ($payload) {
    echo json_encode([
        "message" => "Access granted",
        "user" => $payload["user"],
        "secret_data" => "This is protected data"
    ]);
} else {
    http_response_code(401);
    echo json_encode(["message" => "Invalid or expired token"]);
}
