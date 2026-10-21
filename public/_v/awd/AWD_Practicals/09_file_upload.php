<?php
// Practical 9: Secure File Upload
$message = "";

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_FILES["myfile"])) {
    $file = $_FILES["myfile"];

    $allowedTypes = ["image/jpeg", "image/png", "application/pdf"];
    $allowedExt = ["jpg", "jpeg", "png", "pdf"];
    $maxSize = 2 * 1024 * 1024;   // 2 MB

    // basename() removes folder parts like ../  (prevents directory traversal)
    $originalName = basename($file["name"]);
    $ext = strtolower(pathinfo($originalName, PATHINFO_EXTENSION));

    // check real file type (not what the browser says)
    $finfo = new finfo(FILEINFO_MIME_TYPE);
    $realType = $finfo->file($file["tmp_name"]);

    if ($file["error"] != 0) {
        $message = "Upload error";
    } elseif ($file["size"] > $maxSize) {
        $message = "File is too large (max 2 MB)";
    } elseif (!in_array($ext, $allowedExt) || !in_array($realType, $allowedTypes)) {
        $message = "Only JPG, PNG and PDF files are allowed";
    } else {
        // make a new random file name
        $newName = uniqid("file_", true) . "." . $ext;

        if (!is_dir("uploads")) {
            mkdir("uploads");
        }

        if (move_uploaded_file($file["tmp_name"], "uploads/" . $newName)) {
            $message = "File uploaded as $newName";
        } else {
            $message = "Could not save file";
        }
    }
}
?>
<!DOCTYPE html>
<html>
<body>
    <h3>Secure File Upload</h3>
    <p><?php echo htmlspecialchars($message); ?></p>
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="myfile" required><br><br>
        <button type="submit">Upload</button>
    </form>
    <p>Allowed: JPG, PNG, PDF. Max size: 2 MB.</p>
</body>
</html>
