import Vue from 'vue';
import './style/main.scss';
import App from './App';

Vue.config.productionTip = false;

new Vue({ render: (h) => h(App) }).$mount('#app');