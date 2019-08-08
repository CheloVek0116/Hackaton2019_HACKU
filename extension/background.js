let lastDate = null; 
let isEnabled = false;
var title = null
var link = null

chrome.runtime.onMessage.addListener((action, sender, sendResponse) => {
	switch(action) {
		case "start":
			isEnabled = true;
			break;
		case "stop":
			isEnabled = false;
			break;
		case "get_time": {
			if(isEnabled) {

				chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
					title = tabs[0].title;
				});
				chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
					link = tabs[0].url;
				});
				$.ajax({
					type: "POST",
					url: "http://127.0.0.1:8000/stats/",
					data: {'title': title, 'link': link}
				});
				
				sendResponse({'title': title, 'link': link})
				
			} else {
				sendResponse(null);
			}
			break;
		}
	}
});