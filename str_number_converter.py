def convert(st):
    numbers = (1, 0, 2, 3, 4, 5, 6, 7, 8, 9)
    st = st.lower()
    newst = "1"
    for i in range(1, len(st)):
        a = st.find(st[i], 0, i)
        if a == -1:
            newst += str(numbers[i])
        else:
            newst += newst[a]
    number = int(newst)
    return number
