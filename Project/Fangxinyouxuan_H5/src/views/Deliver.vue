<template>
    <div class="deliver">
        <div class="deliver-config">
            <check-icon :value.sync="deliverConfig">配送到家</check-icon>
        </div>
        <div class="deliver-content">
            <hr class="divider">
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
            <hr class="divider">
        </div>
        <div class="button-submit">
            <XButton mini type="primary">确认提交</XButton>
        </div>
    </div>
</template>

<script>
import { CheckIcon, Checker, CheckerItem, PopupRadio, XInput, XButton } from 'vux'

export default {
  name: 'ranking',
  components: {
    CheckIcon,
    Checker,
    CheckerItem,
    PopupRadio,
    XInput,
    XButton
  },

  data: function () {
    return {
      deliverConfig: false,
      deliverTime: '1',
      deliverDistance: '',
      deliverDistanceList: ['500m', '1000m', '2000m']
    }
  },

  methods: {
  }
}
</script>

<style scoped>
.divider{
    color: #888888;
    margin: 1.25rem 1.25rem;
    line-height: 1px;
}

.deliver{
    display: flex;
    flex-direction: column;
}

.deliver-config{
    margin:4.5rem 0 0 0.9375rem;
}

.deliver-time{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin:.625rem 1.25rem;
}

.deliver-time-item {
  height: 26px;
  line-height: 26px;
  text-align: center;
  border-radius: 3px;
  border: 1px solid #ccc;
  background-color: #fff;
  padding: 0.3125rem 0.9375rem;
  margin-right: 6px;
}

.deliver-time-item-selected {
  border-color: #ff4a00;
}

.button-submit{
    align-self: flex-end;
    margin: 0 1.25rem;

}

</style>
