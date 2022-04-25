# Using OLD pylab module

# Generate data
x = array(linspace(0, pi, 10))
y = sin(x)

# basic plotting
plot(x, y, 'rx')           

# show and halts program until fig is closed 
show(block=True)           