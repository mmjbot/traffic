class Visualize:
 
	def draw(self, traffic_graph, square_size):
		mat = [[] for i in range(square_size+1)]
		for i in range(square_size + 1):
			for j in range(square_size + 1):
				mat[i].append("") 
		for car in traffic_graph.cars:
			row = 0
			column = 0
			if(get_orientation(car.road_segment) == "vertical"):
				row = car.road_segment.endpoints[0].x + car.road_position
				column = car.road_segment.endpoints[0].y
			else:
				column = car.road_segment.endpoints[0].y + car.road_position
				row = car.road_segment.endpoints[0].x
			print("car pos: " + str(row) + ", " + str(column))
			mat[row][column] = "0"
		for intersection in traffic_graph.intersections:
			row = intersection.x
			column = intersection.y
			if(intersection.light == "green"):
				mat[row][column] = "G"
			else:
				mat[row][column] = "R"
		#print
		for ray in mat:
			print(ray)


def get_orientation(road_segment):
	endpoints = road_segment.endpoints
	if(endpoints[0].x - endpoints[1].x == 0):
		return "horizontal"
	if(endpoints[0].y - endpoints[1].y == 0):
		return "vertical"
	else:
		raise Exception("error: road segment not horizontal or vertical")