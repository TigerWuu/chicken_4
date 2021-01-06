<!DOCTYPE html>
<html>
    <head>
    <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge,chrome=1">
        <title>執行python</title>
    </head>

    <body>
         <!-- 選擇按鈕 -->
         <p>
            <form method="post">
            <p><strong>請選擇球的顏色</strong>:
                <input type="radio" name="ball" value="red">red
                <input type="radio" name="ball" value="yellow">yellow
                <input type="radio" name="ball" value="orange">orange
                <input type="radio" name="ball" value="green">green
                <input type="radio" name="ball" value="purple">purple
                <input type="radio" name="ball" value="blue">blue
            </p>
            <p><strong>請選擇目的地的顏色</strong>:
                <input type="radio" name="home" value="red">red
                <input type="radio" name="home" value="yellow">yellow
                <input type="radio" name="home" value="orange">orange
                <input type="radio" name="home" value="green">green
                <input type="radio" name="home" value="blue">blue
            </p>
            <input type="submit" name="submit" value="送出">
            </form>
        </p>

        <?php
            $ball = $_POST['ball'];
            $home =$_POST['home'];

            echo "$ball"." "."$home".'<br>';
            
	    if( isset($ball) && isset($home)){
		    $output = exec('export PYTHONPATH=$PYTHONPATH:/opt/ros/melodic/lib/python2.7/dist-packages && python3 app_color.py '.$ball." ".$home , $out ,$retval);
		    echo "$output". '<br>' ;
		    echo "$out". '<br>' ;
		    echo "$retval";
	    }
            
        ?>
    </body>
</html>
