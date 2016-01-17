""" Opcodes used to communicate between client and server.

There are deliberately few opcodes written below, because I don't want to
clutter this enum with opcodes I will never handle because they will likely not
appear within the goal usages of this emulator. Most of them come from CMangos.
"""

from enum import Enum


class OpCode(Enum):

    CMSG_CHAR_CREATE = 0x036
    CMSG_CHAR_ENUM   = 0x037
    CMSG_CHAR_DELETE = 0x038
    SMSG_CHAR_CREATE = 0x03A
    SMSG_CHAR_ENUM   = 0x03B
    SMSG_CHAR_DELETE = 0x03C

    CMSG_PLAYER_LOGIN     = 0x03D
    SMSG_NEW_WORLD        = 0x03E
    SMSG_TRANSFER_PENDING = 0x03F
    SMSG_TRANSFER_ABORTED = 0x040

    CMSG_NAME_QUERY          = 0x050
    SMSG_NAME_QUERY_RESPONSE = 0x051

    SMSG_UPDATE_OBJECT  = 0x0A9
    SMSG_DESTROY_OBJECT = 0x0AA

    MSG_MOVE_WORLDPORT_ACK = 0x0DC

    SMSG_TUTORIAL_FLAGS = 0x0FD

    CMSG_PING = 0x1DC
    SMSG_PONG = 0x1DD

    SMSG_AUTH_CHALLENGE = 0x1EC
    CMSG_AUTH_SESSION   = 0x1ED
    SMSG_AUTH_RESPONSE  = 0x1EE

    SMSG_COMPRESSED_UPDATE_OBJECT = 0x1F6

    SMSG_LOGIN_VERIFY_WORLD = 0x236
