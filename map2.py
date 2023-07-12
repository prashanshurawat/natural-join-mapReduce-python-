import grpc
import MapReduce_pb2
import MapReduce_pb2_grpc
from concurrent import futures

tables = []


class map(MapReduce_pb2_grpc.map):
    def inputSplits(self, request, context, **kwargs):
        print("______________________________________________________")
        print("Table Received by Map 2: ", request.index_map)
        table = []
        for key, values in request.index_map.items():
            table.append([key])
            table[len(table) - 1].extend(request.index_map[key].input)
        tables.append(table)
        response = MapReduce_pb2.input_response(response="Table Received by map2")
        print("______________________________________________________")
        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
MapReduce_pb2_grpc.add_mapServicer_to_server(map(), server)
server.add_insecure_port("[::]:50053")
server.start()
print("MAP 2 STARTED AT PORT 50053 ")
server.wait_for_termination(timeout=15)
print("50053 TERMINATED")

print("______________________________________________________")
print(tables)
print("______________________________________________________")

rows = []
with open("map2/p0.txt", "w") as file:
    for row in tables[0]:
        if '-'.join(row) not in rows:
            rows.append('-'.join(row) + "\n")
            file.write('-'.join(row) + "\n")

with open("map2/p1.txt", "w") as file:
    for row in tables[1]:
        if '-'.join(row) not in rows:
            rows.append('-'.join(row) + "\n")
            file.write('-'.join(row) + "\n")

