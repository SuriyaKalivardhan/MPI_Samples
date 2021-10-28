from mpi4py import MPI
comm = MPI.COMM_WORLD

rank=comm.Get_rank()

data = None
if rank==0:
    data = {'Agazhi':4, 'Magi':31}

recvData = comm.bcast(data, 0)
print(rank, recvData)