from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank==0:
    data = {'Agazhi':4, 'Magi':32}
    comm.send(data, 1, tag=11)
elif rank == 1:
    data = comm.recv(source=0, tag=11)
    print(rank, data)
print(rank, "Done")