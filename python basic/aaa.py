address= 'http://www.example.com/test?p=1&q=2'

add_list = list(map(str,address.split('/')))
print(add_list)
print("protocol: {0}\n"
      "host: {1}\n"
      "others: {2}".format(add_list[0],add_list[1],add_list[2]))
