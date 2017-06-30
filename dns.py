#!/usr/bin/python

import vymgmt

def createdns(cache_size,port,ip):
        vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
        vyos.configure()
      	vyos.set("service dns forwarding cache-size %s" %(cache_size))
	vyos.set("service dns forwarding listen-on %s" %(port))
	vyos.set("service dns forwarding name-server %s" %(ip))
        vyos.commit()
        vyos.save()
        vyos.exit()
        vyos.logout()

def readdns():
        vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
        vyos.configure()
	print (vyos.run_conf_mode_command("show service dns forwarding"))
        y = vyos.run_conf_mode_command("show service dns forwarding")
        vyos.exit()
	vyos.logout()
        return y

def deldns(ip):
        vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
        vyos.configure()
        vyos.delete("service dns forwarding name-server %s" %(ip))
       	vyos.commit()
        vyos.save()
        vyos.exit()
        vyos.logout()

def updatedns(cache_size,port1,ip,port):
        vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
        vyos.configure()
	vyos.set("service dns forwarding cache-size %s" %(cache_size))
        vyos.set("service dns forwarding listen-on %s" %(port1))
        vyos.set("service dns forwarding name-server %s" %(ip))
	vyos.delete("service dns forwarding listen-on %s" %(port))
        vyos.commit()
        vyos.save()
        vyos.exit()
        vyos.logout()

