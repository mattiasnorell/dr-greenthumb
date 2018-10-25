<!--<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>-->

<div id="chart_humidity" style="width: 100%; height: 240px;"></div>

<?php 
	
	$sensorId = 0;
	$humidityValues;
	$humiditySensorItems;

	$humiditySensors = $this->db->query('SELECT * FROM Sensors where SensorType = "humidity"');
	while ($sensorRow = $humiditySensors->fetchArray()) { 
		$iteration = 0;

		$humidityChartValues = $this->db->query('SELECT * FROM SensorData where SensorId = '. $sensorRow["Id"] .' ORDER BY DateTime DESC LIMIT 144');
		
		$sensorItem = new Sensor();
		$sensorItem->id = $sensorRow["SensorId"];
		$sensorItem->name = $sensorRow["SensorName"];

		$humiditySensorItems[$sensorId] = $sensorItem;

		while ($sensorRow = $humidityChartValues->fetchArray()) { 
			$item = new Temperature();
			$item->timestamp = date('H:i', strtotime($sensorRow["DateTime"]));
			$item->value = $sensorRow["SensorValue"];
			
			$humidityValues[$iteration][$sensorId] = $item;
			$iteration++;
		}

		$sensorId++;
		
	}
?>

<script type="text/javascript">
//  google.charts.load('current', {'packages':['corechart']});

  google.charts.setOnLoadCallback(function(){
  	    var humidityData = google.visualization.arrayToDataTable([
	    	['Tid', '<?php echo $humiditySensorItems[0]->name; ?>'],

	    	<?php
	    		foreach ($humidityValues as $sensorValue) {
	    			echo "['".$sensorValue[0]->timestamp."', ".$sensorValue[0]->value.", ".$sensorValue[1]->value."],";
	    		}
	    	?>
	    ]);

	    var options = {
	    	hAxis: {title: 'Tid',  titleTextStyle: {color: '#333'}},
	    	vAxis: {minValue: 17},
	    	legend: 'top'
	    };

	    var chart = new google.visualization.AreaChart(document.getElementById('chart_humidity'));
	    chart.draw(humidityData, options);

	    window.addEventListener('resize', function(event){
           	chart.draw(humidityData, options);
           });
    });
  
</script>
