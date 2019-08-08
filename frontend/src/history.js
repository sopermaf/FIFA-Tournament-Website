import Vue from 'vue'
import './plugins/vuetify'
import History from './History.vue'

Vue.config.productionTip = false

new Vue({
  render: h => h(History),
}).$mount('#History')
