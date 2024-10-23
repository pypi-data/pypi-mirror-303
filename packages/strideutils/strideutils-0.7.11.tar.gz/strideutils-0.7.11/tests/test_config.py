import copy
from dataclasses import dataclass, fields
from typing import Optional

import pytest
from strideutils.stride_config import (
    ConfigObj,
    ConfigDict,
    HostChainsConfig,
    AppChainsConfig,
    _parse_raw_configs,
    MISSING_CONFIG_MSG,
)


def test_config_obj():
    # Create a dummy config object with a:
    #  - field with a valid value
    #  - field with an empty value
    #  - field with a None value
    @dataclass(repr=False)
    class DummyConfig(ConfigObj):
        field_a: str
        field_b: str = ""
        field_c: Optional[str] = None

    config = DummyConfig(field_a="value_a")

    # Accessing field A should be successful
    assert config.field_a == "value_a"

    # Accessing field B will error since it's empty
    with pytest.raises(AttributeError, match=MISSING_CONFIG_MSG.format(x="field_b")):
        config.field_b

    # Accessing field C will error since it's None
    with pytest.raises(AttributeError, match=MISSING_CONFIG_MSG.format(x="field_c")):
        config.field_c

    # Accessing field D will error since the field doesn't exist
    with pytest.raises(AttributeError, match="'DummyConfig' object has no attribute 'field_d'"):
        config.field_d

    # Check __contains__
    assert "field_a" in config
    assert "field_d" not in config

    # Check __iter__
    config = DummyConfig(field_a="value_a", field_b="value_b", field_c="value_c")
    assert [value for value in config] == ["value_a", "value_b", "value_c"]


def test_config_dict():
    # Create a dummy config dict with a:
    #  - field with a valid value
    #  - field with an empty value
    #  - field with a None value
    config = ConfigDict()
    config["field_a"] = "value_a"
    config["field_b"] = ""
    config["field_c"] = None

    # Accessing field A should be successful
    assert config["field_a"] == "value_a"

    # Accessing field B will error since it's empty
    with pytest.raises(KeyError, match=MISSING_CONFIG_MSG.format(x="field_b")):
        config["field_b"]

    # Accessing field C will error since it's None
    with pytest.raises(KeyError, match=MISSING_CONFIG_MSG.format(x="field_c")):
        config["field_c"]

    # Accessing field D will error since the field doesn't exist
    with pytest.raises(KeyError, match=MISSING_CONFIG_MSG.format(x="field_d")):
        config["field_d"]

    # Check __contains__
    assert "field_a" in config
    assert "field_d" not in config


