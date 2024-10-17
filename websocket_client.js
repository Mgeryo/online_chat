document.addEventListener('DOMContentLoaded', function(){

    const messagesContainer = document.querySelector("#message_container"); // находим по id элемент в доке
    const messageInput = document.querySelector('[name=message_input]'); // находим по названию элемент в доке
    const sendMessageButton = document.querySelector('[name=send_message_button]');

    let websocketClient = new WebSocket("ws://localhost:12345"); // подключение сокета

    websocketClient.onopen = () => {
        console.log("Client connected!"); // перед отправкой сообщений нужно подождать прогрузки вебсокета

        sendMessageButton.onclick = () => {
            websocketClient.send(messageInput.value); // отправляем данные на сервер
            messageInput.value = "";
        };
    };

    websocketClient.onmessage = (message) => {
        const newMessage = document.createElement('div');
        newMessage.innerHTML = message.data;
        messagesContainer.appendChild(newMessage);
    };
}, false); // для первоначальной прогрузки html 