<div class="gadget-info-tab">
	<table>
		<?php
		$log = $this->db->query('SELECT * FROM Logs ORDER BY DateTime DESC LIMIT 10');
		while ($logRow = $log->fetchArray()) { 
		?>
		<tr>
			<td><?php echo $logRow["DateTime"]; ?></td>
			<td><?php echo $logRow["Message"]; ?></td>
		<tr>
		<?php } ?>
	</table>
</div>
