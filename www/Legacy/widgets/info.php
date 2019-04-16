<div class="gadget-info-tab">
	<div class="col-big">
		<h2>Dr. Greenthumb</h2>
		<h3>Chilli, tomat och lite annat</h3>
	</div>
</div>
<div class="gadget-info-tab">
	<table>
	<?php 			
		$schedule = $this->db->query('SELECT StartDate, ItemName FROM Schedule WHERE BrewId = 1 ORDER BY StartDate');
		while ($brewScheduleRow = $schedule->fetchArray()) { ?>
		<tr>
			<td><?php echo $brewScheduleRow["StartDate"] ?></td>
			<td><?php echo $brewScheduleRow["ItemName"] ?></td>
		</tr>
	<?php } ?>
	</table>
</div>
<div class="gadget-info-tab">
	<img src="/snapshots/snapshot.jpg" class="img-responsive" />
</div>
<div class="gadget-info-tab">
	<h2>Widgets</h2>

	<?php
		$widgets = $this->GetWidgets(true);

		foreach ($widgets as $widget) {
			if(!$widget->persistent){
		 	   echo $widget->title . "<br>";
			}
		}
	?>

</div>


<div class="gadget-toggles">
	<ul>
		<li>
			<i class="fa fa-info-circle"></i><br/>Info
		</li>
		<li>
			<i class="fa fa-calendar"></i><br/>Schema
		</li>
		<li>
			<i class="fa fa-camera"></i><br/>Bild
		</li>
		<li>
			<i class="fa fa-cog"></i><br/>Inställningar
		</li>
	</ul>
</div>
