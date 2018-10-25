<?php 
	$lightSensors = $this->db->query('SELECT * FROM Sensors where SensorType = "light"');

	while ($sensorRow = $lightSensors->fetchArray()) { 
	$temperatures = $this->db->query("SELECT * FROM SensorData where SensorId = '". $sensorRow["SensorId"] ."' ORDER BY DateTime DESC LIMIT 6");
?>
<div class="gadget-info-tab">

	<?php  if($temperatures->fetchArray["SensorValue"] == 1){ ?>
	<div class="temperature">
		<i class="fa fa-lightbulb-o"></i>
	</div>
	<div class="description">
		Lampor på
	</div>

	<?php }else{ ?>
	<div class="temperature">
		<i class="fa fa-sun-o"></i>
	</div>
	<div class="description">
		Lampor av
	</div>
	<?php } ?>

	<table>

		<?php while ($tempRow = $temperatures->fetchArray()) { ?>
			<tr>
				<td><?php echo  $tempRow["DateTime"];?></td>
				<td>
				<?php 
					if($tempRow["SensorValue"] == 1){
						echo "P&aring;";
					}else{
						echo "Av";
					} ?>
				</td>
			<tr>
		<?php } ?>
	</table>
</div>
<?php } ?>
