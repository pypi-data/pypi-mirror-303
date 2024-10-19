from circuitmatter.data_model import (
    Cluster,
    ClusterId,
    DeviceTypeId,
    EndpointNumber,
    ListAttribute,
    Uint16,
)
from circuitmatter import tlv


class DescriptorCluster(Cluster):
    CLUSTER_ID = 0x001D

    class DeviceTypeStruct(tlv.Structure):
        DeviceType = DeviceTypeId(0)
        Revision = Uint16(1, minimum=1)

    DeviceTypeList = ListAttribute(0x0000, DeviceTypeStruct)
    ServerList = ListAttribute(0x0001, ClusterId())
    ClientList = ListAttribute(0x0002, ClusterId())
    PartsList = ListAttribute(0x0003, EndpointNumber())
