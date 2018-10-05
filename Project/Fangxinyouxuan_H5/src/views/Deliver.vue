<template>
    <div class="deliver">
        <div class="deliver-config">
            <check-icon :value.sync="deliverConfig">配送到家</check-icon>
        </div>
        <div class="deliver-content">
            <group>
                <div class="deliver-time">
                    <div>配送时间</div>
                    <checker v-model="deliverTime" :max="1" default-item-class="deliver-time-item" selected-item-class="deliver-time-item-selected">
                        <checker-item :value="1">全天</checker-item>
                        <checker-item :value="2">上午09:00-下午18:00</checker-item>
                    </checker>
                </div>
                <PopupRadio title="配送距离" placeholder="500m" v-model="deliverDistance" :options="deliverDistanceList"></PopupRadio>
                <XInput title="配送费用" placeholder="_____元"></XInput>
            </group>
        </div>
        <div class="button-submit">
            <XButton mini type="primary">确认提交</XButton>
        </div>
    </div>
</template>

<script>
import {
    CheckIcon,
    Checker,
    CheckerItem,
    PopupRadio,
    XInput,
    XButton
} from "vux";

export default {
    name: "ranking",
    components: {
        CheckIcon,
        Checker,
        CheckerItem,
        PopupRadio,
        XInput,
        XButton
    },

    data: function() {
        return {
            deliverConfig: false,
            deliverTime: "1",
            deliverDistance: "",
            deliverDistanceList: ["500m", "1000m", "2000m"]
        };
    },

    methods: {}
};
</script>

<style scoped>
.deliver {
    display: flex;
    flex-direction: column;
}

.deliver-config {
    padding: 0.3125rem /* 5/16 */ 0.625rem /* 10/16 */;
    border-bottom: 1px solid #cccccc;
}

.deliver-content {
    font-size: 1rem /* 16/16 */;
}

.deliver-time {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.625rem /* 10/16 */ 0.9375rem /* 15/16 */;
}

.deliver-time-item {
    height: 1.5rem /* 24/16 */;
    line-height: 1.5rem /* 24/16 */;
    text-align: center;
    border-radius: 3px;
    border: 1px solid #cccccc;
    background-color: #fff;
    padding: 0 0.9375rem;
    margin-right: 6px;
}

.deliver-time-item-selected {
    border-color: #f5333f;
}

.button-submit {
    align-self: flex-end;
    margin: 0 1.25rem;
}
</style>
