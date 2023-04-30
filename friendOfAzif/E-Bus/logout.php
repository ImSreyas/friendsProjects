<?php

session_start();

if(isset($_SESSION['user_id']))
{
	unset($_SESSION['user_id']);

}
echo ("<script LANGUAGE='JavaScript'>
    window.alert('Do you need to Logout?');
    window.location.href='Login.php';
    </script>");

//header("Location: Login.php");
die;