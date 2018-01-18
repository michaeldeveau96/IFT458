function openNav() {
	document.getElementById("sidebar_left").style.width = "250px";
	document.getElementById("header").style.marginLeft = "310px";
	document.getElementById("header").style.width = "83.76%";	
	document.getElementById("page").style.marginLeft = "310px";	
	document.getElementById("page").style.width = "83.76%";
	document.getElementById("sideNav-container").style.width = "310px";
}
function closeNav() {
	document.getElementById("sidebar_left").style.width = "0px";
	document.getElementById("SocialMediaLinks").style.marginLeft = "0px";
	document.getElementById("header").style.marginLeft = "60px";
	document.getElementById("header").style.width = "96.75%";
	document.getElementById("page").style.width = "96.75%";
	document.getElementById("page").style.marginLeft = "60px";
	document.getElementById("sideNav-container").style.width = "60px";

}
