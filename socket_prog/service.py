'''
import socket
s=socket.socket()
try:

	host=socket.gethostname()
	print host
except Exception as err:
	print err
finally:
	s.close()
'''
'''
import socket
s=socket.socket()
try:

	host=socket.gethostname()
	port = 8889
	s.bind((host,port))
	s.listen(6)
	print "waiting for client request"
	print s.accept()
except Exception as err:
	print err
finally:
	s.close()
'''
'''
import socket
s=socket.socket()
try:

	host=socket.gethostname()
	port = 8889
	s.bind((host,port))
	s.listen(6)
	print "waiting for client request"
	client_obj,client_info = s.accept()
	client_obj.send("Connected successfully!!")
except Exception as err:
	print err
finally:
	s.close()
'''
'''
def even_odd(number):
	number = int(number)
	if number%2==0:
		return 'even'
	return 'odd'
import socket
s=socket.socket()
try:

	host=socket.gethostname()
	port = 8889
	s.bind((host,port))
	s.listen(6)
	print "waiting for client request"
	client_obj,client_info = s.accept()
	client_obj.send("Connected successfully!!")
	req = client_obj.recv(1024)
	response=even_odd(req)
	client_obj.send(response)
except Exception as err:
	print err
finally:
	s.close()
'''
def even_odd(number):
	number = int(number)
	if number%2==0:
		return 'even'
	return 'odd'
import socket
s=socket.socket()
try:

	host=socket.gethostname()
	port = 8889
	s.bind((host,port))
	s.listen(6)
	print "waiting for client request"
	client_obj,client_info = s.accept()
	client_obj.send("Connected successfully!!")
	req = client_obj.recv(1024)
	response=even_odd(req)
	client_obj.send(response)
except Exception as err:
	print err
finally:
	s.close()
	client_obj.close()