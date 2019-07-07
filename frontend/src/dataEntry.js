import Vue from 'vue'
import './plugins/vuetify'
import DataEntry from './DataEntry.vue'

Vue.config.productionTip = false

new Vue({
  render: h => h(DataEntry),
}).$mount('#DataEntry')
