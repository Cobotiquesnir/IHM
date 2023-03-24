<html>


<body>

	<h1>Clique sur le boutton pour lancer le programme</h1>
	<form name="update" method="post">
		<button name="update" type="submit"> Clique </button>
	</form>
	



<?php

	if (isset($_POST['update']))
	{

		echo shell_exec("python cam.py");
		//echo shell_exec("python cam.py 2>&1");
	}

?>


</body>



</html>
