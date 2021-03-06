.PHONY: clean

clean:
	rm -rf /tmp/mpi_* sshconfig*

run: depth1

depth1:
	mpirun --allow-run-as-root --mca oob_tcp_if_include eth0 --mca btl_tcp_if_include eth0 -np 2 python3 scattergather.py
	cat /tmp/mpi_* | sort
	rm -rf /tmp/mpi_* sshconfig*

depth3:
	mpirun --allow-run-as-root --mca oob_tcp_if_include eth0 --mca btl_tcp_if_include eth0 -hostfile machinelist -np 12 python3 scattergather.py
	cat  /tmp/mpi_* | sort

showlog:
	cat /tmp/mpi_* | sort

docker-build:
	rm -rf sshconfig/*
	mkdir -p sshconfig
	ssh-keygen -b 2048 -t rsa -f sshconfig/id_rsa -q -N ""
	cp sshconfig/id_rsa.pub sshconfig/authorized_keys
	cp config  sshconfig/
	docker build -f Dockerfile -t suriyakalivardhan/multinodempi:v0 .

docker-run:
	docker run -dit --name t0 --network host suriyakalivardhan/multinodempi:v0

docker-login:
	docker exec -it t0 bash