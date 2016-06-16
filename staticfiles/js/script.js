function show_promoted(){
	var prom = document.getElementsByClassName("index-promoted-products")[0];
	var cat = document.getElementsByClassName("index-categories")[0];
	prom.style.display = "block";
	cat.style.display = "none";
}

function show_categories(){
	var prom = document.getElementsByClassName("index-promoted-products")[0];
	var cat = document.getElementsByClassName("index-categories")[0];
	prom.style.display = "none";
	cat.style.display = "block";
}

function show_specification(){
	var spec = document.getElementsByClassName("product-options-specification")[0];
	var img = document.getElementsByClassName("product-options-image")[0];
	spec.style.display = "block";
	img.style.display = "none";
}

function show_product_image(){
	var spec = document.getElementsByClassName("product-options-specification")[0];
	var img = document.getElementsByClassName("product-options-image")[0];
	spec.style.display = "none";
	img.style.display = "block";
}

function show_modal(obj){
	data = obj.dataset;
	console.log(data);
	document.getElementsByClassName("modal-title")[0].innerHTML = data.title;
	document.getElementsByClassName("modal-image")[0].setAttribute("src", data.imageUrl);
	remod.open();
}