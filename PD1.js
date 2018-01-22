function openNav() {
	document.getElementById("sidebar_left").style.width = "250px";
}
function closeNav() {
	document.getElementById("sidebar_left").style.width = "0px";
}

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
