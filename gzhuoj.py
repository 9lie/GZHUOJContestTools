import getpass, requests, random, json

header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

main_url = 'http://172.22.27.1/'
login_url = main_url + 'doLogin'
reg_url = main_url + 'reg'
restorePsw_url = main_url + 'restorePsw'
changeInfo_url = main_url + 'changeInfo'
changePvl_url = main_url + 'changePvl'
regContestAdd_url = main_url + 'regContestAdd'
toggleStar_url = main_url + 'toggleStar'
getStatus_url = main_url + 'getStatus'

def doLogin(username, password):
    '''
    登录
    '''
    global header
    data = {
        'username': username,
        'password': password
    }
    response = requests.post(login_url, headers=header, data=data)
    if response.text == '1':
        print(username, 'the user is not exist!')
    elif response.text == '2':
        print(username, 'username and password do not match!')
    else:
        print(username, 'success login!')
        cookies = requests.utils.dict_from_cookiejar(response.cookies)
        header['cookie'] = '; '.join([str(x) + '=' + str(y) for x, y in cookies.items()])
        return True
    return False


def adminLogin():
    while True:
        password = getpass.getpass('enter the password:')
        if doLogin('admin', password):
            break


def checkLogin():
    '''
    检测是否登录，主要原理是看能不能打开更改头像的页面
    '''
    url = main_url + 'avatar'
    response = requests.get(url, headers=header, allow_redirects=False)
    # 阻止 302 自动重定向
    return response.status_code == 200


def changeInfo(name, oldpassword, password, nick, school='', email='', signature=''):
    '''
    这个函数主要用来更改密码
    '''
    data = {
        'name': name,
        'oldpassword': oldpassword,
        'password': password,
        'nick': nick,
        'school': school,
        'email': email,
        'signature': signature
    }
    response = requests.post(changeInfo_url, headers=header, data=data)
    print(response.text)
    if response.text == '1':
        print('oldpassword is wrong!')
    else:
        print('success changeInfo!')


def restorePsw(name):
    '''
    重置密码为123456
    '''
    requests.post(restorePsw_url, headers=header, data={
        'name': name
    })


def makePassword(length):
    '''
    生成密码
    length 表示密码长度
    '''
    str = '23456789abdefghijmnqrtyABDEFGHJLMNQRTY'
    # 密码的字符集要避免相似的字符，也尽量避免大小写差不多的字符
    return random.sample(str * length, length)


def reg(name, realname, sex, college, gde):
    '''
    可能需要管理员登录才能用这个函数
    这个函数可以用来注册或者更改用户的信息
    name 用户名
    realname 真实姓名
    sex 0 男 1 女
    college
    gde 年级 + 班 例如 181
    collegeList = ['其他', '计机', '数院', '土木', '物电', '机电', '华软', '腾讯', '网易', '阿里', 'YY']，参数为下标

    并且非常难受的一件事是只有这里注册可以更改帐号的学号，并且其他地方暂时找不到可以更改学号的地方
    更难受的是学号直接等于帐号名称，也就是说要么帐号直接用学号注册，要么学号那一栏会显示用户名???
    '''
    data = {
        'name': name,
        'realname': realname,
        'sex': str(sex),
        'college': str(college),
        'gde': str(gde)
    }
    response = requests.post(reg_url, headers=header, data=data)
    print(response.text)
    if response.text == '1' or response.text == '2':
        print(name, 'success reg!')
    else:
        print('something wrong!')


def changePvl(name, pvl, realname, sex, college, grade):
    '''
    pvl ['本校学生', '普通队员', '资深队员', '贵宾', '队长', '老师']
        ['70', '71', '72', '73', '81', '82']
    其他和上面一样
    '''
    requests.post(changePvl_url, headers=header, data={
        'name': name,
        'pvl': pvl,
        'realname': realname,
        'sex': sex,
        'college': college,
        'grade': grade
    })


def regContestAdd(cid, name):
    '''
    给比赛添加选手
    cid 比赛的id
    '''
    requests.post(regContestAdd_url, headers=header, data={
        'cid': str(cid),
        'name': name
    })


def toggleStar(cid, name, type):
    '''
    给比赛选手打星
    type: 1 打星 2 取消打星
    '''
    requests.post(regContestAdd_url, headers=header, data={
        'cid': str(cid),
        'name': name,
        'type': str(type)
    })


def getStatus(cid, page, name, pid, result):
    '''
    获取比赛的榜
    cid 比赛的id
    page 第几页
    name 指定用户名
    pid 指定题目id
    reslut = 2 ac

    返回值有两个
    第一个是一个list，每个元素是一个dict，包括：
        runID 提交的id
        userName 用户名
        problemID 题目id
        result 
        time 运行时间 ms
        memory 运行内存 KB
        language 使用语言
        length 代码长度 B
        inDate 提交时间戳
    第二个返回值是一共有多少页提交
    '''
    response = requests.post(getStatus_url, headers=header, data={
        'cid': str(cid),
        'page': str(page),
        'name': name,
        'pid': str(pid),
        'result': str(result)
    });
    ret = json.loads(response.text)
    return ret[0], ret[1]


if __name__ == '__main__':
    print(checkLogin())
    adminLogin()
    reg('test1231231', '123123', 0, 0, 211)
    restorePsw('test1231231')
    doLogin('test1231231', '123456')
    changeInfo('test1231231', '123456', '114514', '666')
    print(checkLogin())
