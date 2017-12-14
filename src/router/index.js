import Vue from 'vue'
import Router from 'vue-router'
import MainBoard from '@/components/main'
import Cart from '@/components/ShoppingCart/cart'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainBoard
    },
    {
      path: '/test',
      name: 'test',
      component: Cart
    }
  ]
})
