import Vue from 'vue'
import { BootstrapVue, BootstrapVueIcons } from "bootstrap-vue"
import App from './App.vue'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap-vue/dist/bootstrap-vue.css"

// import bootstrap vue
Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
