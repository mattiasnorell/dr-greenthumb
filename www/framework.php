<?php
	spl_autoload_register(function ($class_name) {
	    	include 'classes/' . $class_name . '.php';
	});

	class Framework{
		protected $db;
		private $widgets = array();
		private $widgetPath = "widgets";

		public function __construct () {
			$this->db = new SQLite3('../db/greenhouse.db');
			$this->LoadWidgets();
		}

		public function LoadWidgets(){
			$widgetsDb = $this->db->query('SELECT * FROM Widgets ORDER BY SortOrder');

			while ($tempRow = $widgetsDb->fetchArray()) {
				$this->AddWidget(new Widget($tempRow["Widget"], $tempRow["Title"], $tempRow["Multipage"], $tempRow["Size"],  $tempRow["Active"],  $tempRow["Persistent"], $tempRow["Theme"]));	
			}
		}

		public function AddWidget($widget){
			array_push($this->widgets, $widget);
		}

		public function GetWidgets($onlyActive){
			if($onlyActive == true){
				return $this->widgets;
			}else{
				$activeWidgets = array();

				foreach ($this->widgets as $widget) {
					if($widget->active){
						array_push($activeWidgets, $widget);
					}
				}

				return $activeWidgets;
			}
		}

		public function RenderWidgets(){
			$widgetList = $this->GetWidgets(false);
			
			foreach ($widgetList as $widget) {
				$widgetPath = $this->widgetPath . "/" .$widget->id.".php";
				$widgetSettings = $widget;

				include($this->widgetPath . "/widget-heading.php");
				include($widgetPath);
				include($this->widgetPath . "/widget-footer.php");
			}
		}
	}
?>
