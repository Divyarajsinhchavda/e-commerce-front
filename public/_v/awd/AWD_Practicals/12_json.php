<?php
// Practical 12: JSON Data Handling in PHP

// 1) PHP array -> JSON string
$students = [
    ["id" => 1, "name" => "Ravi", "marks" => 78],
    ["id" => 2, "name" => "Neha", "marks" => 85],
    ["id" => 3, "name" => "Amit", "marks" => 62]
];

$jsonString = json_encode($students, JSON_PRETTY_PRINT);

echo "<h3>Array encoded to JSON</h3>";
echo "<pre>" . $jsonString . "</pre>";

// 2) JSON string -> PHP array
$jsonInput = '{"name":"Priya","city":"Bhavnagar","age":20}';

$data = json_decode($jsonInput, true);   // true = give associative array

echo "<h3>JSON decoded to PHP array</h3>";
echo "Name: " . $data["name"] . "<br>";
echo "City: " . $data["city"] . "<br>";
echo "Age: " . $data["age"] . "<br>";

echo "<h3>print_r of decoded array</h3>";
echo "<pre>";
print_r($data);
echo "</pre>";
