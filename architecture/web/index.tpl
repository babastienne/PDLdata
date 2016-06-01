<html>
<head>
    <link rel="stylesheet" href="semantic/semantic.css" />
</head>
<body>
<div class="ui middle aligned center aligned grid">
<div class="column">
<h1 class ="ui center aligned header">Want to practice an activity in your city?</h1>
<form action='/result' method="post">
<select name="activite" class="ui dropdown segments ">
	%for activite in activites:
	<option value="{{activite[1]}}">{{activite[0]}}</option>
	%end
</select>
</br>
<select name="ville" class="ui dropdown segments ">
	%for ville in villes:
	<option value="{{ville[0]}}">{{ville[1]}}</option>
	%end
</select>
</br>
<input type="submit" name="valide" class="ui primary button center" value="find">
</form>
</div>
</div>
</html>
