#!/usr/bin/env python3
"""
Load Test Script for Redis Clone

This script uses asyncio to concurrently send multiple requests to your
redis_client binary. It covers the following commands:
  - keys
  - get
  - set
  - del
  - pexpire
  - pttl
  - zadd
  - zrem
  - zscore
  - zquery

The script collects response times and calculates average execution time and
overall throughput.
"""

import asyncio
import time

# Path to your redis_client binary
CLIENT_CMD = "./redis_client"

# Number of times each command will be issued
NUM_REQUESTS_PER_COMMAND = 1000

# Define test commands covering all branches of the do_request dispatcher.
# Each command is represented as a list of strings.
COMMANDS = [
    # "keys" command: returns all keys
    ["keys"],
    # "set" command: set key "key1" to "value1"
    ["set", "key1", "value1"],
    # "get" command: get value of "key1"
    ["get", "key1"],
    # "del" command: delete key "key1"
    ["del", "key1"],
    # "pexpire" command: set key "key1" expiration to 5000 milliseconds
    ["pexpire", "key1", "5000"],
    # "pttl" command: get the remaining TTL for key "key1"
    ["pttl", "key1"],
    # "zadd" command: add to zset "zset" with score 1 and name "n1"
    ["zadd", "zset", "1", "n1"],
    # "zadd" command: add to zset "zset" with score 2 and name "n2"
    ["zadd", "zset", "2", "n2"],
    # "zscore" command: get the score of "n1" in zset "zset"
    ["zscore", "zset", "n1"],
    # "zquery" command: query zset "zset" starting from score 1, with an empty string,
    # offset 0, and limit 10 (this should return all elements with score >= 1)
    ["zquery", "zset", "1", "", "0", "10"],
    # "zrem" command: remove the element "n1" from zset "zset"
    ["zrem", "zset", "n1"],
]

async def run_client(cmd_args):
    """
    Asynchronously run the redis_client with the specified command arguments.
    Returns a tuple of (cmd_args, stdout, stderr, elapsed_time).
    """
    cmd = [CLIENT_CMD] + cmd_args
    start = time.perf_counter()
    proc = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    elapsed = time.perf_counter() - start
    return (cmd_args, stdout.decode(), stderr.decode(), elapsed)

async def main():
    """
    Main function to run the load test.

    For each command in COMMANDS, NUM_REQUESTS_PER_COMMAND requests are sent
    concurrently. The script then aggregates the results, calculates the average
    response time for each command, and prints overall throughput.
    """
    tasks = []
    for cmd in COMMANDS:
        for _ in range(NUM_REQUESTS_PER_COMMAND):
            tasks.append(run_client(cmd))
    total_requests = len(tasks)
    print(f"Sending {total_requests} requests in total...")
    
    overall_start = time.perf_counter()
    results = await asyncio.gather(*tasks)
    overall_elapsed = time.perf_counter() - overall_start

    # Aggregate results by command
    metrics = {}
    for cmd_args, stdout, stderr, elapsed in results:
        key = " ".join(cmd_args)
        if key not in metrics:
            metrics[key] = {"count": 0, "total_time": 0.0}
        metrics[key]["count"] += 1
        metrics[key]["total_time"] += elapsed

    print("\nPer-command performance:")
    for key in sorted(metrics.keys()):
        count = metrics[key]["count"]
        avg_time = metrics[key]["total_time"] / count
        print(f"Command: {key:30s} | Count: {count:5d} | Average time: {avg_time*1000:.2f} ms")
    print(f"\nTotal time for {total_requests} requests: {overall_elapsed:.2f} seconds")
    print(f"Overall throughput: {total_requests/overall_elapsed:.2f} requests/second")

if __name__ == "__main__":
    asyncio.run(main())
