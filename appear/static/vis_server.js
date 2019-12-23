var jQueryScript = document.createElement('script');
jQueryScript.setAttribute('src','//cdnjs.cloudflare.com/ajax/libs/socket.io/2.2.0/socket.io.js');
jQueryScript.setAttribute('integrity','sha256-yr4fRk/GU1ehYJPAs8P4JlTgu0Hdsp4ZKrx8bDEDC3I=');
jQueryScript.setAttribute('crossorigin','anonymous');
document.head.appendChild(jQueryScript);


class VisServer {
    constructor() {
        this.socket = io();
        this.visualizations = {};

        this.socket.on('my_response', (function(msg) {
            console.log(msg);
            console.log(this.visualizations);
            console.log(this.visualizations[msg.target])
            console.log(msg.target in this.visualizations)
            if (msg.target in this.visualizations) {
                this.visualizations[msg.target](msg);
            }
        }).bind(this));
    }

    subscribe(target, updateFunction) {
        this.visualizations[target] = updateFunction;
    }
}