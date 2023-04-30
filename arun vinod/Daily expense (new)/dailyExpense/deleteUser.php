<?php
session_start();
error_reporting(0);
include('includes/dbconnection.php');
if(!isset($_SESSION['admin_id'])){
    if(isset($_SESSION['detsuid'])){
        header('location: dashboard.php');
    } else {
        header('location: index.php');
    }
}
$user_id = $_GET['user_id'];
mysqli_query($con, "delete from tbluser where ID='$user_id'") or mysqli_error($conn);
header('location: admin-dashboard.php');
?>