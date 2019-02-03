"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example,
342 (three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters. The use of "and" when writing
out numbers is in compliance with British usage.
"""

num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
             11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
             15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
             19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
             50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
             90: 'Ninety', 100: 'Hundred', 0: 'Zero'}


def translate(num):
    if num >= 0 and num <= 20:
        return num2words.get(num)

    if num > 20 and num < 100:
        a = int(num / 10)
        val = a * 10
        remain = num - val
        if remain != 0:
            return num2words.get(val) + ' ' + num2words.get(remain)
        else:
            return num2words.get(val)

    if num >= 100 and num < 1000:
        a = int(num / 100)
        val = a * 100
        remain = num - val
        if remain != 0:
            return num2words.get(a) + ' ' + num2words.get(100) + ' and ' + translate(remain)
        else:
            return num2words.get(a) + ' ' + num2words.get(100)

    if num == 1000:
        return "One Thousand"

    return "Out of Range"


count = 0
for val in range(1, 1001):
    s = translate(val)
    lenght = len(s) - s.count(' ')
    count = count + lenght

print("amount of letters: %s" % count)
