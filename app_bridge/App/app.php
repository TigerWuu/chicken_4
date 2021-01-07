<?php
$color = $_GET["BALL"];
if($color =="Red")
{
$ball = "Red";
}
elseif($color =="Yellow")
{
$ball = "Yellow";
}
elseif($color =="Purple")
{
$ball = "Purple";
}
elseif($color =="Blue")
{
$ball = "Blue";
}
elseif($color =="Green")
{
$ball = "Green";
}
$color1 = $_GET["CLIENT"];
if($color1 =="Red")
{
$client = "Red";
}
elseif($color1 =="Yellow")
{
$client = "Yellow";
}
elseif($color1 =="Purple")
{
$client = "Purple";
}
elseif($color1 =="Blue")
{
$client = "Blue";
}
elseif($color1 =="Green")
{
$client = "Green";
}

function callpy($arg1 , $arg2) {
           $command= exec('export PYTHONPATH=$PYTHONPATH:/opt/ros/melodic/lib/python2.7/dist-packages && python3 app_color.py '.$arg1.' '.$arg2);
           return $command ;
        }
$command= callpy($ball , $client);
echo "ball：".$ball."\n"."client：".$client."\n".$command;
?>
