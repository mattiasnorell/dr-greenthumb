<?php
	$soilSensors = $this->db->query('SELECT * FROM Sensors where SensorType = "waterlevel"');

        while ($sensorRow = $soilSensors->fetchArray()) {
        $result = $this->db->query("SELECT * FROM SensorData where SensorId = '". $sensorRow["SensorId"] ."' ORDER BY DateTime DESC LIMIT 6");
?>
<div class="gadget-info-tab">

        <div class="temperature">
                <?php echo round($result->fetchArray()["SensorValue"]);?>%
        </div>
        <div class="description">
                kvar i tanken
        </div>

        <table>

                <?php while ($tempRow = $result->fetchArray()) { ?>
                        <tr>
                                <td><?php echo $tempRow["DateTime"];?></td>
                                <td><?php echo round($tempRow["SensorValue"]);?>%</td>
                        <tr>
                <?php } ?>
        </table>
</div>
<?php } ?>

