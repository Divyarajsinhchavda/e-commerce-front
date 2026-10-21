<?php
// Practical 6: PDO Transactions (money transfer: both queries succeed or none)
require "db.php";

$amount = 200;

try {
    $pdo->beginTransaction();

    // take money from Account A
    $stmt1 = $pdo->prepare("UPDATE accounts SET balance = balance - :amt WHERE name = 'Account A'");
    $stmt1->execute([":amt" => $amount]);

    // add money to Account B
    $stmt2 = $pdo->prepare("UPDATE accounts SET balance = balance + :amt WHERE name = 'Account B'");
    $stmt2->execute([":amt" => $amount]);

    // to test rollback, uncomment the next line:
    // throw new Exception("Something went wrong!");

    $pdo->commit();   // save both changes
    echo "Transaction successful: $amount transferred.<br><br>";
} catch (Exception $e) {
    $pdo->rollBack(); // undo both changes
    echo "Transaction failed, rolled back: " . $e->getMessage() . "<br><br>";
}

// show balances
$rows = $pdo->query("SELECT * FROM accounts")->fetchAll(PDO::FETCH_ASSOC);
foreach ($rows as $r) {
    echo $r['name'] . " : " . $r['balance'] . "<br>";
}
