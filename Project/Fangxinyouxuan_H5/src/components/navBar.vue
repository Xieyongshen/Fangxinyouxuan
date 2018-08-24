<template>
    <div class="navBar">
        <span v-if="isChildPage == 'y'">
            <div class="nav-back">
            <!-- <navigator open-type="navigateBack" delta="1" hover-class="none" class="nav-back"> -->
                <x-icon @click="goBack" type="ios-arrow-back" class="icon-out"></x-icon>
            <!-- </navigator> -->
            </div>
        </span>
        <label class="nav-title">{{ navTitle }}</label>
    </div>
</template>

<script>
export default{
  name: 'navBar',
  props: {
    navTitle: {
      type: String,
      default: ''
    },
    isChildPage: {
      type: String,
      default: 'n'
    }
  },

  methods: {
    goBack () {
      this.$router.go(-1)
    }
  }
}
</script>

<style scoped>
.navBar {
    width: 100%;
    height: 2.8125rem /* 45/16 */;
    text-align: center;
    background: #ffffff;
    box-sizing: border-box;
    position: fixed;
    top: 0;
    z-index: 99;
}

.nav-back {
    height: 2.8125rem /* 45/16 */;
    position: absolute;
    left: 1.25rem /* 20/16 */;
}

.icon-out {
    size: 1.5625rem /* 25/16 */;
    margin: .625rem /* 10/16 */ 0;
}

.nav-title{
    font-size: 1.25rem /* 20/16 */;
    line-height: 2.8125rem /* 45/16 */;
    display: inline-block;
}
</style>
