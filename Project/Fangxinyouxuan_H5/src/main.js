import Vue from 'vue'
import VueWechatTitle from 'vue-wechat-title'
import App from './App.vue'
import router from './router'

Vue.use(VueWechatTitle)
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
