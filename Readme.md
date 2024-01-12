## **Apache Kafka**


## Abstract

Apache Kafka is a open source event streaming toolkit to make hard message processing. This repository aims to provide some simple customizable and scalable example using Apache Kafka in Python, C (17) and C++ (17) to subscribe / publisher message in to any topic in a broker, for this effect I use docker and special docker compose to build the cluster of the Kafka engine and Kafka UI client to monitor each event correctly (Note that not all kafka image is supported to all processor [architectures](https://hub.docker.com/r/bitnami/kafka)).


## Table of Contents
- [Build](#build)
- [References](#references)


## Build

It take the Fahid base docker compose yml file [1].

```
    docker compose build 
    docker compose up -d
```

To use kafka engine is necessary to install the lib for each OS, respectively, these commands lines was obtained from the oficial [librdkafka](https://github.com/confluentinc/librdkafka).

On Mac OSX, install librdkafka with homebrew:

```bash
  brew install librdkafka
```

On Debian and Ubuntu, install librdkafka from the Confluent APT repositories,
see instructions [here](https://docs.confluent.io/current/installation/installing_cp/deb-ubuntu.html#get-the-software) and then install librdkafka:

```bash
  apt install librdkafka-dev
```

On RedHat, CentOS, Fedora, install librdkafka from the Confluent YUM repositories,
instructions [here](https://docs.confluent.io/current/installation/installing_cp/rhel-centos.html#get-the-software) and then install librdkafka:

```bash
 yum install librdkafka-devel
```

On Windows, reference [librdkafka.redist](https://www.nuget.org/packages/librdkafka.redist/) NuGet package in your Visual Studio project.


- Python:

```
    conda create --name kafka python=3.11 -y
    conda activate kafka
    pip install -r requirements.txt
```

```
    python sub.py
    python pub.py
```

- C:

```
    clang  ./pub.c -o ./pub.out -I /opt/homebrew/Cellar/librdkafka/2.3.0/include/librdkafka -L /opt/homebrew/Cellar/librdkafka/2.3.0/lib -l rdkafka -g 

    clang  ./sub.c -o ./sub.out -I /opt/homebrew/Cellar/librdkafka/2.3.0/include/librdkafka -L /opt/homebrew/Cellar/librdkafka/2.3.0/lib -l rdkafka -g 
```

- C++:

```
    clang++ -std=c++17  ./sub.cpp -o ./sub.out -I /opt/homebrew/Cellar/librdkafka/2.3.0/include/librdkafka -L /opt/homebrew/Cellar/librdkafka/2.3.0/lib -l rdkafka++ -g 
```

## References

[1] Ahammed, F. (2022, March 25). How to use Apache Kafka with python - dzone. dzone.com. https://dzone.com/articles/apache-kafka-python 

[2] Confluentinc. (n.d.). Confluentinc/Librdkafka: The apache kafka C/C++ library. GitHub. https://github.com/confluentinc/librdkafka 