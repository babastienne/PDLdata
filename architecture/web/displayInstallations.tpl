<html>
<head>
  <script src="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.js"></script>
  <script src="scripts/jquery-1.12.1.min.js"></script>
  <script src="scripts/maps.js"></script>

  <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.css" />
  <link rel="stylesheet" href="style/map.css" />

</head>
<body>
<h1> Vue des Equipements via une maap</h1>
<div style="width:80%; margin:auto" align="center">

<div id="mapid" style="height:500px">
</div>
</div>
<table style="visibility:hidden">
%for ins in instal:
<tr>
<td>{{ins[0]}}</td>
<td>{{ins[5]}}</td>
<td>{{ins[6]}}</td>
<td>{{ins[1]}}</td>
<td>{{ins[2]}}</td>
<td>{{ins[3]}}</td>
</tr>
%end
<h2> Les différents équipements pour l'activité et la ville sélectioné, ci dessous : </h2>
<div class="ui middle gridequal width center aligned padded grid">
%for ins in instal:
    <div id="affichage"><p >{{ins[0]}} - {{ins[1]}}  - {{ins[2]}} - {{ins[3]}} - {{ins[4]}}</p></div>
%end
</div>
</body>
</html>
