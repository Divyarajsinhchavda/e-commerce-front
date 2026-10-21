<?php
// Practical 13: Simple RESTful API (CRUD on products table)
// URL examples (XAMPP):
//   GET    http://localhost/AWD_Practicals/13_restful_api/api.php          -> all products
//   GET    http://localhost/AWD_Practicals/13_restful_api/api.php?id=1     -> one product
//   POST   api.php   body: {"name":"Eraser","price":5}                     -> create
//   PUT    api.php?id=1   body: {"name":"Pen","price":12}                  -> update
//   DELETE api.php?id=1                                                    -> delete
// Test with Postman or the test.html page.

require "../db.php";
header("Content-Type: application/json");

$method = $_SERVER["REQUEST_METHOD"];
$id = $_GET["id"] ?? null;
$input = json_decode(file_get_contents("php://input"), true);

if ($method == "GET") {
    if ($id) {
        $stmt = $pdo->prepare("SELECT * FROM products WHERE id = ?");
        $stmt->execute([$id]);
        echo json_encode($stmt->fetch(PDO::FETCH_ASSOC));
    } else {
        $stmt = $pdo->query("SELECT * FROM products");
        echo json_encode($stmt->fetchAll(PDO::FETCH_ASSOC));
    }
} elseif ($method == "POST") {
    $stmt = $pdo->prepare("INSERT INTO products (name, price) VALUES (?, ?)");
    $stmt->execute([$input["name"], $input["price"]]);
    echo json_encode(["message" => "Product created", "id" => $pdo->lastInsertId()]);
} elseif ($method == "PUT") {
    $stmt = $pdo->prepare("UPDATE products SET name = ?, price = ? WHERE id = ?");
    $stmt->execute([$input["name"], $input["price"], $id]);
    echo json_encode(["message" => "Product updated"]);
} elseif ($method == "DELETE") {
    $stmt = $pdo->prepare("DELETE FROM products WHERE id = ?");
    $stmt->execute([$id]);
    echo json_encode(["message" => "Product deleted"]);
} else {
    http_response_code(405);
    echo json_encode(["message" => "Method not allowed"]);
}
