<template>
    <div class="accountDetail">
        <img src="@/assets/me-bg.png" class="me-bg">
        <navBar navTitle="资金明细" isChildPage="y"></navBar>
    
        <div class="me-userinfo">
            <div class="me-share">分享店铺</div>
            <img src="" class="me-userinfo-avatar">
            <div class="me-userinfo-name">nickName</div>
        </div>

        <div class="accountDetail-list">
            <div class="accountDetail-list-item" v-for="item in items" :key="item.number">
                <div class="accountDetail-list-item-row1">
                    <div class="accountDetail-list-item-name">{{item.name}}</div>
                    <div class="accountDetail-list-item-change">{{item.change}}</div>
                </div>
                <div class="accountDetail-list-item-time">{{item.time}}</div>
                <hr class="divider">
            </div>
        </div>

    </div>
</template>

<script>
import navBar from '@/components/navBar.vue'

export default {
  name: 'accountDetail',
  components: {
    navBar,
  },

  data: function(){
      return{
        items: [
            {
                number: '1',
                name: '资金明细一',
                change: '+88.88',
                time: '2018-07-02 01:11:01'
            },
            {
                number: '2',
                name: '资金明细二',
                change: '-28.88',
                time: '2018-07-02 01:11:01'
            },
            {
                number: '3',
                name: '资金明细三',
                change: '+88.88',
                time: '2018-07-02 01:11:01'
            }
        ]
      }
  }
}
</script>

<style scoped>
.divider{
    color: #888888;
    margin: 1.25rem 0;
    line-height: 1px;
}

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

.accountDetail-list{
    margin: 10rem auto 0;
}

.accountDetail-list-item{
    display: flex;
    flex-direction: column;
    margin: 0 .9375rem;
}

.accountDetail-list-item-row1{
    display: flex;
    flex-direction: row;
    justify-content: space-between
}

</style>