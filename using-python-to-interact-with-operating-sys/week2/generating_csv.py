import csv  # Store the data we want in a list

hosts = [['localhost.com', '123.48.484.4'], ['google.com', '100.48.484.4']]

with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)


def first_message(name):
    print(f'Hi {name}! I am glad to part of this')


first_message('james')
