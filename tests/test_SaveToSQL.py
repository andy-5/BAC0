#!/usr/bin/env python
# -*- coding utf-8 -*-

"""
Test Bacnet communication with another device
"""
import os.path
from typing import AsyncGenerator
import pytest
import asyncio
import BAC0

@pytest.mark.asyncio
async def test_SaveToSQL(network_and_devices):
    async for resources in network_and_devices:
        loop, bacnet, device_app, device30_app, test_device, test_device_30 = resources
        # test_device_300 = network_and_devices.test_device_300
        test_device.save()
        test_device_30.save(filename="obj30.db")
        # test_device_300.save(filename="obj300")
        assert os.path.isfile("{}.db".format(test_device.properties.db_name))
        assert os.path.isfile("{}.db".format("obj30"))
        # assert os.path.isfile("{}.db".format("obj300"))

@pytest.mark.asyncio
async def test_disconnection_of_device(network_and_devices):
    async for resources in network_and_devices:
        loop, bacnet, device_app, device30_app, test_device, test_device_30 = resources
        # test_device_300 = network_and_devices.test_device_300
        test_device.disconnect()
        test_device_30.disconnect()
        # test_device_300.save(filename="obj300")
        assert isinstance(test_device, BAC0.core.devices.Device.DeviceFromDB)
        assert isinstance(test_device_30, BAC0.core.devices.Device.DeviceFromDB)
        # assert os.path.isfile("{}.db".format("obj300"))
        test_device.connect(network=bacnet)
        test_device_30.connect(network=bacnet)
        assert isinstance(test_device, BAC0.core.devices.Device.RPMDeviceConnected)
        assert isinstance(test_device_30, BAC0.core.devices.Device.RPMDeviceConnected)
