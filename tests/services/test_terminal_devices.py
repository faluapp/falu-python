import unittest

import responses
from responses import matchers

import falu


class TerminalDevicesTests(unittest.TestCase):
    base_url = "https://api.falu.io/v1"
    falu.api_key = "fkst_1234"

    device = {
        "label": "Anne's Hand-held",
        "metadata": {
            "property_1": "string",
            "property_2": "string"
        },
        "id": "tdev_602a8dd0a54847479a874de4",
        "created": "2023-04-06T09:46:44Z",
        "updated": "2023-04-06T09:46:44Z",
        "category": "bluetooth",
        "type": "other",
        "serial_number": "123-456-789",
        "location": "tloc_602a8dd0a54847479a874de4",
        "version": {
            "software": "1.0.12.437",
            "firmware": "1.1.4"
        },
        "network": {
            "status": "offline",
            "ip": "196.168.1.52",
            "cellular": {
                "mcc": "639",
                "mnc": "02",
                "lac": "64d7a2"
            }
        },
        "current_task": {
            "visit": "vst_602a8dd0a54847479a874de4"
        },
        "workspace": "wksp_602a8dd0a54847479a874de4",
        "live": True,
        "etag": "FL9rRnlW2Qg="
    }

    @responses.activate
    def test_getting_terminal_devices_works(self):
        resp = responses.get("{}/terminals/devices".format(self.base_url), json=[self.device],
                             status=200)
        responses.add(resp)

        resources = falu.TerminalDevice.get_terminal_devices()

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_getting_terminal_device_works(self):
        resp = responses.get("{}/terminals/devices/{}".format(self.base_url, "tdev_602a8dd0a54847479a874de4"),
                             json=self.device, status=200)
        responses.add(resp)

        resources = falu.TerminalDevice.get_terminal_device(device="tdev_602a8dd0a54847479a874de4")

        self.assertIsNotNone(resources)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_adding_terminal_device_works(self):
        request = {
            "location": "tloc_602a8dd0a54847479a874de4",
            "token": "ey",
            "label": "Anne's Hand-held"
        }

        resp = responses.post(
            "{}/terminals/devices".format(self.base_url),
            json=self.device,
            match=[matchers.json_params_matcher(request)],
            status=200
        )
        responses.add(resp)

        resource = falu.TerminalDevice.create_terminal_device(data=request)

        self.assertIsNotNone(resource)
        self.assertEqual(200, resp.status)

    @responses.activate
    def test_deleting_terminal_device_works(self):
        resp = responses.delete("{}/terminals/devices/{}".format(self.base_url, "tdev_602a8dd0a54847479a874de4"),
                                status=200)
        responses.add(resp)

        falu.TerminalDevice.delete_terminal_device(device="tdev_602a8dd0a54847479a874de4")

        self.assertEqual(200, resp.status)

    @responses.activate
    def test_hand_terminal_device_works(self):
        request = {
            "visit": "vst_602a8dd0a54847479a874de4",
            "configuration": None
        }

        resp = responses.post(
            "{}/terminals/devices/{}/process_visit".format(self.base_url, "tdev_602a8dd0a54847479a874de4"),
            json=self.device,
            match=[matchers.json_params_matcher(request)],
            status=200
        )
        responses.add(resp)

        falu.TerminalDevice.handoff_terminal_device(device="tdev_602a8dd0a54847479a874de4", data=request)

        self.assertEqual(200, resp.status)
