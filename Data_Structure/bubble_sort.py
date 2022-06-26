def bubble_sort(lt):
    for i in range(0, len(lt)-1):
        for j in range(0, len(lt)-i-1):

            # descending order
            if lt[j] < lt[j+1]:
                lt[j], lt[j+1] = lt[j+1], lt[j]

            # ascending order
            # if lt[j] > lt[j+1]:
            #     lt[j], lt[j+1] = lt[j+1], lt[j]
    return lt

lt = [12, 54, 32, 89, 29, 9]
out = bubble_sort(lt)
print(out)