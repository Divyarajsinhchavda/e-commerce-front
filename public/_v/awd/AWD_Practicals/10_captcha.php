<?php
// Practical 10: Google reCAPTCHA v2 in a form
// These are Google's public TEST keys (always pass). Replace with your own keys from
// https://www.google.com/recaptcha/admin for a real website.
$siteKey = "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI";
$secretKey = "6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe";

$message = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $captcha = $_POST["g-recaptcha-response"] ?? "";

    if ($captcha == "") {
        $message = "Please tick the captcha box";
    } else {
        // ask Google to verify the captcha
        $url = "https://www.google.com/recaptcha/api/siteverify?secret=" . $secretKey . "&response=" . $captcha;
        $response = file_get_contents($url);
        $result = json_decode($response, true);

        if ($result["success"]) {
            $message = "Captcha verified. Welcome, " . htmlspecialchars($_POST["name"]) . "!";
        } else {
            $message = "Captcha failed. You may be a bot.";
        }
    }
}
?>
<!DOCTYPE html>
<html>
<head>
    <script src="https://www.google.com/recaptcha/api.js" async defer></script>
</head>
<body>
    <h3>Form with reCAPTCHA</h3>
    <p><?php echo $message; ?></p>
    <form method="post">
        Name: <input type="text" name="name" required><br><br>
        <div class="g-recaptcha" data-sitekey="<?php echo $siteKey; ?>"></div><br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
