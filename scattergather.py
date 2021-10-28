from mpi4py import MPI
import logging

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s', filename=f'/tmp/mpi_{rank}.log', level=logging.INFO)

input = []
if rank==0:
    for i in range(size):
        input.append(i)
    logging.info(f'{rank} processing {input}')

request = comm.scatter(input, root=0)
logging.info(f'{rank} received {request}')
response = request + request
logging.info(f'{rank} responded {response}')
result = comm.gather(response, root=0)

if rank==0:
    logging.info(f'{rank} processed {result}')