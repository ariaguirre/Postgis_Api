import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
/* eslint-disable */
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/home',
      name: 'Home',
      component: Home
    }
  ], 
  mode: 'history'
})
