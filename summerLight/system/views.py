from django.shortcuts import render

# Create your views here.
from system.serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from system.models import *
from common import sqlutils,utils

@api_view(http_method_names=['GET'])
def addValue(request):
  '''
  新增数据
  '''
  # I18n.objects.create(language='zh-cn', code='menu.sys.org.list', value='组织机构')
  # I18n.objects.create(language='zh-tw', code='menu.sys.org.list', value='组织机构')
  # I18n.objects.create(language='en-us', code='menu.sys.org.list', value='organization')

  # dict.objects.create(code='Sourcedata-Interface-Type', name='列表查询', value='queryinlist', pid='13dcb7ca9e2611e988d25076af3da2a3')
  # dict.objects.create(code='Sourcedata-Interface-Type', name='表单查询', value='queryinform', pid='13dcb7ca9e2611e988d25076af3da2a3')
  # dict.objects.create(code='Sourcedata-Interface-Type', name='新增', value='add', pid='13dcb7ca9e2611e988d25076af3da2a3')
  # dict.objects.create(code='Sourcedata-Interface-Type', name='编辑', value='update', pid='13dcb7ca9e2611e988d25076af3da2a3')
  # dict.objects.create(code='Sourcedata-Interface-Type', name='删除', value='delete', pid='13dcb7ca9e2611e988d25076af3da2a3')

  return Response({'msg': '结束'})

@api_view(http_method_names=['GET'])
def getOrgList(request):
  orgList = [{
    
  }]
  return Response({'msg': '结束'})

@api_view(http_method_names=['GET'])
def getI18nList(request):
  '''
  获取国际化的数据列表
  '''
  sqlSession = sqlutils.SqlUtils()
  sql = '''
    SELECT "code" FROM system_i18n GROUP BY "code"
  '''
  resultList = sqlSession.getDictResult(sql)
  sqlSession.closeConnect()
  return Response(resultList)

@api_view(http_method_names=['GET'])
def getI18nInfo(request):
  '''
  获取国际化的数据详情
  '''
  i18nCode = request.query_params['code']
  sqlSession = sqlutils.SqlUtils()
  sql = f'''
    SELECT * FROM system_i18n WHERE "code" = '{i18nCode}'
  '''
  resultList = sqlSession.getDictResult(sql)
  return Response(resultList)

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
            'icon': { 'type': 'icon', 'value': 'setting' },
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
              {
                'text': '国际化配置',
                'i18n': 'menu.sys.i18n.list',
                'link': '/sys/i18nlist',
              },
              {
                'text': '组织机构配置',
                'i18n': 'menu.sys.org.list',
                'link': '/sys/orglist',
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
    lan = 'zh-CN'
    if 'lan' in request.GET:
      lan = request.GET['lan']
    sqlSession = sqlutils.SqlUtils()
    sql = f'''
      SELECT "code", "value" FROM system_i18n WHERE "language" = '{lan}' ORDER BY "update_date"
    '''
    resultList = sqlSession.getDictResult(sql)
    i18nList = {}
    for item in resultList:
      i18nList[item['code']] = item['value']
    return Response(i18nList)

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

@api_view(http_method_names=['GET'])
def getDictItemByCode(request):
    '''
    根据code获取字典列表
    '''
    resultObj = utils.successMes()
    dictCode = request.GET['code']
    sqlSession = sqlutils.SqlUtils()
    dictSql = f'''
      SELECT * FROM system_dict WHERE "code" = '{dictCode}' AND "pid" <> '-1'
    '''
    dictList = sqlSession.getDictResult(dictSql)
    resultObj['data'] = dictList
    return Response(resultObj)

@api_view(http_method_names=['GET'])
def initSourcedata(request):
    sqlSession = sqlutils.SqlUtils()
    columns = sqlSession.getTableStructure('customer_customer')
    sqlSession.closeConnect()
    columnsInfo = []
    for col in columns:
      columnInfo = {}
      columnInfo['field'] = col['column_name']
      columnInfo['label'] = ''
      if 'char' in col['column_name'] or 'text' in col['column_name']:
        columnInfo['fieldType'] = 'string'
      elif 'int' in col['column_name'] or 'float' in col['column_name']:
        columnInfo['fieldType'] = 'number'
      elif 'time' in col['column_name'] or 'date' in col['column_name']:
        columnInfo['fieldType'] = 'date'
      else:
        columnInfo['fieldType'] = 'string'
      if col['column_name'] == 'id':
        columnInfo['primarykey'] = True
      else:
        columnInfo['primarykey'] = False
      columnInfo['controlType'] = ''
      columnInfo['labelspan'] = 150
      columnInfo['dict'] = ''
      columnInfo['dateformat'] = 'yyyy/MM/dd'
      columnsInfo.append(columnInfo)
    tableinfo = {
      "id": "",
      "tablename": "customer_customer",
      "tabledesc": "",
      "type": "",
      "remark": "",
      "roptions": {
        "interface": [{
          "type": "queryinlist",
          "url": "/api/queryxxx"
        }],
        "listConfig": {
          "columns": []
        },
        "formConfig": {
          "columns": []
        },
        "columns": columnsInfo
      }
    }
    return Response(tableinfo)