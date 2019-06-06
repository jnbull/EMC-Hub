import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'

// Report Section
import ReportLanding from '@/components/ReportLanding'
import ReportCreation from '@/components/ReportCreation'
import ReportForm from '@/components/ReportForm'
import ReportSuccess from '@/components/ReportSuccess'

// Verification Section
import VerificationLanding from '@/components/VerificationLanding'
import VerificationCreation from '@/components/VerificationCreation'
import VerificationTests from '@/components/VerificationTests'
import VerificationEFT from '@/components/VerificationEFT'

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
    },
    {
      path: '/reports/success',
      name: 'ReportSuccess',
      component: ReportSuccess
    },
    {
      path: '/verifications',
      name: 'VerificationLanding',
      component: VerificationLanding
    },
    {
      path: '/verifications/create',
      name: 'VerificationCreation',
      component: VerificationCreation
    },
    {
      path: '/verifications/create/testsetup',
      name: 'VerificationTests',
      component: VerificationTests
    },
    {
      path: '/verifications/create/testsetup/eft',
      name: 'VerificationEFT',
      component: VerificationEFT
    }
  ]
})
