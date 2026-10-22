CN EXAM - Practicals 1, 6, 8, 9, 10
===================================

P1_Packet_Tracer\      6 topologies (Bus, Star, Ring, Tree, Mesh, Hybrid) - double-click to open
P6_Packet_Tracer\      6_Network_Commands.pkt
P10_Packet_Tracer\     10_HTTP_DNS_SMTP.pkt
Wireshark_P8_P9_P10\   sample captures (open with Wireshark: File > Open)

--- P1 ---
PCs get 192.168.1.10, .11, .12 ... (mask 255.255.255.0).  Test: PC > Desktop > Command Prompt > ping 192.168.1.11
Ring / Mesh / Hybrid use spanning tree: wait ~30 s (green link lights) before pinging.
Bus / Ring / Mesh use a switch per PC because a Packet Tracer PC has only ONE Ethernet port.

--- P6 and P10 network (same layout in both files) ---
  PC0 192.168.1.10 --\
                      Switch0 -- Router0 (Fa0/0 192.168.1.1 | Fa0/1 192.168.2.1) -- Switch1 -- Server0 192.168.2.10
  PC1 192.168.1.11 --/
PC gateway 192.168.1.1, DNS 192.168.2.10.  Server gateway 192.168.2.1.

P6 - on PC0: Desktop > Command Prompt, then run
  ipconfig        ipconfig /all        ping 192.168.2.10        ping www.example.com
  tracert 192.168.2.10        nslookup www.example.com        arp -a        netstat

P10 - Server0 has HTTP, DNS and Email (SMTP + POP3) switched on.
  Web   : PC0 > Desktop > Web Browser > http://www.example.com
  DNS   : names on the server: example.com, www.example.com, mail.example.com -> 192.168.2.10
  Mail  : domain example.com. PC0 = user0 / pass0, PC1 = user1 / pass1 (already set in each PC's Email app)
          PC0 > Desktop > Email > Compose > To: user1@example.com > Send;  PC1 > Email > Receive
  See the packets: click Simulation (bottom right) > Edit Filters > tick only HTTP / DNS / SMTP / POP3 > send the request > click each packet to see the PDU details.

--- Wireshark (P8, P9, P10) ---
Sample captures made for practice, NOT recorded from a real network:
  P8_P9_general_capture.pcap   ARP, ICMP ping, DNS, TCP handshake, HTTP, DNS
  P10_HTTP.pcap  P10_DNS.pcap  P10_SMTP.pcap
Display filters:  http   dns   smtp   icmp   arp   tcp.port == 80   ip.addr == 192.168.1.10
In the exam capture your own traffic live: pick your Wi-Fi/Ethernet adapter > Start (blue shark fin) > browse a site / run ping > Stop (red square).
