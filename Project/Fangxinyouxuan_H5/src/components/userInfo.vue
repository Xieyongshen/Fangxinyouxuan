<template>
    <div>
        <img src="@/assets/me-bg.png" class="me-bg">

        <div class="me-userinfo">
            <div class="me-share">分享店铺</div>
            <img class="me-userinfo-avatar">
            <div class="me-userinfo-name">小鱼</div>
        </div>
    </div>
</template>

<script>
export default {
    name: "userInfo",
    props: {},

    methods: {}
};
</script>

<style scoped>
.me-bg {
    width: 100%;
    height: 18.75rem;
    position: absolute;
    z-index: -1;
}

.me-userinfo {
    width: 100%;
    height: 14.6875rem;
    margin-bottom: 5rem;
    padding-top: 0.9375rem;
    text-align: center;
    box-sizing: border-box;
    position: relative;
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
    font-size: 1rem /* 16/16 */;
    line-height: 1.875rem;
    text-align: center;
    margin-top: 0.625rem;
    box-sizing: border-box;
    display: block;
}

.me-share {
    color: #ffffff;
    font-size: 1rem /* 16/16 */;
    line-height: 30px;
    position: absolute;
    top: 0.625rem;
    left: 1.875rem;
}
</style>
