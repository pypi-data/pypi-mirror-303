from pyproto import ProtoBuf

from AndroidQQ.struct import PackHeadNoToken, Pack_


def OidbSvcTrpcTcp_0xfe1_2(info):
    """查询非好友"""
    buffer = ProtoBuf({1: 4065, 2: 2, 4: {1: 'u_YzatHGDbllkvQ41liEoiyQ', 3: {1: 20037}}, 5: ''}
                      ).toBuf()
    buffer = PackHeadNoToken(info, buffer, 'OidbSvcTrpcTcp.0xfe1_2')
    buffer = Pack_(info, buffer, Types=11, encryption=1, sso_seq=info.seq)
    return buffer
