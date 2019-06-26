from django.shortcuts import render

# Create your views here.
from system.serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from system.models import *

@api_view(http_method_names=['POST'])
def userLogin(request):
    '''
    登陆
    '''
    return Response({'msg':'ok', 'user':{'email': "admin@qq.com",
'id': 10000,
'name': "admin",
'time': 1560477993122,
'token': "a123456B"}})

@api_view(http_method_names=['GET'])
def getUserMenu(request):
    
    '''
    获取菜单
    '''
    # print(request.META)
    userMenu = {
        'app': {
            'name': 'ng-alain-rw',
            'description': 'Ng-zorro admin panel front-end framework',
        },
        'user': {
            'name': 'sola',
            'avatar': 'http://i2.tiimg.com/674794/2b045fc622344d1c.png',
            'email': 'crystalwings@aliyun.com',
            'token': 'a@123456B',
        },
        'menu':[
      {
        'text': '主导航',
        'group': True,
        'children': [
          {
            'text': '仪表盘',
            'link': '/dashboard',
            'icon': { 'type': 'icon', 'value': 'appstore' },
          },
          {
            'text': '快捷菜单',
            'icon': { 'type': 'icon', 'value': 'rocket' },
            'shortcutRoot': True,
          },
          {
            'text': '基础功能',
            'i18n': 'menu.base',
            'group': True,
            'hideInBreadcrumb': True,
            'icon': { 'type': 'icon', 'value': 'appstore' },
            'children': [
              {
                'text': '客户列表',
                'i18n': 'menu.base.customers',
                'hideInBreadcrumb': True,
                'icon': { 'type': 'icon', 'value': 'appstore' },
                'link': '/base/customerlist',
              },
              {
                'text': '客户信息',
                'i18n': 'menu.base.customerinfo',
                'hide': True,
                'link': '/base/customerview',
              },
            ],
          },
          {
            'text': '系统管理',
            'i18n': 'menu.sys',
            'group': True,
            'hideInBreadcrumb': True,
            'icon': { 'type': 'icon', 'value': 'appstore' },
            'children': [
              {
                'text': '用户管理',
                'i18n': 'menu.sys.users',
                'hideInBreadcrumb': True,
                'icon': 'anticon anticon-dashboard',
                'link': '/sys/userlist',
              },
              {
                'text': '用户信息',
                'i18n': 'menu.sys.usersinfo',
                'hide': True,
                'link': '/sys/userinfo',
              },
              {
                'text': '角色管理',
                'i18n': 'menu.sys.role',
                'hideInBreadcrumb': True,
                'icon': 'anticon anticon-dashboard',
                'link': '/sys/rolelist',
              },
              {
                'text': '角色信息',
                'i18n': 'menu.sys.roleinfo',
                'hide': True,
                'link': '/sys/roleinfo',
              },
              {
                'text': '元数据管理',
                'i18n': 'menu.sys.sourcedata',
                'hideInBreadcrumb': True,
                'icon': 'anticon anticon-dashboard',
                'link': '/sys/sourcedata',
              },
              {
                'text': '元数据编辑',
                'i18n': 'menu.sys.sourcedataedit',
                'hide': True,
                'link': '/sys/sourcedataedit',
              },
            ],
          },
        ],
      },
    ]
    }
    return Response(userMenu)

