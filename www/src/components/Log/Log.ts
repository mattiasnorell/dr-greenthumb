import Vue from 'vue'
import { Component } from 'vue-property-decorator';
import { LogModel } from 'models/LogModel';

@Component({
    template: require('./Log.html'),
    data: () => ({
        logItems: ''
    }),
    computed: {

    }
})

export default class LogComponent extends Vue {
    private logItems: Array<LogModel>;

    constructor() {
        super();

        const result = new Array<LogModel>();

        for (let i = 0; i < 10; i++) {
            const item = new LogModel();
            item.message = 'Lorem ipsum dolor sit amet';
            item.timestamp = new Date();
            result.push(item);
        }

        this.logItems = result;

    }
}

/*
axios
  .get('https://api.coindesk.com/v1/bpi/currentprice.json')
  .then(response => (this.info = response.data.bpi))
*/