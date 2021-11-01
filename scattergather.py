from mpi4py import MPI
import logging
import time

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

#logging.basicConfig(format='%(asctime)s     %(message)s', filename=f'/tmp/mpi_{rank}.log', level=logging.INFO)
logging.basicConfig(format='%(asctime)s     %(message)s', level=logging.INFO)

input = []
if rank==0:
    for i in range(size):
        input.append(i)
    logging.info(f'{rank} processing {input}')

request = comm.scatter(input, root=0)
logging.info(f'{rank} received {request}')
response = request + request
time.sleep(0.001)
logging.info(f'{rank} responded {response}')
result = comm.gather(response, root=0)

if rank==0:
    time.sleep(0.001)
    logging.info(f'{rank} processed {result}')