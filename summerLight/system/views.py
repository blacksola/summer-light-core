import json
import logging
# Create your views here.
import urllib.parse
import urllib.request

from django.forms.models import model_to_dict
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from common import sqlutils, utils
from system.models import *
from system.serializer import *

logger = logging.getLogger('summerLight')
@api_view(http_method_names=['GET'])
def addValue(request):
  '''
  新增数据
  '''
  # I18n.objects.create(language='zh-CN', code='rw.incontrol.actions.reset', value='重置')
  # I18n.objects.create(language='zh-TW', code='rw.incontrol.actions.reset', value='重置')
  # I18n.objects.create(language='en-US', code='rw.incontrol.actions.reset', value='reset')
  # dict.objects.create(code='Table-RowHeight', name='表格高', pid='-1')
  # dict.objects.create(code='Button-Layout', name='标准客户', value='l2', pid='3c4c96d2a76f11e996ac5076af3da2a3')
  # dict.objects.create(code='Button-Layout', name='普通客户', value='l3', pid='3c4c96d2a76f11e996ac5076af3da2a3')
  # dict.objects.create(code='Button-Layout', name='黑名单', value='l9', pid='3c4c96d2a76f11e996ac5076af3da2a3')

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
    logger.debug('debug-----------------------------------qweqwe3453')
    logger.info('info-----------------------------------qweqwe1123')
    logger.error('error-----------------------------------qweqwe678')
    # print(request.META)
    userMenu = {
        'app': {
            'name': 'in-control-rw',
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
            'text': '基础功能',
            'i18n': 'menu.base',
            'group': True,
            'hideInBreadcrumb': True,
            'icon': { 'type': 'icon', 'value': 'wallet' },
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
              {
                'text': '数据字典',
                'i18n': 'menu.sys.dict.list',
                'link': '/sys/dictlist',
              },
              {
                'text': '模块管理',
                'i18n': 'menu.sys.module.list',
                'link': '/sys/modulelist',
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
def getUserTables(request):
    '''
    获取数据库所有的表
    '''
    resultObj = utils.successMes()
    sqlSession = sqlutils.SqlUtils()
    dictSql = f'''
      SELECT tablename FROM pg_tables WHERE tablename NOT LIKE 'pg%' AND tablename NOT LIKE 'sql_%' ORDER BY tablename
    '''
    dictList = sqlSession.getDictResult(dictSql)
    resultObj['data'] = dictList
    return Response(resultObj)

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
def getAllSourcedata(request):
  '''
  获取元数据配置列表
  '''
  resultObj = utils.successMes()
  try:
    pageSize = request.GET['pageSize']
    pageIndex = int(request.GET['pageIndex'])-1
    sortField = request.GET['sortField']
    sortOrder = request.GET['sortOrder']
    whereStr = ''
    sqlSession = sqlutils.SqlUtils()
    querySql = f'''
      SELECT "id", "tablename", "tabledesc", "tablestatus", "type", "remark", "add_date", "update_date" 
      FROM system_sourcedata {whereStr} ORDER BY {sortField} {sortOrder} LIMIT {pageSize} OFFSET {pageIndex}
    '''
    listData = sqlSession.getDictResult(querySql)
    total = sqlSession.getTotal(querySql)
    resultObj['data'] = {
      'list': listData,
      'total': total
    }
  except Exception as e:
    resultObj = utils.errorMes(e)
    print(e)
  finally:
    if sqlSession:
      sqlSession.closeConnect()
  return Response(resultObj)

@api_view(http_method_names=['POST'])
def initSourcedata(request):
  '''
  初始化元数据
  '''
  initInfo = request.data['initInfo']
  resultObj = utils.successMes()
  sqlSession = sqlutils.SqlUtils()
  columns = sqlSession.getTableStructure(initInfo['selectTable'])
  sqlSession.closeConnect()
  columnsInfo = []
  for col in columns:
    columnInfo = {}
    columnInfo['field'] = col['column_name']
    columnInfo['label'] = ''
    if columnInfo['field'] == 'name':
      columnInfo['label'] = '名称'
    if columnInfo['field'] == 'sub_name':
      columnInfo['label'] = '简称'
    if columnInfo['field'] == 'address':
      columnInfo['label'] = '地址'
    if columnInfo['field'] == 'type':
      columnInfo['label'] = '类型'
    if columnInfo['field'] == 'tags':
      columnInfo['label'] = '标签'
    if columnInfo['field'] == 'phone':
      columnInfo['label'] = '电话'
    if columnInfo['field'] == 'email':
      columnInfo['label'] = '邮箱'
    if columnInfo['field'] == 'web_site':
      columnInfo['label'] = '网址'
    if columnInfo['field'] == 'level':
      columnInfo['label'] = '等级'
    if columnInfo['field'] == 'status':
      columnInfo['label'] = '状态'
    if 'char' in col['column_name'] or 'text' in col['column_name']:
      columnInfo['fieldType'] = 'char'
    elif 'int' in col['column_name'] or 'float' in col['column_name']:
      columnInfo['fieldType'] = 'number'
    elif 'time' in col['column_name'] or 'date' in col['column_name']:
      columnInfo['fieldType'] = 'date'
    else:
      columnInfo['fieldType'] = 'char'
    if col['column_name'] == 'id':
      columnInfo['primaryKey'] = 'y'
      columnInfo['label'] = '主键'
    else:
      columnInfo['primaryKey'] = 'n'
    columnInfo['controlType'] = 'text'
    columnInfo['labelspan'] = 130
    columnInfo['dict'] = ''
    columnInfo['dateformat'] = 'YYYY/MM/DD'
    columnsInfo.append(columnInfo)
  tableinfo = {
    "id": "",
    "tablename": initInfo['selectTable'],
    "tabledesc": initInfo['desc'],
    "type": "table",
    "tablestatus": "enable",
    "remark": "",
    "roptions": {
      "listConfig": {
        "base": {},
        "columns": []
      },
      "formConfig": {
        "base": {},
        "columns": []
      },
      "columns": columnsInfo
    }
  }
  row = sourceData.objects.create(tablename=initInfo['selectTable'], tabledesc=initInfo['desc'], 
                      tablestatus='enable', type='table', remark='备注、、、、、、备注',
                      roptions=json.dumps(tableinfo['roptions']))
  tableinfo['id'] = row.id
  resultObj['data'] = tableinfo
  return Response(resultObj)

@api_view(http_method_names=['POST'])
def saveSourceData(request):
    '''
    保存元数据
    '''
    resultObj = utils.successMes()
    obj = request.data['params']
    if 'id' in obj and len(obj['id']) > 1:
      row = sourceData.objects.get(id=obj['id'])
      row.tablename=obj['tablename']
      row.tabledesc=obj['tabledesc']
      row.tablestatus=obj['tablestatus']
      row.type=obj['type']
      row.remark=obj['remark']
      row.roptions=json.dumps(obj['roptions'])
      row.save()
    else:
      sourceData.objects.create(tablename=obj['tablename'], tabledesc=obj['tabledesc'], 
                      tablestatus=obj['tablestatus'], type=obj['type'], remark=obj['remark'],
                      roptions=json.dumps(obj['roptions']))
    resultObj['data'] = ''
    resultObj['interfaceType'] = 'save'
    resultObj['msg'] = '保存成功'
    return Response(resultObj)    

@api_view(http_method_names=['GET'])
def getSourceData(request):
  '''
  根据id获取元数据配置
  '''
  resultObj = utils.successMes()
  try:
    sqlSession = sqlutils.SqlUtils()
    row = sourceData.objects.get(id=str(request.GET['id']))
    resultData = model_to_dict(row)
    resultData['roptions'] = json.loads(resultData['roptions'])
    resultData['id'] = row.id
    resultObj['data'] = resultData
  except Exception as e:
    resultObj = utils.errorMes(e)
    print(e)
  finally:
    if sqlSession:
      sqlSession.closeConnect()
  return Response(resultObj)

@api_view(http_method_names=['POST'])
def getDataByDataSourceConfig(request):
  '''
  根据元数据配置获取业务数据
  '''
  resultObj = utils.successMes()
  try:
    configs = request.data['params']
    tableName = configs['tablename']
    sqlSession = sqlutils.SqlUtils()
    querySql = f'''
      SELECT * FROM {tableName}
    '''
    listData = sqlSession.getDictResult(querySql)
    total = sqlSession.getTotal(querySql)
    resultObj['data'] = {
      'list': listData,
      'total': total
    }
  except Exception as e:
    resultObj = utils.errorMes(e)
    print(e)
  finally:
    if sqlSession:
      sqlSession.closeConnect()
  return Response(resultObj)
  
@api_view(http_method_names=['GET'])
def getTables(request):
  '''
  根据id获取元数据配置
  '''
  resultObj = utils.successMes()
  try:
    sqlSession = sqlutils.SqlUtils(dbType='mysql')
    sqlStr = f'''
    SELECT
      table_name,
      table_type,
      `ENGINE`
    FROM
      information_schema. TABLES
    WHERE
      table_schema = 'incontrol'
    ORDER BY
      table_name DESC
    '''
    rows = sqlSession.getDictResult(sqlStr)
    resultObj['data'] = rows
  except Exception as e:
    resultObj = utils.errorMes(e)
    print(e)
  finally:
    if sqlSession:
      sqlSession.closeConnect()
  return Response(resultObj)

@api_view(http_method_names=['POST'])
def getIncontrolUsers(request):
  '''
  获取用户信息
  '''
  resultObj = utils.successMes()
  try:
    sqlSession = sqlutils.SqlUtils(dbType='mysql')
    querySql = '''
      SELECT *
      FROM sys_user ORDER BY MODIFYDATE 
    '''
    listData = sqlSession.getDictResult(querySql + ' LIMIT 15 OFFSET 1')
    total = sqlSession.getTotal(querySql)
    resultObj['records'] = listData
    resultObj['total'] = total['total']
  except Exception as e:
    resultObj = utils.errorMes(e)
    print(e)
  finally:
    if sqlSession:
      sqlSession.closeConnect()
  return Response(resultObj)

@api_view(http_method_names=['POST'])
def doWxLogin(request):
  resultObj = utils.successMes()
  try:
    obj = request.data['code']
    data = urllib.parse.urlencode({'appid': 'wx351b6e0935ab0156', 'secret': '02d1893f939b1fbd4160991b34112945', 'js_code':str(obj),'grant_type':'authorization_code'})
    response = urllib.request.urlopen('https://api.weixin.qq.com/sns/jscode2session?%s' % data)
    html = response.read()
    returnMsg = html.decode('utf-8')
    print(returnMsg)
    resultObj['records'] = returnMsg;
  except Exception as e:
    resultObj = utils.errorMes(e)
    print(e)
  finally:
    pass
  return Response(resultObj)

@api_view(http_method_names=['POST'])
def getBillList(request):
  resultObj = utils.successMes()
  try:
    obj = request.data['codes']
    billList = [{
        'addressName': '我家',
        'amount': '600',
        'amountSymbol': '￥',
        'waterRate': {
          'name': '水费-浦东新区 2019年8月',
          'amount': 35.98,
          'showDetail': False,
          'start': 230,
          'end': 260,
        },
        'propertyCosts': {
          'name': '物业费-浦东新区  2019年8月',
          'amount': 1170,
          'showDetail': False,
          'detail': [{
              'name': '物业费',
              'amount': 8
            },
            {
              'name': '垃圾处置费',
              'amount': 8
            },
            {
              'name': '垃圾清运费',
              'amount': 5
            },
            {
              'name': '路灯费',
              'amount': 0.45
            },
            {
              'name': '电梯服务费',
              'amount': 35.26
            },
            {
              'name': '房租',
              'amount': 67.25
            }
          ]
        }
      },
      {
        'addressName': '父母家',
        'amount': '500',
        'amountSymbol': '￥',
        'waterRate': {
          'name': '水费-浦东新区 2019年8月',
          'amount': 35.98,
          'showDetail': False,
          'start': 230,
          'end': 260,
        },
        'propertyCosts': {
          'name': '物业费-浦东新区  2019年8月',
          'amount': 1170,
          'showDetail': False,
          'detail': [{
              'name': '物业费',
              'amount': 8
            },
            {
              'name': '垃圾处置费',
              'amount': 8
            },
            {
              'name': '垃圾清运费',
              'amount': 5
            },
            {
              'name': '路灯费',
              'amount': 0.45
            },
            {
              'name': '电梯服务费',
              'amount': 35.26
            },
            {
              'name': '房租',
              'amount': 67.25
            }
          ]
        }
      },
      {
        'addressName': '张飞家',
        'amount': '1170',
        'amountSymbol': '￥',
        'waterRate': {},
        'propertyCosts': {
          'name': '物业费-浦东新区  2019年8月',
          'amount': 1170,
          'showDetail': False,
          'detail': [{
              'name': '物业费',
              'amount': 8
            },
            {
              'name': '垃圾处置费',
              'amount': 8
            },
            {
              'name': '垃圾清运费',
              'amount': 5
            },
            {
              'name': '路灯费',
              'amount': 0.45
            },
            {
              'name': '电梯服务费',
              'amount': 35.26
            },
            {
              'name': '房租',
              'amount': 67.25
            }
          ]
        }
      },
      {
        'addressName': '段誉家',
        'amount': '35.98',
        'amountSymbol': '￥',
        'waterRate': {
          'name': '水费-浦东新区 2019年8月',
          'amount': 35.98,
          'showDetail': False,
          'start': 230,
          'end': 260,
        },
        'propertyCosts': {}
      }
    ]
    resultObj['data'] = billList
  except Exception as e:
    resultObj = utils.errorMes(e)
  finally:
    return Response(resultObj)
  
@api_view(http_method_names=['GET'])
def getAPI(request):
  '''
  函数说明
  '''
  resultObj = utils.successMes()
  try:
    # sqlSession = sqlutils.SqlUtils()
    resultObj['data'] = {'msg': '结束'}
  except Exception as e:
    resultObj = utils.errorMes(e)
    print(e)
  finally:
    pass
    # if sqlSession:
    #   sqlSession.closeConnect()
  return Response(resultObj)

@api_view(http_method_names=['POST'])
def postAPI(request):
  '''
  函数说明
  '''
  resultObj = utils.successMes()
  try:
    # sqlSession = sqlutils.SqlUtils()
    resultObj['data'] = {'msg': '结束'}
  except Exception as e:
    resultObj = utils.errorMes(e)
    print(e)
  finally:
    pass
    # if sqlSession:
    #   sqlSession.closeConnect()
  return Response(resultObj)