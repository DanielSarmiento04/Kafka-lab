## Kafka 


## Abstract

Apache Kafka is a open source event streaming toolkit to make hard message processing, 


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


