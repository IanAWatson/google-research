import pickle
from smu import dataset_pb2

class Foo:
    def __init__(self, bar):
        self.bar = bar

print(pickle.dumps(Foo))
print(pickle.dumps(Foo(12345)))
bts = dataset_pb2.BondTopologySummary()
print(pickle.dumps(bts))
print(pickle.dumps(dataset_pb2.BondTopologySummary))
