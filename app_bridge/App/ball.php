<?php
$color = $_GET["BALL"];
$ball = $color

$color1 = $_GET["CLIENT"];
$client = $color1 


function callpy($arg) {
            $command= exec("python3 app_color.py $arg");
           return $command ;
        }
$command= callpy($ball);
echo "ball：".$ball."\n"."client：".$client."\n".$command;
?>
