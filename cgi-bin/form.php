<?php 
	 
	$uname = $_POST["uname"];
	//$lastName = $_POST["lastName"];
	//$email = $_POST["email"];
	//$message =$_POST["message"];
    //$human = $_POST["human"];
	//$from = "From: Resume Website";
	//$to = "elwincab@buffalo.edu";
	//$subject ="Hello";
    
	
	//$body = "From: $firstName $lastName\n E-Mail: $email\n Message:\n $message";
	
	if ($_POST["submit"]) {
    	if ($firstName != "" && $email != "" && $lastName != "") {
        	if ($human == "4") {				 
            	if (mail ($to, $subject, $body, $from)) { 
	        		echo "<p>Your message has been sent!</p>";
	    		} else { 
	        		echo "<p>Something went wrong, go back and try again!</p>"; 
	    		}	 
			} else if ($_POST["submit"] && $human != "4") {
	    		echo "<p>You answered the anti-spam question incorrectly!</p>";
			}
    	} else {
        	echo "<p>You need to fill in all required fields!!</p>";
    	}
	}
	
 
 
	
?>
