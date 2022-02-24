"""
Author: Prajwal Somashekara
Date: 23/09/2021 Thursday
"""


def getValues(dic):
    variable = dic
    TotalValue = 0
    checkValue = True

    while checkValue:
        if isinstance(variable, dict):
            for key in variable:
                if variable[key] is None:
                    checkValue = False
                if isinstance(variable[key], int):
                    TotalValue = TotalValue + variable[key]
                    variable[key] = None

                elif isinstance(variable[key], list) or isinstance(variable[key], dict):
                    variable = variable[key]

        elif isinstance(variable, list):
            for keyList in variable:
                variable = keyList

    return TotalValue


x = {
    "value": 7,
    "next": [
        {"value": 13,
         "next":
             {
                 "value": 4,
                 "next": [
                     {
                         "value": 7
                     }
                 ]
             }
         }
    ],
}


result = getValues(x)
