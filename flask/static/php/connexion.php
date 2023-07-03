<?php
// Connexion à la base de données
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "login";

$conn = mysqli_connect($servername, $username, $password, $dbname);

// Vérification de la connexion
if (!$conn) {
	die("La connexion a échoué : " . mysqli_connect_error());
}

// Vérification des données du formulaire
$email = $_POST["email"];
$password = $_POST["password"];

// Récupération du hachage de mot de passe de l'utilisateur correspondant à l'adresse e-mail fournie
$sql = "SELECT * FROM utilisateurs WHERE email='$email'";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
	$row = mysqli_fetch_assoc($result);
	$hash = $row["password"];
	
	// Vérification du mot de passe
	if (password_verify($password, $hash)) {
		// Connexion réussie, rediriger vers la page d'accueil
		header("Location: index.html");
		exit;
	} else {
		// Mot de passe incorrect
		header("Location: connexion.php?erreur=mot_de_passe_incorrect");
		exit;
	}
} else {
	// Adresse e-mail non trouvée
	header("Location: connexion.php?erreur=adresse_email_non_trouvee");
	exit;
}

// Fermeture de la connexion à la base de données
mysqli_close($conn);
?>