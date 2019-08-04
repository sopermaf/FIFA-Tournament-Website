import Vue from 'vue'
import './plugins/vuetify'
import Profile from './Profile.vue'

Vue.config.productionTip = false

new Vue({
  render: h => h(Profile),
}).$mount('#Profile')
