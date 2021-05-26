# What are log files?
#!/usr/bin/env python3
import os
import sys
import re

logfile = sys.argv[1]
usernames = {}
with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)
        if result is None:
            continue
        name = result[1]
        usernames[name] = usernames.get(name, 0) + 1
print(usernames)


def show_time_of_pid(line):
    pattern = r"^([A-Za-z]+\s\d+\s\d+:\d+:\d+).*\[(\d+)\]"
    result = re.search(pattern, line)
    return "{} pid:{}".format(result[1], result[2])


# Jul 6 14:01:23 pid:29440
print(show_time_of_pid(
    "Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)"))

# Jul 6 14:02:08 pid:29187
print(show_time_of_pid(
    "Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)"))

# Jul 6 14:02:09 pid:29187
print(show_time_of_pid(
    "Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)"))

# Jul 6 14:03:01 pid:29440
print(show_time_of_pid(
    "Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)"))

# Jul 6 14:03:40 pid:29807
print(show_time_of_pid(
    "Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\""))

# Jul 6 14:04:01 pid:29440
print(show_time_of_pid(
    "Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)"))

# Jul 6 14:05:01 pid:29440
print(show_time_of_pid(
    "Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)"))

#!/usr/bin/env python3


def error_search(log_file):
    error = input("What is the error? ")
    returned_errors = []
    with open(log_file, mode='r', encoding='UTF-8') as file:
        for log in file.readlines():
            error_patterns = ["error"]
            for i in range(len(error.split(' '))):
                error_patterns.append(r"{}".format(
                    error.split(' ')[i].lower()))
            if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                returned_errors.append(log)
        file.close()
    return returned_errors


def file_output(returned_errors):
    with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
        for error in returned_errors:
            file.write(error)
        file.close()


if __name__ == "__main__":
    log_file = sys.argv[1]
    returned_errors = error_search(log_file)
    file_output(returned_errors)
    sys.exit(0)
