#!/usr/bin/env python3

import re
import subprocess

def main():
    result = subprocess.run(['ps', 'ax', '--no-headers', '--format', 'user,priority,pid,%cpu,%mem,time,stat,command'], stdout=subprocess.PIPE)
    if result.returncode == 0:
        pattern = 'proc_stat,command="{}",user="{}" prioriy={},pid={},cpu_percent={},mem_percent={},uptime="{}",stat="{}"'
        for line in result.stdout.decode('ascii').split('\n'):
            if len(line) > 0:
                stats = line.split(None, 7)
                print(pattern.format(re.sub('(\,| |=)+', r'\\\1', stats[7]), stats[0], stats[1], stats[2], stats[3], stats[4], stats[5], stats[6]))

if __name__ == '__main__':
    main()