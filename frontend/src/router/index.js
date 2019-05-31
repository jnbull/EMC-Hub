import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import ReportLanding from '@/components/ReportLanding'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/reports',
      name: 'ReportLanding',
      component: ReportLanding
    }
  ]
})
