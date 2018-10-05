<template>
    <div class="myAccount">
        <user-info></user-info>

        <div class="wallet-money">
            <label class="wallet-money-label">我的金库</label>
            <div class="wallet-money-total">
                <img src="@/assets/ic_money.png" class="wallet-money-total-icon">
                <label>{{totalMoney}}</label>
            </div>
        </div>

        <div class="wallet-manage weui-cells">
            <a @click="goFan" class="weui-cell weui-cell_access" href="javascript:;">
                <div class="weui-cell__bd">
                    <p>我的粉丝</p>
                </div>
                <div class="weui-cell__ft">{{fansNumber}}个</div>
            </a>
            <a @click="goAccountDetai" class="weui-cell weui-cell_access" href="javascript:;">
                <div class="weui-cell__bd">
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
import userInfo from "@/components/userInfo.vue";

export default {
    name: "account",
    components: { userInfo },

    data: function() {
        return {
            totalMoney: 0.0,
            fansNumber: 666
        };
    },

    methods: {
        goFan() {
            this.$router.push("/account/fan");
        },
        goAccountDetai() {
            this.$router.push("/account/accountDetail");
        },
        goWithdrawRecord() {
            this.$router.push("/account/withdrawRecord");
        },
        goRecharge() {
            this.$router.push("/account/recharge");
        },
        goWithdraw() {
            this.$router.push("/account/withdraw");
        }
    }
};
</script>

<style scoped>
.wallet-money {
    width: 100%;
    color: #333;
    font-size: 1.0625rem /* 17/16 */;
    text-align: center;
    margin: 0 auto 1.25rem;
}

.wallet-monye-label {
    display: block;
}

.wallet-money-total {
    color: #fdb85d;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 0.5rem;
}

.wallet-money-total-icon {
    width: 2.25rem;
    height: 2.25rem;
}

.wallet-option {
    margin: 1.875rem 1.875rem;
}
</style>
