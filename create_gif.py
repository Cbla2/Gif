import imageio.v3 as iio
import os
print("Working directory:", os.getcwd())


filenames = ['AL_1.png', 'AL_2.png', 'AL_3.png']
images = [ ]

for filename in filenames:
    images.append(iio.imread(filename))

    iio.imwrite('AL_chibi.gif', images, duration = 45, loop = 0)

    print("Script finished")
