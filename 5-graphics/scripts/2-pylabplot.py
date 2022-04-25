# Using OLD pylab module

# Import pylab module 
from pylab import * 

x = array(linspace(0, pi, 10))
y = sin(x)

# Basic plotting with title, labels and ranges 
plot(x, y, 'r:o')

title('Harmonic motion')
xlabel('Time (s)')
ylabel('Distance (m)')
xlim(0, pi)
ylim(0, 1.1)
grid()
show()  # show and halts program until fig is closed.



