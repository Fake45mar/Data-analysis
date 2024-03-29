import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data_file = np.loadtxt('data_file.txt', delimiter=',')
    time = data_file[:,0]
    yhat = data_file[:,1]
    yhat = yhat - yhat[0]
    time = time - time[0]
    sensors = data_file[:,1:3]
    avg = np.mean(sensors, axis=1)
    export = np.vstack((time, sensors.T))
    export = export.T
    plt.plot(time, sensors[:,1], 'ro')
    plt.plot(time, avg, 'k.')
    plt.plot(yhat, sensors[:,1], 'bo')
    plt.savefig('foo.png', bbox_inches='tight')
    plt.show()
