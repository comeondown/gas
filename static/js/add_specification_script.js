var table = $(".spec-table");
var rows = 2;
var columns = 1;

$(document).ready(function(){

		

});

var addCol= function(){
		var row = $(".spec-table tr");
		row.append("<td> <input type='text'></input> </td>");
		console.log(columns++);
	};

var addRow= function(){
		var col = $(".spec-table");
		html_row = '';
		html_row += "<tr>";
		for (var i=0; i<columns; i++){
			html_row += "<td> <input type='text'></input> </td>";
		}
		html_row +="</tr>";
		col.append(html_row);
		console.log(rows++);
	};

var save=function(product_id){
	if (confirm('Вы уверены, что хотите добавить спецификацию? Пока что редактирование спецификаций трудоемкий и нудный процесс, может быть проверите еще раз?')){
		var row = $(".spec-table tr");
		var table = $(".spec-table");
		var fields = [];
		var specs = [];	
		var measures = [];
		var spec_value = [];
		var fields_obj = {'fields':[]};

		row.each(function(index, elem){
			//Составление списка параметров спецификаций
			if (index==0){
				cells = elem.children;
				for (var i=0;i<cells.length;i++){
					if (cells[i].children[0]){
						fields.push(cells[i].children[0].value);
					}
				}
			}
			//Составление списка измерений параметров спецификаций
			if (index==1){
				cells = elem.children;
				for (var i=0;i<cells.length;i++){
					if (cells[i].children[0]){
						measures.push(cells[i].children[0].value);
					}
				}
			}
			//составление списка спецификаций (номеров по каталогу) и списка (номер по каталогу + значения)
			if (index >=2 ){
				cells = elem.children;
				sp = cells[0].children[0].value;
				specs.push(sp);
				spec_value.push({'spec':sp, 'values':[]});

				for (var i=1;i<cells.length;i++){
					spec_value[index-2]['values'].push(cells[i].children[0].value);
				}

			}
		
		});
		
		for (var i=0;i<fields.length;i++){
				
			fields_obj['fields'].push({'field':fields[i], 'measure':measures[i], values:[]});
			for (var j=0;j<spec_value.length;j++){
				fields_obj['fields'][i]['values'].push({'specification':spec_value[j]['spec'], 'value':spec_value[j]['values'][i]});
			}

		}	
		fields_obj['specs']=specs;
		final_json = JSON.stringify(fields_obj);
		console.log(final_json);
		$.ajax({
			url: product_id,
			method: 'POST',
			data: final_json,
			success: function(data){
						alert(data);
					}
			});
	}
}
