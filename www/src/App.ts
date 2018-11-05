import Vue from 'vue';
import Component from 'vue-class-component';
import LogComponent from 'components/Log/Log';

@Component({
    name: 'App',
    components: {
        LogComponent
    }
})
export default class App extends Vue {
    public message: string = 'test message';

}