n = int(input())


def check_same_digits(phone):
    phone = sorted(phone)
    prev_repeat = 1
    for i in range(1, len(phone)):
        if phone[i] == phone[i - 1]:
            prev_repeat += 1
        else:
            prev_repeat = 1

        if prev_repeat >= 4:
            return True
    return False


def check_sequance(phone):
    prev_repeat = 1
    for i in range(1, len(phone)):
        if phone[i] == phone[i - 1]:
            prev_repeat += 1
        else:
            prev_repeat = 1

        if prev_repeat >= 3:
            return True
    return False


def check_palindrom(phone):
    for i in range(0, len(phone) // 2):
        if phone[i] != phone[len(phone) - i - 1]:
            return False
    return True


ronds = []

for i in range(n):
    phone = input()

    if check_palindrom(phone) or check_sequance(phone) or check_same_digits(phone):
        ronds.append('Ronde!')
    else:
        ronds.append('Rond Nist')

for r in ronds:
    print(r)