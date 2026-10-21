<?php
// Practical 3: Error Handling with Try-Catch and Custom Exception

// Custom exception class
class AgeException extends Exception {
    public function errorMessage() {
        return "Custom Error: " . $this->getMessage();
    }
}

// Function that throws exceptions
function checkAge($age) {
    if (!is_numeric($age)) {
        throw new Exception("Age must be a number");
    }
    if ($age < 18) {
        throw new AgeException("Age $age is below 18, not allowed");
    }
    return "Age $age is valid";
}

function divide($a, $b) {
    if ($b == 0) {
        throw new Exception("Cannot divide by zero");
    }
    return $a / $b;
}

// Test 1: normal exception
try {
    echo divide(10, 2) . "<br>";
    echo divide(10, 0) . "<br>";
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "<br>";
} finally {
    echo "Division test finished<br><br>";
}

// Test 2: custom exception
try {
    echo checkAge(25) . "<br>";
    echo checkAge(15) . "<br>";
} catch (AgeException $e) {
    echo $e->errorMessage() . "<br>";
} catch (Exception $e) {
    echo "General Error: " . $e->getMessage() . "<br>";
}
