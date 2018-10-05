import wepy from 'wepy';

const log_in = async (params) => {
    let login_res = await wepy.login();
    let code = login_res.code
    let get_res = await wepy.getUserInfo()
    let encryptedData = get_res.encryptedData || 'encry';
    let iv = get_res.iv || 'iv';
    let jwt = await wepy.request({
        url:
            'http://fangxintech.com' +
            '/auth/token?code=' +
            code,
        data: {
            username: encryptedData,
            password: iv,
            grant_type: 'password',
            auth_approach: 'wxapp'
        },
        method: 'POST',
        header: {
            'Content-Type':
                'application/x-www-form-urlencoded'
        },
    });
    wx.showToast({
        title: '登录成功',
        icon: 'success'
    });
    wx.setStorageSync('jwt',jwt);
    return jwt
}

module.exports = {
    log_in
}

