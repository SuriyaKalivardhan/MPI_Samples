from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data = []
if rank == 0:
    for i in range(size):
        data.append(i)    
    print(rank, " scattering ", data)

result = comm.scatter(data, root=0)
print(rank, " received ", result)