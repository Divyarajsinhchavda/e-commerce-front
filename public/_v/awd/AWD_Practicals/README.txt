ADVANCE WEB DEVELOPMENT (BETCE15316) - PHP PRACTICALS
=====================================================

HOW TO RUN
1. Install XAMPP and start Apache + MySQL.
2. Copy this whole folder (AWD_Practicals) into  C:\xampp\htdocs\
3. Open phpMyAdmin (http://localhost/phpmyadmin), go to the SQL tab,
   paste the contents of database.sql and run it.
4. Open the practicals in your browser, for example:
   http://localhost/AWD_Practicals/01_class_object.php

FILES
01_class_object.php          Class and object
02_inheritance_abstract.php  Inheritance, method overriding, abstract class
03_try_catch.php             Try-catch with custom exception
04_pdo_select.php            PDO connection and SELECT query   (needs database.sql)
05_prepared_statement.php    Prepared statements, SQL injection safe  (needs database.sql)
06_pdo_transaction.php       PDO transaction with commit/rollback    (needs database.sql)
07_session_login/            Login, dashboard, logout using sessions (open login.php)
08_form_validation.php       Form validation and sanitization
09_file_upload.php           Secure file upload (creates uploads/ folder itself)
10_captcha.php               Google reCAPTCHA (uses Google test keys, needs internet)
11_ajax/                     AJAX with fetch (open index.html)       (needs database.sql)
12_json.php                  json_encode and json_decode
13_restful_api/              REST API CRUD (open test.html)          (needs database.sql)
14_jwt/                      JWT login and secured API (open test.html)
15_third_party_api.php       Weather API (needs internet)

NOTES
- db.php holds the database login. Default is user root, empty password (XAMPP).
- Practical 10: the keys inside are Google's public test keys. For a real site,
  get your own keys from https://www.google.com/recaptcha/admin
- Login for practicals 7 and 14: admin / 1234
