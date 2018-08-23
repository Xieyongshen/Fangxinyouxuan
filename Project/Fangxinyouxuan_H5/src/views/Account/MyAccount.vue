<template>
  <div class="myAccount">
    <img src="@/assets/me-bg.png" class="me-bg">
    <navBar navTitle="我的金库" isChildPage="y"></navBar>
    
    <div class="me-userinfo">
        <div class="me-share">分享店铺</div>
        <img src="" class="me-userinfo-avatar">
        <div class="me-userinfo-name">nickName</div>
    </div>

    <div class="wallet-money">
        <label class="wallet-money-label">我的金库</label>
        <div class="wallet-money-total">
          <img src="@/assets/ic_money.png" class="wallet-money-total-icon">
          <label>{{totalMoney}}</label>
        </div>
    </div>

    <div class="wallet-manage weui-cells">
            <a  @click="goFan" class="weui-cell weui-cell_access" href="javascript:;">
                <div class="weui-cell__bd">
                    <p>我的粉丝</p>
                </div>
                <div class="weui-cell__ft">{{fansNumber}}个</div>
            </a>
            <a @click="goAccountDetai" class="weui-cell weui-cell_access" href="javascript:;">
                <div  class="weui-cell__bd">
                    <p>资金明细</p>
                </div>
                <div class="weui-cell__ft"></div>
            </a>
            <a @click="goWithdrawRecord" class="weui-cell weui-cell_access" href="javascript:;">
                <div class="weui-cell__bd">
                    <p>提现记录</p>
                </div>
                <div class="weui-cell__ft"></div>
            </a>
      </div>

      <div class="wallet-option">
          <a @click="goRecharge" class="weui-btn weui-btn_plain-default">我要充值</a>
          <a @click="goWithdraw" class="weui-btn weui-btn_plain-default">我要提现</a>
      </div>
   
  </div>
</template>

<script>
import navBar from '@/components/navBar.vue'

export default {
  name: 'account',
  components: {
    navBar
  },

  data: function(){
      return{
        totalMoney: 0.0,
        fansNumber: 666
      }
  },

  methods: {
    goFan(){
      this.$router.push('/account/fan')
    },
    goAccountDetai(){
      this.$router.push('/account/accountDetail')
    },
    goWithdrawRecord(){
      this.$router.push('/account/withdrawRecord')
    },
    goRecharge(){
      this.$router.push('/account/recharge')
    },
    goWithdraw(){
      this.$router.push('/account/withdraw')
    }
  }

}
</script>

<style scoped>
.me-bg {
    width: 100%;
    height: 18.75rem;
    position: absolute;
    top: 3.875rem;
    z-index: -1;
}

.me-userinfo {
    width: 100%;
    height: 14.6875rem;
    margin-bottom: 4.375rem;
    padding-top: 0.9375rem;
    text-align: center;
    box-sizing: border-box;
    position: relative;
    top:3.875rem;
   
}

.me-userinfo-avatar {
    width: 6.25rem;
    height: 6.25rem;
    border: 0.3125rem solid #ffffff;
    border-radius: 50%;
    background: #d4d5d2;
    box-sizing: border-box;
    margin-top: 3.125rem;
}

.me-userinfo-name {
    width: 100%;
    height: 2.1875rem;
    color: #ffffff;
    font-size: 17px;
    line-height: 1.875rem;
    text-align: center;
    margin-top: 0.625rem;
    box-sizing: border-box;
    display: block;
}

.me-share {
    color: #ffffff;
    font-size: 17px;
    line-height: 30px;
    position: absolute;
    top: 0.625rem;
    left: 1.875rem;
}

.wallet-money{
  width: 100%;
  color: #333;
  font-size: 17px;
  text-align: center;
  margin: 10rem auto 1.25rem;
}

.wallet-monye-label{
  display: block;
}

.wallet-money-total{
  color: #fdb85d;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: .5rem;
}

.wallet-money-total-icon{
  width: 2.25rem;
  height: 2.25rem;
}

.wallet-option{
  margin: 1.875rem 1.875rem;
}
</style>