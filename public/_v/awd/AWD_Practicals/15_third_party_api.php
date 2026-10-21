<?php
// Practical 15: Consume Third-Party API (Open-Meteo weather API, no API key needed)
$city = "Bhavnagar";
$lat = 21.77;
$lon = 72.15;

$url = "https://api.open-meteo.com/v1/forecast?latitude=$lat&longitude=$lon&current_weather=true";

$response = file_get_contents($url);

if ($response === false) {
    die("Could not connect to the weather API");
}

$data = json_decode($response, true);
$weather = $data["current_weather"];
?>
<!DOCTYPE html>
<html>
<body>
    <h3>Weather in <?php echo $city; ?></h3>
    <table border="1" cellpadding="8">
        <tr><td>Temperature</td><td><?php echo $weather["temperature"]; ?> &deg;C</td></tr>
        <tr><td>Wind Speed</td><td><?php echo $weather["windspeed"]; ?> km/h</td></tr>
        <tr><td>Wind Direction</td><td><?php echo $weather["winddirection"]; ?>&deg;</td></tr>
        <tr><td>Time</td><td><?php echo $weather["time"]; ?></td></tr>
    </table>
</body>
</html>
