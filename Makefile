.PHONY: clean

clean:
	rm -rf /tmp/mpi_* /tmp/rsa* /tmp/sshkey*

run: depth1

depth1:
	mpirun -np 2 python3 scattergather.py
	cat /tmp/mpi_* | sort
	rm -rf /tmp/mpi_* /tmp/rsa*

depth2:
	mpirun -hostfile machinelist.txt -np 4 python3 scattergather.py
	cat  /tmp/mpi_* | sort
showlog:
	cat /tmp/mpi_* | sort

docker-build:
	rm -rf /tmp/sshkey*
	ssh-keygen -b 2048 -t rsa -f /tmp/sshkey -q -N ""
	docker build -f Dockerfile -t mpi:v0 .