async function sendMessage(){

let message = document.getElementById("userInput").value;

let response = await fetch("/ask",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({message:message})
});

let data = await response.json();

let chat = document.getElementById("chat");

chat.innerHTML += "<p><b>You:</b> "+message+"</p>";
chat.innerHTML += "<p><b>AI:</b> "+data.reply+"</p>";

speak(data.reply);

}


function startVoice(){

let recognition = new webkitSpeechRecognition();

recognition.onresult=function(event){

let text=event.results[0][0].transcript;

document.getElementById("userInput").value=text;

sendMessage();

}

recognition.start();

}


function speak(text){

let speech=new SpeechSynthesisUtterance(text);

speech.rate=1;

speech.pitch=1;

window.speechSynthesis.speak(speech);

}


function toggleAccessibility(){

document.body.classList.toggle("accessibility");

}