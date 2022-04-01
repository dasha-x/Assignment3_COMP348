from Q5 import Shape, Ellipse, Circle, Rhombus

file1 = open('myShapes', 'r')
lines = file1.readlines()

Shapes = []
statistics = {}

for line in lines:
    info = line.split()
    if info[0] == 'shape':
        obj = Shape()
        Shapes.append(obj.__class__.__name__)
        obj.print()
    elif info[0] == 'ellipse':
        obj = Ellipse(float(info[1]), float(info[2]))
        Shapes.append(obj.__class__.__name__)
        if obj.a is None or obj.b is None:
            print('Error: Invalid Ellipse')
            obj.print()
        else:
            obj.print()
            print('   linear eccentricity: ', obj.eccentricity())
    elif info[0] == 'circle':
        obj = Circle(float(info[1]))
        Shapes.append(obj.__class__.__name__)
        obj.print()
    elif info[0] == 'rhombus':
        obj = Rhombus(float(info[1]), float(info[2]))
        Shapes.append(obj.__class__.__name__)
        obj.print()
        print('   in-radius: ', obj.inradius())

print()

statistics = {"Circle(s):": Shapes.count('Circle'), "Ellipse(s):": Shapes.count('Ellipse'),
              "Rhombus(es):": Shapes.count('Rhombus'), "--": None, "Shape(s):": len(Shapes)}


def print_statistics(dict):
    print("\nStatistics:")
    for item, amount in dict.items():
        if amount is not None:
            print("    {} {}".format(item, amount))
        else:
            print("    {}".format(item))


print_statistics(statistics)

