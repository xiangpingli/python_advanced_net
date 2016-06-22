#!/usr/bin/python

import socket


def gethostname_test():
  host_name = socket.gethostname()
  print("host_name:%s" % host_name)

  ip_address = socket.gethostbyname(host_name)
  print("ip_address:%s" % ip_address);


if __name__=="__main__":
  gethostname_test()
