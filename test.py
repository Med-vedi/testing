flowers = {
    "iris_setosa": {
        "sepal_length": [3.6, 4.9, 4.8, 4.7],
        "sepal_width": [2.9, 3.3, 3.2, 3.1],
        "petal_length": [1.3, 1.2, 1.5, 1.4],
    },
    "iris_virginica": {
        "sepal_length": [7.2, 7.0, 7.9],
         "sepal_width": [3.1, 2.7, 2.8],
        "petal_length": [5.5, 5.5, 6.5],
    },
    "iris_versicolor": {
        "sepal_length": [6.5, 6.0, 6.1, 6.2, 6.3],
         "sepal_width": [2.8, 2.9, 2.4, 2.7, 2.7],
        "petal_length": [4.8, 4.7, 5.0, 4.9, 4.8],
    },
}

total_items = {}
for f,s in flowers.items():
    flower = (s)
    s_length = flower["sepal_length"]
    total_length = round(sum(s_length), 1)
    # TO DO//////////////////Как сложить числа в total_length без sum() для получения в дальейшем ср.арифм.?
    # т.е. result = sum(total_length)/len(total_length)  не работает///////////////
    print("sepal_length: ", total_length)



# for f,s in flowers.items():
#     flower = (s)
#     s_length = flower["sepal_width"]
#     total_length = round(sum(s_length), 1)
#     print("sepal_width: ",total_length)

# for f, s in flowers.items():
#     flower = (s)
#     s_length = flower["sepal_width"]
#     total_length = round(sum(s_length), 1)
#     print("sepal_width: ", total_length)