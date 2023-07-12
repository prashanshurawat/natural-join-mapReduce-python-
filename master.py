import grpc
import MapReduce_pb2
import MapReduce_pb2_grpc
import time

input_path = "input_files/"
file1 = input_path+"input1_table1.txt"
file2 = input_path+"input2_table1.txt"
file3 = input_path+"input1_table2.txt"
file4 = input_path+"input2_table2.txt"

join1 = ["input_files/input1_table1.txt", "input_files/input1_table2.txt"]
join2 = ["input_files/input2_table1.txt", "input_files/input2_table2.txt"]

tables = [join1, join2]

maps = ["50052", "50053"]

i = 0
for table in tables:
    file_table = {}
    for join in table:
        with open(join, "r") as file:
            data = file.readlines()[1:]

            for entries in data:

                row = entries.replace("\n", "").split(",")

                name = row[0]
                value = row[1]
                file_table[name] = MapReduce_pb2.input_split(input=[value])
        channel = grpc.insecure_channel('localhost:{0}'.format(maps[i]))
        server_stub = MapReduce_pb2_grpc.mapStub(channel)
        request = MapReduce_pb2.input_map(index_map=file_table)
        response = server_stub.inputSplits(request)
        print(response.response)
    i += 1

time.sleep(5)

reducers = ["50054", "50055"]
for reducer in reducers:
    channel = grpc.insecure_channel('localhost:{0}'.format(reducer))
    server_stub = MapReduce_pb2_grpc.mapStub(channel)
    request = MapReduce_pb2.input_split(input=["map1", "map2"])
    response = server_stub.reducer_inputs(request)
    print(response.response)
