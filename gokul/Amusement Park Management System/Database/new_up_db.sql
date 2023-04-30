/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.7.9 : Database - amusement_park
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`amusement_park` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `amusement_park`;

/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `booking_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `ride_id` int(11) DEFAULT NULL,
  `book_date` date DEFAULT NULL,
  `book_status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`booking_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `booking` */

/*Table structure for table `customer` */

DROP TABLE IF EXISTS `customer`;

CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `age` varchar(50) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `customer` */

insert  into `customer`(`customer_id`,`login_id`,`name`,`age`,`address`,`email`,`phone`,`place`) values (2,3,'Bency Baby','25','Modiyil','bency@gmail.com','8978675671','Alappuzha'),(3,4,'Blesson Baby','21','Modiyil','blesson@gmail.com','9656323075','Alappuzha');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `feedback` varchar(500) DEFAULT NULL,
  `reply` varchar(500) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`customer_id`,`feedback`,`reply`,`date`) values (2,2,'Hellooo','Hellooo','2022-03-28');

/*Table structure for table `food_menu` */

DROP TABLE IF EXISTS `food_menu`;

CREATE TABLE `food_menu` (
  `food_id` int(11) NOT NULL AUTO_INCREMENT,
  `park_id` int(11) DEFAULT NULL,
  `food_name` varchar(50) DEFAULT NULL,
  `price` varchar(50) DEFAULT NULL,
  `image` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`food_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `food_menu` */

insert  into `food_menu`(`food_id`,`park_id`,`food_name`,`price`,`image`) values (1,2,'Burgur','100','static/uploads/94e20330-62dc-41bf-ac1b-b4b2e89b5530OIP.jpg'),(2,2,'Pizza','250','static/uploads/ef80d739-3316-428a-8694-e5ec8a39dc4fOIP (1).jpg'),(3,2,'Hotdog','150','static/uploads/782da231-d2fd-47c8-865f-4438e43619a3OIP (3).jpg');

/*Table structure for table `food_order` */

DROP TABLE IF EXISTS `food_order`;

CREATE TABLE `food_order` (
  `fd_id` int(11) NOT NULL AUTO_INCREMENT,
  `food_id` int(11) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `order_status` varchar(50) DEFAULT NULL,
  `quantity` varchar(50) DEFAULT NULL,
  `total_amount` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`fd_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `food_order` */

insert  into `food_order`(`fd_id`,`food_id`,`customer_id`,`order_status`,`quantity`,`total_amount`) values (1,1,2,'Order Accept','7','700'),(2,2,2,'Order Accept','3','750');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `usertype` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(3,'bency','bency','Customer'),(4,'bless','bless','Customer'),(7,'libi','libi','staff'),(8,'anu','anu','staff');

/*Table structure for table `park_register` */

DROP TABLE IF EXISTS `park_register`;

CREATE TABLE `park_register` (
  `park_id` int(11) NOT NULL AUTO_INCREMENT,
  `park_name` varchar(50) DEFAULT NULL,
  `park_image` varchar(500) DEFAULT NULL,
  `park_des` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`park_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `park_register` */

insert  into `park_register`(`park_id`,`park_name`,`park_image`,`park_des`) values (2,'Veegaland','static/uploads/d667b6c9-f57e-4ce9-ae0f-a24b341a0b5adf.jpg','Water Theme Park'),(3,'Wonderla','static/uploads/669b2870-adce-4d40-b577-2788d2a49a05ed.jpg','Theme Park');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` int(11) DEFAULT NULL,
  `pay_status` varchar(50) DEFAULT NULL,
  `pay_date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

/*Table structure for table `price` */

DROP TABLE IF EXISTS `price`;

CREATE TABLE `price` (
  `price_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `ride_id` int(11) DEFAULT NULL,
  `new_price` varchar(50) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  PRIMARY KEY (`price_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `price` */

insert  into `price`(`price_id`,`staff_id`,`ride_id`,`new_price`,`start_date`,`end_date`) values (1,2,1,'600','2022-03-30','2022-04-07'),(2,2,1,'600','2022-03-31','2022-04-06');

/*Table structure for table `rides` */

DROP TABLE IF EXISTS `rides`;

CREATE TABLE `rides` (
  `ride_id` int(11) NOT NULL AUTO_INCREMENT,
  `park_id` int(11) DEFAULT NULL,
  `ride_name` varchar(50) DEFAULT NULL,
  `ride_description` varchar(300) DEFAULT NULL,
  `ride_amount` varchar(50) DEFAULT NULL,
  `ride_image` varchar(500) DEFAULT NULL,
  `max_capacity` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ride_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `rides` */

insert  into `rides`(`ride_id`,`park_id`,`ride_name`,`ride_description`,`ride_amount`,`ride_image`,`max_capacity`) values (1,2,'Abc','abc','1000','static/uploads/e23a5a91-9c61-4b56-8b7c-8a9486628195ab.jpg','24'),(2,3,'Abc','abc','1000','static/uploads/8476f6d0-9362-42b7-868d-2bba669fdc2edff.jpg','30');

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `park_id` int(11) DEFAULT NULL,
  `login_id` int(11) DEFAULT NULL,
  `staff_name` varchar(50) DEFAULT NULL,
  `staff_address` varchar(200) DEFAULT NULL,
  `staff_email` varchar(50) DEFAULT NULL,
  `staff_phone` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`park_id`,`login_id`,`staff_name`,`staff_address`,`staff_email`,`staff_phone`) values (2,2,7,'Libin Mathew','ABCD','libi@gmail.com','9196564323'),(3,3,8,'Anu Elsa','Modiyil','anu@gmail.com','8978675671');

/*Table structure for table `ticket` */

DROP TABLE IF EXISTS `ticket`;

CREATE TABLE `ticket` (
  `ticket_id` int(11) NOT NULL AUTO_INCREMENT,
  `price_id` int(11) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `ticket_status` varchar(50) DEFAULT NULL,
  `quantity` varchar(50) DEFAULT NULL,
  `total_amount` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ticket_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `ticket` */

insert  into `ticket`(`ticket_id`,`price_id`,`customer_id`,`ticket_status`,`quantity`,`total_amount`) values (16,2,2,'Booking Accept','6','3600'),(17,1,2,'Booking Reject','1','600'),(18,1,2,'Pending','7','4200');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
