GET= None #GET Method
def ssh_run(addr :str,username :str,passwdOrId_rsa :str,command :str) -> None:
	"""
	New Module
	"""
	pass
POST= None #POST Method
def request(method :str,targetUrl :str,params :object,data :object,headers :object,verify :bool,proxyStr :str,timeout :int) -> object:
	"""
	发起请求
	"""
	pass
def ssh(addr :str,username :str,passwdOrId_rsa :str) -> None:
	"""
	New Module
	"""
	pass
def ssh_exec(addr :str,username :str,passwdOrId_rsa :str,command :str) -> str:
	"""
	New Module
	"""
	pass
def new_ssh(addr :str,username :str,passwdOrId_rsa :str) -> object:
	"""
	New Module
	"""
	pass
class SSH:
	def exec_command(self,command :str) -> str:
		"""
		New API
		"""
		pass
	def close(self) -> object:
		"""
		New Module
		"""
		pass
	pass
class HTTPRequest:
	def __init__(self,data :object) -> object:
		"""
		New Module
		"""
		pass
	def body(self,body :object) -> object:
		"""
		New Module
		"""
		pass
	def raw_query(self,query :object) -> str:
		"""
		New Module
		"""
		pass
	def header(self,header :object) -> object:
		"""
		New Module
		"""
		pass
	def to_request(self) -> object:
		"""
		New Module
		"""
		pass
	def path(self,path :object) -> str:
		"""
		New Module
		"""
		pass
	def query(self,k :object,v :object,diableCover :bool) -> object:
		"""
		New Module
		"""
		pass
	def url(self) -> str:
		"""
		New Module
		"""
		pass
	def method(self,method :object) -> str:
		"""
		New Module
		"""
		pass
	def proto(self,p :object) -> str:
		"""
		New Module
		"""
		pass
	pass
class HTTPResponse:
	def __init__(self,data :object,req :object) -> object:
		"""
		New Module
		"""
		pass
	def header(self,header :object) -> object:
		"""
		New Module
		"""
		pass
	def body(self,body :object) -> object:
		"""
		New Module
		"""
		pass
	def request(self) -> object:
		"""
		New Module
		"""
		pass
	def to_response(self) -> object:
		"""
		New Module
		"""
		pass
	def status(self,text :object) -> str:
		"""
		New Module
		"""
		pass
	def status_code(self,code :object) -> int:
		"""
		New Module
		"""
		pass
	pass
class HTTPProxyServer:
	def __init__(self,handleReq :object,handleResp :object,caRootPath :str) -> object:
		"""
		New API
		"""
		pass
	def start(self,addr :str,proxy :str,verbose :bool) -> None:
		"""
		New Module
		"""
		pass
	pass
class WebSocketServer:
	def __init__(self,handler :object,welcome :str) -> object:
		"""
		New Module
		"""
		pass
	def start(self,addr :str,path :str) -> None:
		"""
		New Module
		"""
		pass
	pass