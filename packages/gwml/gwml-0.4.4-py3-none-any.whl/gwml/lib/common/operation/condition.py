import operator as op


operatorMapper = {
    "gt": op.gt,     #>
    "gteq": op.ge,   #>=
    "lt": op.lt,     #<
    "lteq": op.le,   #<=
    "eq": op.eq,     #==
    "nq": op.ne      #!=
}


def callFunc(x, y, func):
    try: 
        return operatorMapper[func](x, y)
    except Exception as e:
        print(str(e))
        return "Invalid function"


def operatorAccuracy(condition, pred):
    checker = False
    leftCondition = condition["leftCondition"] # if "none" not in condition["leftCondition"] else ""
    rightCondition = condition["rightCondition"] # if "none" not in condition["rightCondition"] else ""

    leftValue = float(condition["leftValue"]) if condition["leftValue"] != "" else 0.01
    rightValue = float(condition["rightValue"]) if condition["rightValue"] != "" else 0.01

    if leftValue > 1.0:
        leftValue /= 100.0

    if rightValue > 1.0:
        rightValue /= 100.0

    logical = 'none'
    if ("lt" in leftCondition and "lt" in rightCondition) or ("gt" in leftCondition and "lt" in rightCondition): # <  < or > <
        logical = 'and'
    elif "gt" in leftCondition and "gt" in rightCondition: # > >
        logical = 'or'

    
    target = pred["accuracy"]
    tmp = pred

    if condition["className"] == tmp["label"]:
      if logical == 'none':
          condition1 = leftCondition if leftCondition != "none" else rightCondition
          value1 = leftValue if leftCondition != "none" else rightValue
          
          if rightCondition == "none":
              if callFunc(value1, target, condition1):
                  tmp["color"] = condition["color"]
                  tmp["targetColumn"] = condition["className"]
                  tmp["conditionName"] = condition["conditionName"]
                  checker = True


          elif leftCondition == "none":
              if callFunc(target, value1, condition1):
                  tmp["color"] = condition["color"]
                  tmp["targetColumn"] = condition["className"]
                  tmp["conditionName"] = condition["conditionName"]
                  tmp["accuracy"] = float(tmp["accuracy"])
                  checker = True

      elif logical == 'and':
          condition1 = leftCondition
          value1 = leftValue

          condition2 = rightCondition
          value2 = rightValue

          if callFunc(value1, target, condition1) and callFunc(target, value2, condition2):
              # tmp = pred
              tmp["color"] = condition["color"]
              tmp["targetColumn"] = pred["label"]
              tmp["conditionName"] = condition["conditionName"]
              tmp["accuracy"] = float(tmp["accuracy"])
              checker = True
          # else:
          #     tmp = pred

      elif logical == 'or':
          condition1 = leftCondition
          value1 = leftValue

          condition2 = rightCondition
          value2 = rightValue

          if callFunc(value1, target, condition1) or callFunc(target, value2, condition2):
              # tmp = pred
              tmp["color"] = condition["color"]
              tmp["targetColumn"] = pred["label"]
              tmp["conditionName"] = condition["conditionName"]
              tmp["accuracy"] = float(tmp["accuracy"])
              checker = True
      else:
          checker = True

    return tmp, checker



