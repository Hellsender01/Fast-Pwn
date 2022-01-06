from __future__ import absolute_import
from __future__ import division

from ..log import getLogger

log = getLogger(__name__)


def ret2system(rop, elf, aling=True, bin_sh=None):
    """Create Return to system ROP chain

    Args:
        aling (bool, optional): Add return instruction before system for stack alingment
        bin_sh (int, optional): /bin/sh address

    Returns:
        TYPE: Description
    """

    if "system" not in elf.sym:
        log.error("Fuction system not found in symbols.")
        return None

    if aling:
        rop.raw(rop.ret[0])

    if bin_sh:
        rop.system(bin_sh)
    else:
        if not elf.find_bin_sh():
            log.error("/bin/sh not found.")
            return None
        rop.system(elf.find_bin_sh())

