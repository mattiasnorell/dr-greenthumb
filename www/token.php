<?php
	if($_GET['hub_verify_token'] == 'calling_dr_green_thumb'){
		echo $_GET['hub_challenge'];
	}

//	echo $_GET['test'];


?>
