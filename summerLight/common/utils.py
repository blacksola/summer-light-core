def errorMes(mes):
    errObj = {
        "data": {},
        "msg": "failure",
        "code": "1",
    }
    if mes is not None:
        errObj['data'] = mes
    return errObj;


def successMes():
    successObj = {
        "data": {},
        "msg": "success",
        "code": "0",
    }
    return successObj;