import matplotlib.pyplot as plt
import math

def myfun(minv,maxv,stepv):
	i = minv
	lista=[]
	while i < maxv:
		lista.append(i)
		i += stepv
	return lista
print(myfun(0,2,.5))

def plotceil(x):
	coordx=myfun(x[0],x[1],x[2])
	coordy=[]
	for i in coordx:
		coordy.append(math.ceil(i))
	plt.plot(coordx,coordy)
	plt.ylabel("Ceil of x", fontsize = 20)
	plt.xlabel("From -pi to pi ", fontsize = 20)
	plt.title("Ceil of values", fontsize = 20)
	plt.show()
plotceil([-math.pi,math.pi,0.01])

def plotcos(x):
	coordx=myfun(x[0],x[1],x[2])
	coordy=[]
	for i in coordx:
		coordy.append(math.cos(i))
	plt.plot(coordx,coordy)
	plt.ylabel("Cosine of x", fontsize = 20)
	plt.xlabel("From -pi to pi ", fontsize = 20)
	plt.title("Cosiine of values", fontsize = 20)
	plt.show()
plotcos([-math.pi,math.pi,0.01])

def plotp4(x):
	coordx=myfun(x[0],x[1],x[2])
	coordy1=[]
	coordy2=[]
	coordy3=[]
	for i in coordx:
		coordy1.append(2*i)
		coordy2.append(math.pow(i,2)-5)
		coordy3.append(0.1*math.pow(i,3))
	plt.plot(coordx,coordy1)
	plt.plot(coordx,coordy2)
	plt.plot(coordx,coordy3)
	plt.xlabel("From -2 to 2", fontsize = 20)
	plt.ylabel("Basic y functions ", fontsize = 20)
	plt.title("x*2,x²-5 and .1x³", fontsize = 20)
	plt.legend( ('x*2', 'x²-5', '.1x³'), loc = 'upper right')
	plt.axis('scaled')
	plt.axis('equal')
	plt.show()
plotp4([-2,2,0.001])

def plotp5(x):
	lista=[x["Acuaticas"],x["Atmosfericas"],x["Ambientales"],x["Espaciales"],x["Solida"]]
	plt.bar(range(len(lista)),lista,1/1.5,color="blue")
	plt.xlabel("Areas for class", fontsize = 10)
	plt.ylabel("Percentage of students with this area", fontsize = 10)
	plt.title("Area preferences", fontsize = 10)
	orientaciones=("Acuáticas","Atmosféricas","Ambientales","Espaciales","Sólida")
	plt.xticks(range(len(lista)), orientaciones)
	plt.show()
area = {"Acuaticas":45.5 ,"Atmosfericas":22.7 ,"Ambientales":0,"Espaciales":9.1 , "Solida":22.7}
plotp5(area)

def plotp6(x):
	lista=[x["Acuaticas"],x["Atmosfericas"],x["Ambientales"],x["Espaciales"],x["Solida"]]
	orientaciones="Acuáticas","Atmosféricas","Ambientales","Espaciales","Sólida"
	plt.pie(lista,labels=orientaciones)
	plt.title("Area preferences", fontsize = 10)
	plt.show()
area = {"Acuaticas":45.5 ,"Atmosfericas":22.7 ,"Ambientales":0,"Espaciales":9.1 , "Solida":22.7}
plotp6(area)
