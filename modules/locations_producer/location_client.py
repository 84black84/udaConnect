import grpc
import location_pb2
import location_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC server.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = location_pb2_grpc.LocationServiceStub(channel)

# Update this with desired payload
item = location_pb2.LocationMessage(
    person_id=6,
    longitude = '35.14968',
    latitude = '-90.04892',
    creation_time='2020-08-18T10:37:06'
)

response = stub.Create(item)
print('response ->')
print(response)