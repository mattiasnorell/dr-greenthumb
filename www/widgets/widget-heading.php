<div class="gadget gadget-size-<?php echo $widgetSettings->size; ?> gadget-theme-<?php echo $widgetSettings->theme;?> gadget-<?php echo $widgetSettings->id;?>">
        
        <?php if($widgetSettings->title != Null) { ?>
        <div class="gadget-header">
        	<?php echo $widgetSettings->title; ?>

                 <?php if($widgetSettings->multipage){?>
                 <div class="gadget-toggle-prev">
                	 <i class="fa fa-chevron-circle-left"></i>
                 </div>

                 <div class="gadget-toggle-next">
                 	<i class="fa fa-chevron-circle-right"></i>
                 </div>
                 <?php } ?>

        </div>

        <?php } ?>
        
        <div class="gadget-content">
