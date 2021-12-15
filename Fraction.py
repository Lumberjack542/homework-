num1 = int(input('enter numerator 1:'))
den1 = int(input('enter denominator 1:'))
operator = input('enter operator:')
num2 = int(input('enter numerator 2:'))
den2 = int(input('enter denominator 2:'))
outcome = 0
if operator == '+':
    if den1 == den2:
        outcome = num1 + num2
        print(outcome, '/', den2)
    elif den1 != den2:
        num1 *= den2
        num2 *= den1
        den2 *= den1
        outcome = num1 + num2
        print(outcome, '/', den2)

elif operator == '-':
    if den1 == den2:
        outcome = num1 - num2
        print(outcome, '/', den2)
    elif den1 != den2:
        num1 *= den2
        num2 *= den1
        den2 *= den1
        outcome = num1 - num2
        print(outcome, '/', den2)
        if outcome == 0:
            print(outcome)


elif operator == '/':
    num1 *= den2
    den1 *= num2
    print(num1, '/', den1)


elif operator == '*':
    num1 *= num2
    den1 *= den2
    print(num1, '/', den1)



