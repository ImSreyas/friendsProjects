
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Ebus Login</title>
    <link rel="stylesheet" href="cssfile/nav.css">
    <link rel="stylesheet" href="cssfile/footer_l.css">
    <!--  <link rel="stylesheet" type="text/css" href="cssfile/container.css">-->
    <link rel="stylesheet" href="cssfile/login.css">
    <link rel="stylesheet" a href="css\font-awesome.min.css">
   
    <link href="http://fonts.googleapis.com/css?family=Cookie" rel="stylesheet" type="text/css">
   <!-- <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css">-->
    <script src="https://kit.fontawesome.com/a076d05399.js"></script>
    <script src="https://kit.fontawesome.com/a076d05399.js"></script>
    <script src="https://code.jquery.com/jquery-3.4.1.js"></script>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://pro.fontawesome.com/releases/v5.10.0/css/all.css" integrity="sha384-AYmEC3Yw5cVb3ZcuHtOA93w35dYTsvhLPVnYs9eStHfGJvOvKxVfELGroGkvsg+p" crossorigin="anonymous"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"/>
    


    <style type="text/css">


       body{
                margin: 0;
                padding: 0;
                width: 100%;
                height: 100%;
                background-image: url(image/2233.jpg);
                background-repeat: no-repeat;
                background-attachment: fixed;
                background-size: cover;

            }
            .sign_up{

                font-size: 20px;

            }
            .sign_up:hover{

                background-color: #fff;
                

            }

     

      
    </style>

  </head>
  <body>




              <!--this is the header callling(nav bar)-->
            <?php include("nav.php");
             ?>




             <?php 

session_start();

    include("connection.php");
    include("function.php");


    if($_SERVER['REQUEST_METHOD'] == "POST")
    {
        //something was posted
        $user_name = $_POST['user_name'];
        $password = $_POST['password'];

        if(!empty($user_name) && !empty($password) && !is_numeric($user_name))
        {

            //read from database
            $query = "select * from users where username = '$user_name' limit 1";
            $result = mysqli_query($conn, $query);

            if($result)
            {
                if($result && mysqli_num_rows($result) > 0)
                {

                    $user_data = mysqli_fetch_assoc($result);
                    
                    if($user_data['password'] === $password)
                    {

                        $_SESSION['user_id'] = $user_data['user_id'];
                        header("Location:viewBus.php");
                        die;
                    }
                }
            }
            
            echo "wrong username or password!";
        }else
        {
            echo "wrong username or password!";
        }
    }

?>







<!------------------------------------------------------------------>
 <div class="login-box">
    <img src="image/avatar.png" class="avatar">
        <h1>Login For Ebus</h1>
            <form method="post">
            <p>Username</p>
            <input type="text" name="user_name" placeholder="Enter Username">
            <p>Password</p>
            <input type="password" name="password" placeholder="Enter Password">
            <input type="submit" name="login" value="Login">
            <a href="signUp.php" class="sign_up">sign up</a>&nbsp&nbsp&nbsp
            <a href="#">Forget Password</a>    
            </form>
        
        
        </div>
    


 
            
 <!------------------------------------------------------------------>

           



  </body>
</html>
