import random
import math
from PIL import ImageTk, Image


class Point:

    def __init__(self, coordinates):
        self.coordinates = coordinates


class Cluster:

    def __init__(self, center, points):
        self.center = center
        self.points = points


class KMeans():

    def __init__(self, n_clusters, min_diff=1, max_iteration=1):
        self.n_clusters = n_clusters
        self.min_diff = min_diff
        self.max_iteration = max_iteration

    def calculate_center(self, points):
        n_dim = len(points[0].coordinates)
        vals = [0.0 for i in range(n_dim)]
        for p in points:
            for i in range(n_dim):
                vals[i] += p.coordinates[i]
        coords = [(v / len(points)) for v in vals]
        return Point(coords)

    def assign_points(self, clusters, points):
        plists = [[] for i in range(self.n_clusters)]
        print("no of points:"+ str(len(points)))
        for p in points:
            smallest_distance = float('inf')
            for i in range(self.n_clusters):
                distance = euclidean(p, clusters[i].center)
                if distance < smallest_distance:
                    smallest_distance = distance
                    idx = i

            plists[idx].append(p)
        print("In assign points, after for loop")
        return plists

    def fit(self, points):
        clusters = [Cluster(center=p, points=[p]) for p in random.sample(points, self.n_clusters)]
        for i in range(self.max_iteration):
            plists = self.assign_points(clusters, points)
            diff = 0

            for i in range(self.n_clusters):
                if not plists[i]:
                    continue
                old = clusters[i]
                center = self.calculate_center(plists[i])
                new = Cluster(center, plists[i])
                clusters[i] = new
                diff = max(diff, euclidean(old.center, new.center))
            if diff < self.min_diff:
                break
        return clusters

def get_points(file):
    new_name = "./compress" + file[2:]
    print(new_name)
    image = Image.open(file)
    image = image.resize((250, 250))
    w, h = image.size
    points = []
    for count, color in image.getcolors(w * h):
        for x in range(count):
            points.append(Point(color))
    return points


def euclidean(p, q):
    n_dim = len(p.coordinates)
    return math.sqrt(sum([(p.coordinates[i] - q.coordinates[i]) ** 2 for i in range(n_dim)]))
