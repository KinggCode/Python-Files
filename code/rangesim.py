old_min = 1.5
old_max = 6
new_min = 0
new_max = 90

x = 0

new_value = (((x - old_min) * (new_max - new_min)) / (old_max - old_min)) + new_min

print(new_value)
