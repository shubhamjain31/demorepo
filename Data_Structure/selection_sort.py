def selection_sort(lt):
    for i in range(0, len(lt)):
        for j in range(i+1, len(lt)):

            # descending order
            # if lt[j] > lt[i]:
            #     lt[j], lt[i] = lt[i], lt[j]

            # ascending order
            if lt[i] > lt[j]:
                lt[i], lt[j] = lt[j], lt[i]
    return lt

lt = [12, 54, 32, 89, 29, 9]
out = selection_sort(lt)
print(out)