def operatorValue(condition, pred):
    checker = False
    leftCondition = condition["leftCondition"]
    rightCondition = condition["rightCondition"]

    leftValue = float(condition["leftValue"]) if condition["leftValue"] != "" else 0.01
    rightValue = float(condition["rightValue"]) if condition["rightValue"] != "" else 0.01

    logical = 'none'
    if ("lt" in leftCondition and "lt" in rightCondition) or ("gt" in leftCondition and "lt" in rightCondition):
        logical = 'and'
    elif "gt" in leftCondition and "gt" in rightCondition:
        logical = 'or'

    target = pred["label"]
    tmp = pred

    if logical == 'none':
        condition1 = leftCondition if leftCondition != "none" else rightCondition
        value1 = leftValue if leftCondition != "none" else rightValue
        
        if rightCondition == "none":
            if callFunc(value1, target, condition1):
                tmp["color"] = condition["color"]
                tmp["targetColumn"] = condition["className"]
                tmp["conditionName"] = condition["conditionName"]
                tmp["accuracy"] = float(tmp["accuracy"])
                checker = True

        elif leftCondition == "none":
            if callFunc(target, value1, condition1):
                tmp["color"] = condition["color"]
                tmp["targetColumn"] = condition["className"]
                tmp["conditionName"] = condition["conditionName"]
                tmp["accuracy"] = float(tmp["accuracy"])
                checker = True

    elif logical == 'and':
        condition1 = leftCondition
        value1 = leftValue

        condition2 = rightCondition
        value2 = rightValue

        if callFunc(value1, target, condition1) and callFunc(target, value2, condition2):
            tmp["color"] = condition["color"]
            tmp["targetColumn"] = condition["className"]
            tmp["conditionName"] = condition["conditionName"]
            tmp["accuracy"] = float(tmp["accuracy"])
            checker = True

    elif logical == 'or':
        condition1 = leftCondition
        value1 = leftValue

        condition2 = rightCondition
        value2 = rightValue

        if callFunc(value1, target, condition1) or callFunc(target, value2, condition2):
            tmp["color"] = condition["color"]
            tmp["targetColumn"] = condition["className"]
            tmp["conditionName"] = condition["conditionName"]
            tmp["accuracy"] = float(tmp["accuracy"])
            checker = True

    else:
        checker = True

    return tmp, checker


def operatorCount(condition, predInfo, purposeType):
    leftCondition = condition["leftCondition"] if "none" not in condition["leftCondition"] else ""
    rightCondition = condition["rightCondition"] if "none" not in condition["rightCondition"] else ""

    leftValue = float(int(condition["leftValue"])) if condition["leftValue"] != "" else 1
    rightValue = float(int(condition["rightValue"])) if condition["rightValue"] != "" else 1

    logical = 'none'
    if ("lt" in leftCondition and "lt" in rightCondition) or ("gt" in leftCondition and "lt" in rightCondition):
        logical = 'and'
    elif "gt" in leftCondition and "gt" in rightCondition:
        logical = 'or'

    target = 0
    flag = False
    result = []

    if len(predInfo) != 0:
        for pred in predInfo:
            if pred["className"] == condition["className"]:
                target += 1

        if logical == 'none':
            condition1 = leftCondition if leftCondition is not None else rightCondition
            value1 = leftValue if leftCondition is not None else rightValue

            if callFunc(value1, target, condition1):
                flag = True
            else:
                flag = False

        elif logical == 'and':
            condition1 = leftCondition
            value1 = leftValue

            condition2 = rightCondition
            value2 = rightValue
            if callFunc(value1, target, condition1) and callFunc(target, value2, condition2):
                flag = True
            else:
                flag = False

        elif logical == 'or':
            condition1 = leftCondition
            value1 = leftValue

            condition2 = rightCondition
            value2 = rightValue

            if callFunc(value1, target, condition1) or callFunc(target, value2, condition2):
                flag = True
            else:
                flag = False

    for pred in predInfo:
        if pred["className"] == condition["className"]:
            tmp = pred

            if flag:
                tmp["color"] = condition["color"]
                tmp["targetColumn"] = pred["className"]
                tmp["conditionName"] = condition["conditionName"]
                tmp["accuracy"] = float(tmp["accuracy"])

                result.append(tmp)
        else:
            result.append(pred)

    return result


def operation(conditionTarget, condition, predInfo):
    if conditionTarget == "accuracy":
        return operatorAccuracy(condition, predInfo)
    elif conditionTarget == "value":
        return operatorValue(condition, predInfo)
    elif conditionTarget == "count":
        return operatorCount(condition, predInfo)
