'''
import socket
host = 'www.google.com'
port = 80
s=socket.socket()
try:
	s.connect((host,port))
	print "connected"
except:
	print "not connected"
finally:
	s.close()
'''
'''
import socket
host = 'www.google.com'
port = 800
s=socket.socket()
try:
	s.connect((host,port))
	print "connected"
except:
	print "not connected"
finally:
	s.close()

'''
'''
import socket
host=socket.gethostname()
port = 8889
s=socket.socket()
try:
	s.connect((host,port))
	ack = s.recv(1024)
	print ack
except:
	print "not connected"
finally:
	s.close()
'''
'''
import socket
host=socket.gethostname()
port = 8889
s=socket.socket()
try:
	s.connect((host,port))
	ack = s.recv(1024)
	print ack
	s.send('20')
	resp = s.recv(1024)
	print resp
except Exception as err:
	print err
finally:
	s.close()
'''
import socket
host=socket.gethostname()
port = 8889
s=socket.socket()
try:
	s.connect((host,port))
	ack = s.recv(1024)
	print ack
	req = raw_input("Enter number:")
	s.send(req)
	resp = s.recv(1024)
	print resp
except Exception as err:
	print err
finally:
	s.close()