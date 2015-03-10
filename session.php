<?php 

    //error handler function
    function customError($errno, $errstr) {
      echo "
* Error : [$errno] 
* $errstr !
";
    }

    //set error handler
    set_error_handler("customError");
      ?>