@api_view(http_method_names=['GET'])
def getI18n(request):
    '''
    获取国际化配置文件
    '''
    sysI18n = {
        "menu.search.placeholder": "搜索：员工、文件、照片等",
        "menu.fullscreen": "全屏",
        "menu.fullscreen.exit": "退出全屏",
        "menu.clear.local.storage": "清理本地缓存",
        "menu.lang": "语言",
        "menu.main": "主导航",
        "menu.dashboard": "仪表盘",
        "menu.dashboard.v1": "默认页",
        "menu.dashboard.analysis": "分析页",
        "menu.dashboard.monitor": "监控页",
        "menu.dashboard.workplace": "工作台",
        "menu.shortcut": "快捷菜单",
        "menu.widgets": "小部件",
        "menu.alain": "Alain",
        "menu.style": "样式",
        "menu.style.typography": "字体排印",
        "menu.style.gridmasonry": "瀑布流",
        "menu.style.colors": "色彩",
        "menu.delon": "Delon 类库",
        "menu.delon.form": "动态表单",
        "menu.delon.table": "简易表格",
        "menu.delon.util": "工具集",
        "menu.delon.print": "打印",
        "menu.delon.guard": "路由守卫",
        "menu.delon.cache": "字典缓存",
        "menu.delon.qr": "二维码",
        "menu.delon.acl": "基于角色访问控制",
        "menu.delon.downfile": "下载文件",
        "menu.delon.xlsx": "Excel操作",
        "menu.delon.zip": "本地解压缩",
        "menu.pro": "Antd Pro",
        "menu.form": "表单页",
        "menu.form.basicform": "基础表单",
        "menu.form.stepform": "分步表单",
        "menu.form.stepform.info": "分步表单（填写转账信息）",
        "menu.form.stepform.confirm": "分步表单（确认转账信息）",
        "menu.form.stepform.result": "分步表单（完成）",
        "menu.form.advancedform": "高级表单",
        "menu.list": "列表页",
        "menu.list.searchtable": "查询表格",
        "menu.list.basiclist": "标准列表",
        "menu.list.cardlist": "卡片列表",
        "menu.list.searchlist": "搜索列表",
        "menu.list.searchlist.articles": "搜索列表（文章）",
        "menu.list.searchlist.projects": "搜索列表（项目）",
        "menu.list.searchlist.applications": "搜索列表（应用）",
        "menu.profile": "详情页",
        "menu.profile.basic": "基础详情页",
        "menu.profile.advanced": "高级详情页",
        "menu.result": "结果页",
        "menu.result.success": "成功页",
        "menu.result.fail": "失败页",
        "menu.exception": "异常页",
        "menu.exception.not-permission": "403",
        "menu.exception.not-find": "404",
        "menu.exception.server-error": "500",
        "menu.account": "个人页",
        "menu.account.center": "个人中心",
        "menu.account.settings": "个人设置",
        "menu.account.trigger": "触发错误",
        "menu.account.logout": "退出登录",
        "menu.more": "更多",
        "menu.report": "报表",
        "menu.report.relation": "全屏关系图",
        "menu.extras": "扩展",
        "menu.extras.helpcenter": "帮助中心",
        "menu.extras.settings": "设置",
        "menu.extras.poi": "门店",
        "app.analysis.test": "工专路 {{no}} 号店",
        "app.analysis.introduce": "指标说明",
        "app.analysis.total-sales": "总销售额",
        "app.analysis.day-sales": "日销售额",
        "app.analysis.visits": "访问量",
        "app.analysis.visits-trend": "访问量趋势",
        "app.analysis.visits-ranking": "门店访问量排名",
        "app.analysis.day-visits": "日访问量",
        "app.analysis.week": "周同比",
        "app.analysis.day": "日同比",
        "app.analysis.payments": "支付笔数",
        "app.analysis.conversion-rate": "转化率",
        "app.analysis.operational-effect": "运营活动效果",
        "app.analysis.sales-trend": "销售趋势",
        "app.analysis.sales-ranking": "门店销售额排名",
        "app.analysis.all-year": "全年",
        "app.analysis.all-month": "本月",
        "app.analysis.all-week": "本周",
        "app.analysis.all-day": "今日",
        "app.analysis.search-users": "搜索用户数",
        "app.analysis.per-capita-search": "人均搜索次数",
        "app.analysis.online-top-search": "线上热门搜索",
        "app.analysis.the-proportion-of-sales": "销售额类别占比",
        "app.analysis.channel.all": "全部渠道",
        "app.analysis.channel.online": "线上",
        "app.analysis.channel.stores": "门店",
        "app.analysis.sales": "销售额",
        "app.analysis.traffic": "客流量",
        "app.analysis.table.rank": "排名",
        "app.analysis.table.search-keyword": "搜索关键词",
        "app.analysis.table.users": "用户数",
        "app.analysis.table.weekly-range": "周涨幅",
        "app.monitor.trading-activity": "活动实时交易情况",
        "app.monitor.total-transactions": "今日交易总额",
        "app.monitor.sales-target": "销售目标完成率",
        "app.monitor.remaining-time": "活动剩余时间",
        "app.monitor.total-transactions-per-second": "每秒交易总额",
        "app.monitor.activity-forecast": "活动情况预测",
        "app.monitor.efficiency": "券核效率",
        "app.monitor.ratio": "跳出率",
        "app.monitor.proportion-per-category": "各品类占比",
        "app.monitor.fast-food": "中式快餐",
        "app.monitor.western-food": "西餐",
        "app.monitor.hot-pot": "火锅",
        "app.monitor.waiting-for-implementation": "等待后期实现",
        "app.monitor.popular-searches": "热门搜索",
        "app.monitor.resource-surplus": "资源剩余",
        "app.monitor.fund-surplus": "补贴资金剩余",
        "app.lock": "锁屏",
        "app.login.message-invalid-credentials": "账户或密码错误（admin/ant.design）",
        "app.login.message-invalid-verification-code": "验证码错误",
        "app.login.tab-login-credentials": "账户密码登录",
        "app.login.tab-login-mobile": "手机号登录",
        "app.login.remember-me": "自动登录",
        "app.login.forgot-password": "忘记密码",
        "app.login.sign-in-with": "其他登录方式",
        "app.login.signup": "注册账户",
        "app.login.login": "登录",
        "app.register.register": "注册",
        "app.register.get-verification-code": "获取验证码",
        "app.register.sign-in": "使用已有账户登录",
        "app.register-result.msg": "你的账户：{{email}} 注册成功",
        "app.register-result.activation-email": "激活邮件已发送到你的邮箱中，邮件有效期为24小时。请及时登录邮箱，点击邮件中的链接激活帐户。",
        "app.register-result.back-home": "返回首页",
        "app.register-result.view-mailbox": "查看邮箱",
        "validation.email.required": "请输入邮箱地址！",
        "validation.email.wrong-format": "邮箱地址格式错误！",
        "validation.password.required": "请输入密码！",
        "validation.password.twice": "两次输入的密码不匹配!",
        "validation.password.strength.msg": "请至少输入 6 个字符。请不要使用容易被猜到的密码。",
        "validation.password.strength.strong": "强度：强",
        "validation.password.strength.medium": "强度：中",
        "validation.password.strength.short": "强度：太短",
        "validation.confirm-password.required": "请确认密码！",
        "validation.phone-number.required": "请输入手机号！",
        "validation.phone-number.wrong-format": "手机号格式错误！",
        "validation.verification-code.required": "请输入验证码！",
        "validation.title.required": "请输入标题",
        "validation.date.required": "请选择起止日期",
        "validation.goal.required": "请输入目标描述",
        "validation.standard.required": "请输入衡量标准",
        "menu.base": "基础模块",
        "menu.base.customers": "客户管理",
        "menu.base.customerinfo": "客户详情",
        "menu.sys": "系统设置",
        "menu.sys.users": "用户管理",
        "menu.sys.usersinfo": "用户详情",
        "menu.sys.role": "角色管理",
        "menu.sys.roleinfo": "角色详情",
        "menu.sys.gridster": "gridster插件",
        "menu.sys.sourcedata": "元数据管理",
  "menu.sys.sourcedataedit": "元数据编辑"
    }
    return Response(sysI18n)

