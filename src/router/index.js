import Vue from 'vue'
import Router from 'vue-router'
import MainBoard from '@/components/main'
import Alert from '@/components/AlertSystem/AlertSystem'
Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainBoard
    },
    {
      path: '/alert',
      name: 'alert',
      component: Alert
    }
  ]
})
