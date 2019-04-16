<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>

<div id="chart_temperature" style="width: 100%; height: 240px;"></div>

<?php 
	
	$sensorId = 0;
	$values;
	$sensorItems;

	$temperatureSensors = $this->db->query('SELECT * FROM Sensors where SensorType = "temp"');
	while ($sensorRow = $temperatureSensors->fetchArray()) { 
		$iteration = 0;

		$temperatures = $this->db->query('SELECT * FROM SensorData where SensorId = '. $sensorRow["Id"] .' ORDER BY DateTime DESC LIMIT 144');
		
		$sensorItem = new Sensor();
		$sensorItem->id = $sensorRow["SensorId"];
		$sensorItem->name = $sensorRow["SensorName"];

		$sensorItems[$sensorId] = $sensorItem;

		while ($tempRow = $temperatures->fetchArray()) { 
			$item = new Temperature();
			$item->timestamp = date('H:i', strtotime($tempRow["DateTime"]));
			$item->value = $tempRow["SensorValue"];
			
			$values[$iteration][$sensorId] = $item;
			$iteration++;
		}

		$sensorId++;
		
	}
?>

<script type="text/javascript">
  google.charts.load('current', {'packages':['corechart']});
  google.charts.setOnLoadCallback(function(){
  	    var data = google.visualization.arrayToDataTable([
	    	["{type: 'date', label: 'Tid'}", "<?php echo $sensorItems[0]->name; ?>", "<?php echo $sensorItems[1]->name; ?>"],

	    	<?php
	    		foreach ($values as $sensorValue) {
	    			echo "['". $sensorValue[0]->timestamp ."', ".$sensorValue[0]->value.", ".$sensorValue[1]->value."],";
	    		}
	    	?>
	    ]);

	    var options = {
	    	hAxis: {
	    		title: 'Tid',  
	    		titleTextStyle: {
	    			color: '#333'
	    		}	    		
	      	},
	    	vAxis: {
	    		minValue: 17
	    	},
	    	legend: 'top'
	    };

	    var chart = new google.visualization.AreaChart(document.getElementById('chart_temperature'));
	    chart.draw(data, options);

	    window.addEventListener('resize', function(event){
			chart.draw(data, options);  
		});
    });
  
</script>
