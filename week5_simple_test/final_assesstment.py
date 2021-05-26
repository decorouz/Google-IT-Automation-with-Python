#!/usr/bin/env/ python3
import sys
import re
import csv
import operator

errors_count = dict()
per_user = dict()


f = open('syslog.log', 'r')

errorfile = 'error_message.csv'
userfile = 'user_statastics.csv'

for log in f:
    result = re.search(
        r"ticky: ([\w+]*):? ([\w' ]*) [\[0-9#]*\]?]? ?\((.*)\)$", log)
    if result.group(2) not in errors_count.keys():
        errors_count[result.group(2)] = 0
    errors_count[result.group(2)] += 1
    if result.group(3) not in per_user.keys():
        per_user[result.group(3)] = {}
        per_user[result.group(3)]["INFO"] = 0
        per_user[result.group(3)]["ERROR"] = 0

    if result.group(1) == "INFO":
        per_user[result.group(3)]["INFO"] += 1
    elif result.group(1) == "ERROR":
        per_user[result.group(3)]["ERROR"] += 1

errors_count = sorted(errors_count.items(),
                      key=operator.itemgetter(1), reverse=True)
per_user = sorted(per_user.items())

f.close()

errors_count.insert(0, ("Error", "Count"))

f = open(errorfile, 'w')
f.write("Username,INFO,ERROR\n")
for stats in per_user:
    a, b = stats
    f.write(str(a)+','+str(b["INFO"])+','+str(b["ERROR"])+'\n')


f = open(userfile, 'w')
f.write("Username,INFO,ERROR\n")
for stats in per_user:
    a, b = stats
    f.write(str(a)+','+str(b["INFO"])+','+str(b["ERROR"])+'\n')
