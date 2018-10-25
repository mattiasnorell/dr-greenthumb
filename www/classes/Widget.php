<?php
	class Widget{
		public $id;
		public $title;
		public $multipage;
		public $size;
		public $theme;

		public function __construct ( $id, $title, $multiPage, $size, $active, $persistent, $theme = "blue") {
			$this->id = $id;
			$this->title = $title;
		 	$this->multipage = $multiPage;
			$this->size = $size;
			$this->theme = $theme;
			$this->active = $active;
			$this->persistent = $persistent;
		}
	}
?>