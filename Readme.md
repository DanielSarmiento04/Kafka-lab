## Apache Kafka 


## Abstract

Apache Kafka is a open source event streaming toolkit to make hard message processing. This repository aims to provide some simple customizable and scalable example using Apache Kafka in Python, C (17) and C++ (17) to subscribe / publisher to any topic in a broker, for this effect I use docker and special docker compose to build the cluster of the Kafka engine and Kafka UI client to monitor each event correctly (Note that not all kafka image is supported to all processor architectures).


## Table of Contents



## Introduction




## Set UP

```
    docker compose build 
    docker compose up -d
```



cpp support

clang  ./main.c -o ./main.out -I /opt/homebrew/Cellar/librdkafka/2.3.0/include/librdkafka -L /opt/homebrew/Cellar/librdkafka/2.3.0/lib -l rdkafka -g 
clang  ./pub.c -o ./pub.out -I /opt/homebrew/Cellar/librdkafka/2.3.0/include/librdkafka -L /opt/homebrew/Cellar/librdkafka/2.3.0/lib -l rdkafka -g 
clang  ./sub.c -o ./sub.out -I /opt/homebrew/Cellar/librdkafka/2.3.0/include/librdkafka -L /opt/homebrew/Cellar/librdkafka/2.3.0/lib -l rdkafka -g 

clang++ -std=c++17  ./sub.cpp -o ./sub.out -I /opt/homebrew/Cellar/librdkafka/2.3.0/include/librdkafka -L /opt/homebrew/Cellar/librdkafka/2.3.0/lib -l rdkafka++ -g 


## References


