<?php
session_start();
error_reporting(0);
include('includes/dbconnection.php');
$admin_id = $_SESSION['admin_id'];
?>


<div id="sidebar-collapse" class="col-sm-3 col-lg-2 sidebar">
        <div class="profile-sidebar">
            <div class="profile-userpic">
                <img src="   https://cdn-icons-png.flaticon.com/512/7124/7124675.png " class="img-responsive" alt="">
            </div>
            <div class="profile-usertitle">
                <?php
                    $uid=$_SESSION['detsuid'];
                    $ret=mysqli_query($con,"select username from admin where id='$admin_id'");
                    $row=mysqli_fetch_array($ret);
                    $name=$row['username'];
                ?>
                <div class="profile-usertitle-name"><?php echo $name; ?></div>
                <div class="profile-usertitle-status"><span class="indicator label-success"></span>Online</div>
            </div>
            <div class="clear"></div>
        </div>
        <div class="divider"></div>
        <ul class="nav menu">
            <li class=<?php if($_SERVER['REQUEST_URI'] == '/de/admin-dashboard.php') echo 'active';  ?>><a href="admin-dashboard.php"><em class="fa fa-dashboard">&nbsp;</em> Dashboard</a></li>
            <li class=<?php if($_SERVER['REQUEST_URI'] == '/de/admin-change-password.php') echo 'active';  ?>><a href="admin-change-password.php"><em class="fa fa-clone">&nbsp;</em> Change Password</a></li>
            <li><a href="admin-logout.php"><em class="fa fa-power-off">&nbsp;</em> Logout</a></li>
        </ul>
    </div>