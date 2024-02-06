
def iteration_sort(comp, lst):
    def increment(lst, base):
        for i in range(len(lst)):
            lst[i] += 1
            if (lst[i] == base):
                lst[i] = 0
            else:
                return
        return
    
    current = [*range(len(lst))]

    while True:
        increment(current, len(lst))
        seen = set()
        if len(lst) > 0:
            seen.add(current[-1])
        sorted = True
        for i in range(len(lst) - 1):
            if comp(lst[current[i]], lst[current[i + 1]] > 0):
                sorted = False
                break
            if current[i] in seen:
                sorted = False
                break
            else:
                seen.add(current[i])
        if sorted:
            result = [0] * len(lst)
            for i in range(len(lst)):
                result[i] = lst[current[i]]
            return result

test = []
print("Input the integers of your list, then a non-integer.")
user_in = input()
try:
    while True:
        test.append(int(user_in))
        print("Inputted ", test)
        user_in = input()

except Exception:
    print(test)
    print(iteration_sort(lambda x, y: x - y, test))
