import Vue from 'vue'
import './plugins/vuetify'
import Fixtures from './Fixtures.vue'

Vue.config.productionTip = false

new Vue({
  render: h => h(Fixtures),
}).$mount('#Fixtures')