class TestParseConfig:

    def setup_class(self):
        """
        Initailizes the raw json to represent the host chain and app chain configs
        """
        self.host_chain_names = [f.name for f in fields(HostChainsConfig)]
        self.app_chain_names = [f.name for f in fields(AppChainsConfig)]

        self.raw_stride = {
            "name": "stride",
            "id": "stride-1",
            "ticker": "STRD",
            "denom": "ustrd",
        }
        self.raw_host_chains = {chain: {"name": chain, "id": f"{chain}-1"} for chain in self.host_chain_names}
        self.raw_app_chains = {chain: {"name": chain, "id": f"{chain}-1"} for chain in self.app_chain_names}

        self.raw_config = {
            "stride": self.raw_stride,
            "host_zones": self.raw_host_chains,
            "app_chains": self.raw_app_chains,
        }
        self.raw_secrets = {"ENV": "DEV"}

    def test_parse_valid_config(self):
        """
        Tests parsing a valid config
        """
        # Parsing should not error
        config = _parse_raw_configs(self.raw_config, self.raw_secrets)

        # Validate all chains are set
        assert config.stride.name == "stride"
        assert {chain.name for chain in config.host_zones} == set(self.host_chain_names)
        assert {chain.name for chain in config.app_chains} == set(self.app_chain_names)

    def test_parse_config_missing_stride(self):
        """
        Tests that parsing a config without stride will fail
        """
        # Create a copy of the valid dict, and remove stride
        raw_config = copy.deepcopy(self.raw_config)
        del raw_config["stride"]

        # Confirm parsing fails
        with pytest.raises(KeyError, match="stride"):
            _parse_raw_configs(raw_config, self.raw_secrets)

    def test_parse_config_extra_host_zone(self):
        """
        Tests that parsing a config with a host zone that's not defined in
        the strideutils version will succeed
        This is to to allow certain apps to stay on old strideutils version
        even if the config was updated to add more hosts
        """
        # Create a copy of the valid dict, add a new chain
        raw_config = copy.deepcopy(self.raw_config)
        raw_config["host_zones"]["new_host"] = {"name": "new_host", "id": "newhost-1"}

        # Confirm parsing succeeds
        config = _parse_raw_configs(raw_config, self.raw_secrets)

        # Attempt to access the new chain, it should fail
        with pytest.raises(AttributeError, match="'HostChainsConfig' object has no attribute 'new_host'"):
            config.host_zones.new_host

    def test_parse_config_missing_host_zone(self):
        """
        Tests that parsing a config that's missing a host zone will succeed,
        but an error will be thrown later if access is attempted
        """
        # Create a copy of the valid dict, and remove the hub
        raw_config = copy.deepcopy(self.raw_config)
        del raw_config["host_zones"]["cosmoshub"]

        # Confirm parsing succeeds
        config = _parse_raw_configs(raw_config, self.raw_secrets)

        # Attempt to grab the hub, it should fail
        # TODO: Improve error so that it says "cosmoshub" is not set instead of "name"
        with pytest.raises(AttributeError, match="environment variable 'name' is not set"):
            config.host_zones.cosmoshub.name

    def test_parse_config_extra_app_chain(self):
        """
        Tests that parsing a config with an app chain that's not defined in
        the strideutils version will succeed
        This is to to allow certain apps to stay on old strideutils version
        even if the config was updated to add more app chains
        """
        # Create a copy of the valid dict, add a new chain
        raw_config = copy.deepcopy(self.raw_config)
        raw_config["app_chains"]["new_app"] = {"name": "new_app", "id": "newapp-1"}

        # Confirm parsing succeeds
        config = _parse_raw_configs(raw_config, self.raw_secrets)

        # Attempt to access the new chain, it should fail
        with pytest.raises(AttributeError, match="'AppChainsConfig' object has no attribute 'new_app'"):
            config.app_chains.new_app

    def test_parse_config_missing_app_chain(self):
        """
        Tests that parsing a config without an app chain will succeed,
        but an error will be thrown later if access is attempted
        """
        # Create a copy of the valid dict, and remove the hub
        raw_config = copy.deepcopy(self.raw_config)
        del raw_config["app_chains"]["neutron"]

        # Confirm parsing succeeds
        config = _parse_raw_configs(raw_config, self.raw_secrets)

        # Attempt to grab the hub, it should fail
        # TODO: Improve error so that it says "neutron" is not set instead of "name"
        with pytest.raises(AttributeError, match="environment variable 'name' is not set"):
            config.app_chains.neutron.name

    def test_parse_config_extra_host_chain_field(self):
        """
        Tests that parsing a config with a host chain field that's not defined in
        the strideutils version will succeed
        This is to to allow certain apps to stay on old strideutils version
        even if the config was updated to add more app chains
        """
        # Create a copy of the valid dict, add a new chain
        raw_config = copy.deepcopy(self.raw_config)
        raw_config["host_zones"]["cosmoshub"] = {"name": "new_app", "id": "newapp-1", "new_field": "value1"}

        # Confirm parsing succeeds
        config = _parse_raw_configs(raw_config, self.raw_secrets)

        # Attempt to access the new field, it should fail
        with pytest.raises(AttributeError, match="'HostChainConfig' object has no attribute 'new_field'"):
            config.host_zones.cosmoshub.new_field

    def test_parse_config_extra_app_chain_field(self):
        """
        Tests that parsing a config with a app chain field that's not defined in
        the strideutils version will succeed
        This is to to allow certain apps to stay on old strideutils version
        even if the config was updated to add more app chains
        """
        # Create a copy of the valid dict, add a new chain
        raw_config = copy.deepcopy(self.raw_config)
        raw_config["app_chains"]["neutron"] = {"name": "new_app", "id": "newapp-1", "new_field": "value1"}

        # Confirm parsing succeeds
        config = _parse_raw_configs(raw_config, self.raw_secrets)

        # Attempt to access the new field, it should fail
        with pytest.raises(AttributeError, match="'ChainConfig' object has no attribute 'new_field'"):
            config.app_chains.neutron.new_field

    def test_get_chain(self):
        """
        Test the get_chain lookup
        """
        # Parse the default valid conifg
        config = _parse_raw_configs(self.raw_config, self.raw_secrets)

        # Test looking up a stride by name and id
        assert config.get_chain(name="stride").id == "stride-1"
        assert config.get_chain(id="stride-1").name == "stride"

        # Test looking up a host zone by name and id
        assert config.get_chain(name="osmosis").id == "osmosis-1"
        assert config.get_chain(id="osmosis-1").name == "osmosis"

        # Test looking up an app chain by name and id
        assert config.get_chain(name="neutron").id == "neutron-1"
        assert config.get_chain(id="neutron-1").name == "neutron"

        # Test looking up a chain that doesn't exist
        with pytest.raises(KeyError, match="environment variable 'non-existent' is not set"):
            config.get_chain(name="non-existent")

    def test_get_host_chain(self):
        """
        Tests looking up a host zone
        """
        # Parse the default valid conifg
        config = _parse_raw_configs(self.raw_config, self.raw_secrets)

        # Test looking up a host zone by name and id
        assert config.get_host_chain(name="osmosis").id == "osmosis-1"
        assert config.get_host_chain(id="osmosis-1").name == "osmosis"

        # Test looking up stride, it should fail
        with pytest.raises(AssertionError, match="chain stride is not a host zone"):
            config.get_host_chain(name="stride").id

        # Test looking up an app chain, it should fail
        with pytest.raises(AssertionError, match="chain neutron is not a host zone"):
            config.get_host_chain(name="neutron").id
