var modal = document.getElementById('loginForm');

function openLogin() {
	document.getElementById('loginForm').style.display='block';
}
function closeLogin() {
	document.getElementById('loginForm').style.display='none'
}
function openRegister() {
	document.getElementById('registerForm').style.display='block';
}
function closeRegister() {
	document.getElementById('registerForm').style.display='none'
}
window.onclick = function(event) {
	if (event.target == modal) {
		modal.style.display = "none";
	}
}
var x = document.getElementById('main');

function getLocation() {
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(showPosition, showError);
	}else{
		x.innerHTML = "Geolocation is not supported by this browser.";
	}
}
function showPosition(position) {
	var pos = position.coords.latitude + "," + position.coords.longitude;
	var mapurl = "https://maps.googleapis.com/maps/api/staticmap?center="+pos+"&zoom=14&size=400x300&sensor=false&key=AIzaSyADUsX33Gx5AO62IjvtQuuuNT0323pkDgY";
	document.getElementById("map").innerHTML += "<img src='"+mapurl+"'>";
}
function showError(error) {
	switch(error.code) {
		case error.PERMISSION_DENIED:
			x.innerHTML = "User denied the request for Geolocation."
			break;
		case error.POSITION_UNAVAILABLE:
			x.innerHTML = "Location information si unavailable."
			break;
		case error.TIMEOUT:
			x.innerHTML = "The request to get user location timed out."
			break;
		case error.UNKNOWN_ERROR:
			x.innerHTML = "An unknown error occurred."
			break;
	}
}
function reload() {
	location.reload();
}

function loggedIn() {	
	var username = document.getElementById("uname").value;
	document.getElementById("registration").style.color = "#F7CE3E";
	document.getElementById("registration").innerHTML += "Logged in: "+username;
	document.getElementById('registerForm').style.display='none'
	document.getElementById('register').style.display='none';
	document.getElementById('login').style.display='none';
}