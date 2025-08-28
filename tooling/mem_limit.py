#!/usr/bin/env python3

import os
import resource

def print_cgroup_memory_limit():
    mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
    limit = mem_bytes
    
    path_used = None
    for path in [
        "/sys/fs/cgroup/memory/memory.limit_in_bytes",  # cgroups v1 hard limit
        "/sys/fs/cgroup/memory/memory.soft_limit_in_bytes",  # cgroups v1 soft limit
        "/sys/fs/cgroup/memory.max",  # cgroups v2 hard limit
        "/sys/fs/cgroup/memory.high",  # cgroups v2 soft limit
    ]:
        try:
            with open(path) as f:
                cgroups_limit = int(f.read())
            if cgroups_limit > 0:
                path_used = path
                limit = min(limit, cgroups_limit)
        except Exception:
            pass
        
    if path_used is None:
        print(f'no cgroup memory limits applied.')
    else:
        print(f'cgroup path applied: {path_used}')

        
    hard_limit = resource.getrlimit(resource.RLIMIT_RSS)[1]
    if 0 < hard_limit < limit:
        print(f'limiting system memory based on RLIMIT_RSS to: {hard_limit}')
        limit = hard_limit    

    limit_gb = limit/1000/1000/1000
    limit_gib = limit/1024/1024/1024

    print(f'memory limit: {limit_gb:.2f} GB')
    print(f'memory limit: {limit_gib:.2f} GiB')

    
if __name__ == '__main__':
    print_cgroup_memory_limit()
