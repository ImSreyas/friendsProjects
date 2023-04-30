<?php
session_start();
error_reporting(0);
include('includes/dbconnection.php');
if(!isset($_SESSION['admin_id'])){
    header('location: index.php');
}
?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Daily Expense Tracker - Dashboard</title>
	<link href="css/bootstrap.min.css" rel="stylesheet">
	<link href="css/font-awesome.min.css" rel="stylesheet">
	<link href="css/datepicker3.css" rel="stylesheet">
	<link href="css/styles.css" rel="stylesheet">
	
	<!--Custom Font-->
	<link href="https://fonts.googleapis.com/css?family=Montserrat:300,300i,400,400i,500,500i,600,600i,700,700i" rel="stylesheet">
	<!--[if lt IE 9]>
	<script src="js/html5shiv.js"></script>
	<script src="js/respond.min.js"></script>
	<![endif]-->
</head>
<body>
	<?php include_once('includes/header.php');?>
	<?php include_once('includes/adminSidebar.php');?>
    <div class="col-sm-9 col-sm-offset-3 col-lg-10 col-lg-offset-2 main">
        <div class="main-body-container">
            <div class="user-list-header">user list</div>
            <div class="user-list-body">
                <?php 
                    $userListQuery = mysqli_query($con,"select * from tbluser");
                    while($userList = $userListQuery->fetch_assoc()){
                        ?>

                            <div class="user-card">
                                <div class="user-header"><?php echo $userList['FullName'] ?></div>
                                <div class="user-body">
                                    <div><?php echo $userList['Email'] ?></div>
                                    <div><?php echo $userList['MobileNumber'] ?></div>
                                    <div><?php echo $userList['RegDate'] ?></div>
                                </div>
                                <div class="delete-btn-container">
                                    <a href="deleteUser.php?user_id=<?php echo $userList['ID'] ?>" class="delete-btn">Delete</a>
                                </div>
                            </div>

                        <?php
                    }
                ?>
            </div>
        </div>
    </div>
</body>
</html>