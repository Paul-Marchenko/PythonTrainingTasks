from die_new import Die
import pygal


die_1 = Die()
die_2 = Die(10)
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
hist = pygal.Bar()