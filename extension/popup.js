var domain = 'http://localhost:8000/';

window.onload = function() {
	var list = document.querySelector("#list");
	var rubricListLoader = new XMLHttpRequest();

	rubricListLoader.onreadystatechange = function() {
		if (rubricListLoader.readyState == 4) {
			if (rubricListLoader.status == 200) {
				var data = JSON.parse(rubricListLoader.responseText);
				var s = '<ul>';
				for (var i = 0; i < data.length; i++) {
					s += '<li>' + data[i].username + '</li>';
				}
				s += '</ul>';
				list.innerHTML = s;
			}
		}
	}

	function rubricListLoad() {
		rubricListLoader.open('GET', domain + 'profile/get/', true);
		rubricListLoader.send();
	}
	rubricListLoad ();
}