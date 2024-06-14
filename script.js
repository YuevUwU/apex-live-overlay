const WEBSOCKET_URL = "ws://localhost:4567/";
let websocket;

function connect() {
  websocket = new WebSocket(WEBSOCKET_URL);

  websocket.onopen = () => {
    console.log("Connected to WebSocket server");
  };

  websocket.onmessage = ({ data }) => {
    console.debug(data)
    const team_name_element = document.querySelector(".team-name");
    team_name_element.innerText = data;
  };

  websocket.onclose = () => {
    console.log("WebSocket connection closed. Attempting to reconnect...");
    setTimeout(connect, 500);
  };

  websocket.onerror = (error) => {
    console.error("WebSocket error:", error);
    websocket.close();
  };
}

window.addEventListener("DOMContentLoaded", () => {
  connect();
});
