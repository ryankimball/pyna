**UGLY JSON-LIKE BLOB:**  
{`'running':` '! Command: show running-config\n! device: SW3 (vEOS, EOS-4.17.8M)\n!\n! boot system flash:/vEOS-lab.swi\n!\ntransceiver qsfp default-mode 4x10G\n!\nhostname SW3\n!\nspanning-tree mode mstp\n!\nno aaa root\n!\nusername admin role network-admin secret sha512 $6$LH6hfO1CqguRBpkk$7OgT5zhOX2rx27dovb9gfXcpqz9uscLidFGjgGesGX/qpTei1aJPhJfQ9TugGomE00RYywma/qUZC9RDboKe/0\n!\ninterface Ethernet1\n!\ninterface Ethernet2\n!\ninterface Ethernet3\n!\ninterface Ethernet4\n!\ninterface Ethernet5\n!\ninterface Ethernet6\n!\ninterface Ethernet7\n!\ninterface Ethernet8\n!\ninterface Ethernet9\n!\ninterface Ethernet10\n!\ninterface Ethernet11\n!\ninterface Ethernet12\n!\ninterface Management1\n   mtu 1450\n   ip address 172.16.2.20/24\n!\nip route 0.0.0.0/0 172.16.2.100\n!\nno ip routing\n!\nmanagement api http-commands\n   protocol http\n   no shutdown\n!\n!\nend\n', `'candidate':` '', `'startup':` '! Command: show startup-config\n! Startup-config last modified at  Thu Mar 22 14:28:10 2018 by admin\n! device: SW3 (vEOS, EOS-4.17.8M)\n!\n! boot system flash:/vEOS-lab.swi\n!\ntransceiver qsfp default-mode 4x10G\n!\nhostname SW3\n!\nspanning-tree mode mstp\n!\nno aaa root\n!\nusername admin role network-admin secret sha512 $6$LH6hfO1CqguRBpkk$7OgT5zhOX2rx27dovb9gfXcpqz9uscLidFGjgGesGX/qpTei1aJPhJfQ9TugGomE00RYywma/qUZC9RDboKe/0\n!\ninterface Ethernet1\n!\ninterface Ethernet2\n!\ninterface Ethernet3\n!\ninterface Ethernet4\n!\ninterface Ethernet5\n!\ninterface Ethernet6\n!\ninterface Ethernet7\n!\ninterface Ethernet8\n!\ninterface Ethernet9\n!\ninterface Ethernet10\n!\ninterface Ethernet11\n!\ninterface Ethernet12\n!\ninterface Management1\n   mtu 1450\n   ip address 172.16.2.20/24\n!\nip route 0.0.0.0/0 172.16.2.100\n!\nno ip routing\n!\nmanagement api http-commands\n   protocol http\n   no shutdown\n!\n!\nend\n'}

**REAL JSON:**  
{  
`"running":` "! Command: show running-config\n! device: SW3 (vEOS, EOS-4.17.8M)\n!\n! boot system flash:/vEOS-lab.swi\n!\ntransceiver qsfp default-mode 4x10G\n!\nhostname SW3\n!\nspanning-tree mode mstp\n!\nno aaa root\n!\nusername admin role network-admin secret sha512 $6$LH6hfO1CqguRBpkk$7OgT5zhOX2rx27dovb9gfXcpqz9uscLidFGjgGesGX/qpTei1aJPhJfQ9TugGomE00RYywma/qUZC9RDboKe/0\n!\ninterface Ethernet1\n!\ninterface Ethernet2\n!\ninterface Ethernet3\n!\ninterface Ethernet4\n!\ninterface Ethernet5\n!\ninterface Ethernet6\n!\ninterface Ethernet7\n!\ninterface Ethernet8\n!\ninterface Ethernet9\n!\ninterface Ethernet10\n!\ninterface Ethernet11\n!\ninterface Ethernet12\n!\ninterface Management1\n   mtu 1450\n   ip address 172.16.2.20/24\n!\nip route 0.0.0.0/0 172.16.2.100\n!\nno ip routing\n!\nmanagement api http-commands\n   protocol http\n   no shutdown\n!\n!\nend\n",  
`"candidate":` "",  
`"startup":` "! Command: show startup-config\n! Startup-config last modified at  Thu Mar 22 14:28:10 2018 by admin\n! device: SW3 (vEOS, EOS-4.17.8M)\n!\n! boot system flash:/vEOS-lab.swi\n!\ntransceiver qsfp default-mode 4x10G\n!\nhostname SW3\n!\nspanning-tree mode mstp\n!\nno aaa root\n!\nusername admin role network-admin secret sha512 $6$LH6hfO1CqguRBpkk$7OgT5zhOX2rx27dovb9gfXcpqz9uscLidFGjgGesGX/qpTei1aJPhJfQ9TugGomE00RYywma/qUZC9RDboKe/0\n!\ninterface Ethernet1\n!\ninterface Ethernet2\n!\ninterface Ethernet3\n!\ninterface Ethernet4\n!\ninterface Ethernet5\n!\ninterface Ethernet6\n!\ninterface Ethernet7\n!\ninterface Ethernet8\n!\ninterface Ethernet9\n!\ninterface Ethernet10\n!\ninterface Ethernet11\n!\ninterface Ethernet12\n!\ninterface Management1\n   mtu 1450\n   ip address 172.16.2.20/24\n!\nip route 0.0.0.0/0 172.16.2.100\n!\nno ip routing\n!\nmanagement api http-commands\n   protocol http\n   no shutdown\n!\n!\nend\n"  
}
