var mouseOverListener = function(){
	
	var img = this.dataset.image;
	var image_holder = document.getElementsByClassName('image-preview')[0];
	image_holder.innerHTML = "<img width='75px' src='"+ img +"' >"
	console.log(img);

};
var mouseOutListener = function(){
	
	var img = this.dataset.image;
	var image_holder = document.getElementsByClassName('image-preview')[0];
	image_holder.innerHTML = "";
	console.log(img);

};

window.onload = function(){
	var links = document.getElementsByClassName('product-link');
	console.log(links);
	for (var i=0; i<links.length; i++){
		links[i].addEventListener('mouseover', mouseOverListener);
		links[i].addEventListener('mouseout', mouseOutListener);
	}
}