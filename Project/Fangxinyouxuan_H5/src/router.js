import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/account',
      name: 'account',
      component: () => import('./views/Account/Account.vue'),
      children: [
        {
          path: '',
          name: 'myAccount',
          component: () => import('./views/Account/MyAccount.vue')
        },
        {
          path: 'fan',
          name: 'fan',
          component: () => import('./views/Account/Fan.vue')
        },
        {
          path: 'accountDetail',
          name: 'accountDetail',
          component: () => import('./views/Account/AccountDetail.vue')
        },
        {
          path: 'withdrawRecord',
          name: 'withdrawRecord',
          component: () => import('./views/Account/WithdrawRecord.vue')
        },
        {
          path: 'recharge',
          name: 'recharge',
          component: () => import('./views/Account/Recharge.vue')
        },
        {
          path: 'withdraw',
          name: 'withdraw',
          component: () => import('./views/Account/Withdraw.vue')
        }]
    },
    {
      path: '/order',
      name: 'order',
      component: () => import('./views/Order.vue')
    },
    {
      path: '/income',
      name: 'income',
      component: () => import('./views/Income.vue')
    },
    {
      path: '/manage',
      name: 'manage',
      component: () => import('./views/Manage.vue')
    },
    {
      path: '/team',
      name: 'team',
      component: () => import('./views/Team.vue')
    }
  ]
})
