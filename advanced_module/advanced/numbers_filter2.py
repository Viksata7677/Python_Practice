def even_odd_filter(**kwargs):

    if "odd" in kwargs:
        filtered_odds = []
        for num in kwargs["odd"]:
            if num % 2 != 0:
                filtered_odds.append(num)
        kwargs["odd"] = filtered_odds

    if "even" in kwargs:
        filtered_evens = []
        for num in kwargs["even"]:
            if num % 2 == 0:
                filtered_evens.append(num)
        kwargs["even"] = filtered_evens

    filtered = sorted(kwargs.items(), key=lambda x: len(x[1]), reverse=True)

    return dict(filtered)

print(even_odd_filter(

odd=[1, 2, 3, 4, 10, 5],

even=[3, 4, 5, 7, 10, 2, 5, 5, 2],

))