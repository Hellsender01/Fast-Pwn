from __future__ import absolute_import
from __future__ import division

from ..log import getLogger

log = getLogger(__name__)


def ret2plt(rop, elf, leak, ret=None):
    """Create ret2plt ROP chain

    Args:
        elf (pwnlib.elf.elf.ELF): ELF Object of binary
        leak (int): Function address to leak from GOT
        ret (int,None): Address to return
    """

    if "puts" not in elf.got:
        log.error("Fuction puts not found in GOT.")
        return None

    if leak not in elf.got.values():
        log.error("No such address to leak in GOT.")

    rop.puts(leak)

    if ret:
        rop.call(ret)
