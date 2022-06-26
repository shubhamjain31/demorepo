def insertion_sort(lt):
    for step in range(1, len(lt)):
        key = lt[step]
        j = step - 1

        while j >= 0 and key <= lt[j]:
            lt[j+1] = lt[j]
            j = j - 1

        lt[j+1] = key
    return lt

lt = [2, 54, 32, 89, 29, 9]
out = insertion_sort(lt)
print(out)