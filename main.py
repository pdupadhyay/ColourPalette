import math
import random
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image


class class1(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg="white")
        self.geometry("1200x700")
        self.title("Colour Palette")
        self.upload = Button(self, height=3, width=20, text="UPLOAD IMAGE", bg="Cyan", fg="White", command=UploadAction)
        self.upload.place(x=100, y=400)


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
        print(len(points))
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
    image = Image.open(file)
    w, h = image.size
    points = []
    for count, color in image.getcolors(w * h):
        for x in range(count):
            points.append(Point(color))
    return points


def euclidean(p, q):
    n_dim = len(p.coordinates)
    return math.sqrt(sum([(p.coordinates[i] - q.coordinates[i]) ** 2 for i in range(n_dim)]))


def rgb_to_hex(rgb):
  return '#%s' % ''.join(('%02x' % p for p in rgb))


def get_colors(filename, n_colors=3):
    points = get_points(filename)
    clusters = KMeans(n_clusters=n_colors).fit(points)
    clusters.sort(key=lambda c: len(c.points), reverse=True)
    rgbs = [map(int, c.center.coordinates) for c in clusters]
    return list(map(rgb_to_hex, rgbs))


def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    image = Image.open(filename)
    image = image.resize((550, 550))
    image = ImageTk.PhotoImage(image)
    panel = Label(root, image=image)
    panel.image = image
    panel.place(x=600, y=0)
    colors = get_colors(filename, n_colors=5)
    color_label1 = Label(root, text=colors[0])
    color_label1.place(x=600, y=600)
    color_label2 = Label(root, text=colors[1])
    color_label2.place(x=700, y=600)
    color_label3 = Label(root, text=colors[2])
    color_label3.place(x=800, y=600)
    color_label4 = Label(root, text=colors[3])
    color_label4.place(x=900, y=600)
    color_label5 = Label(root, text=colors[4])
    color_label5.place(x=1000, y=600)



if __name__ == '__main__':
    root = class1()
    root.mainloop()
