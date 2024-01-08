from operator import itemgetter

question = {"blah": "test", "x": "wuff"}
get_blah_value = itemgetter("blah")

result = get_blah_value(question)

print(result)


