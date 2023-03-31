
from random import getrandbits, randint
import ipaddress

class RandomPrefixGenerator:

    def __init__(self, version: int, mode='prefix', min_length=16, max_length=24 ) -> None:
        """
        Constructor for the RandomPrefixGenerator class

        :param version: The IP version to generate prefixes for. Can be 4 or 6.
        :type version: int
        :param mode: The type of address to generate. Can be 'prefix' or 'ip'.
        :type mode: str
        :param min_length: The minimum prefix length to generate.
        :type min_length: int
        :param max_length: The maximum prefix length to generate.
        :type max_length: int
        """
        if version == 4 or version == 6:
            self._version = version
        else:
            raise ValueError("Invalid IP version")

        if mode not in ('ip', 'prefix'):
            raise ValueError("Invalid mode - use 'ip' or 'prefix'")

        self._mode = mode
        if mode == 'prefix':
            self._min = min_length
            self._max = max_length

    def __iter__(self):
        return self

    def __next__(self):
        if self._version == 4:
            bits = getrandbits(32)
            addr = ipaddress.IPv4Address(bits)
            if self._mode == 'ip':
                return str(addr)

            mask_bits = randint(self._min, self._max)
            subnet = ipaddress.IPv4Network( (addr,mask_bits), False )
            return str(subnet)

        elif self._version == 6:
            bits = getrandbits(128)
            addr = ipaddress.IPv6Address(bits)
            if self._mode == 'ip':
                return str(addr)

            mask_bits = randint(self._min, self._max)
            subnet = ipaddress.IPv6Network( (addr,mask_bits), False )
            return str(subnet)
