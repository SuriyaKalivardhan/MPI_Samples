FROM ubuntu:latest
EXPOSE 20003
RUN apt-get -qq update && apt-get -qq --no-install-recommends install openssh-server python3-mpi4py mpich vim curl net-tools git make -y
RUN mkdir -p /var/run/sshd /root/.ssh
COPY sshconfig/* /root/.ssh
RUN sed -i "s/#Port/Port/g; s/^Port.*/Port 20003/" /etc/ssh/sshd_config
RUN /etc/init.d/ssh restart
RUN git clone https://github.com/SuriyaKalivardhan/MPI_Samples.git
CMD ["/usr/sbin/sshd", "-D"]