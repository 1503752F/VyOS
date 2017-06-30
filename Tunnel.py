#!/usr/bin/python

import vymgmt

def createtunnel(vti_id,ip):
        vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
        vyos.configure()
        vyos.set("interfaces vti %s address %s" %(vti_id,ip))
        vyos.commit()
        vyos.save()
        vyos.exit()
        vyos.logout()

def readtunnel():
        vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
        vyos.configure()
	print (vyos.run_conf_mode_command("show interfaces vti"))
        y = vyos.run_conf_mode_command("show interfaces vti")
        vyos.exit()
	vyos.logout()
        return y

def deltunnel(vti_id):
        vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
        vyos.configure()
        vyos.delete("interfaces vti %s" %(vti_id))
        vyos.commit()
        vyos.save()
        vyos.exit()
        vyos.logout()

def updatetunnel(vti_id,vti_id1,ip):
        vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
        vyos.configure()
        vyos.delete("interfaces vti %s" %(vti_id))
        vyos.set("interfaces vti %s address %s" %(vti_id1,ip))
        vyos.commit()
        vyos.save()
        vyos.exit()
        vyos.logout()
