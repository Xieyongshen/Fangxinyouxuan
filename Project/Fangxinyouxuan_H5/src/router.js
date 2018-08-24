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
      meta: {
        title: '放心优选'
      },
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
          meta: {
            title: '我的金库'
          },
          component: () => import('./views/Account/MyAccount.vue')
        },
        {
          path: 'fan',
          name: 'fan',
          meta: {
            title: '我的粉丝'
          },
          component: () => import('./views/Account/Fan.vue')
        },
        {
          path: 'accountDetail',
          name: 'accountDetail',
          meta: {
            title: '资金明细'
          },
          component: () => import('./views/Account/AccountDetail.vue')
        },
        {
          path: 'withdrawRecord',
          name: 'withdrawRecord',
          meta: {
            title: '提现记录'
          },
          component: () => import('./views/Account/WithdrawRecord.vue')
        },
        {
          path: 'recharge',
          name: 'recharge',
          meta: {
            title: '充值'
          },
          component: () => import('./views/Account/Recharge.vue')
        },
        {
          path: 'withdraw',
          name: 'withdraw',
          meta: {
            title: '提现'
          },
          component: () => import('./views/Account/Withdraw.vue')
        }]
    },
    {
      path: '/order',
      name: 'order',
      meta: {
        title: '本店订单'
      },
      component: () => import('./views/Order.vue')
    },
    {
      path: '/income',
      name: 'income',
      meta: {
        title: '本店收益'
      },
      component: () => import('./views/Income.vue')
    },
    {
      path: '/manage',
      name: 'manage',
      meta: {
        title: '商品管理'
      },
      component: () => import('./views/Manage.vue')
    },
    {
      path: '/team',
      name: 'team',
      meta: {
        title: '我的团队'
      },
      component: () => import('./views/Team.vue')
    },
    {
      path: '/ranking',
      name: 'ranking',
      meta: {
        title: '优质用户排名'
      },
      component: () => import('./views/Ranking.vue')
    },
    {
      path: '/deliver',
      name: 'deliver',
      meta: {
        title: '门店配送设置'
      },
      component: () => import('./views/Deliver.vue')
    }
  ]
})
