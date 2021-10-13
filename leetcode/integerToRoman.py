romans = {
            'M'   :1000,
            'CM'  :900,
            'D'   :500,
            'CD'  :400,
            'C'   :100,
            'XC'  :90,
            'L'   :50,
            'XL'  :40,
            'X'   :10,
            'IX'  :9,
            'V'   :5,
            'IV'  :4,
            'I'   : 1,
}

def intToRoman(num):
    output = ''
    for k, v in romans.items():
        while num > 0:
            if v <= num:
                output += k
                num -= v
            else:
                break
    return output

print(intToRoman(1994))