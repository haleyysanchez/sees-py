o = open("k_20181007_test.txt", "r")
c = open("k_20181007_test1Cel.txt", "w")
f = open("k_20181007_test1F.txt", "w")
c.write(o.readline())
l = o.readline()
r = l.split(" ")
rows = r[9].split("\n")
c.write(l)
for i in range(4):
    c.write(o.readline())
for x in range(int(rows[0])):
    temps = o.readline().split(" ")
    temps.pop()
    for kelvin in temps:
        cel = float(kelvin) - 273.15
        c.write("%.1f " %(cel))
    c.write("\n")
o.close()
c.close()
o = open("k_20181007_test.txt", "r")
f.write(o.readline())
f.write(o.readline())
for i in range(4):
    f.write(o.readline())
for x in range(int(rows[0])):
    temps = o.readline().split(" ")
    temps.pop()
    for kelvin in temps:
        fah = (float(kelvin) - 273.15) * (9/5) + 32
        f.write("%.1f " %(fah))
    f.write("\n")
o.close()
f.close()
