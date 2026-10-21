<?php
// Practical 7: Logout (destroy session)
session_start();
session_unset();
session_destroy();
header("Location: login.php");
exit;
