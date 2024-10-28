const socketURL =  `ws://${window.location.host}/ws/messages/{{room_name}}/`;
            console.log("Establising Socket Connection")
            const socket = new WebSocket(socketURL)

        // send messages to backend
            const message_form = document.getElementById("msg-form")
            message_form.addEventListener("submit", function(e){
                e.preventDefault();
                let message_sent = document.getElementById("message").value;
                console.log('Sending..', message_sent);
                socket.send(
                    JSON.stringify({
                        message : message_sent,
                        room_name : "{{room_name}}",
                        sender : "{{username}}"
                    })
                )
            })

            const chat_divs = document.getElementById('container')
            // scroll to bottom 
            const scrollToBottom = () => {
                chat_divs.scrollTop = chat_divs.scrollHeight;
            }

            //Receive message_form the backend
            socket.addEventListener("message", (e) => {
                const data = JSON.parse(e.data)["message"]
                
                console.log(data)

                let sender = data["sender"]
                let content = data["message"]

                if(sender == "{{username}}"){
                    document.getElementById("message").value = ''
                }
                if(sender == "{{username}}"){
                    document.getElementById("message").value = ''
                }

                const chat_divs = document.getElementById('container')
                if(sender == "{{username}}"){
                    chat_divs.innerHTML += `
                        <div class="mymessage">
                            <div class="message-content">${content}</div>
                            <p class="message-timestamp-right">Me</p>
                        </div>
                    `; 
                }else{
                    chat_divs.innerHTML += `
                        <div class="sendermessage">
                            <div class="message-content">${content}</div>
                            <p class="message-timestamp-right">${sender}</p>
                        </div>
                    `; 
                }

                scrollToBottom();

            });
