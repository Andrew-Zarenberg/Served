served = []

$(".name-address").each(function(){
	if($(this).html().split("<br").length == 2){
		name = $.trim($(this).children("a:first").text())
		category = $.trim($(this).html().split("</a>")[1].split("<br")[0].split(",")[0].replace(name,""))
		address = $.trim($(this).html().split("</a>")[1].split("<br>")[1].split("<a")[0].split("|")[0])
		served.push([name, category, address]);
	}
});

$("body").append("<div id='served'></div>");

for(x=0;x<served.length;x++){
	$("#served").append('{"name": "'+served[x][0]+'", "address": "'+served[x][2]+'", "neighborhood": "Downtown Brooklyn", "category": "'+served[x][1]+'", "pictures": [], "ratings": []}<br />')
}