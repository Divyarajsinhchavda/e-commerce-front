<?php
// Practical 2: Inheritance and Abstract Classes

// Parent class
class Animal {
    public $name;

    public function __construct($name) {
        $this->name = $name;
    }

    public function sound() {
        return "Some sound";
    }

    public function show() {
        echo "$this->name says: " . $this->sound() . "<br>";
    }
}

// Child class (overrides sound method)
class Dog extends Animal {
    public function sound() {
        return "Bark";
    }
}

class Cat extends Animal {
    public function sound() {
        return "Meow";
    }
}

echo "<h3>Inheritance</h3>";
$a = new Animal("Animal");
$d = new Dog("Tommy");
$c = new Cat("Kitty");
$a->show();
$d->show();
$c->show();

// Abstract class
abstract class Shape {
    abstract public function area();   // child must define this

    public function show() {
        echo "Area = " . $this->area() . "<br>";
    }
}

class Circle extends Shape {
    private $r;
    public function __construct($r) { $this->r = $r; }
    public function area() { return 3.14 * $this->r * $this->r; }
}

class Rectangle extends Shape {
    private $l, $b;
    public function __construct($l, $b) { $this->l = $l; $this->b = $b; }
    public function area() { return $this->l * $this->b; }
}

echo "<h3>Abstract Class</h3>";
$circle = new Circle(5);
$rect = new Rectangle(4, 6);
echo "Circle: ";
$circle->show();
echo "Rectangle: ";
$rect->show();
