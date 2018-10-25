<?php
	$waterFlowSensors = $this->db->query('SELECT * FROM Sensors where SensorType = "waterflow"');

        while ($sensorRow = $waterFlowSensors->fetchArray()) {
        $result = $this->db->query("SELECT * FROM SensorData where SensorId = '". $sensorRow["SensorId"] ."' ORDER BY DateTime DESC LIMIT 7");
?>
<div class="gadget-info-tab">

        <div class="temperature">
                <?php echo $result->fetchArray()["SensorValue"];?>
        </div>
        <div class="description">
                liter per minut
        </div>

        <table>

                <?php while ($tempRow = $result->fetchArray()) { ?>
                        <tr>
                                <td><?php echo  $tempRow["DateTime"];?></td>
                                <td><?php echo $tempRow["SensorValue"];?> L</td>
                        <tr>
                <?php } ?>
        </table>
</div>
<?php } ?>
