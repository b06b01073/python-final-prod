def getCommonThreat(speciesDict):
    list1 = list(speciesDict.values())
    counter = {}

    for ls in list1:
        for threat in ls:
            threat = threat[threat.find('. ')+2:]
            if threat not in counter:
                counter[threat] = 1
            else:
                counter[threat] += 1

    a = 0
    common_threat = ""
    for num in counter.values():
        if a < num:
            a = num

    for threat in counter.keys():
        if counter[threat] == a:
            common_threat = threat
    return common_threat, counter