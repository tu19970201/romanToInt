def romanToInt(roman:str) -> int:
    wrongNum = '請輸入I~MMMCMXCIX的羅馬數字'
    romanList = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    intList = [1, 5, 10, 50, 100, 500, 1000]
    integer = []
    x = 0 # final answer
    i = 0 # 計數器
    # 排除輸入非羅馬數字者
    for a in roman:
        if a not in romanList:
            print(wrongNum)
            return
    # 排除IIII, VV等不符格式者
    while True:
        if romanList[i] * 4 in roman:
            print(wrongNum)
            return
        i += 1
        if i > 6:
            break
        if romanList[i] * 2 in roman:
            print(wrongNum)
            return
        i += 1
    # 將對應羅馬數字轉換為阿拉伯數字並加總
    for r in romanList:
        integer.append(roman.count(r))
    for n in range(0,7):
        x += ( integer[n] * intList[n] )
    # 將4, 9以減去的方式修正
    if 'IV' in roman or 'IX' in roman:
        x -= 2
    if 'XL' in roman or 'XC' in roman:
        x -= 20
    if 'CD' in roman or 'CM' in roman:
        x -= 200
    print(x)

# main
roman = input('請輸入羅馬數字')
romanToInt(roman)