$(document).ready(function(){
	$('.gadget.gadget-info .gadget-toggles li').click(function(){
		var gadget = $(this).closest('.gadget'),
			index = $(this).index();
		gadget.find('.gadget-info-tab').hide().eq(index).show();
	});
	
	
	$('.gadget .gadget-toggle-prev').click(function(){
		var gadget = $(this).closest('.gadget'),
		slides = gadget.find('.gadget-info-tab'),
		currentActiveSlide = gadget.attr('data-active'),
		activeSlide;
		
		if(typeof currentActiveSlide == "undefined"){
			currentActiveSlide = 0;
		}
		
		activeSlide = parseInt(currentActiveSlide) - 1;
		
		if(activeSlide < 0){
			activeSlide = slides.length - 1;
		}
	
		gadget.attr('data-active', activeSlide).find('.gadget-info-tab').hide().eq(activeSlide).show();
	});
	
	$('.gadget .gadget-toggle-next').click(function(){
		var gadget = $(this).closest('.gadget'),
		slides = gadget.find('.gadget-info-tab'),
		currentActiveSlide = gadget.attr('data-active'),
		activeSlide;
		
		if(typeof currentActiveSlide == "undefined"){
			currentActiveSlide = 0;
		}
		
		activeSlide = parseInt(currentActiveSlide) + 1;
		
		if(activeSlide >= slides.length){
			activeSlide = 0;
		}
	
		gadget.attr('data-active', activeSlide).find('.gadget-info-tab').hide().eq(activeSlide).show();
	});
});