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