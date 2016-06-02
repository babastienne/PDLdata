<html>
<head>
  <script src="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.js"></script>
  <script src="scripts/jquery-1.12.1.min.js"></script>
  <script src="scripts/maps.js"></script>

  <link rel="stylesheet" href="semantic/semantic.css" />
  <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.css" />
</head>
<body>
<div style="width:80%; margin:auto" align="center">
<div class="ui middle gridequal width center aligned padded grid">
%for ins in instal:
    <div class="olive five wide column">{{ins[0]}}</div>
    <div class="black one wide column">{{ins[1]}}</div>
    <div class="olive four wide column">{{ins[2]}}</div>
    <div class="black two wide column">{{ins[3]}}</div>
    <div class="olive four wide column">{{ins[4]}}</div>
%end
</div>
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
</body>
</html>
