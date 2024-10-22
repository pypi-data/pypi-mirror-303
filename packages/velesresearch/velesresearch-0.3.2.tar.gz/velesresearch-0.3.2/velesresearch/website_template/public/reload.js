const ws = new WebSocket('ws://localhost:8080');

ws.onmessage = (event) => {
    if (event.data === 'reload') {
        console.log('Reloading page due to file change...');
        window.location.reload();  // Reload the page when the server signals a change
    }
};

ws.onopen = () => {
    console.log('WebSocket connection established');
};