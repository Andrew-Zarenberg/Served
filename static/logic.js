var imgIndex = 0;
var imgIndexMax = 0;

var LOCATION = 0;

if(document.getElementById("suggestion_images")){
    imgIndexMax = document.getElementById("suggestion_images").getElementsByTagName("img").length-1;
}

function nextImage(){ changeImage(1); }
function prevImage(){ changeImage(-1); }

function changeImage(offset){
    document.getElementById("img"+imgIndex).style.display = "none";

    imgIndex += offset;

    // Prev Image button
    if(imgIndex == 0) document.getElementById("prevImage").disabled = true;
    else document.getElementById("prevImage").disabled = false;

    // Next Image button
    if(imgIndex == imgIndexMax) document.getElementById("nextImage").disabled = true;
    else document.getElementById("nextImage").disabled = false;

    //if(imgIndex < 0) imgIndex = imgIndexMax;
    //else if(imgIndex > imgIndexMax) imgIndex = 0;

    document.getElementById("img"+imgIndex).style.display = "";
}


function ratingUp(restaurantId){
    $.get("rate?restaurant="+restaurantId+"&type=Like");
    $("#suggestion .result").html("<span style='color:green;font-weight:bold'>Liked!</span>").fadeOut(1000);
    loadNextSuggestion();
}

function ratingDown(restaurantId){
    $.get("rate?restaurant="+restaurantId+"&type=Dislike")
    $("#suggestion .result").html("<span style='color:red;font-weight:bold'>Disliked!</span>").fadeOut(1000);
    loadNextSuggestion();
}

function loadNextSuggestion(){
    nabe = location.href.split("neighborhood=")[1];
    $.get("suggestion?neighborhood="+nabe,function(d){
	$("#suggestion_body").html(d);
	imgIndex = 0;
	imgIndexMax = document.getElementById("suggestion_images").getElementsByTagName("img").length-1;
    });
}


function superlike(restaurantId){
    $.get("superlike?restaurant="+restaurantId, function(d){
	$("#superlike_body").html(d);
    });
    $("#suggestion .result").html("<span style='color:blue;font-weight:bold'>I want to eat here!</span>").fadeOut(1000);
    loadNextSuggestion();
}

function clearSuperlikes(){
    $.get("clear_superlikes", function(d){
	$("#superlike_body").html(d);
    });
}

function seeRepeats(){
    $.get("see_repeats", function(){
	loadNextSuggestion();
    });
}

function removeSuperlike(restaurantId){
    $.get("remove_superlike?restaurant="+restaurantId, function(d){
	$("#superlike_body").html(d);
    });
}

function deleteRestaurant(){
    ret_val = confirm("Are you sure you wish to delete this restaurant?");
    if(ret_val){
	window.location = "/delete_restaurant?id="+location.href.split("id=")[1];
    }
}