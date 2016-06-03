<html>

<head>
    <link rel="stylesheet" href="style/index.css" />
</head>
<body>

	<div id="englobeTout">
			<div id="TitrePage" >
				<h1 id="txtTitre"> Site De Référence Sportive </h1>
			</div>
			</br>
					<fieldset>
  					<legend>Recherche D'activité</legend>
						<form action='/result' method="post"></br></br>
							<label> Choisissez le type d'activité : </label></br></br>
							<select id="sel1" name="activity" class="ui dropdown segments ">
								%for allAct in activity:
								<option class="opt1" value="{{allAct[1]}}">{{allAct[0]}}</option>
								%end
							</select></br></br></br>
							<label> Choisissez le lieu :</label></br></br>
							<div class="DivPlacementForm">
								<select id="sel2" name="city" class="ui dropdown segments ">
                  <option class="opt1" value="" selected="True"> </option>
									%for c in city:
									<option class="opt2" value="{{c[0]}}">{{c[1]}}</option>
									%end
								</select>
							</div></br></br>
							<div class="DivPlacementForm">
								<input id ="sent"type="submit" name="valider" class="ui primary button center" value="Chercher">
							</div>
						</form>
					</fieldset>
	</div>
		</br></br>
			<table>
				<tr>
					<td> <img src="img/sport2.png" alt="Sport2" style="width:304px;height:228px;"></td>
					<td> <img src="img/sport3.jpg" alt="Sport3" style="width:304px;height:228px;"></td>
					<td> <img src="img/sport4.jpg" alt="Sport4" style="width:304px;height:228px;"></td>
					<td> <img src="img/sport5.png" alt="Sport5" style="width:304px;height:228px;"></td>
				</tr>
			</table></br></br></br>
	</div>
		<h4>Site réalisé dans le cadre d'un projet du module : Technologies pour la production de logiciels
		</h4>
	</div>
</body>
</html>
