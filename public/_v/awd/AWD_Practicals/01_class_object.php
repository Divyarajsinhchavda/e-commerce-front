<?php
// Practical 1: Create a PHP Class and Object

class Student {
    // properties
    public $name;
    public $rollNo;
    public $marks;

    // constructor
    public function __construct($name, $rollNo, $marks) {
        $this->name = $name;
        $this->rollNo = $rollNo;
        $this->marks = $marks;
    }

    // methods
    public function getResult() {
        return $this->marks >= 35 ? "Pass" : "Fail";
    }

    public function display() {
        echo "Name: $this->name <br>";
        echo "Roll No: $this->rollNo <br>";
        echo "Marks: $this->marks <br>";
        echo "Result: " . $this->getResult() . "<br><br>";
    }
}

// create objects
$s1 = new Student("Ravi", 1, 78);
$s2 = new Student("Neha", 2, 30);

$s1->display();
$s2->display();

// change a property
$s2->marks = 50;
echo "After updating marks:<br>";
$s2->display();
