<?php
    $numb = escapeshellarg($_POST["numb"]);
    $msg = escapeshellarg($_POST["message"]);
    
    $command = "python3 process.py $numb $msg";
    $output = shell_exec($command);
    
    echo "<div>$output</div>";
?>