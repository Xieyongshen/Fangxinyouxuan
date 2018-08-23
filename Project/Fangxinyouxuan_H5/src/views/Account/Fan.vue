<template>
    <div class="fan">
        <img src="@/assets/me-bg.png" class="me-bg">
        <navBar navTitle="我的粉丝" isChildPage="y"></navBar>
    
        <div class="me-userinfo">
            <div class="me-share">分享店铺</div>
            <img src="" class="me-userinfo-avatar">
            <div class="me-userinfo-name">nickName</div>
        </div>

        <div class="fan-order">
            <group>
                <PopupRadio title="用户筛选排序" placeholder="本月消费top10用户" v-model="fanOrder" :options="fanOrderList"></PopupRadio>
            </group>
        </div>

        <div class="fan-list">
            <div class="fan-list-item" v-for="item in items" :key="item.number">
                <div class="fan-list-item-content">
                    <div class="fan-list-item-number">{{item.number}}</div>
                    <img src="@/assets/ic_user.png" class="icon-user">
                
                    <div class="fan-list-item-userinfo">
                        <div class="fan-list-userinfo-baseinfo">
                            <div class="fan-list-userinfo-name">{{item.name}}</div>
                            <div class="fan-list-userinfo-sex">{{item.sex}}</div>
                        </div>
                        <div class="fan-list-userinfo-cost">本月消费: {{item.cost}}</div>
                    </div>
                    <div class="fan-list-item-contact">
                        <div class="fan-list-userinfo-wechat">微信: {{item.wechat}}</div>
                        <div class="fan-list-userinfo-tel">电话: {{item.tel}}</div>
                    </div>
                </div>
                <hr class="divider">
            </div>
        </div>

    </div>
</template>

<script>
import navBar from '@/components/navBar.vue'
import { PopupRadio } from 'vux'

export default {
  name: 'fan',
  components: {
    navBar,
    PopupRadio,
  },

  data: function(){
      return{
        fanOrder:'',
        fanOrderList: [{key: '0', value: '本月消费top10用户'}, {key: '1', value: '本周消费top10用户'}, {key: '2', value: '累计消费排名'}],
        items: [
            {
                number: '1',
                name: '小花',
                sex: '女',
                wechat: 'xiaohuazuimei',
                cost: '999',
                tel: '13006666666'
            },
            {
                number: '2',
                name: '小花',
                sex: '女',
                wechat: 'xiaohuazuimei',
                cost: '999',
                tel: '13006666666'
            },
            {
                number: '3',
                name: '小花',
                sex: '女',
                wechat: 'xiaohuazuimei',
                cost: '999',
                tel: '13006666666'
            },
            {
                number: '4',
                name: '小花',
                sex: '女',
                wechat: 'xiaohuazuimei',
                cost: '999',
                tel: '13006666666'
            },
             {
                number: '5',
                name: '小花',
                sex: '女',
                wechat: 'xiaohuazuimei',
                cost: '999',
                tel: '13006666666'
            },
             {
                number: '6',
                name: '小花',
                sex: '女',
                wechat: 'xiaohuazuimei',
                cost: '999',
                tel: '13006666666'
            },
             {
                number: '7',
                name: '小花',
                sex: '女',
                wechat: 'xiaohuazuimei',
                cost: '999',
                tel: '13006666666'
            },
             {
                number: '8',
                name: '小花',
                sex: '女',
                wechat: 'xiaohuazuimei',
                cost: '999',
                tel: '13006666666'
            },
             {
                number: '9',
                name: '小花',
                sex: '女',
                wechat: 'xiaohuazuimei',
                cost: '999',
                tel: '13006666666'
            },
            {
                number: '10',
                name: '小花',
                sex: '女',
                wechat: 'xiaohuazuimei',
                cost: '999',
                tel: '13006666666'
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

.fan-order{
    margin: 10rem auto .625rem;
}

.fan-list{
    display: flex;
    flex-direction: column;
}

.fan-list-item{
    display: flex;
    flex-direction: column;
    margin: 0 .9375rem;
}

.fan-list-item-content{
    display: flex;
    align-items: center;
    justify-content: space-between; 
}

.fan-list-item-number{
    width: 2.5rem;
    height: 1.875rem;
    background:#ddbe59;
    border-radius:.625rem;
    text-align: center;
    color: #ffffff;
    /* margin-left: .9375rem; */
}

.icon-user{
    width: 3.75rem;
    height: 3.75rem;
    /* margin: 0 auto; */
}

.fan-list-userinfo-baseinfo{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

.fan-list-userinfo-contact{
    display: flex;
    flex-direction: column;
}

</style>