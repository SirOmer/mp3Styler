var socket = io.connect('http://localhost:8080/sock_connect')

socket.on('message', function(msg) {
	if (msg == "Connected to the stream") {
		console.log("connected")
	}
})

socket.on('song_added', function(msg) {
	var d1 = document.getElementById('one');
	d1.insertAdjacentHTML('afterend', msg);
})