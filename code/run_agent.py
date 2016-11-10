from city import City, CityViewer

city = City(n=10)
viewer = CityViewer(city)
anim = viewer.animate(frames=30)

anim
