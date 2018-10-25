<?php 

	$temperatureSensors = $this->db->query('SELECT * FROM Sensors where SensorType = "temp"');
	while ($sensorRow = $temperatureSensors->fetchArray()) { 
		$temperatures = $this->db->query('SELECT * FROM SensorData where SensorId = '. $sensorRow["Id"] .' ORDER BY DateTime DESC LIMIT 7');
?>

	<div class="gadget-info-tab">
		<div class="temperature"><?php echo $temperatures->fetchArray()["SensorValue"]?>&deg;</div>
		<div class="description"><?php echo $sensorRow["SensorName"] ?></div>
		
		<table>

		<?php while ($tempRow = $temperatures->fetchArray()) { ?>
			<tr>
				<td><?php echo $tempRow["DateTime"] ?></td>
				<td><?php echo $tempRow["SensorValue"] ?> &deg;</td>
			<tr>
		<?php } ?>
		</table>
	</div>
<?php } ?>		
