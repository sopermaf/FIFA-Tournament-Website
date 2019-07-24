import Vue from 'vue'
import './plugins/vuetify'
import PlayerTeam from './PlayerTeam.vue'

Vue.config.productionTip = false

new Vue({
  render: h => h(PlayerTeam),
}).$mount('#PlayerTeam')
