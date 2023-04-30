<?php 

	session_start();

?>
<?php include("connection.php")?>
<!--
<!DOCTYPE html>
<html>
<head>
	<title>admin Panel </title>
</head>
<body>

   <?php // echo "welcome:".  $_SESSION['id']; ?>
   <a href="adminLogout.php"><button class="btnHome">logout</button></a>

</body>
</html>

-->


<!DOCTYPE html>
<html>
<head>
  <title>Add Route</title>
  <!--cdn icon library -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link rel="stylesheet" href="cssfile/sidebar.css">
<link rel="stylesheet" href="cssfile/signUp.css">
	<style type="text/css">

			body{

		  background-image: url("image/20.jpg");
		  background-position: center;
		  background-size: cover;
		  height: 700px;
		  background-repeat: no-repeat;
      background-attachment: fixed;

		}
		.adminTopic{
			text-align: center;
			color: #fff;
			

		}
    .form_wrap .submit_btn:hover{

      color:#fff;
      font-weight: 600;

    }
    .idclass{

      width: 100%;
      border-radius: 3px;
      border: 1px solid #9597a6;
      padding: 10px;
      outline: none;
      color: black;

    }




	</style>
</head>
<body>
  <input type="checkbox" id="check">

  <label for="check">
<i class="fa fa-bars" id="btn"></i>
<i class="fa fa-times" id="cancle"></i>


  </label>
  <div class="sidebar">
<header><img src="image/Re.png">
<p><?php echo $_SESSION['username']; ?></p>
</header>
<ul>

 <li><a href="adminDash.php">Manage Routes</a></li>
    <li><a href="ManagesBuses.php">Manage Buses</a></li>
    <li><a href="BookingManage.php">Booking People</a></li>
    <li><a href="PaymentManage.php">Transaction</a></li>
    <li><a href="adminLogout.php">logout</a></li>
  <!--  <li><a href="#">Event</a></li>
    <li><a href="#">About</a></li>
    <li><a href="#">Service</a></li>
    <li><a href="#">Contact</a></li>-->
    </ul>
 <!--  <li>
      <div class="social-links">
        <a href="#" class="twitter"><i class="fa fa-twitter"></i></a>
        <a href="#" class="facebook"><i class="fa fa-facebook"></i></a>
        <a href="#" class="instagram"><i class="fa fa-instagram"></i></a>
        <a href="#" class="google-plus"><i class="fa fa-youtube"></i></a>
        
      </div>
    </li>-->
   

</div>



<div class="sidebar2">


        <?php 


  if(isset($_POST['routeAdd'])){

     $via_city=$_POST['via_city'];
     $destination=$_POST['destination'];
     $bus_name=$_POST['bus_name'];
     $dep_date=$_POST['departure_date'];
     $dep_time=$_POST['departure_time'];
     $cost=$_POST['cost'];
    

    


       if($conn->connect_error)
          {
            die('Connection Failed :'.$conn->connect_error);
          }
          else
          {

              //$userPay_id = random_num(20);
              $stmt=$conn->prepare("INSERT INTO route(via_city,destination,bus_name,departure_date,departure_time,cost) VALUES(?,?,?,?,?,?)");
              //table3 is the table name//

              $stmt->bind_param("sssssi",$via_city,$destination,$bus_name,$dep_date, $dep_time,$cost);

              $stmt->execute();
              
               echo '<script type="text/javascript">alert("Route add successfully")</script>';
               


              
              $stmt->close();
              $conn->close();
              }
                
          
      }     
  

   ?>




          <div class="wrapper">
  <div class="registration_form">
    <div class="title">
      Adding routes
    </div>

    <form action="#" method="POST">
      <div class="form_wrap">
        
        <div class="input_wrap">
          <label for="title">Via City</label>
          <input type="text" id="title" name="via_city" placeholder="Via_city" required>
        </div>

        <div class="input_wrap">
          <label for="title">Destination</label>
          <input type="text" id="title" name="destination" placeholder="Destination" required>
        </div>


        <div class="input_wrap">
          <label for="title">Bus Name</label>
          <input type="text" id="title" name="bus_name" placeholder="Bus Name"  required>
        </div>

        <div class="input_wrap">
          <label for="title">Departure Date</label>
          <input type="date" id="title" name="departure_date" placeholder="Date of Departure" class="idclass" required>
        </div>

        <div class="input_wrap">
          <label for="title">Departure Time</label>
          <input type="Time" id="title" name="departure_time" placeholder="Time of Departure" class="idclass" required>
        </div>

        <div class="input_wrap">
          <label for="title">Cost</label>
          <input type="text" id="title" name="cost" placeholder="Cost" class="idclass" required>
        </div>
        
        
        <div class="input_wrap">
          <input type="submit" value="Add Route Now" class="submit_btn" name="routeAdd">

        </div>



      </div>
    </form>
  </div>
</div>




</div>

</body>
</html>