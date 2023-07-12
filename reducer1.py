import grpc
import MapReduce_pb2
import MapReduce_pb2_grpc
from concurrent import futures

map_input = ""


class map(MapReduce_pb2_grpc.map):
    def reducer_inputs(self, request, context, **kwargs):
        print("______________________________________________________")
        print("locations received: ", request.input)
        map_input = request.input[0]
        response = MapReduce_pb2.input_response(response="Locations received")
        print("______________________________________________________")
        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
MapReduce_pb2_grpc.add_mapServicer_to_server(map(), server)
server.add_insecure_port("[::]:50054")
server.start()
print("REducer 1 STARTED AT PORT 50054 ")
server.wait_for_termination(timeout=20)
print("50054 TERMINATED")

table1 = []
with open("map1/p0.txt", "r") as file:
    rows = file.readlines()
    for line in rows:
        name = line.split('-')[0]
        age = line.split('-')[1]
        table1.append([name, age])


table2 = []
with open("map1/p1.txt", "r") as file:
    rows = file.readlines()
    for line in rows:
        name = line.replace("\n", "").split('-')[0]
        pos = line.replace("\n", "").split('-')[1]
        table2.append([name, pos])


joined_row = []

with open("output_files/table1.txt", "w") as file:
    for row1 in table1:
        for data in row1:
            data.replace("\n", "")
            file.write(data+" ")
        joined_row.append(row1)
        for row2 in table2:
            flag = 0
            for line in joined_row:
                if flag == 1: break
                if row2[0] in line:
                    file.write(row2[1])

                    flag = 1
