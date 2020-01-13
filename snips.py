import numpy.compat.tests.test_compat
import scipy as sp
import json
import os
import statistics
from typing import List, Dict, Any


def pythagoras(nums):
    numsa = numpy.array(nums)
    return numpy.sqrt(numpy.sum(numsa ** 2))


def randomnums(a, b, size=1):
    return (b - a) * numpy.random.rand() + a


def factorial(n):
    return sp.special.factorial(n)


def input_(filename):
    with open(filepath(filename)) as infile:
        return json.load(infile)


def output(filename, data):
    with open(filepath(filename), "w") as outfile:
        json.dump(data, outfile, indent=4, sort_keys=True)


def filepath(
    filename,
):  # deze functie geeft het path van het bestand zelf terug hoe je het ook
    # uitvoert, zodat het programma het bestand goed kan vinden
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, filename)


# def update(seeds, index):
#     seed = seeds[index]
#     values = seed["values"]
#     amt = seed["amtfound"]
#     values.append(seed["averageworth"] * amt)
#     print(values)
#     mean = statistics.mean(values)
#     stdev = statistics.stdev(values)
#     seed["averageworth"] = mean
#     seed["stdev"] = stdev
#     seed["amtfound"] = amt + len(values)
#     seed["values"] = []
#     return seeds


def addvals(
    index: int,
    value: int,
    filename: str,
    data: List[Dict[str, Any]] = None,
    okey: str = "values",
):
    data = input_(filename)
    data[index][okey].append(value)
    return data


def findvalinkey(val, data, skey):
    index = None
    for i, dic in enumerate(data):
        if dic[skey] == val:
            index = i
    return index


def texttoint(text, before="$", after=" "):
    value = text.partition(before)[2].partition(after)[0].replace(",", "")
    if len(value) == 0:
        numval = 0
    elif "M" in value:
        numval = int(float(value[0:-1]) * 1000000)
    elif "B" in value:
        numval = int(float(value[0:-1]) * 1000000000)
    else:
        numval = int(float(value))
    return numval

