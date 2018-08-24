<template>
    <div class="team">

        <search class="team-search"
            @result-click="resultClick"
            @on-change="getResult"
            :results="results"
            v-model="value"
            position="absolute"
            auto-scroll-to-top
            @on-focus="onFocus"
            @on-cancel="onCancel"
            @on-submit="onSubmit"
            ref="search">
        </search>

        <div :class="{ placeHolder: placeHolderShow}"></div>

        <div class="team-toolBar">
            <div class="team-toolBar-select">
                <img src="">
                <div class="team-toolBar-select-text">全部</div>
            </div>
            <div class="team-toolBar-totalTeamMenber">团队总人数: {{totalTeamMenber}}</div>
        </div>

        <div class="team-list">
            <div class="team-list-item" v-for="item in items" :key="item.number">
                <div class="team-list-item-content">
                    <img src="@/assets/ic_user.png" class="icon-user">
                    <div class="team-list-item-userinfo">
                        <div class="accountDetail-list-item-name">{{item.username}}</div>
                        <div class="accountDetail-list-item-recommendedBy">推荐人: {{item.recommendedBy}}</div>
                        <div class="accountDetail-list-item-recommendedTime">{{item.recommendedTime}}</div>
                    </div>
                    <div class="accountDetail-list-item-recommendedFrom">来源: {{item.recommendedFrom}}</div>
                    <img src="@/assets/in.png" class="icon-in">
                </div>
                <hr class="divider">
            </div>
        </div>

    </div>
</template>

<script>
import { Search } from 'vux'

export default {
  name: 'team',
  components: {
    Search
  },

  data: function () {
    return {
      totalTeamMenber: '85',
      results: [],
      value: '',
      placeHolderShow: false,
      items: [
        {
          number: '1',
          username: '初夏',
          recommendedBy: '小黄',
          recommendedTime: '2018-07-02 01:11:01',
          recommendedFrom: '二维码'
        },
        {
          number: '2',
          username: '李颖',
          recommendedBy: 'lily bai',
          recommendedTime: '2018-07-02 01:11:01',
          recommendedFrom: '分享'
        },
        {
          number: '3',
          username: '薄荷',
          recommendedBy: '多多麻麻',
          recommendedTime: '2018-07-02 01:11:01',
          recommendedFrom: '二维码'
        }
      ]
    }
  },

  methods: {
    setFocus () {
      this.$refs.search.setFocus()
    },
    resultClick (item) {
      window.alert('you click the result item: ' + JSON.stringify(item))
    },
    getResult (val) {
      console.log('on-change', val)
      this.results = val ? getResult(this.value) : []
    },
    onSubmit () {
      this.$refs.search.setBlur()
    },
    onFocus () {
      console.log('on focus')
      this.placeHolderShow = true
    },
    onCancel () {
      console.log('on cancel')
      this.placeHolderShow = false
    }
  }

}

function getResult (val) {
  let rs = []
  for (let i = 0; i < 20; i++) {
    rs.push({
      title: `${val} result: ${i + 1} `,
      other: i
    })
  }
  return rs
}
</script>

<style scoped>
.divider{
    color: #888888;
    margin: 1.25rem 0;
    line-height: 1px;
}

.team-search{
    margin-top: 3.875rem;
}

.placeHolder{
    height: 7.5625rem;
}

.team-toolBar{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin: .9375rem 0.9375rem;
}

.team-toolBar-select{
    display: flex;
    flex-direction: column;
}

.team-list{
    display: flex;
    flex-direction: column;
}

.team-list-item{
    display: flex;
    flex-direction: column;
    margin: 0 0.9375rem;
}

.team-list-item-content{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}

.team-list-item-userinfo{
    display: flex;
    flex-direction: column;
}

.accountDetail-list-item-recommendedBy{
    font-size: 15px;
    color: #888888;
}

.accountDetail-list-item-recommendedTime{
    font-size: 15px;
    color: #888888;
}

.accountDetail-list-item-recommendedFrom{
    font-size: 15px;
    align-self: flex-end;
}

.icon-user{
    width: 6.25rem;
    height: 6.25rem;
    /* margin: 0 auto; */
}

.icon-in{
    width: 0.875rem;
    height: 1.5rem;
}

</style>
