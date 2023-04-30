<?php
session_start();
error_reporting(0);
include('includes/dbconnection.php');
if(!isset($_SESSION['admin_id'])){
    header('location: index.php');
}
$admin_id = $_SESSION['admin_id'];
$currentPassword = '';
$newPassword = '';
if(isset($_POST['submit']))
{
    $currentPassword = $_POST['currentpassword'];
    $newPassword = $_POST['newpassword'];

    $adminList = mysqli_query($con, "select * from admin where id='$admin_id' and password='$currentPassword'");
    if($adminList->num_rows > 0){
        mysqli_query($con, "update admin set password='$newPassword' where id='$admin_id'") or mysqli_error($con);
        $successMessage = "Password changed successfully.";
        //- changing it to empty. so it wont appear on the textbox.
        $currentPassword = '';
        $newPassword = '';
    } else {
        $msg = "Current Password is wrong.";
    }
}
?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Daily Expense Tracker || Change Password</title>
	<link href="css/bootstrap.min.css" rel="stylesheet">
	<link href="css/font-awesome.min.css" rel="stylesheet">
	<link href="css/datepicker3.css" rel="stylesheet">
	<link href="css/styles.css" rel="stylesheet">
	
	<!--Custom Font-->
	<link href="https://fonts.googleapis.com/css?family=Montserrat:300,300i,400,400i,500,500i,600,600i,700,700i" rel="stylesheet">
	<script type="text/javascript">
        function checkpass()
        {
        if(document.changepassword.newpassword.value!=document.changepassword.confirmpassword.value)
        {
        alert('New Password and Confirm Password field does not match');
        document.changepassword.confirmpassword.focus();
        return false;
        }
        return true;
        } 
    </script>
</head>
<body>
	<?php include_once('includes/header.php');?>
	<?php include_once('includes/adminSidebar.php');?>
		
	<div class="col-sm-9 col-sm-offset-3 col-lg-10 col-lg-offset-2 main">
		<div class="row">
			<ol class="breadcrumb">
				<li><a href="#">
					<em class="fa fa-home"></em>
				</a></li>
				<li class="active">Change Password</li>
			</ol>
		</div><!--/.row-->
		
		
				
		
		<div class="row">
			<div class="col-lg-12">
			
				
				
				<div class="panel panel-default rp">
					<div class="panel-heading">Change Password</div>
					<div class="panel-body">
						<p style="font-size:16px; color:red" align="center"> 
                        <?php 
                            if(isset($msg)){
                                echo $msg; 
                            }  
                        ?> 
                        </p>
                        <p style="font-size:16px; color:#0ac200" align="center"> 
                        <?php 
                            if(isset($successMessage)){
                                echo $successMessage; 
                            }  
                        ?> 
                        </p>
						<div class="col-md-12">
							<form role="form" method="post" action="" name="changepassword" onsubmit="return checkpass();">
								<div class="form-group">
									<label>Current Password</label>
									<input type="password" name="currentpassword" class=" form-control" required= "true" value="<?php echo $currentPassword ?>">
								</div>
								<div class="form-group">
									<label>New Password</label>
									<input type="password" name="newpassword" class="form-control" value="<?php echo $newPassword ?>" required="true">
								</div>
								
								<div class="form-group">
									<label>Confirm Password</label>
									<input type="password" name="confirmpassword" class="form-control" value="<?php echo $newPassword ?>" required="true">
								</div>
								
								<div class="form-group has-success">
									<button type="submit" class="btn btn-primary" name="submit">Change</button>
								</div>
								
								
								</div>
							</form>
						</div>
					</div>
				</div><!-- /.panel-->
			</div><!-- /.col-->
			<?php include_once('includes/footer.php');?>
		</div><!-- /.row -->
	</div><!--/.main-->
	
<script src="js/jquery-1.11.1.min.js"></script>
	<script src="js/bootstrap.min.js"></script>
	<script src="js/chart.min.js"></script>
	<script src="js/chart-data.js"></script>
	<script src="js/easypiechart.js"></script>
	<script src="js/easypiechart-data.js"></script>
	<script src="js/bootstrap-datepicker.js"></script>
	<script src="js/custom.js"></script>
</body>
</html>
