<?php
        $soilSensors = $this->db->query("SELECT * FROM Sensors where SensorType = 'moisture'");

        while ($sensorRow = $soilSensors->fetchArray()) {
        $moistureResult = $this->db->query("SELECT * FROM SensorData where SensorId = ". $sensorRow["Id"] ." ORDER BY DateTime DESC LIMIT 7");
?>

<div class="gadget-info-tab">

         <div class="temperature">
               <?php echo $moistureResult->fetchArray()["SensorValue"]  == 1 ? "Torr" : "Fuktig"; ?>
        </div>
        <div class="description">
		<?php echo $sensorRow["SensorName"]; ?>                
        </div>
        
        <table>

                <?php while ($tempRow = $moistureResult->fetchArray()) { ?>
                        <tr>
                                <td><?php echo $tempRow["DateTime"]; ?></td>
                                <td><?php echo $tempRow["SensorValue"] == 1 ? "Torr jord" : "Fuktig jord"; ?></td>
                        <tr>
                <?php } ?>
        </table>
</div>
<?php } ?>

