<template>
  <div class="home">
        <img src="@/assets/me-bg.png" class="me-bg">
        <navBar navTitle="放心优选"></navBar>

        <div class="me-userinfo">
            <div class="me-share">分享店铺</div>
            <img src="" class="me-userinfo-avatar">
            <div class="me-userinfo-name">nickName</div>
        </div>

        <div class="me-function">
            <div class="me-function-item">
                <img @click="goOrder" class="me-icon" src="@/assets/ic_order.png">
                <router-link to="/order" class="me-function-item-a">本店订单</router-link>
            </div>
            <div class="me-function-item">
                <img @click="goIncome" class="me-icon" src="@/assets/ic_income.png">
                <router-link to="/income" class="me-function-item-a">本店收益</router-link>
            </div>
            <div class="me-function-item">
                <img @click="goManage" class="me-icon" src="@/assets/ic_manage.png">
                <router-link to="/manage" class="me-function-item-a">商品管理</router-link>
            </div>
        </div>

        <div class="me-manage weui-cells">
            <a @click="goAccount" class="weui-cell weui-cell_access" href="javascript:;">
                <div class="weui-cell__bd">
                    <p>我的金库</p>
                </div>
                <div class="weui-cell__ft"></div>
            </a>
            <a @click="goOrder" class="weui-cell weui-cell_access" href="javascript:;">
                <div class="weui-cell__bd">
                    <p>货品到店</p>
                </div>
                <div class="weui-cell__ft">一键收货</div>
            </a>
            <a @click="goTeam" class="weui-cell weui-cell_access" href="javascript:;">
                <div class="weui-cell__bd">
                    <p>我的团队</p>
                </div>
                <div class="weui-cell__ft"></div>
            </a>
            <a class="weui-cell weui-cell_access" href="javascript:;">
                <div class="weui-cell__bd">
                    <p>优质用户排行榜</p>
                </div>
                <div class="weui-cell__ft"></div>
            </a>
            <a class="weui-cell weui-cell_access" href="javascript:;">
                <div class="weui-cell__bd">
                    <p>门店配送设置</p>
                </div>
                <div class="weui-cell__ft">{{postConfig}}</div>
            </a>

        </div>
    </div>
</template>

<script>
import navBar from '@/components/navBar.vue'

export default {
  name: 'home',
  components: {
    navBar
  },

    data: function() {
        return {
            postConfig:'已开启'
        }
    },

  methods: {
    goOrder(){
      this.$router.push('/order')
    },
    goIncome(){
      this.$router.push('/income')
    },
    goManage(){
      this.$router.push('/manage')
    },
    goAccount(){
      this.$router.push('/account')
    },
    goTeam(){
      this.$router.push('/team')
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

.me-function{
    margin: 0 auto;
    display: flex;

}

.me-function-item{
    width: 13.75rem;
    margin: 3.875rem auto 0;
    padding: 0.9375rem;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.me-function-item-a{
    font-size: 17px;
    text-decoration: none;
    color: #333;
}

.me-icon{
    width: 2.5rem;
    height: 2.5rem;
    margin-bottom: 0.625rem;
}
</style>

