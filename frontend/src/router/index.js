import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import ReportLanding from '@/components/ReportLanding'
import ReportCreation from '@/components/ReportCreation'
import ReportForm from '@/components/ReportForm'

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
    },
    {
      path: '/reports/create',
      name: 'ReportCreation',
      component: ReportCreation
    },
    {
      path: '/reports/create/report',
      name: 'ReportForm',
      component: ReportForm
    }
  ]
})
