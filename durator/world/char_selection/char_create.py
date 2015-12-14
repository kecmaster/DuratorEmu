from enum import Enum
import io
from struct import Struct

from durator.world.character import ( CharacterRace, CharacterClass
                                    , CharacterGender, CharacterManager )
from durator.world.opcodes import OpCode
from durator.world.world_packet import WorldPacket
from pyshgck.bin import read_cstring, read_struct


class CharCreateResponseCode(Enum):

    SUCCESS             = 0x2D
    ERROR               = 0x2E
    FAILED              = 0x2F
    NAME_IN_USE         = 0x30
    SERVER_LIMIT        = 0x33
    ACCOUNT_LIMIT       = 0x34


class CharCreateHandler(object):

    PACKET_CHAR_BIN = Struct("<9B")
    RESPONSE_BIN = Struct("<B")

    def __init__(self, connection, packet):
        self.conn = connection
        self.packet = packet

        self.char_name = ""
        self.char_race = None
        self.char_class = None
        self.char_gender = None
        self.char_features = None
        self.unk_value = 0

    def process(self):
        self._parse_packet(self.packet)

        char_values = ( self.char_name, self.char_race, self.char_class
                      , self.char_gender, self.char_features )
        manager_code = CharacterManager.create_character(
            self.conn.account, char_values
        )

        packet = self._get_packet(manager_code)
        return None, packet

    def _parse_packet(self, packet):
        packet_io = io.BytesIO(packet)
        char_name_bytes = read_cstring(packet_io, 0)
        self.char_name = char_name_bytes.decode("utf8")
        char_data = read_struct(packet_io, self.PACKET_CHAR_BIN)

        self.char_race = CharacterRace(char_data[0])
        self.char_class = CharacterClass(char_data[1])
        self.char_gender = CharacterGender(char_data[2])
        self.char_features = char_data[3:8]
        self.unk_value = char_data[8]

    def _get_packet(self, manager_code):
        response_code = {
            0: CharCreateResponseCode.SUCCESS,
            1: CharCreateResponseCode.FAILED,
            2: CharCreateResponseCode.NAME_IN_USE
        }.get(manager_code)

        packet = WorldPacket(self.RESPONSE_BIN.pack(response_code.value))
        packet.opcode = OpCode.SMSG_CHAR_CREATE
        return packet
