<?php
$color = $_GET["BALL"];
$ball = $color

$color1 = $_GET["CLIENT"];
$client = $color1 


function callpy($arg1 , $arg2) {
           $command= exec("python3 app_color.py $arg1 $arg2");
           return $command ;
        }
$command= callpy($ball , $client);
echo "ball：".$ball."\n"."client：".$client."\n".$command;
?>
