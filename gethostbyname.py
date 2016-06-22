#!/usr/bin/python

import socket

def get_remote_machine_info():
  remote_host = 'mirrors.hikvision.com.cn'
  ip_addr = socket.gethostbyname(remote_host)
  print("remote_host:%s\nip_addr:%s" % (remote_host, ip_addr)) 

if __name__=="__main__":
  get_remote_machine_info()
