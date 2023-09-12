import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# 创建地图
fig = plt.figure(figsize=(12, 9))
map = Basemap(llcrnrlon=73, llcrnrlat=15, urcrnrlon=135, urcrnrlat=54, resolution='l')

# 绘制海岸线和边界
map.drawcoastlines()
map.drawcountries()

# 绘制城市位置
city_data = {
    "shenyang": (123.429092, 41.796768),
    "changchun": (125.324501, 43.886841),
    "haerbing": (126.642464, 45.756966),
    "tianjin": (117.190182, 39.125596),
    "beijing": (116.405289, 39.904987),
    "shijiazhuang": (114.502461, 38.045474),
    "taiyuan": (112.549248, 37.857014),
    "jinan": (117.120098, 36.6512),
    "huhehaote": (111.670801, 40.818311),
    "zhengzhou": (113.665412, 34.757975),
    "xian": (108.948024, 34.263161),
    "hefei": (117.283042, 31.86119),
    "nanjing": (118.796877, 32.060255),
    "hangzhou": (120.15507, 30.274084),
    "shanghai": (121.473701, 31.230416),
    "wuhan": (114.305393, 30.593099),
    "nanchang": (115.892151, 28.676493),
    "changsha": (112.982279, 28.19409),
    "fuzhou": (119.296494, 26.074508),
    "taibei": (121.565418, 25.032969),
    "lanzhou": (103.834303, 36.061089),
    "xining": (101.778228, 36.617144),
    "yinchuan": (106.230909, 38.487193),
    "guangzhou": (113.264435, 23.129163),
    "aomen": (113.54909, 22.198951),
    "xianggang": (114.173355, 22.320048),
    "haikou": (110.33119, 20.031971),
    "nanning": (108.366543, 22.817002),
    "guiyang": (106.713478, 26.578343),
    "chongqing": (106.551557, 29.56301),
    "chengdu": (104.071216, 30.576279),
    "kunming": (102.712251, 25.040609),
    "lasa": (91.140856, 29.645554),
    "wulumuqi": (87.564988, 43.84038)
}

for city, (lon, lat) in city_data.items():
    x, y = map(lon, lat)
    map.plot(x, y, 'ro', markersize=5)  # 标记城市位置
    plt.text(x, y, city, color='black', fontsize=8, ha='center', va='center')  # 标注城市名称

# 标注城市之间的连接
connections = [
    ("shenyang", "changchun"),
    ("changchun", "haerbing"),
    ("haerbing", "tianjin"),
    ("tianjin", "beijing"),
    ("beijing", "shijiazhuang"),
    ("shijiazhuang", "taiyuan"),
    ("taiyuan", "jinan"),
    ("jinan", "huhehaote"),
    ("huhehaote", "zhengzhou"),
    ("zhengzhou", "xian"),
    ("xian", "hefei"),
    ("hefei", "nanjing"),
    ("nanjing", "hangzhou"),
    ("hangzhou", "shanghai"),
    ("shanghai", "wuhan"),
    ("wuhan", "nanchang"),
    ("nanchang", "changsha"),
    ("changsha", "fuzhou"),
    ("fuzhou", "taibei"),
    ("taibei", "lanzhou"),
    ("lanzhou", "xining"),
    ("xining", "yinchuan"),
    ("yinchuan", "guangzhou"),
    ("guangzhou", "aomen"),
    ("aomen", "xianggang"),
    ("xianggang", "haikou"),
    ("haikou", "nanning"),
    ("nanning", "guiyang"),
    ("guiyang", "chongqing"),
    ("chongqing", "chengdu"),
    ("chengdu", "kunming"),
    ("kunming", "lasa"),
    ("lasa", "wulumuqi")
]

for i, (city1, city2) in enumerate(connections):
    lon1, lat1 = city_data[city1]
    lon2, lat2 = city_data[city2]
    x1, y1 = map(lon1, lat1)
    x2, y2 = map(lon2, lat2)
    x_mid = (x1 + x2) / 2
    y_mid = (y1 + y2) / 2
    map.plot([x1, x2], [y1, y2], 'b-')  # 连接线
    plt.text(x_mid, y_mid, str(i+1), color='b', ha='center', va='center')  # 标注连接顺序

# 显示地图
plt.title('City Connections')
plt.show()