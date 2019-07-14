
document.querySelector('#start').addEventListener('click', () => {
	chrome.runtime.sendMessage('start');
});

document.querySelector('#stop').addEventListener('click', () => {
	chrome.runtime.sendMessage('stop');
});

// Запрос значения таймера. Можно выполнять по-необходимости
setInterval(() => {
	
	chrome.runtime.sendMessage('get_time', data => {
		$.ajax({
			type: "POST",
			url: "http://localhost:8000/stats/",
			data: data
		});
	});
}, 200);