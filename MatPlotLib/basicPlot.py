from pylab import plot, show
from pylab import legend

# x_numbers = [1,2,3,4,5]
# y_numbers = [3,2,0,4,5]
# plot(x_numbers, y_numbers, 'o')
# show()

#temps
seattle_temp = [41.3, 43.0, 56.9, 51, 52.4, 68.2]
seattle_temp2 = [45.1, 41.2, 51.4, 43, 61.0, 62.2]
years = range(2000, 2006)
plot(years, seattle_temp, years, seattle_temp2,'o')
legend([2000, 2006])
show()