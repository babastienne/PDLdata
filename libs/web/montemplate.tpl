<html>
	<head>
		<!-- Javascript -->
		<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.0/jquery.min.js"></script>
		<script type="text/javascript" src="script/scroll.js"></script>

		<title>Installations sportives | Pays de la Loire</title>
		<meta charset="utf-8"/>
		<meta name="description" content=""/>
		<meta name="keywords" content=""/>
		<link rel="shortcut icon" type="image/x-icon" href="img/favicon.ico" />
		<link rel="stylesheet" type="text/css" href="css/style.css"/>
	</head>

	<body>
		<div id="page">

	
			<div id="head">
			
				<div id="logonom"><a href="index.html"><img src="img/logo.png" alt=""></a>
				<h1><a href="index.html">Pays de la Loire - Installations sportives et activités communales</a></h1></div>
				
			
			
				<ul id="nav" class>
					<li><a href="index.html">Accueil</a></li>
					<li><a href="#">Clips</a></li>
					<li><a href="#">Concerts</a></li>
					<li><a href="#">Contact</a></li>
				</ul>
				
				<div id="ligne" class></div>
			</div>

		
			<div id="contenu">	

				<h2>Informations</h2>

				<p><b>Une page répertoriant les différentes installations sportives et activités disponibles dans les Pays de la Loire</b></p>
				<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras eleifend quam convallis, viverra nunc sit amet, rhoncus risus. Donec leo felis, porta eget fermentum sed, semper ut massa. Nam tempus est sit amet cursus pellentesque. Donec ut ex mollis nisl imperdiet viverra. In volutpat ullamcorper accumsan. Cras consectetur euismod diam, sit amet pharetra dolor vulputate non. Etiam efficitur nunc non consequat ornare. Duis pellentesque sit amet ipsum sit amet fermentum. </p>
				<p>Ce site a été imaginé dans le cadre d'un cours. Pour plus d'informations voir la section mentions légales</p>

				<hr/>
				%if commune == 'void':
					<h1>PAS DE COMMUNE</h1>
				%else:
					<h1>Commune : {{commune}}</h1>
				%end
							<h2>Formulaire de selection</h2>
									<p>Utilisez ce formulaire pour rechercher des installations près de chez vous :</p>
						
				<!-- formulaire -->
				<form action="/action" method="get">

					<div>Commune :</div>
					<input type="text" name="commune"/>
					<div>Activité :</div>
					<input type="text" name="activite"/>
					<div>Installation :</div>
					<input type="text" name="installation"/>

					<input type="submit" name="Envoyer"/>

				</form>

				<hr/>
				<h2>Mentions légales</h2>
				<p>Site entièrement imaginé et conçu dans le cadre d'un projet de travail autour du language Python à l'<a href="http://www.iutnantes.univ-nantes.fr/">IUT de Nantes section Info</a>. Conçu  par : Julien NACHOUKI - Bastien POTIRON</p>

				<p><strong>Pour tout contact : </strong><u>Tel :</u> 02.01.03.04.05<u>E-mail :</u> <a href="mailto:bastien.potiron@etu.univ-nantes.fr">bastien.potiron@etu.univ-nantes.fr</a></p>
					


			</div>
		</div>
	</body>

</html>