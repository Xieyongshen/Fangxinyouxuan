<template>
  <div id="app">
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div> -->
    <router-view  v-wechat-title='$route.meta.title' />
  </div>
</template>

<style>
#app {
    word-wrap: break-word;
    font-family: Microsoft YaHei;
    color: #333;
    -webkit-text-size-adjust: none;
}

#app *{
    -webkit-tap-highlight-color: transparent;
    -webkit-user-select:none;
}

html{
  color: #424242;
  font-size: 16px;
}
</style>

<style lang="less">
@import '~vux/src/styles/reset.less';
</style>

<style lang="less">
@import '~vux/src/styles/reset.less';
</style>

<style lang="less">
@import '~vux/src/styles/reset.less';
</style>
