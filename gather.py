from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data = rank
result = comm.gather(data, root=0)
print(rank, result)