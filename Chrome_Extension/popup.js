'use strict';

//send GET request to server to get json configure for buttons
const Http = new XMLHttpRequest();
const url='http://127.0.0.1:5000/view';
Http.onreadystatechange=function(){
	if (this.readyState == 4 && this.status == 200){
		console.log(Http.responseText)
		var obj = JSON.parse(this.responseText);
		var neg = obj.neg;
		var pos = obj.pos;
		var neu = obj.neu;
		var total = neg + pos + neu;
		document.getElementById("neg").textContent="Negative Posts: "+neg+'-'+Math.floor((neg / total) * 100)+'%';
		document.getElementById("pos").textContent="Positive Posts: "+pos+'-'+Math.floor((pos / total) * 100)+'%';
		document.getElementById("neu").textContent="Neutrual Posts: "+neu+'-'+Math.floor((neu / total) * 100)+'%';
		document.getElementById("total").textContent="Total Posts with Women Topic: "+total;
	}
}
Http.open("GET", url);
Http.send();
