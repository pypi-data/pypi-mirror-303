chat = """
/*
How to run
==========
save the file as chat.java (filename can be anything)
Command Prompt 1 (go to the location the file is saved)
javac *.java
java Server

Command Prompt 2 (go to the location the file is saved)
java Client
*/

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.net.*;

class Client extends JFrame{
    JTextField jt;
    JButton send;
    JLabel lbl;
    public static void main(String[] args) {
	new Client();
    }
    Client(){
        setTitle("Client");
	setSize(400, 200);
        setVisible(true);
	setLayout(new FlowLayout());
	lbl = new JLabel("Enter a string:");
        jt = new JTextField(20);
        send = new JButton("Send");
	add(lbl);
	add(jt);
	add(send);
	validate();
        send.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent ae) {
                try{
                    Socket s = new Socket("localhost", 1234);
                    DataOutputStream out = new DataOutputStream(s.getOutputStream());
                    out.writeUTF(jt.getText());
		    jt.setText("");
                    s.close();
                }catch(Exception e){System.out.println(e);}
            }
        });
    }
}

class Server extends JFrame{
    JTextArea jta;
    String newline = System.lineSeparator();
    public static void main(String[] args) {
	new Server();
    }
    Server(){
        setTitle("Server");
        setSize(400, 200);
        setVisible(true);
        jta = new JTextArea("Waiting for message..."+newline);
        add(jta);
	validate();
	try{
		ServerSocket ss = new ServerSocket(1234);
		while(true){
			Socket s = ss.accept();
	                DataInputStream in = new DataInputStream(s.getInputStream());
               		String msg = in.readUTF();
		        jta.append("Received: "+msg+" ("+check(msg)+")"+newline);
               		s.close();
                }
	}catch(Exception e){System.out.println(e);}
    }
    String check(String msg){
	StringBuffer rmsg = new StringBuffer(msg);
	rmsg.reverse();
	return msg.equalsIgnoreCase(new String(rmsg)) ? "It is a palindrome" : "It is not a palindrome";
    }
}
"""
file_transfer = """
/*
How to run
==========
save the file as filetransfer.java (filename can be anything)
Command Prompt 1 (go to the location the file is saved)
javac *.java
java Server

Command Prompt 2 (go to the location the file is saved)
java Client

select file_to_send.txt which will be there in the file location
(any file can be sent)
*/

import java.io.*;
import java.net.*;
import javax.swing.*;
import java.awt.event.*;

class Client extends JFrame {
	JTextArea jta;
	JButton send;
	JFileChooser jc;
	static String newline = System.lineSeparator();
	Client(){
		setTitle("File Client");
		setSize(400, 300);
		setVisible(true);
		jta = new JTextArea();
		send = new JButton("Send File");
		jc = new JFileChooser();
		send.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e){
				int op = jc.showOpenDialog(null);
				if(op == JFileChooser.APPROVE_OPTION)
					sendFile(jc.getSelectedFile());
			}
		});
		add(new JScrollPane(jta), "Center");
		add(send, "South");
		validate();
	}
	void sendFile(File f) {
		try{
			Socket s = new Socket("localhost", 5000);
			jta.setText("Connected to server"+newline);
			FileInputStream fin = new FileInputStream(f);
			OutputStream out = s.getOutputStream();

			byte[] buffer = new byte[1024];
			int bytesRead;
			while ((bytesRead = fin.read(buffer)) != -1){
				for (int i = 0; i < bytesRead; i++){
					byte plainByte = buffer[i];
					byte cipherByte = (byte) ((plainByte + 3) % 256);
					jta.append("Plain Text: " + plainByte + " (" + (char) plainByte + ") -> Cipher Text: " + cipherByte + " (" + (char) cipherByte + ")"+newline);
					buffer[i] = cipherByte;
				}
				out.write(buffer, 0, bytesRead);
			}
			fin.close();
			out.close();
			s.close();
			jta.append("File encrypted and sent successfully"+newline);
		}catch(Exception e){System.out.println(e);}
	}
	public static void main(String[] args){
		try{
			FileWriter fout = new FileWriter("file_to_send.txt");
			fout.write("Hello World"+newline+"Hello To JAVA");
			fout.close();
			new Client();
		}catch(Exception e){System.out.println(e);}
	}
}

class Server extends JFrame{
	JTextArea jta;
	String newline = System.lineSeparator();
	Server(){
		setTitle("File Server");
		setSize(400, 300);
		setVisible(true);
        	jta = new JTextArea();
        	add(new JScrollPane(jta));
		validate();
        	try{
            		ServerSocket ss = new ServerSocket(5000);
            		jta.append("Server is listening on port 5000"+newline);
	    		for(int n=1;n<=10;n++){
            			Socket s = ss.accept();
            			jta.setText("Client connected"+newline);
            			InputStream in = s.getInputStream();
            			FileOutputStream fout = new FileOutputStream("received_file_"+n+".txt");

            			byte[] buffer = new byte[1024];
            			int bytesRead;
            			while ((bytesRead = in.read(buffer)) != -1){
                			for (int i = 0; i < bytesRead; i++){
                    				byte cipherByte = buffer[i];
                    				byte plainByte = (byte) ((cipherByte - 3 + 256) % 256);
                    				jta.append("Cipher Text: " + cipherByte + " (" + (char) cipherByte + ") -> Plain Text: " + plainByte + " (" + (char) plainByte + ")"+newline);
                    				buffer[i] = plainByte;
                			}
                			fout.write(buffer, 0, bytesRead);
            			}
            			fout.close();
	            		in.close();
        	    		s.close();
	            		jta.append("File received and decrypted successfully"+newline);
			}
			ss.close();
        	}catch(Exception e){System.out.println(e);}
	}
	public static void main(String[] args){
		new Server();
	}
}
"""
rmi = """
/*
How to run
==========
save the file as rmi.java (filename can be anything)
Command Prompt 1 (go to the location the file is saved)
javac *.java
start rmiregistry
java Server

Command Prompt 2 (go to the location the file is saved)
java Client localhost

Note: If version error occurs, Compile following way:
javac --release 8 *.java
*/

import java.net.*;
import java.rmi.*;
import java.rmi.server.*;

interface MyServerIntf extends Remote{	
	String add(double a, double b) throws RemoteException;
}

class MyServerImpl extends UnicastRemoteObject implements MyServerIntf{
	MyServerImpl()throws RemoteException{}
	public String add(double a, double b)throws RemoteException{
		return a+" + "+b+" = "+(a+b);
	}	
}

class Client{
	public static void main(String[] arg){
		try{
			String name;
			if(arg.length == 0)
				name = "rmi://localhost/RMServer";
			else
				name = "rmi://"+arg[0]+"/RMServer";
			MyServerIntf asif = (MyServerIntf)Naming.lookup(name);
			System.out.println("Addition: "+asif.add(1200,1300));
		}catch(Exception e){System.out.println("Exception: "+e);}
	}
}


class Server{
	public static void main(String[] arg){
		try 	{
			MyServerImpl asi = new MyServerImpl();
			Naming.rebind("RMServer",asi);
			System.out.println("Server Started...");
		}
		catch(Exception e){System.out.println("Exception: "+e);}
	}
}
"""
wired_tcl = """
#How to run
#==========
#save this file as wired.tcl in desktop folder
#also save wired.awk file in the same location
#open desktop right-click and choose 'Open in Terminal'
#run this command
#ns wired.tcl

#both nam and awk file will be executed automatically

#create a simulator object 
set ns [new Simulator]

#create a trace file, this file is for logging purpose 
set tracefile [open wired.tr w]
$ns trace-all $tracefile

#create a animation infomration or NAM file creation
set namfile [open wired.nam w]
$ns namtrace-all $namfile

#create nodes
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]

#creation of link between nodes with DropTail Queue
#Droptail means Dropping the tail.
$ns duplex-link $n0 $n1 5Mb 2ms DropTail
$ns duplex-link $n2 $n1 10Mb 5ms DropTail
$ns duplex-link $n1 $n4 3Mb 10ms DropTail
$ns duplex-link $n4 $n3 100Mb 2ms DropTail
$ns duplex-link $n4 $n5 4Mb 10ms DropTail

#creation of Agents
#node 0 to Node 3
set udp [new Agent/UDP]
set null [new Agent/Null]
$ns attach-agent $n0 $udp
$ns attach-agent $n3 $null
$ns connect $udp $null

#creation of TCP Agent
set tcp [new Agent/TCP]
set sink [new Agent/TCPSink]
$ns attach-agent $n2 $tcp
$ns attach-agent $n5 $sink
$ns connect $tcp $sink

#creation of Application CBR, FTP
#CBR - Constant Bit Rate (Example nmp3 files that have a CBR or 192kbps, 320kbps, etc.)
#FTP - File Transfer Protocol (Ex: To download a file from a network)
set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp

set ftp [new Application/FTP]
$ftp attach-agent $tcp

#Start the traffic 
$ns at 1.0 "$cbr start"
$ns at 2.0 "$ftp start"

$ns at 10.0 "finish"

#the following procedure will be called at 10.0 seconds 
proc finish {} {
 global ns tracefile namfile
 $ns flush-trace
 close $tracefile
 close $namfile
 puts "Executing nam file"
 exec nam wired.nam &
 exec awk -f wired.awk wired.tr &
 exit 0
}

puts "Simulation is starting..."
$ns run
"""
wired_awk = """
BEGIN{
	r1=r2=d1=d2=total=0
	ratio=tp1=tp2=0.0
}

{
	if($1 =="r" && $4 == 3 && $5=="cbr")r1++
	if($1 =="d" && $4 == 3 && $5=="cbr")d1++
	if($1 =="r" && $4 == 5 && $5=="tcp")r2++
	if($1 =="d" && $4 == 5 && $5=="tcp")d2++
}

END{
	total = r1+r2+d1+d2
	ratio = (r1+r2)*100/total
	tp1 = (r1+d1)*8/1000000
	tp2 = (r2+d2)*8/1000000
	print("")
	print("Wired-Network")
	print("Packets Received:",r1+r2)
	print("Packets Dropped :",d1+d2)
	print("Packets Delivery Ratio:",ratio,"%")
	print("UDP Throughput:",tp1,"Mbps")
	print("TCP Throughput:",tp2,"Mbps")
}
"""
wireless_tcl = """
#How to run
#==========
#save this file as wireless.tcl in desktop folder
#also save wireless.awk file in the same location
#open desktop right-click and choose 'Open in Terminal'
#run this command
#ns wireless.tcl

#both nam and awk file will be executed automatically


#Example of Wireless networks
#Step 1 initialize variables
#Step 2 - Create a Simulator object
#step 3 - Create Tracing and animation file
#step 4 - topography
#step 5 - GOD - General Operations Director
#step 6 - Create nodes
#Step 7 - Create Channel (Communication PATH)
#step 8 - Position of the nodes (Wireless nodes needs a location)
#step 9 - Any mobility codes (if the nodes are moving)
#step 10 - TCP, UDP Traffic
#run the simulation

#initialize the variables
set val(chan)           Channel/WirelessChannel    ;#Channel Type
set val(prop)           Propagation/TwoRayGround   ;# radio-propagation model
set val(netif)          Phy/WirelessPhy            ;# network interface type WAVELAN DSSS 2.4GHz
set val(mac)            Mac/802_11                 ;# MAC type
set val(ifq)            Queue/DropTail/PriQueue    ;# interface queue type
set val(ll)             LL                         ;# link layer type
set val(ant)            Antenna/OmniAntenna        ;# antenna model
set val(ifqlen)         50                         ;# max packet in ifq
set val(nn)             6                          ;# number of mobilenodes
set val(rp)             AODV                       ;# routing protocol
set val(x)  500   ;# in metres
set val(y)  500   ;# in metres
#Adhoc OnDemand Distance Vector

#creation of Simulator
set ns [new Simulator]

#creation of Trace and namfile 
set tracefile [open wireless.tr w]
$ns trace-all $tracefile

#Creation of Network Animation file
set namfile [open wireless.nam w]
$ns namtrace-all-wireless $namfile $val(x) $val(y)

#create topography
set topo [new Topography]
$topo load_flatgrid $val(x) $val(y)

#GOD Creation - General Operations Director
create-god $val(nn)

set channel1 [new $val(chan)]
set channel2 [new $val(chan)]
set channel3 [new $val(chan)]

#configure the node
$ns node-config -adhocRouting $val(rp) \
  -llType $val(ll) \
  -macType $val(mac) \
  -ifqType $val(ifq) \
  -ifqLen $val(ifqlen) \
  -antType $val(ant) \
  -propType $val(prop) \
  -phyType $val(netif) \
  -topoInstance $topo \
  -agentTrace ON \
  -macTrace ON \
  -routerTrace ON \
  -movementTrace ON \
  -channel $channel1 

set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]

$n0 random-motion 0
$n1 random-motion 0
$n2 random-motion 0
$n3 random-motion 0
$n4 random-motion 0
$n5 random-motion 0

$ns initial_node_pos $n0 20
$ns initial_node_pos $n1 20
$ns initial_node_pos $n2 20
$ns initial_node_pos $n3 20
$ns initial_node_pos $n4 20
$ns initial_node_pos $n5 50

#initial coordinates of the nodes 
$n0 set X_ 10.0
$n0 set Y_ 20.0
$n0 set Z_ 0.0

$n1 set X_ 210.0
$n1 set Y_ 230.0
$n1 set Z_ 0.0

$n2 set X_ 100.0
$n2 set Y_ 200.0
$n2 set Z_ 0.0

$n3 set X_ 150.0
$n3 set Y_ 230.0
$n3 set Z_ 0.0

$n4 set X_ 430.0
$n4 set Y_ 320.0
$n4 set Z_ 0.0

$n5 set X_ 270.0
$n5 set Y_ 120.0
$n5 set Z_ 0.0
#Dont mention any values above than 500 because in this example, we use X and Y as 500,500

#mobility of the nodes
#At what Time? Which node? Where to? at What Speed?
$ns at 1.0 "$n1 setdest 490.0 340.0 25.0"
$ns at 1.0 "$n4 setdest 300.0 130.0 5.0"
$ns at 1.0 "$n5 setdest 190.0 440.0 15.0"
#the nodes can move any number of times at any location during the simulation (runtime)
$ns at 20.0 "$n5 setdest 100.0 200.0 30.0"

#creation of agents
set tcp [new Agent/TCP]
set sink [new Agent/TCPSink]
$ns attach-agent $n0 $tcp
$ns attach-agent $n5 $sink
$ns connect $tcp $sink
set ftp [new Application/FTP]
$ftp attach-agent $tcp
$ns at 1.0 "$ftp start"

set udp [new Agent/UDP]
set null [new Agent/Null]
$ns attach-agent $n2 $udp
$ns attach-agent $n3 $null
$ns connect $udp $null
set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp
$ns at 1.0 "$cbr start"

$ns at 30.0 "finish"

proc finish {} {
 global ns tracefile namfile
 $ns flush-trace
 close $tracefile
 close $namfile
 puts "Executing nam file"
 exec nam wireless.nam &
 exec awk -f wireless.awk wireless.tr &
 exit 0
}

puts "Starting Simulation"
$ns run
"""
wireless_awk = """
BEGIN {
	rec=sen=drp=0
	res=start=end=0.0
}

{
	if($1 == "s")sen++
	if($1 == "r"){
		if(rec==0)start = $2
		rec++		
		res += $8
		end = $2
	}
	if($1 == "D")drp++
}

END {
	print("")
	print("Wireless-Network")
	print("Number Of Packets Sent : ", sen)
	print("Number Of Packets Recieved : ", rec)
	print("Number Of Packets Dropped  : ", drp)
	print("Start Of Simulation (in sec) : ", start)
	print("End Of Simulation (in sec)   : ", end)
	print("Total Throughput : ",((res*8) / ((end-start)*1000000))," Mbps")
	print("Packet Delivery Ratio: ",rec*100/sen,"%")
}
"""
tahoe_tcl = """
#How to run
#==========
#save this file as tahoe.tcl in desktop folder
#also save analysis.awk file in the same location
#open desktop right-click and choose 'Open in Terminal'
#run this command
#ns tahoe.tcl

#both nam and awk file will be executed automatically

set ns [ new Simulator ]
$ns color 3 Green
set tf [open tahoe.tr w]
$ns trace-all $tf

set nf [open tahoe.nam w]
$ns namtrace-all $nf

set ft3 [open tahoe_Sender_throughput w]

proc finish {} {
 global ns nf ft3 
 $ns flush-trace
 close $nf
 close $ft3
 exec xgraph tahoe_Sender_throughput &
 puts "running nam..." 
 exec nam tahoe.nam &
 exec awk -f analysis.awk tahoe.tr &
 exit 0
}

proc record {} {
 global null3 ft3 
 global http1
 set ns [Simulator instance]
 set time 0.1
 set now [$ns now]
 set bw2 [$null3 set bytes_]
 puts $ft3 "$now [expr $bw2/$time*8/1000000]"
 $null3 set bytes_ 0
 $ns at [expr $now+$time] "record"
 }

for {set i 0} {$i < 6} {incr i} {
 set n($i) [$ns node]
}

$ns duplex-link $n(0) $n(1) 10Kb 10ms DropTail
$ns duplex-link $n(0) $n(3) 100Kb 10ms RED
$ns duplex-link $n(1) $n(2) 50Kb 10ms DropTail
$ns duplex-link $n(2) $n(5) 200Kb 10ms RED
$ns duplex-link $n(3) $n(4) 70Kb 10ms DropTail
$ns duplex-link $n(4) $n(5) 100Kb 10ms DropTail

$ns duplex-link-op $n(0) $n(1) orient right
$ns duplex-link-op $n(1) $n(2) orient right-down
$ns duplex-link-op $n(0) $n(3) orient left-down
$ns duplex-link-op $n(3) $n(4) orient right-down
$ns duplex-link-op $n(4) $n(5) orient right
$ns duplex-link-op $n(2) $n(5) orient left-down
 

set tcp3 [new Agent/TCP]
set null3 [new Agent/TCPSink]
$ns attach-agent $n(0) $tcp3
$ns attach-agent $n(5) $null3
$ns connect $tcp3 $null3
set http1 [new Application/Traffic/Exponential]
$http1 attach-agent $tcp3
 
$ns at 0.5 "record"
$ns at 0.2 "$ns trace-annotate \"Starting HTTP from 0 to 5\""
$ns at 0.2 "$n(0) color \"green\""
$ns at 0.2 "$n(5) color \"green\""
$ns at 0.2 "$http1 start"
$ns at 3.2 "$http1 stop" 
$ns at 5.0 "finish"
$ns run
"""
reno_tcl = """
#How to run
#==========
#save this file as reno.tcl in desktop folder
#also save analysis.awk file in the same location
#open desktop right-click and choose 'Open in Terminal'
#run this command
#ns reno.tcl

#both nam and awk file will be executed automatically

set ns [ new Simulator ]
$ns color 3 Green
set tf [open reno.tr w]
$ns trace-all $tf

set nf [open reno.nam w]
$ns namtrace-all $nf

set ft3 [open reno_Sender_throughput w]

proc finish {} {
 global ns nf ft3 
 $ns flush-trace
 close $nf
 close $ft3
 exec xgraph reno_Sender_throughput &
 puts "running nam..." 
 exec nam reno.nam &
 exec awk -f analysis.awk reno.tr &
 exit 0
}

proc record {} {
 global null3 ft3 
 global http1
 set ns [Simulator instance]
 set time 0.1
 set now [$ns now]
 set bw2 [$null3 set bytes_]
 puts $ft3 "$now [expr $bw2/$time*8/1000000]"
 $null3 set bytes_ 0
 $ns at [expr $now+$time] "record"
 }

for {set i 0} {$i < 6} {incr i} {
 set n($i) [$ns node]
}

$ns duplex-link $n(0) $n(1) 10Kb 10ms DropTail
$ns duplex-link $n(0) $n(3) 100Kb 10ms RED
$ns duplex-link $n(1) $n(2) 50Kb 10ms DropTail
$ns duplex-link $n(2) $n(5) 200Kb 10ms RED
$ns duplex-link $n(3) $n(4) 70Kb 10ms DropTail
$ns duplex-link $n(4) $n(5) 100Kb 10ms DropTail

$ns duplex-link-op $n(0) $n(1) orient right
$ns duplex-link-op $n(1) $n(2) orient right-down
$ns duplex-link-op $n(0) $n(3) orient left-down
$ns duplex-link-op $n(3) $n(4) orient right-down
$ns duplex-link-op $n(4) $n(5) orient right
$ns duplex-link-op $n(2) $n(5) orient left-down
 
set tcp3 [new Agent/TCP/Reno] 
set null3 [new Agent/TCPSink] 
$ns attach-agent $n(0) $tcp3
$ns attach-agent $n(5) $null3
$ns connect $tcp3 $null3
set http1 [new Application/Traffic/Exponential] 
$http1 attach-agent $tcp3  

$ns at 0.5 "record"
$ns at 0.2 "$ns trace-annotate \"Starting HTTP from 0 to 5\""
$ns at 0.2 "$n(0) color \"green\""
$ns at 0.2 "$n(5) color \"green\""
$ns at 0.2 "$http1 start" 
$ns at 3.2 "$http1 stop"  
$ns at 5.0 "finish"
$ns run
"""
sack_tcl = """
#How to run
#==========
#save this file as sack.tcl in desktop folder
#open desktop right-click and choose 'Open in Terminal'
#run this command
#ns sack.tcl

#nam file, xgraph and awk file will be executed automatically

#creating a simulator object
set ns [ new Simulator ]
$ns color 3 Green
#creating trace file
set tf [open sack.tr w]
$ns trace-all $tf

#creating nam file
set nf [open sack.nam w]
$ns namtrace-all $nf

set ft3 [open sack_Sender_throughput w]

#finish procedure to call nam and xgraph
proc finish {} {
 global ns nf ft3 
 $ns flush-trace
 close $nf
 close $ft3
 exec xgraph sack_Sender_throughput &
 puts "running nam..." 
 exec nam sack.nam &
 exec awk -f analysis.awk sack.tr &
 exit 0
}
#record procedure to calculate total bandwidth and throughput
proc record {} {
 global null3 ft3 
 global http1
 set ns [Simulator instance]
 set time 0.1
 set now [$ns now]
 set bw2 [$null3 set bytes_]
 puts $ft3 "$now [expr $bw2/$time*8/1000000]"
 $null3 set bytes_ 0
 $ns at [expr $now+$time] "record"
 }
#creating 10 nodes
for {set i 0} {$i < 6} {incr i} {
 set n($i) [$ns node]
}
#creating duplex links
$ns duplex-link $n(0) $n(1) 10Kb 10ms DropTail
$ns duplex-link $n(0) $n(3) 100Kb 10ms RED
$ns duplex-link $n(1) $n(2) 50Kb 10ms DropTail
$ns duplex-link $n(2) $n(5) 200Kb 10ms RED
$ns duplex-link $n(3) $n(4) 70Kb 10ms DropTail
$ns duplex-link $n(4) $n(5) 100Kb 10ms DropTail

#orienting links
$ns duplex-link-op $n(0) $n(1) orient right
$ns duplex-link-op $n(1) $n(2) orient right-down
$ns duplex-link-op $n(0) $n(3) orient left-down
$ns duplex-link-op $n(3) $n(4) orient right-down
$ns duplex-link-op $n(4) $n(5) orient right
$ns duplex-link-op $n(2) $n(5) orient left-down
 

set tcp3 [new Agent/TCP/Sack1] 
set null3 [new Agent/TCPSink] 
$ns attach-agent $n(0) $tcp3
$ns attach-agent $n(5) $null3
$ns connect $tcp3 $null3
set http1 [new Application/Traffic/Exponential] 
$http1 attach-agent $tcp3  
 
 
#scheduling events
$ns at 0.5 "record"
$ns at 0.2 "$ns trace-annotate \"Starting HTTP from 0 to 5\""
$ns at 0.2 "$n(0) color \"green\""
$ns at 0.2 "$n(5) color \"green\""
$ns at 0.2 "$http1 start" 
$ns at 3.2 "$http1 stop"  
$ns at 5.0 "finish"
$ns run
"""
vegas_tcl = """
#How to run
#==========
#save this file as vegas.tcl in desktop folder
#open desktop right-click and choose 'Open in Terminal'
#run this command
#ns vegas.tcl

#nam file, xgraph and awk file will be executed automatically

#creating a simulator object
set ns [ new Simulator ]
$ns color 3 Green
#creating trace file
set tf [open vegas.tr w]
$ns trace-all $tf

#creating nam file
set nf [open vegas.nam w]
$ns namtrace-all $nf

set ft3 [open vegas_Sender_throughput w]

#finish procedure to call nam and xgraph
proc finish {} {
 global ns nf ft3 
 $ns flush-trace
 close $nf
 close $ft3
 exec xgraph vegas_Sender_throughput &
 puts "running nam..." 
 exec nam vegas.nam &
 exec awk -f analysis.awk vegas.tr &
 exit 0
}
#record procedure to calculate total bandwidth and throughput
proc record {} {
 global null3 ft3 
 global http1
 set ns [Simulator instance]
 set time 0.1
 set now [$ns now]
 set bw2 [$null3 set bytes_]
 puts $ft3 "$now [expr $bw2/$time*8/1000000]"
 $null3 set bytes_ 0
 $ns at [expr $now+$time] "record"
 }
#creating 10 nodes
for {set i 0} {$i < 6} {incr i} {
 set n($i) [$ns node]
}
#creating duplex links
$ns duplex-link $n(0) $n(1) 10Kb 10ms DropTail
$ns duplex-link $n(0) $n(3) 100Kb 10ms RED
$ns duplex-link $n(1) $n(2) 50Kb 10ms DropTail
$ns duplex-link $n(2) $n(5) 200Kb 10ms RED
$ns duplex-link $n(3) $n(4) 70Kb 10ms DropTail
$ns duplex-link $n(4) $n(5) 100Kb 10ms DropTail

#orienting links
$ns duplex-link-op $n(0) $n(1) orient right
$ns duplex-link-op $n(1) $n(2) orient right-down
$ns duplex-link-op $n(0) $n(3) orient left-down
$ns duplex-link-op $n(3) $n(4) orient right-down
$ns duplex-link-op $n(4) $n(5) orient right
$ns duplex-link-op $n(2) $n(5) orient left-down
 

set tcp3 [new Agent/TCP/Vegas] 
set null3 [new Agent/TCPSink] 
$ns attach-agent $n(0) $tcp3
$ns attach-agent $n(5) $null3
$ns connect $tcp3 $null3
set http1 [new Application/Traffic/Exponential] 
$http1 attach-agent $tcp3  
 
 
#scheduling events
$ns at 0.5 "record"
$ns at 0.2 "$ns trace-annotate \"Starting HTTP from 0 to 5\""
$ns at 0.2 "$n(0) color \"green\""
$ns at 0.2 "$n(5) color \"green\""
$ns at 0.2 "$http1 start" 
$ns at 3.2 "$http1 stop"  
$ns at 5.0 "finish"
$ns run
"""
flow_tcl = """
#How to run
#==========
#save this file as flow.tcl in desktop folder
#open desktop right-click and choose 'Open in Terminal'
#run this command
#ns flow.tcl

#nam file, xgraph and awk file will be executed automatically

#creating a simulator object
set ns [ new Simulator ]
#creating trace file
set tf [open flow.tr w]
$ns trace-all $tf
#creating nam file
set nf [open flow.nam w]
$ns namtrace-all $nf

#creating variables for throughput files
set ft1 [open "Sender1_throughput" "w"]
set ft2 [open "Sender2_throughput" "w"]
set ft3 [open "Sender3_throughput" "w"]
set ft4 [open "Total_throughput" "w"]

#creating variables for bandwidth files
set fb1 [open "Bandwidth1" "w"] 
set fb2 [open "Bandwidth2" "w"]
set fb3 [open "Bandwidth3" "w"]
set fb4 [open "TotalBandwidth" "w"]

#finish procedure to call nam and xgraph
proc finish {} {
 global ns nf ft1 ft2 ft3 ft4 fb1 fb2 fb3 fb4 
 $ns flush-trace
 #closing all files
 close $nf
 close $ft1 
 close $ft2
 close $ft3
 close $ft4 
 close $fb1 
 close $fb2 
 close $fb3 
 close $fb4 
 #executing graphs
 exec xgraph Sender1_throughput Sender2_throughput Sender3_throughput Total_throughput &
 exec xgraph Bandwidth1 Bandwidth2 Bandwidth3 TotalBandwidth &
 puts "running nam..." 
 exec nam flow.nam &
 exec awk -f analysis.awk flow.tr &
 exit 0
}

#record procedure to calculate total bandwidth and throughput
proc record {} {
 global null1 null2 null3 ft1 ft2 ft3 ft4 fb1 fb2 fb3 fb4 
 global ftp1 smtp1 http1

 set ns [Simulator instance]
 set time 0.1
 set now [$ns now]
 
 set bw0 [$null1 set bytes_]
 set bw1 [$null2 set bytes_]
 set bw2 [$null3 set bytes_]

 set totbw [expr $bw0 + $bw1 + $bw2]
 puts $ft4 "$now [expr $totbw/$time*8/1000000]"

 puts $ft1 "$now [expr $bw0/$time*8/1000000]"
 puts $ft2 "$now [expr $bw1/$time*8/1000000]"
 puts $ft3 "$now [expr $bw2/$time*8/1000000]"

 puts $fb1 "$now [expr $bw0]"
 puts $fb2 "$now [expr $bw1]"
 puts $fb3 "$now [expr $bw2]"
 puts $fb4 "$now [expr $totbw]"

 $null1 set bytes_ 0
 $null2 set bytes_ 0
 $null3 set bytes_ 0

 $ns at [expr $now+$time] "record"
 }
 
#creating 10 nodes
for {set i 0} {$i < 10} {incr i} {
 set n($i) [$ns node]
}

#creating duplex links
$ns duplex-link $n(0) $n(1) 1Mb 10ms DropTail
$ns duplex-link $n(0) $n(3) 1.5Mb 10ms RED
$ns duplex-link $n(1) $n(2) 1Mb 10ms DropTail
$ns duplex-link $n(2) $n(7) 2Mb 10ms RED
$ns duplex-link $n(7) $n(8) 2Mb 10ms DropTail
$ns duplex-link $n(8) $n(9) 2Mb 10ms RED
$ns duplex-link $n(3) $n(5) 1Mb 10ms DropTail
$ns duplex-link $n(5) $n(6) 1Mb 10ms RED
$ns duplex-link $n(6) $n(4) 1Mb 10ms DropTail
$ns duplex-link $n(4) $n(7) 1Mb 10ms RED

#orienting links
$ns duplex-link-op $n(0) $n(1) orient right-up
$ns duplex-link-op $n(1) $n(2) orient right
$ns duplex-link-op $n(0) $n(3) orient right-down
$ns duplex-link-op $n(2) $n(7) orient right-down
$ns duplex-link-op $n(7) $n(8) orient right-up
$ns duplex-link-op $n(5) $n(6) orient right
$ns duplex-link-op $n(6) $n(4) orient left-up
$ns duplex-link-op $n(3) $n(5) orient right-down
$ns duplex-link-op $n(4) $n(7) orient right-up
$ns duplex-link-op $n(8) $n(9) orient right-down

proc ftp_traffic {node0 node9 } { 
 global ns null1 tcp1 ftp1
 set tcp1 [new Agent/TCP] 
 set null1 [new Agent/TCPSink] 
 $ns attach-agent $node0 $tcp1
 $ns attach-agent $node9 $null1
 $ns connect $tcp1 $null1
 set ftp1 [new Application/FTP] 
 $ftp1 attach-agent $tcp1  
 $ns at 1.0 "$ftp1 start" 
 $ns at 3.2 "$ftp1 stop"  
 }  
ftp_traffic $n(0) $n(8)

proc smtp_traffic {node0 node3 } { 
 global ns null2 tcp2 smtp1
 set tcp2 [new Agent/TCP] 
 set null2 [new Agent/TCPSink] 
 $ns attach-agent $node0 $tcp2
 $ns attach-agent $node3 $null2
 $ns connect $tcp2 $null2
 set smtp1 [new Application/Traffic/Exponential] 
 $smtp1 attach-agent $tcp2 
 $ns at 2.0 "$smtp1 start" 
 $ns at 3.8 "$smtp1 stop"  
 }  
smtp_traffic $n(3) $n(6)
 
proc http_traffic {node1 node7 } {  
 global ns null3 tcp3 http1
 set tcp3 [new Agent/TCP] 
 set null3 [new Agent/TCPSink] 
 $ns attach-agent $node1 $tcp3
 $ns attach-agent $node7 $null3
 $ns connect $tcp3 $null3
 set http1 [new Application/Traffic/Exponential] 
 $http1 attach-agent $tcp3  
 $ns at 0.2 "$http1 start" 
 $ns at 3.2 "$http1 stop"  }  
http_traffic $n(0) $n(7)
 
#scheduling events
$ns at 0.5 "record"
$ns at 0.2 "$ns trace-annotate \"Starting HTTP from 0 to 7\""
$ns at 1.0 "$ns trace-annotate \"Starting FTP from 0 to 8\""
$ns at 2.0 "$ns trace-annotate \"Starting SMTP from 3 to 6\""
$ns at 5.0 "finish"
$ns run
"""
tcp_flow_congestion_awk = """
BEGIN{
start = end = th = dly = 0
flag = data = 0
}
 
{
if($1=="r"&&$4==5){
	data+=$6
	if(flag==0){
		start=$2
		flag=1
	}	
	if(flag==1) 
		end=$2
}
}

END{
dly = end - start
th = data/dly
print("")
print("**********HTTP***********")
print("Start time:",start)
print("End time:",end)
print("Data =",data)
print("Throughput =",th)
print("Delay =",dly)
}

"""
LS_tcl = """
#How to run
#==========
#save this file as LS.tcl in desktop folder
#also save analysis.awk file in the same location
#open desktop right-click and choose 'Open in Terminal'
#run this command
#ns LS.tcl

#both nam and awk file will be executed automatically

set ns [new Simulator]
$ns rtproto LS
$ns color 1 green
set node0 [$ns node]
set node1 [$ns node]
set node2 [$ns node]
set node3 [$ns node]
set node4 [$ns node]
set node5 [$ns node]
set node6 [$ns node]
set tf [open out_ls.tr w]
$ns trace-all $tf
set nf [open out_ls.nam w]
$ns namtrace-all $nf
set ft [open "lsr_th" "w"]
$node0 label "node 0"
$node1 label "node 1"
$node2 label "node 2"
$node3 label "node 3"
$node4 label "node 4"
$node5 label "node 5"
$node6 label "node 6"
$ns duplex-link $node0 $node1 1.5Mb 10ms DropTail
$ns duplex-link $node1 $node2 1.5Mb 10ms DropTail
$ns duplex-link $node2 $node3 1.5Mb 10ms DropTail
$ns duplex-link $node3 $node4 1.5Mb 10ms DropTail
$ns duplex-link $node4 $node5 1.5Mb 10ms DropTail
$ns duplex-link $node5 $node6 1.5Mb 10ms DropTail
$ns duplex-link $node6 $node0 1.5Mb 10ms DropTail

$ns duplex-link-op $node0 $node1 orient left-down
$ns duplex-link-op $node1 $node2 orient left-down
$ns duplex-link-op $node2 $node3 orient right-down
$ns duplex-link-op $node3 $node4 orient right
$ns duplex-link-op $node4 $node5 orient right-up
$ns duplex-link-op $node5 $node6 orient left-up
$ns duplex-link-op $node6 $node0 orient left-up

set tcp2 [new Agent/TCP]
$tcp2 set class_ 1
$ns attach-agent $node0 $tcp2
set sink2 [new Agent/TCPSink]
$ns attach-agent $node3 $sink2
$ns connect $tcp2 $sink2

set traffic_ftp2 [new Application/FTP]
$traffic_ftp2 attach-agent $tcp2
proc record {} {
global sink2 tf ft
global ftp

set ns [Simulator instance]
set time 0.1
set now [$ns now]
set bw0 [$sink2 set bytes_]
puts $ft "$now [expr $bw0/$time*8/1000000]"
$sink2 set bytes_ 0
$ns at [expr $now+$time] "record"
}

proc finish {} {
global ns nf
$ns flush-trace
close $nf
exec nam out_ls.nam &
exec xgraph lsr_th &
exec awk -f analysis.awk out_ls.tr &
exit 0
}

$ns at 0.55 "record"
$ns at 0.5 "$node0 color \"Green\""
$ns at 0.5 "$node3 color \"Green\""
$ns at 0.5 "$ns trace-annotate \"Starting FTP node0 to node3\""
$ns at 0.5 "$node0 label-color green"
$ns at 0.5 "$node3 label-color green"

$ns at 0.5 "$traffic_ftp2 start"
$ns at 0.5 "$node1 label-color green"
$ns at 0.5 "$node2 label-color green"
$ns at 0.5 "$node4 label-color blue"
$ns at 0.5 "$node5 label-color blue"
$ns at 0.5 "$node6 label-color blue"
$ns rtmodel-at 2.0 down $node2 $node3
$ns at 2.0 "$node4 label-color green"
$ns at 2.0 "$node5 label-color green"
$ns at 2.0 "$node6 label-color green"
$ns at 2.0 "$node1 label-color blue"
$ns at 2.0 "$node2 label-color blue"
$ns rtmodel-at 3.0 up $node2 $node3
$ns at 3.0 "$traffic_ftp2 start"
$ns at 4.9 "$traffic_ftp2 stop"
$ns at 5.0 "finish"
$ns run
"""
DV_tcl = """
#How to run
#==========
#save this file as DV.tcl in desktop folder
#also save analysis.awk file in the same location
#open desktop right-click and choose 'Open in Terminal'
#run this command
#ns DV.tcl

#both nam and awk file will be executed automatically

set ns [new Simulator]
$ns rtproto DV
$ns color 1 green
set node0 [$ns node]
set node1 [$ns node]
set node2 [$ns node]
set node3 [$ns node]
set node4 [$ns node]

set node5 [$ns node]
set node6 [$ns node]
set tf [open out_dv.tr w]
$ns trace-all $tf
set nf [open out_dv.nam w]
$ns namtrace-all $nf

set ft [open "dvr_th" "w"]
$node0 label "node 0"
$node1 label "node 1"
$node2 label "node 2"
$node3 label "node 3"
$node4 label "node 4"

$node5 label "node 5"
$node6 label "node 6"
$ns duplex-link $node0 $node1 1.5Mb 10ms DropTail
$ns duplex-link $node1 $node2 1.5Mb 10ms DropTail
$ns duplex-link $node2 $node3 1.5Mb 10ms DropTail
$ns duplex-link $node3 $node4 1.5Mb 10ms DropTail

$ns duplex-link $node4 $node5 1.5Mb 10ms DropTail
$ns duplex-link $node5 $node6 1.5Mb 10ms DropTail
$ns duplex-link $node6 $node0 1.5Mb 10ms DropTail
$ns duplex-link-op $node0 $node1 orient left-down
$ns duplex-link-op $node1 $node2 orient left-down
$ns duplex-link-op $node2 $node3 orient right-down
$ns duplex-link-op $node3 $node4 orient right
$ns duplex-link-op $node4 $node5 orient right-up
$ns duplex-link-op $node5 $node6 orient left-up
$ns duplex-link-op $node6 $node0 orient left-up

set tcp2 [new Agent/TCP]
$tcp2 set class_ 1
$ns attach-agent $node0 $tcp2
set sink2 [new Agent/TCPSink]
$ns attach-agent $node3 $sink2
$ns connect $tcp2 $sink2
set traffic_ftp2 [new Application/FTP]

$traffic_ftp2 attach-agent $tcp2
proc record {} {
global sink2 tf ft
global ftp
set ns [Simulator instance]
set time 0.1
set now [$ns now]
set bw0 [$sink2 set bytes_]
puts $ft "$now [expr $bw0/$time*8/1000000]"
$sink2 set bytes_ 0
$ns at [expr $now+$time] "record"
}

proc finish {} {
global ns nf
$ns flush-trace
close $nf
exec nam out_dv.nam &
exec xgraph dvr_th &
exec awk -f analysis.awk out_dv.tr &
exit 0
}

$ns at 0.55 "record"
$ns at 0.5 "$node0 color \"Green\""
$ns at 0.5 "$node3 color \"Green\""
$ns at 0.5 "$ns trace-annotate \"Starting FTP node0 to node6\""
$ns at 0.5 "$node0 label-color green"
$ns at 0.5 "$node3 label-color green"
$ns at 0.5 "$traffic_ftp2 start"
$ns at 0.5 "$node1 label-color green"

$ns at 0.5 "$node2 label-color green"
$ns at 0.5 "$node4 label-color blue"
$ns at 0.5 "$node5 label-color blue"
$ns at 0.5 "$node6 label-color blue"
$ns rtmodel-at 2.0 down $node2 $node3

$ns at 2.0 "$node4 label-color green"
$ns at 2.0 "$node5 label-color green"
$ns at 2.0 "$node6 label-color green"
$ns at 2.0 "$node1 label-color blue"
$ns at 2.0 "$node2 label-color blue"

$ns rtmodel-at 3.0 up $node2 $node3
$ns at 3.0 "$traffic_ftp2 start"
$ns at 4.9 "$traffic_ftp2 stop"
$ns at 5.0 "finish"
$ns run
"""
link_state_distance_vector_awk = """
BEGIN {
recvdSize = 0
startTime = 0.5
stopTime = 5.0
}

{
event = $1
time = $2
node_id = $3
pkt_size = $6
level = $4

if (event == "s") {
if (time < startTime) {
startTime = time
}
}

if (event == "r") {
if (time > stopTime) {
stopTime = time
}
recvdSize += pkt_size
}
}

END{
print("")
printf("Average Throughput[kbps] = %.2f",(recvdSize/(stopTime-startTime))*(8/1000))
print("")
printf("StartTime = %.2f",startTime)
print("")
printf("StopTime  = %.2f",stopTime)
print("")
}
"""
multicast_tcl = """
#How to run
#==========
#save this file as multicast.tcl in desktop folder
#also save analysis.awk file in the same location
#open desktop right-click and choose 'Open in Terminal'
#run this command
#ns multicast.tcl

#both nam and awk file will be executed automatically

set ns [new Simulator -multicast on]
set tf [open multicast.tr w]
$ns trace-all $tf

set fd [open multicast.nam w]
$ns namtrace-all $fd

set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]
set n6 [$ns node]
set n7 [$ns node]

$ns duplex-link $n0 $n2 1.5Mb 10ms DropTail
$ns duplex-link $n1 $n2 1.5Mb 10ms DropTail
$ns duplex-link $n2 $n3 1.5Mb 10ms DropTail
$ns duplex-link $n3 $n4 1.5Mb 10ms DropTail
$ns duplex-link $n3 $n7 1.5Mb 10ms DropTail
$ns duplex-link $n4 $n5 1.5Mb 10ms DropTail
$ns duplex-link $n4 $n6 1.5Mb 10ms DropTail

set mproto DM
set mrthandle [$ns mrtproto $mproto {}]

set group1 [Node allocaddr]

set group2 [Node allocaddr]

set udp0 [new Agent/UDP]
$ns attach-agent $n0 $udp0
$udp0 set dst_addr_ $group1
$udp0 set dst_port_ 0
set cbr1 [new Application/Traffic/CBR]
$cbr1 attach-agent $udp0

set udp1 [new Agent/UDP]
$ns attach-agent $n1 $udp1
$udp1 set dst_addr_ $group2
$udp1 set dst_port_ 0
set cbr2 [new Application/Traffic/CBR]
$cbr2 attach-agent $udp1

set rcvr1 [new Agent/Null]
$ns attach-agent $n5 $rcvr1
$ns at 1.0 "$n5 join-group $rcvr1 $group1"
set rcvr2 [new Agent/Null]
$ns attach-agent $n6 $rcvr2
$ns at 1.5 "$n6 join-group $rcvr2 $group1"

set rcvr3 [new Agent/Null]
$ns attach-agent $n7 $rcvr3
$ns at 2.0 "$n7 join-group $rcvr3 $group1"

set rcvr4 [new Agent/Null]
$ns attach-agent $n5 $rcvr1
$ns at 2.5 "$n5 join-group $rcvr4 $group2"

set rcvr5 [new Agent/Null]
$ns attach-agent $n6 $rcvr2
$ns at 3.0 "$n6 join-group $rcvr5 $group2"

set rcvr6 [new Agent/Null]
$ns attach-agent $n7 $rcvr3

$ns at 3.5 "$n7 join-group $rcvr6 $group2"
$ns at 4.0 "$n5 leave-group $rcvr1 $group1"
$ns at 4.5 "$n6 leave-group $rcvr2 $group1"
$ns at 5.0 "$n7 leave-group $rcvr3 $group1"
$ns at 5.5 "$n5 leave-group $rcvr4 $group2"
$ns at 6.0 "$n6 leave-group $rcvr5 $group2"
$ns at 6.5 "$n7 leave-group $rcvr6 $group2"

$ns at 0.5 "$cbr1 start"
$ns at 9.5 "$cbr1 stop"
$ns at 0.5 "$cbr2 start"
$ns at 9.5 "$cbr2 stop"

$ns at 10.0 "finish"
proc finish {} {
global ns tf
$ns flush-trace
close $tf
puts "Executing nam..."
exec nam multicast.nam &
exec awk -f analysis.awk multicast.tr &
exit 0
}

$ns set-animation-rate 3.0ms
$ns run
"""
broadcast_tcl = """
#How to run
#==========
#save this file as broadcast.tcl in desktop folder
#also save analysis.awk file in the same location
#open desktop right-click and choose 'Open in Terminal'
#run this command
#ns broadcast.tcl

#both nam and awk file will be executed automatically

set ns [new Simulator -multicast on]

set tf [open broadcast.tr w]
$ns trace-all $tf

set namfile [open broadcast.nam w]
$ns namtrace-all $namfile

set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]

$ns duplex-link $n0 $n1 1Mb 10ms DropTail
$ns duplex-link $n0 $n2 1Mb 10ms DropTail
$ns duplex-link $n1 $n3 1Mb 10ms DropTail
$ns duplex-link $n2 $n4 1Mb 10ms DropTail

set mproto DM
set mrthandle [$ns mrtproto $mproto {}]

set group [Node allocaddr]

set udp [new Agent/UDP]
$ns attach-agent $n0 $udp

$udp set dst_addr_ $group
$udp set dst_port_ 0

set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp

set rcvr1 [new Agent/Null]
set rcvr2 [new Agent/Null]
set rcvr3 [new Agent/Null]
set rcvr4 [new Agent/Null]

$ns attach-agent $n1 $rcvr1
$ns attach-agent $n2 $rcvr2
$ns attach-agent $n3 $rcvr3
$ns attach-agent $n4 $rcvr4

$ns at 0.0 "$n1 join-group $rcvr1 $group"
$ns at 0.0 "$n2 join-group $rcvr2 $group"
$ns at 0.0 "$n3 join-group $rcvr3 $group"
$ns at 0.0 "$n4 join-group $rcvr4 $group"

$ns at 0.5 "$cbr start"
$ns at 2.0 "$cbr stop"

$ns at 2.5 "finish"

proc finish {} {
    global ns tf namfile
    $ns flush-trace
    close $tf
    close $namfile
    puts "Executing nam..."
    exec nam broadcast.nam &
    exec awk -f analysis.awk broadcast.tr &
    exit 0
}

$ns run
"""
multicast_broadcast_awk = """
BEGIN{
	r1=d1=total=0
	ratio=tp1=0.0
}

{
	if($1 =="r" && $5=="cbr")r1++
	if($1 =="d" && $5=="cbr")d1++
}

END{
	total = r1+d1
	ratio = (r1)*100/total
	tp1 = (r1+d1)*8/1000000
	print("")
	print("Packets Received:",r1)
	print("Packets Dropped:",d1)
	print("Packets Delivery Ratio:",ratio,"%")
	print("UDP Throughput:",tp1,"Mbps")
}
"""
dhcp = """
/*
How to run
==========
save the file as DHCP.java (filename can be anything)
Command Prompt 1 (go to the location the file is saved)
javac *.java
java Server

Command Prompt 2 (go to the location the file is saved)
java Client
*/

import java.io.*;
import java.net.*;
import java.util.*;

class Server{
	static int SERVER_PORT = 4900;
	static String SERVER_IP = "127.0.0.1"; // Change to your server's IP
	static String IP_ALLOCATIONS_FILE = "ip_allocations.txt";
	static List<String> availableIpAddresses = new ArrayList<>();
	static Map<String, String> ipAllocations = new HashMap<>();

	public static void main(String[] args){
		loadIpAllocations(); // Load IP allocations from file (if available)
		initializeIpAddresses();

		try{
			DatagramSocket socket = new DatagramSocket(SERVER_PORT);
			while(true){
				byte[] receiveData = new byte[1024];
				DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
				socket.receive(receivePacket);
				
				InetAddress clientAddress = receivePacket.getAddress();
				String macAddress = extractMacAddress(receiveData);
				String allocatedIp = allocateIpAddress(macAddress);

				byte[] responseData = createDHCPResponse(macAddress, allocatedIp);
				DatagramPacket responsePacket = new DatagramPacket(responseData, responseData.length, clientAddress, receivePacket.getPort());
				socket.send(responsePacket);

				System.out.println("Allocated IP " + allocatedIp + " to client with MAC " + macAddress);
				saveIpAllocations();
			}
		}catch(Exception e){
			e.printStackTrace();}
	}

	private static void initializeIpAddresses(){
		for(int i = 2; i <= 254; i++)
			availableIpAddresses.add("192.168.1." + i);
	}

	private static String extractMacAddress(byte[] data){
		return "00:11:22:33:44:55";
	}

	private static String allocateIpAddress(String macAddress){
		if(availableIpAddresses.isEmpty())
			return "No available IP addresses";
		Random random = new Random();
		int index = random.nextInt(availableIpAddresses.size());
		String allocatedIp = availableIpAddresses.remove(index);
		ipAllocations.put(macAddress, allocatedIp);
		return allocatedIp;
	}

	private static byte[] createDHCPResponse(String macAddress, String allocatedIp) {
		// Simulate creating a DHCP response with the allocated IP address
		// In a real implementation, you'd construct a proper DHCP packet
		return ("Allocated IP: " + allocatedIp).getBytes();
	}

	private static void saveIpAllocations() {
		try(ObjectOutputStream outputStream = new ObjectOutputStream(new FileOutputStream(IP_ALLOCATIONS_FILE))){
			outputStream.writeObject(ipAllocations);
			System.out.println("Saved IP allocations to " + IP_ALLOCATIONS_FILE);
		}catch (IOException e){
			e.printStackTrace();
		}
	}

	private static void loadIpAllocations() {
		try(ObjectInputStream inputStream = new ObjectInputStream(new FileInputStream(IP_ALLOCATIONS_FILE))){
			ipAllocations = (HashMap<String, String>) inputStream.readObject();
			System.out.println("Loaded IP allocations from " + IP_ALLOCATIONS_FILE);
		}catch(FileNotFoundException e){
			System.out.println(IP_ALLOCATIONS_FILE + " not found. Starting with an empty IP allocations map.");
		}catch(IOException | ClassNotFoundException e){
			e.printStackTrace();
		}
	}
}


class Client{
	static int SERVER_PORT = 4900;
	static String SERVER_IP = "127.0.0.1"; // Change to your server's IP

	public static void main(String[] args) {
		try{
			DatagramSocket socket = new DatagramSocket();
			InetAddress serverAddress = InetAddress.getByName(SERVER_IP);

			byte[] requestData = createDHCPRequest("00:11:22:33:44:55"); // Replace with your MAC address
			DatagramPacket requestPacket = new DatagramPacket(requestData, requestData.length, serverAddress, SERVER_PORT);
			socket.send(requestPacket);

			byte[] receiveData = new byte[1024];
			DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
			socket.receive(receivePacket);

			String response = new String(receivePacket.getData()).trim();
			System.out.println("Received DHCP Response: " + response);
		}catch(Exception e){
			e.printStackTrace();
		}
	}

	private static byte[] createDHCPRequest(String macAddress) {
		String request = "DHCP Request with MAC: " + macAddress;
		return request.getBytes();
	}
}
"""
LAN_tcl = """
#How to run
#==========
#save this file as LAN.tcl in desktop folder
#also save analysis.awk file in the same location
#open desktop right-click and choose 'Open in Terminal'
#run this command
#ns LAN.tcl

#both nam and awk file will be executed automatically

set ns [new Simulator]

set tr [open "LAN.tr" w]
$ns trace-all $tr

set nam [open "LAN.nam" w]
$ns namtrace-all $nam

set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]
set n6 [$ns node]

$ns make-lan "$n1 $n2 $n3 $n4 $n5 $n6" 0.2Mb 20ms LL Queue/DropTail Mac/802_3

set tcpsendagent1 [new Agent/TCP]
set tcpsendagent2 [new Agent/TCP]

set tcprecvagent1 [new Agent/TCPSink]
set tcprecvagent2 [new Agent/TCPSink]

$ns attach-agent $n1 $tcpsendagent1
$ns attach-agent $n2 $tcpsendagent2

$ns attach-agent $n6 $tcprecvagent1
$ns attach-agent $n6 $tcprecvagent2

set app1 [new Application/FTP]
set app2 [new Application/FTP]

$app1 attach-agent $tcpsendagent1
$app2 attach-agent $tcpsendagent2


$ns connect $tcpsendagent1 $tcprecvagent1
$ns connect $tcpsendagent2 $tcprecvagent2

$ns at 0.1 "$app1 start"
$ns at 0.4 "$app2 start"

proc finish { } {
global ns tr nam
$ns flush-trace
close $tr
close $nam
exec nam LAN.nam &
exec awk -f analysis.awk LAN.tr &
exit 0
}

$ns at 10 "finish"

$ns run
"""
ethernet_LAN_awk = """
BEGIN{
drop=0
recv=0
starttime1=0
endtime1=0
latency1=0
filesize1=0
starttime2=0
endtime2=0
latency2=0
filesize2=0
flag0=0
flag1=0
bandwidth1=0
bandwidth2=0
}

{

if($1=="r" && $3==6)
{
if(flag1=0)
{
flag1=1
starttime1=$2
}
filesize1+=$6
endtime1=$2
latency=endtime1-starttime1
bandwidth1=filesize1/latency
printf "%f %f", endtime1, bandwidth1 >> "file.xg"

}

}
END{
bandwidth1 = filesize1/latency
latency = endtime1-starttime1
print("")
print("Final Values..")
print("Filesize:",filesize1)
print("Latency:",latency)
print("Throughput(Mbps):",bandwidth1/1000000)
}
"""
complexdcf_tcl = """
#How to run
#==========
#save this file as complexdcf.tcl in desktop folder
#open desktop right-click and choose 'Open in Terminal'
#run this command
#ns complexdcf.tcl

#nam file will be executed automatically

Mac/802_11 set dataRate_ 1Mb
set val(chan) Channel/WirelessChannel ;# channel type
set val(prop) Propagation/TwoRayGround ;# radio-propagation model

set val(ant) Antenna/OmniAntenna ;# Antenna type
set val(ll) LL ;# Link layer type
set val(ifq) Queue/DropTail/PriQueue ;# Interface queue type
set val(ifqlen) 50 ;# max packet in ifq
set val(netif) Phy/WirelessPhy ;# network interface type
set val(mac) Mac/802_11 ;# MAC type
set val(nn) 15 ;# number of mobilenodes
set val(rp) AODV ;# routing protocol
set val(x) 800
set val(y) 800

# Creating simulation object
set ns [new Simulator]

#creating Output trace files
set f [open complexdcf.tr w]
$ns trace-all $f

set namtrace [open complexdcf.nam w]
$ns namtrace-all-wireless $namtrace $val(x) $val(y)

set f0 [open complexdcf_AT.tr w]

set topo [new Topography]
$topo load_flatgrid 800 800
# Defining Global Variables
create-god $val(nn)
set chan_1 [new $val(chan)]
# setting the wireless nodes parameters
$ns node-config -adhocRouting $val(rp) \
-llType $val(ll) \
-macType $val(mac) \
-ifqType $val(ifq) \
-ifqLen $val(ifqlen) \
-antType $val(ant) \
-propType $val(prop) \
-phyType $val(netif) \
-topoInstance $topo \
-agentTrace OFF \
-routerTrace ON \
-macTrace ON \
-movementTrace OFF \
-channel $chan_1 

proc finish {} {
global ns namtrace f f0
$ns flush-trace
close $namtrace
close $f0
puts "Executing nam..."
exec nam -r 5m complexdcf.nam &
exit 0
}
# Defining a procedure to calculate the througpout
proc record {} {
global sink1 sink3 sink7 sink10 sink11 f0
set ns [Simulator instance]
set time 0.5
set bw0 [$sink3 set bytes_]
set bw3 [$sink3 set bytes_]
set bw7 [$sink7 set bytes_]
set bw10 [$sink10 set bytes_]
set bw11 [$sink11 set bytes_]
set now [$ns now]
puts $f0 "$now [expr ($bw0+$bw3+$bw7+$bw10+$bw11)/$time*8/1000000]"
# Calculating the average throughput

$sink1 set bytes_ 0
$sink3 set bytes_ 0
$sink7 set bytes_ 0
$sink10 set bytes_ 0
$sink11 set bytes_ 0
$ns at [expr $now+$time] "record"
}
#Creating the wireless Nodes
for {set i 0} {$i < $val(nn) } {incr i} {
set n($i) [$ns node]
$n($i) random-motion 0 ;
}
#setting the initial position for the nodes
for {set i 0} {$i < $val(nn)} {incr i} {
$ns initial_node_pos $n($i) 30+i*100
}
for {set i 0} {$i < $val(nn)} {incr i} {
$n($i) set X_ 0.0
$n($i) set Y_ 0.0
$n($i) set Z_ 0.0
}
# making some nodes move in the topography
$ns at 0.0 "$n(0) setdest 100.0 100.0 3000.0"
$ns at 0.0 "$n(1) setdest 200.0 200.0 3000.0"
$ns at 0.0 "$n(2) setdest 300.0 200.0 3000.0"
$ns at 0.0 "$n(3) setdest 400.0 300.0 3000.0"
$ns at 0.0 "$n(4) setdest 500.0 300.0 3000.0"
$ns at 0.0 "$n(5) setdest 600.0 400.0 3000.0"
$ns at 0.0 "$n(6) setdest 600.0 100.0 3000.0"
$ns at 0.0 "$n(7) setdest 600.0 200.0 3000.0"

$ns at 0.0 "$n(8) setdest 600.0 300.0 3000.0"
$ns at 0.0 "$n(9) setdest 600.0 350.0 3000.0"
$ns at 0.0 "$n(10) setdest 700.0 100.0 3000.0"
$ns at 0.0 "$n(11) setdest 700.0 200.0 3000.0"
$ns at 0.0 "$n(12) setdest 700.0 300.0 3000.0"
$ns at 0.0 "$n(13) setdest 700.0 350.0 3000.0"
$ns at 0.0 "$n(14) setdest 700.0 400.0 3000.0"
$ns at 2.0 "$n(5) setdest 100.0 400.0 500.0"
$ns at 1.5 "$n(3) setdest 450.0 150.0 500.0"
$ns at 50.0 "$n(7) setdest 300.0 400.0 500.0"
$ns at 2.0 "$n(10) setdest 200.0 400.0 500.0"
$ns at 2.0 "$n(11) setdest 650.0 400.0 500.0"
#Creating receiving sinks with monitoring ability to monitor the incoming bytes
# LossMonitor objects are a subclass of agent objects that implement a traffic sink.
set sink1 [new Agent/LossMonitor]
set sink3 [new Agent/LossMonitor]
set sink7 [new Agent/LossMonitor]
set sink10 [new Agent/LossMonitor]
set sink11 [new Agent/LossMonitor]
$ns attach-agent $n(1) $sink1
$ns attach-agent $n(3) $sink3
$ns attach-agent $n(7) $sink7
$ns attach-agent $n(10) $sink10
$ns attach-agent $n(11) $sink11
# setting TCP as the transmission protocol over the connections
set tcp0 [new Agent/TCP]
$ns attach-agent $n(0) $tcp0
set tcp2 [new Agent/TCP]
$ns attach-agent $n(2) $tcp2
set tcp4 [new Agent/TCP]

$ns attach-agent $n(4) $tcp4
set tcp5 [new Agent/TCP]
$ns attach-agent $n(5) $tcp5
set tcp9 [new Agent/TCP]
$ns attach-agent $n(9) $tcp9
set tcp13 [new Agent/TCP]
$ns attach-agent $n(13) $tcp13
set tcp6 [new Agent/TCP]
$ns attach-agent $n(6) $tcp6
set tcp14 [new Agent/TCP]
$ns attach-agent $n(14) $tcp14
set tcp8 [new Agent/TCP]
$ns attach-agent $n(8) $tcp8
set tcp12 [new Agent/TCP]
$ns attach-agent $n(12) $tcp12
# Setting FTP connections
set ftp9 [new Application/FTP]
$ftp9 attach-agent $tcp9
$ftp9 set type_ FTP
set ftp13 [new Application/FTP]
$ftp13 attach-agent $tcp13
$ftp13 set type_ FTP
set ftp6 [new Application/FTP]
$ftp6 attach-agent $tcp6
$ftp6 set type_ FTP
set ftp14 [new Application/FTP]
$ftp14 attach-agent $tcp14
$ftp14 set type_ FTP
set ftp8 [new Application/FTP]
$ftp8 attach-agent $tcp8

$ftp8 set type_ FTP
set ftp12 [new Application/FTP]
$ftp12 attach-agent $tcp12
$ftp12 set type_ FTP
#connecting the nodes
$ns connect $tcp0 $sink3
$ns connect $tcp5 $sink3
$ns connect $tcp2 $sink1
$ns connect $tcp4 $sink1
$ns connect $tcp9 $sink7
$ns connect $tcp13 $sink7
$ns connect $tcp6 $sink10
$ns connect $tcp14 $sink10
$ns connect $tcp8 $sink11
$ns connect $tcp12 $sink11
# Defining CBR procedure with the required parametes
proc attach-CBR-traffic { node sink size interval } {
set ns [Simulator instance]
set cbr [new Agent/CBR]
$ns attach-agent $node $cbr
$cbr set packetSize_ $size
$cbr set interval_ $interval
$ns connect $cbr $sink
return $cbr
}
set cbr0 [attach-CBR-traffic $n(0) $sink3 1000 .015]
set cbr1 [attach-CBR-traffic $n(5) $sink3 1000 .015]
set cbr2 [attach-CBR-traffic $n(2) $sink1 1000 .015]
set cbr3 [attach-CBR-traffic $n(4) $sink1 1000 .015]
# Setting the begining and ending time of each connection

$ns at 0.0 "record"
$ns at 20.0 "$cbr0 start"
$ns at 20.0 "$cbr2 start"
$ns at 800.0 "$cbr0 stop"
$ns at 850.0 "$cbr2 stop"
$ns at 30.0 "$cbr1 start"
$ns at 30.0 "$cbr3 start"
$ns at 850.0 "$cbr1 stop"
$ns at 870.0 "$cbr3 stop"
$ns at 25.0 "$ftp6 start"
$ns at 25.0 "$ftp14 start"
$ns at 810.0 "$ftp6 stop"
$ns at 860.0 "$ftp14 stop"
$ns at 35.0 "$ftp9 start"
$ns at 35.0 "$ftp13 start"
$ns at 830.0 "$ftp9 stop"
$ns at 889.0 "$ftp13 stop"
$ns at 40.0 "$ftp8 start"
$ns at 40.0 "$ftp12 start"
$ns at 820.0 "$ftp8 stop"
$ns at 890.0 "$ftp12 stop"
$ns at 10.0 "finish"
# Runnning the simulation
puts "Start of simulation.."
$ns run
"""
