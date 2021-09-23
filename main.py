import numpy as np
from PIL import Image
from random import randint
import sys
# np.set_printoptions(threshold=sys.maxsize)

image_file = sys.argv[1]
k = int(sys.argv[2])

def main():
    image = Image.open(image_file) 
    data = np.asarray(image)
    # k = 2
    these_centers = init_centers(k)
    d_array = find_distances(these_centers, data, k)
    array_im = generate_clusters(d_array, k, these_centers, data)
    new_im = Image.fromarray(array_im.astype(np.uint8), 'RGB')
    new_im.save('panda k=20.png')
    #new_im.show()

def init_centers(k):
    centers = np.empty((k, 1, 3))
    for i in range(k):
        for j in range(3):
            rand_val = randint(0, 255)
            centers[i, 0, j] = rand_val
    return centers

def find_distances(centers, data, k):
    distances = np.empty((data.shape[0], data.shape[1], k))
    for i in range(len(centers)):
        distances[:, :, i] = np.sum(((data - centers[i, 0]) ** 2), axis=2)
    return distances

def generate_clusters(d_array, k, centers, data):
    old_centers = centers
    clusters_marks = np.argmin(d_array, axis=2)
    new_centers = np.empty((centers.shape[0], centers.shape[1], centers.shape[2]))
    for i in range(k):
        indy = np.where(clusters_marks == i)
        indexes = np.empty((len(indy[0]), 2))
        indexes[:, 0] = indy[0]
        indexes[:, 1] = indy[1]
        indexes = indexes.astype(int)
        if indexes.shape[0] > 0:
            for j in range(3):
                this_mean = data[indexes[:,0], indexes[:,1]][:, j].mean()
                new_centers[i, 0, j] = int(round(this_mean))
        else:
            for j in range(3):
                new_centers[i, 0, j] = i
    if (old_centers == new_centers).all():
        new_data = np.empty((data.shape[0], data.shape[1], data.shape[2]))
        for i in range(k):
            indy = np.where(clusters_marks == i)
            indexes = np.empty((len(indy[0]), 2))
            indexes[:, 0] = indy[0]
            indexes[:, 1] = indy[1]
            indexes = indexes.astype(int)
            new_data[indexes[:, 0], indexes[:, 1]] = new_centers[i, 0]
        return new_data
    else:
        new_d_array = find_distances(new_centers, data, k)
        return generate_clusters(new_d_array, k, new_centers, data)

main()