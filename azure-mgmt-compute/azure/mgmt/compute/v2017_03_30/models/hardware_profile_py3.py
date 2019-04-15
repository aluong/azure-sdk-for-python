# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class HardwareProfile(Model):
    """Specifies the hardware settings for the virtual machine.

    :param vm_size: Specifies the size of the virtual machine. For more
     information about virtual machine sizes, see [Sizes for virtual
     machines](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-sizes?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json).
     <br><br> The available VM sizes depend on region and availability set. For
     a list of available sizes use these APIs:  <br><br> [List all available
     virtual machine sizes in an availability
     set](https://docs.microsoft.com/rest/api/compute/availabilitysets/listavailablesizes)
     <br><br> [List all available virtual machine sizes in a
     region](https://docs.microsoft.com/rest/api/compute/virtualmachinesizes/list)
     <br><br> [List all available virtual machine sizes for
     resizing](https://docs.microsoft.com/rest/api/compute/virtualmachines/listavailablesizes).
     Possible values include: 'Basic_A0', 'Basic_A1', 'Basic_A2', 'Basic_A3',
     'Basic_A4', 'Standard_A0', 'Standard_A1', 'Standard_A2', 'Standard_A3',
     'Standard_A4', 'Standard_A5', 'Standard_A6', 'Standard_A7', 'Standard_A8',
     'Standard_A9', 'Standard_A10', 'Standard_A11', 'Standard_A1_v2',
     'Standard_A2_v2', 'Standard_A4_v2', 'Standard_A8_v2', 'Standard_A2m_v2',
     'Standard_A4m_v2', 'Standard_A8m_v2', 'Standard_D1', 'Standard_D2',
     'Standard_D3', 'Standard_D4', 'Standard_D11', 'Standard_D12',
     'Standard_D13', 'Standard_D14', 'Standard_D1_v2', 'Standard_D2_v2',
     'Standard_D3_v2', 'Standard_D4_v2', 'Standard_D5_v2', 'Standard_D11_v2',
     'Standard_D12_v2', 'Standard_D13_v2', 'Standard_D14_v2',
     'Standard_D15_v2', 'Standard_DS1', 'Standard_DS2', 'Standard_DS3',
     'Standard_DS4', 'Standard_DS11', 'Standard_DS12', 'Standard_DS13',
     'Standard_DS14', 'Standard_DS1_v2', 'Standard_DS2_v2', 'Standard_DS3_v2',
     'Standard_DS4_v2', 'Standard_DS5_v2', 'Standard_DS11_v2',
     'Standard_DS12_v2', 'Standard_DS13_v2', 'Standard_DS14_v2',
     'Standard_DS15_v2', 'Standard_F1', 'Standard_F2', 'Standard_F4',
     'Standard_F8', 'Standard_F16', 'Standard_F1s', 'Standard_F2s',
     'Standard_F4s', 'Standard_F8s', 'Standard_F16s', 'Standard_G1',
     'Standard_G2', 'Standard_G3', 'Standard_G4', 'Standard_G5',
     'Standard_GS1', 'Standard_GS2', 'Standard_GS3', 'Standard_GS4',
     'Standard_GS5', 'Standard_H8', 'Standard_H16', 'Standard_H8m',
     'Standard_H16m', 'Standard_H16r', 'Standard_H16mr', 'Standard_L4s',
     'Standard_L8s', 'Standard_L16s', 'Standard_L32s', 'Standard_NC6',
     'Standard_NC12', 'Standard_NC24', 'Standard_NC24r', 'Standard_NV6',
     'Standard_NV12', 'Standard_NV24'
    :type vm_size: str or
     ~azure.mgmt.compute.v2017_03_30.models.VirtualMachineSizeTypes
    """

    _attribute_map = {
        'vm_size': {'key': 'vmSize', 'type': 'str'},
    }

    def __init__(self, *, vm_size=None, **kwargs) -> None:
        super(HardwareProfile, self).__init__(**kwargs)
        self.vm_size = vm_size
