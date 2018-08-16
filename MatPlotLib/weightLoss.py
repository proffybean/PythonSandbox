from pylab import plot, show, title, xlabel, ylabel, legend, axis
import matplotlib.pyplot as plt

# https://www.epochconverter.com/days/2018
day = [59, 80, 81, 82, 83, 85, 86, 87, 89, 90, # March
       92, 101, 103, 108, 112, 116, 120,  #April
       121, 122, 124, 125, 126, 127, 132,  #May
       157, 162, 163, 180,  #June
       182, 187, 191, 193, 195, 197, 198,199,200,201, 202, 205, 207, 209, 210,211,212,214,#July
       215] #Aug

weight = [184.8, 181.4, 181.4, 179.8, 179.8, 178.8, 177.4, 178.4, 178.4, 177.2, #March
          176.2, 176.2, 176.2, 177, 175.2, 173.4, 171.8, #April
          172.4, 171.6, 172.6, 171.6, 171.6, 171.0, 169.2,  #May
          168.4, 167.6, 166.8, 165.2, #June
          164.6, 164.6, 165.4, 165.4, 163.8, 163.0, 163,162.4,162.6,161.8, 162.6, 161.4, 160.6, 160.4, 162.6, 162.6,160.6,160, #July 
          160] #Aug
plt.plot(day, weight, 'o')
plt.title('Weight since learning Python')
plt.xlabel('Day of the year')
plt.ylabel('Weight (lbs)')
plt.axis([50, 230, 150, 190])
plt.show()