@api_view(http_method_names=['GET'])
def getUserList(request):
    '''
    获取用户列表
    '''
    # print(request.META.get("HTTP_SUMMER_LIGHT_TOKEN"))
    users = User.objects.all()[:10]
    serializer = UserSerializer(users, many=True)
    return Response({'total':130, 'list':serializer.data})

@api_view(http_method_names=['GET'])
def getUserById(request):
    '''
    获取单个用户
    '''
    print(request.query_params['id'])
    user = User.objects.get(id=str(6))
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(http_method_names=['GET'])
def getRoleList(request):
    '''
    获取角色列表
    '''
    roles = Role.objects.all()[:10]
    serializer = RoleSerializer(roles, many=True)
    return Response({'total':130, 'list':serializer.data})

@api_view(http_method_names=['GET'])
def getRoleById(request):
    '''
    获取单个角色
    '''
    role = Role.objects.get(id=str(6))
    serializer = RoleSerializer(role, many=False)
    return Response(serializer.data)

@api_view(http_method_names=['GET'])
def getRoleByUserId(request):
    '''
    获取某用户的角色
    '''
    roles = Role.objects.all()[:10]
    serializer = RoleSerializer(roles, many=True)
    return Response({'total':130, 'list':serializer.data})

@api_view(http_method_names=['GET'])
def getMenuList(request):
    '''
    获取菜单列表
    '''
    menus = Menu.objects.all()[:10]
    serializer = MenuSerializer(menus, many=True)
    return Response({'total':130, 'list':serializer.data})

@api_view(http_method_names=['GET'])
def getMenuById(request):
    '''
    获取单个菜单
    '''
    menu = Menu.objects.get(id=str(6))
    serializer = MenuSerializer(menu, many=False)
    return Response(serializer.data)

@api_view(http_method_names=['GET'])
def getMenuByUserId(request):
    '''
    获取某用户的菜单
    '''
    menus = Menu.objects.all()[:10]
    serializer = MenuSerializer(menus, many=True)
    return Response({'total':130, 'list':serializer.data})