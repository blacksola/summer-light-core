def errorMes(mes):
    errObj = {
        "data": {},
        "status": "failure"
    }
    if mes is not None:
        errObj['data'] = mes
    return errObj;


def successMes():
    successObj = {
        "data": {},
        "status": "success"
    }
    return successObj;