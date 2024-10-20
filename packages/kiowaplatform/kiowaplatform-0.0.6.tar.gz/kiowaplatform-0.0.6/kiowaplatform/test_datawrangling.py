# test_datawrangling_unittest.py

import unittest
from kiowaplatform.datawrangling import get_starlink_data_v1, get_victor_vedirect_data_v1

# Helper functions to create DynamoDB-like structures
def make_dynamodb_string(value):
    return {'S': value}

def make_dynamodb_number(value):
    return {'N': str(value)}

def make_dynamodb_bool(value):
    return {'BOOL': value}

def make_dynamodb_map(mapping):
    return {'M': mapping}

class TestDataWrangling(unittest.TestCase):

    def compare_dicts(self, actual, expected, path=""):
        """
        Recursively compare two dictionaries.
        Use assertAlmostEqual for float values and assertEqual for others.
        """
        for key in expected:
            current_path = f"{path}.{key}" if path else key
            self.assertIn(key, actual, f"Missing key '{current_path}' in actual output.")

            expected_value = expected[key]
            actual_value = actual[key]

            if isinstance(expected_value, dict):
                self.compare_dicts(actual_value, expected_value, current_path)
            elif isinstance(expected_value, float):
                self.assertIsInstance(actual_value, float, f"Type mismatch at '{current_path}': expected float, got {type(actual_value).__name__}")
                self.assertAlmostEqual(actual_value, expected_value, places=2, msg=f"Mismatch at '{current_path}': expected {expected_value}, got {actual_value}")
            else:
                self.assertEqual(actual_value, expected_value, f"Mismatch at '{current_path}': expected {expected_value}, got {actual_value}")

        # Check for unexpected keys in actual
        for key in actual:
            current_path = f"{path}.{key}" if path else key
            self.assertIn(key, expected, f"Unexpected key '{current_path}' found in actual output.")

    def test_get_starlink_data_v1_valid_payload(self):
        payload = {
            'payload': {
                'M': {
                    'sensor_1': {
                        'M': {
                            'location': {
                                'M': {
                                    'lla': {
                                        'M': {
                                            'alt': {'N': '550.5'},
                                            'lon': {'N': '-122.084'},
                                            'lat': {'N': '37.422'},
                                        }
                                    },
                                    'source': {'N': '1'}
                                }
                            },
                            'status': {
                                'M': {
                                    'software_update_state': {'N': '2'},
                                    'eth_speed_mbps': {'N': '100'},
                                    'downlink_throughput_bps': {'N': '500000'},
                                    'uplink_throughput_bps': {'N': '300000'},
                                    'pop_ping_latency_ms': {'N': '20'},
                                    'initialization_duration_seconds': {
                                        'M': {
                                            'initial_network_entry': {'N': '30'},
                                            'stable_connection': {'N': '45'},
                                            'attitude_initialization': {'N': '60'},
                                            'first_cplane': {'N': '75'},
                                            'gps_valid': {'N': '90'},
                                            'burst_detected': {'N': '105'},
                                            'network_schedule': {'N': '120'},
                                            'first_pop_ping': {'N': '135'},
                                            'rf_ready': {'N': '150'},
                                            'ekf_converged': {'N': '165'}
                                        }
                                    },
                                    'alignment_stats': {
                                        'M': {
                                            'boresight_azimuth_deg': {'N': '180'},
                                            'boresight_elevation_deg': {'N': '45'},
                                            'tilt_angle_deg': {'N': '10'},
                                            'desired_boresight_azimuth_deg': {'N': '190'},
                                            'desired_boresight_elevation_deg': {'N': '50'},
                                            'attitude_uncertainty_deg': {'N': '0.5'}
                                        }
                                    },
                                    'device_info': {
                                        'M': {
                                            'country_code': {'S': 'US'},
                                            'id': {'S': 'device_123'},
                                            'software_version': {'S': 'v1.2.3'},
                                            'hardware_version': {'S': 'h1.0'},
                                            'bootcount': {'N': '42'},
                                            'generation_number': {'N': '3'}
                                        }
                                    },
                                    'device_state': {
                                        'M': {
                                            'uptime_s': {'N': '3600'}
                                        }
                                    },
                                    'software_update_stats': {
                                        'M': {
                                            'software_update_progress': {'N': '75'}
                                        }
                                    },
                                    'obstruction_stats': {
                                        'M': {
                                            'fraction_obstructed': {'N': '0.1'}
                                        }
                                    },
                                    'config': {
                                        'M': {
                                            'apply_location_request_mode': {'BOOL': True}
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        edge_type = 'starlink_edge'
        expected_output = {
            'edge_type': 'starlink_edge',
            'sensor_1': {
                'location': {
                    'altitude': 550.5,
                    'longitude': -122.084,
                    'latitude': 37.422,
                    'source': 1
                },
                'status': {
                    'software_update_state': 2,
                    'eth_speed_mbps': 100,
                    'downlink_throughput_bps': 500000,
                    'uplink_throughput_bps': 300000,
                    'pop_ping_latency_ms': 20,
                    'initialization_duration': {
                        'initial_network_entry': 30,
                        'stable_connection': 45,
                        'attitude_initialization': 60,
                        'first_cplane': 75,
                        'gps_valid': 90,
                        'burst_detected': 105,
                        'network_schedule': 120,
                        'first_pop_ping': 135,
                        'rf_ready': 150,
                        'ekf_converged': 165
                    }
                },
                'alignment_stats': {
                    'boresight_azimuth_deg': 180,
                    'boresight_elevation_deg': 45,
                    'tilt_angle_deg': 10,
                    'desired_boresight_azimuth_deg': 190,
                    'desired_boresight_elevation_deg': 50,
                    'attitude_uncertainty_deg': 0.5
                },
                'device_info': {
                    'country_code': 'US',
                    'id': 'device_123',
                    'software_version': 'v1.2.3',
                    'hardware_version': 'h1.0',
                    'bootcount': 42,
                    'generation_number': 3
                },
                'device_state': {
                    'uptime_s': 3600
                },
                'software_update_stats': {
                    'software_update_progress': 75
                },
                'obstruction_stats': {
                    'fraction_obstructed': 0.1
                },
                'config': {
                    'apply_location_request_mode': True
                }
            }
        }
        result = get_starlink_data_v1(payload, edge_type)
        self.compare_dicts(result, expected_output)

    def test_get_starlink_data_v1_missing_payload(self):
        payload = {}
        edge_type = 'starlink_edge'
        expected_output = {}
        result = get_starlink_data_v1(payload, edge_type)
        self.assertEqual(result, expected_output)

    def test_get_starlink_data_v1_missing_M_key(self):
        payload = {'payload': {}}
        edge_type = 'starlink_edge'
        expected_output = {}
        result = get_starlink_data_v1(payload, edge_type)
        self.assertEqual(result, expected_output)

    def test_get_starlink_data_v1_incomplete_sensor_data(self):
        payload = {
            'payload': {
                'M': {
                    'sensor_1': {
                        'M': {
                            # Missing 'location' and 'status'
                        }
                    }
                }
            }
        }
        edge_type = 'starlink_edge'
        expected_output = {
            'edge_type': 'starlink_edge',
            'sensor_1': {
                'location': {
                    'altitude': None,
                    'longitude': None,
                    'latitude': None,
                    'source': None
                },
                'status': {
                    'software_update_state': None,
                    'eth_speed_mbps': None,
                    'downlink_throughput_bps': None,
                    'uplink_throughput_bps': None,
                    'pop_ping_latency_ms': None,
                    'initialization_duration': {
                        'initial_network_entry': None,
                        'stable_connection': None,
                        'attitude_initialization': None,
                        'first_cplane': None,
                        'gps_valid': None,
                        'burst_detected': None,
                        'network_schedule': None,
                        'first_pop_ping': None,
                        'rf_ready': None,
                        'ekf_converged': None
                    }
                },
                'alignment_stats': {
                    'boresight_azimuth_deg': None,
                    'boresight_elevation_deg': None,
                    'tilt_angle_deg': None,
                    'desired_boresight_azimuth_deg': None,
                    'desired_boresight_elevation_deg': None,
                    'attitude_uncertainty_deg': None
                },
                'device_info': {
                    'country_code': None,
                    'id': None,
                    'software_version': None,
                    'hardware_version': None,
                    'bootcount': None,
                    'generation_number': None
                },
                'device_state': {
                    'uptime_s': None
                },
                'software_update_stats': {
                    'software_update_progress': None
                },
                'obstruction_stats': {
                    'fraction_obstructed': None
                },
                'config': {
                    'apply_location_request_mode': None
                }
            }
        }
        result = get_starlink_data_v1(payload, edge_type)
        self.compare_dicts(result, expected_output)

    def test_get_victor_vedirect_data_v1_valid_payload(self):
        payload = {
            'payload': {
                'M': {
                    'sensor_1': {
                        'M': {
                            'V': {'N': '12450'},  # 12.45 V
                            'I': {'N': '1500'},   # 1.5 A
                            'IL': {'N': '500'},   # 0.5 A
                            'VPV': {'N': '23000'}, # 23.0 V
                            'MPPT': {'N': '1'},
                            'OR': {'S': 'Operational'},
                            'ERR': {'N': '0'},
                            'SER#': {'S': 'SN123456'},
                            'LOAD': {'S': 'ON'},
                            'H21': {'N': '100'},
                            'H20': {'N': '200'},
                            'H23': {'N': '300'},
                            'H22': {'N': '400'},
                            'PID': {'S': 'PID123'},
                            'CS': {'N': '1'},
                            'FW': {'N': '101'},
                            'H19': {'N': '500'},
                            'PPV': {'N': '150'},
                            'HSDS': {'N': '250'},
                        }
                    }
                }
            }
        }
        edge_type = 'vedirect_edge'
        expected_output = {
            'edge_type': 'vedirect_edge',
            'sensor_1': {
                'MPPT': 1,
                'OperationalRunningStatus': 'Operational',
                'LoadCurrentA': 0.5,
                'LoadPowerW': round(0.5 * 12.45, 2),  # 6.225 W rounded to 6.23 W
                'ErrorCode': 0,
                'SerialNumber': 'SN123456',
                'LoadStatus': 'ON',
                'History21': 100,
                'History20': 200,
                'History23': 300,
                'BatteryVoltageV': 12.45,
                'BatteryCurrentA': 1.5,
                'History22': 400,
                'ProductID': 'PID123',
                'ChargingState': 1,
                'FirmwareVersion': 101,
                'History19': 500,
                'PanelPowerW': 150,
                'HistorySolarDailyYieldWh': 250,
                'PanelVoltageV': 23.0
            }
        }
        result = get_victor_vedirect_data_v1(payload, edge_type)
        self.compare_dicts(result, expected_output)

    def test_get_victor_vedirect_data_v1_missing_payload(self):
        payload = {}
        edge_type = 'vedirect_edge'
        expected_output = {}
        result = get_victor_vedirect_data_v1(payload, edge_type)
        self.assertEqual(result, expected_output)

    def test_get_victor_vedirect_data_v1_missing_M_key(self):
        payload = {'payload': {}}
        edge_type = 'vedirect_edge'
        expected_output = {}
        result = get_victor_vedirect_data_v1(payload, edge_type)
        self.assertEqual(result, expected_output)

    def test_get_victor_vedirect_data_v1_incomplete_sensor_data(self):
        payload = {
            'payload': {
                'M': {
                    'sensor_1': {
                        'M': {
                            'V': {'N': '12450'},  # 12.45 V
                            'I': {'N': '1500'},   # 1.5 A
                            # 'IL' is missing
                            # 'VPV' is missing
                            'MPPT': {'N': '1'},
                            # Other keys missing
                        }
                    }
                }
            }
        }
        edge_type = 'vedirect_edge'
        expected_output = {
            'edge_type': 'vedirect_edge',
            'sensor_1': {
                'MPPT': 1,
                'OperationalRunningStatus': None,
                'LoadCurrentA': None,
                'LoadPowerW': None,
                'ErrorCode': None,
                'SerialNumber': None,
                'LoadStatus': None,
                'History21': None,
                'History20': None,
                'History23': None,
                'BatteryVoltageV': 12.45,
                'BatteryCurrentA': 1.5,
                'History22': None,
                'ProductID': None,
                'ChargingState': None,
                'FirmwareVersion': None,
                'History19': None,
                'PanelPowerW': None,
                'HistorySolarDailyYieldWh': None,
                'PanelVoltageV': None
            }
        }
        result = get_victor_vedirect_data_v1(payload, edge_type)
        self.compare_dicts(result, expected_output)

    def test_get_victor_vedirect_data_v1_load_power_calculation(self):
        payload = {
            'payload': {
                'M': {
                    'sensor_1': {
                        'M': {
                            'V': {'N': '12000'},  # 12.0 V
                            'I': {'N': '2000'},   # 2.0 A
                            'IL': {'N': '500'},   # 0.5 A
                            'VPV': {'N': '23000'}, # 23.0 V
                            'MPPT': {'N': '1'},
                            'OR': {'S': 'Operational'},
                            'ERR': {'N': '0'},
                            'SER#': {'S': 'SN123456'},
                            'LOAD': {'S': 'ON'},
                            'H21': {'N': '100'},
                            'H20': {'N': '200'},
                            'H23': {'N': '300'},
                            'H22': {'N': '400'},
                            'PID': {'S': 'PID123'},
                            'CS': {'N': '1'},
                            'FW': {'N': '101'},
                            'H19': {'N': '500'},
                            'PPV': {'N': '150'},
                            'HSDS': {'N': '250'},
                        }
                    }
                }
            }
        }
        edge_type = 'vedirect_edge'
        expected_output = {
            'edge_type': 'vedirect_edge',
            'sensor_1': {
                'MPPT': 1,
                'OperationalRunningStatus': 'Operational',
                'LoadCurrentA': 0.5,
                'LoadPowerW': round(0.5 * 12.0, 2),  # 6.0 W
                'ErrorCode': 0,
                'SerialNumber': 'SN123456',
                'LoadStatus': 'ON',
                'History21': 100,
                'History20': 200,
                'History23': 300,
                'BatteryVoltageV': 12.0,
                'BatteryCurrentA': 2.0,
                'History22': 400,
                'ProductID': 'PID123',
                'ChargingState': 1,
                'FirmwareVersion': 101,
                'History19': 500,
                'PanelPowerW': 150,
                'HistorySolarDailyYieldWh': 250,
                'PanelVoltageV': 23.0
            }
        }
        result = get_victor_vedirect_data_v1(payload, edge_type)
        self.compare_dicts(result, expected_output)

if __name__ == '__main__':
    unittest.main()
