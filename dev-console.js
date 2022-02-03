// Ctrl + Shift + I and paste the script
// Click twice on a username to get their id (only click once if they don't look like a bot)
// Press = when done to copy all the ids
// Ctrl + R to stop the script

var elements = document.getElementsByClassName("anchor-1MIwyf anchorUnderlineOnHover-2qPutX");
var ids = ""

function textToClipboard(text) {                       // function taken from walkman from stackoverflow
     var dummy = document.createElement("textarea");
     document.body.appendChild(dummy);
     dummy.value = text;
     dummy.select();
     document.execCommand("copy");
     document.body.removeChild(dummy);
}

var getId = function() {
     var popup = document.getElementById(this.getAttribute("aria-controls"));
     if (popup) {
          ids += popup.getElementsByClassName("avatar-b5OQ1N")[0].src.split('/')[4] + " ";
     }
};

for (var i = 0; i < elements.length; i++) {
     elements[i].addEventListener('click', getId, false);
}

document.addEventListener("keydown", function(event) {
     if (event.key == "=") {
          console.log(ids);
          textToClipboard(ids);
     }
});
