def cocktail_shaker_sort(unsorted: list) -> list:

    for i in range(len(unsorted) - 1, 0, -1):
        swapped = False

        #Este bucle recorre la lista de izqda a dcha 
        for j in range(i, 0, -1):
            if unsorted[j] < unsorted[j - 1]:
                unsorted[j], unsorted[j - 1] = unsorted[j - 1], unsorted[j]
                swapped = True

        #Este bucle recorre la lista de dcha a izqda
        for j in range(i):
            if unsorted[j] > unsorted[j + 1]:
                unsorted[j], unsorted[j + 1] = unsorted[j + 1], unsorted[j]
                swapped = True

        if not swapped:
            break
    return unsorted