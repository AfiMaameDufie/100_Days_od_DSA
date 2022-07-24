animals = ['lion', 'cheeetah', 'rhino', 'dog', 'ape']
sorted(animals)
# To reverse output
sorted(animals, reverse=True)


# Output
# >>> animals = ['lion', 'cheeetah', 'rhino', 'dog', 'ape']
# >>> sorted(animals)
# ['ape', 'cheeetah', 'dog', 'lion', 'rhino']

# Something a bit more complex
# shift, option, arrow 
animals = [
    {'type': 'cat', 'name': 'Stephanie', 'age': '5'},
    {'type': 'rhino', 'name': 'Moe', 'age': '7'}, 
    {'type': 'dog', 'name': 'Billie', 'age': '3'}
]
sorted(animals, key=lambda animal: animal['age'])
sorted(animals, key=lambda animal: animal['age'], reverse=True)
sorted(animals, key=lambda animal: animal['age'], reverse=True)[0]

# Output
# >>> animals = [
# ...     {'type': 'cat', 'name': 'Stephanie', 'age': '5'},
# ...     {'type': 'rhino', 'name': 'Moe', 'age': '7'}, 
# ...     {'type': 'dog', 'name': 'Billie', 'age': '3'}
# ... ]
# >>> 
# >>> sorted(animals, key=lambda animal: animal['age'])
# [{'type': 'dog', 'name': 'Billie', 'age': '3'}, {'type': 'cat', 'name': 'Stephanie', 'age': '5'}, {'type': 'rhino', 'name': 'Moe', 'age': '7'}]
# >>> sorted(animals, key=lambda animal: animal['age'], reverse=True)
# [{'type': 'rhino', 'name': 'Moe', 'age': '7'}, {'type': 'cat', 'name': 'Stephanie', 'age': '5'}, {'type': 'dog', 'name': 'Billie', 'age': '3'}]
# >>> sorted(animals, key=lambda animal: animal['age'], reverse=True)[0]
# {'type': 'rhino', 'name': 'Moe', 'age': '7'}