# getting started with Matplotlib

import matplotlib.pyplot as plt
plt.plot (range(10))
#plt.show()

time = range(7)
co2 = [250,265,272,260,300,320,389]
plt.plot(time, co2)

plt.title("Conc of CO2 vs time")
plt.ylabel("[CO2]")
plt.xlabel("Time (decade)")
#plt.show()

temp = [14.1, 15.5, 16.3, 18.1, 17.3,19.1,20.2]
plt.plot(time, co2, 'b--', time, temp, 'r*-')
plt.show()
