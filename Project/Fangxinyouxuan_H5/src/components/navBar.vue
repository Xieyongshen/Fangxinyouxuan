<template>
    <div class="navBar">
        <block v-if="isChildPage == 'y'">
            <div class="nav-back">
            <!-- <navigator open-type="navigateBack" delta="1" hover-class="none" class="nav-back"> -->
                <img @click="goBack" src="@/assets/out.png" class="icon-out">
            <!-- </navigator> -->
            </div>
        </block>
        <label class="nav-title">{{ navTitle }}</label>
    </div>
</template>

<script>
    export default{
        name: 'navBar',
        props: {
            navTitle: {
                type: String,
                default: '',
            },
            isChildPage: {
                type: String,
                default: 'n'
            }
       },

       methods: {
           goBack(){
               this.$router.go(-1)
           }
       }
    }
</script>

<style scoped>
.navBar {
    width: 100%;
    height: 3.875rem;
    text-align: center;
    padding: 1.25rem 0;
    background: #ffffff;
    box-sizing: border-box;
    position: fixed;
    top: 0;
    z-index: 99;
}

.nav-back {
    width: 3.125rem;
    text-align: left;
    position: absolute;
    left: 1.875rem;
}

.icon-out {
    width: 0.75rem;
    height: 1.25rem;
}

.nav-title{
    font-size: 20px;
    line-height: 1rem;
    display: inline-block;
}
</style>