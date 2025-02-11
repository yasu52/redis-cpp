# Build Your Own Redis in C/C++

This repository is my implementation of a Redis-like server from scratch, inspired by the ["Build Your Own Redis with C/C++"](https://build-your-own.org/redis/) guide. It focuses on network programming (TCP/IP) and fundamental data structures (hashtables, balanced trees, etc.), aiming to deepen understanding of systems programming by doing.

## Features

- **TCP Server & Request-Response Protocol**  
  Basic socket programming for handling multiple client connections, plus a custom request/response format.

- **Concurrent I/O**  
  Uses \`epoll\` on Linux and \`kqueue\` on macOS to handle multiple connections efficiently (non-blocking mode). This reduces overhead compared to \`poll\` or \`select\`.

- **Data Structures**

  - Hashtables for O(1) key lookups
  - AVL-tree-based Sorted Set implementation (like Redis ZSET)
  - Heap-based TTL timers for automatic key expiration

- **Thread Pool**  
  Thread pool for asynchronous tasks (such as large data deallocation), improving responsiveness under heavy load.

- **Memory Pool Optimization**  
  Custom memory pool to reduce frequent \`malloc/free\` calls, lowering fragmentation and allocation overhead.

- **Performance Tweaks**
  - **Receive Buffer Offset**: Minimize \`memmove\` calls by tracking data offset in the buffer.
  - **\`std::string\` Reserve**: Avoid repeated small allocations when generating responses.
  - **Preallocated Vectors**: Reserve capacity for \`std::vector\` to reduce reallocations in the event loop.

## Why Build Redis from Scratch?

1. **Learn Low-Level Fundamentals**  
   Gain hands-on experience in C/C++ network programming (sockets, non-blocking I/O, concurrency) and in data structure design (hashtable, balanced trees).

2. **Deeper Understanding**  
   As Richard Feynman once said, “What I cannot create, I do not understand.” Building key components yourself reinforces how things work under the hood.

3. **Practical System Skills**  
   C/C++ remain prevalent in systems and infrastructure development. Mastering memory management, concurrency, and performance tuning in C/C++ is valuable.

## Building & Running

```bash
cd redis/src

# Example build
clang++ -std=c++17 -O2 redis_server.cpp avl.cpp hashtable.cpp heap.cpp thread_pool.cpp zset.cpp memory_pool.cpp -o redis_server

# Run server (listens on port 1234)
./redis_server &

# In another terminal, use the included client to test commands
./redis_client set key1 value1
./redis_client get key1
./redis_client zadd zset 1 n1
./redis_client zscore zset n1
```

## Reference

Guide: [Build Your Own Redis with C/C++](https://build-your-own.org/redis/)
Author: James Smith
Why from scratch? Quoting from the guide:

> “Reading about things often just gives an illusion of knowledge. Learn deeper by doing!”
