<?php 
	$humiditySensors = $this->db->query('SELECT * FROM Sensors where SensorType = "humidity"');

	while ($sensorRow = $humiditySensors->fetchArray()) { 
		$humidityResult = $this->db->query("SELECT * FROM SensorData where SensorId = '". $sensorRow["Id"] ."' ORDER BY DateTime DESC LIMIT 7");
?>
<div class="gadget-info-tab">

	<div class="temperature">
		<?php echo round($humidityResult->fetchArray()["SensorValue"],3)?>%
	</div>
	<div class="description">
		<?php echo $sensorRow["SensorName"] ?>
	</div>

	<table>

		<?php while ($tempRow = $humidityResult->fetchArray()) { ?>
			<tr>
				<td><?php echo  $tempRow["DateTime"];?></td>
				<td><?php echo round($tempRow["SensorValue"],3); ?>%</td>
			<tr>
		<?php } ?>
	</table>
</div>
<?php } ?>
