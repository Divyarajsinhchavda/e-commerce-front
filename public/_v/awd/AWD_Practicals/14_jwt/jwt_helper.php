<?php
// Practical 14: JWT helper functions (HS256, no library needed)

$secret = "my_secret_key_123";   // keep this private

function base64url_encode($data) {
    return rtrim(strtr(base64_encode($data), '+/', '-_'), '=');
}

function base64url_decode($data) {
    return base64_decode(strtr($data, '-_', '+/'));
}

// create a token
function createJWT($payload, $secret) {
    $header = base64url_encode(json_encode(["alg" => "HS256", "typ" => "JWT"]));
    $body = base64url_encode(json_encode($payload));
    $signature = base64url_encode(hash_hmac("sha256", "$header.$body", $secret, true));
    return "$header.$body.$signature";
}

// check a token, returns payload array or false
function verifyJWT($token, $secret) {
    $parts = explode(".", $token);
    if (count($parts) != 3) {
        return false;
    }

    list($header, $body, $signature) = $parts;

    $expected = base64url_encode(hash_hmac("sha256", "$header.$body", $secret, true));
    if (!hash_equals($expected, $signature)) {
        return false;   // signature does not match
    }

    $payload = json_decode(base64url_decode($body), true);

    if ($payload["exp"] < time()) {
        return false;   // token expired
    }

    return $payload;
}
