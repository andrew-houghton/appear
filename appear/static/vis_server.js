class VisServer {
    constructor() {
        this.socket = io();
        this.visualizations = {};

        this.socket.on('my_response', (function(msg) {
            if (msg.target in this.visualizations) {
                this.visualizations[msg.target](msg);
            }
        }).bind(this));
    }

    subscribe(target, updateFunction) {
        this.visualizations[target] = updateFunction;
    }
}