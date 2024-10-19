# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities
from . import outputs
from .. import solana as _solana
from .. import ssh as _ssh
from ._inputs import *

__all__ = ['SolanaArgs', 'Solana']

@pulumi.input_type
class SolanaArgs:
    def __init__(__self__, *,
                 connection: pulumi.Input['_ssh.ConnectionArgs'],
                 flags: pulumi.Input['_solana.GenesisFlagsArgs'],
                 primordial: pulumi.Input[Sequence[pulumi.Input['PrimorialEntryArgs']]]):
        """
        The set of arguments for constructing a Solana resource.
        """
        pulumi.set(__self__, "connection", connection)
        pulumi.set(__self__, "flags", flags)
        pulumi.set(__self__, "primordial", primordial)

    @property
    @pulumi.getter
    def connection(self) -> pulumi.Input['_ssh.ConnectionArgs']:
        return pulumi.get(self, "connection")

    @connection.setter
    def connection(self, value: pulumi.Input['_ssh.ConnectionArgs']):
        pulumi.set(self, "connection", value)

    @property
    @pulumi.getter
    def flags(self) -> pulumi.Input['_solana.GenesisFlagsArgs']:
        return pulumi.get(self, "flags")

    @flags.setter
    def flags(self, value: pulumi.Input['_solana.GenesisFlagsArgs']):
        pulumi.set(self, "flags", value)

    @property
    @pulumi.getter
    def primordial(self) -> pulumi.Input[Sequence[pulumi.Input['PrimorialEntryArgs']]]:
        return pulumi.get(self, "primordial")

    @primordial.setter
    def primordial(self, value: pulumi.Input[Sequence[pulumi.Input['PrimorialEntryArgs']]]):
        pulumi.set(self, "primordial", value)


class Solana(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connection: Optional[pulumi.Input[Union['_ssh.ConnectionArgs', '_ssh.ConnectionArgsDict']]] = None,
                 flags: Optional[pulumi.Input[Union['_solana.GenesisFlagsArgs', '_solana.GenesisFlagsArgsDict']]] = None,
                 primordial: Optional[pulumi.Input[Sequence[pulumi.Input[Union['PrimorialEntryArgs', 'PrimorialEntryArgsDict']]]]] = None,
                 __props__=None):
        """
        Create a Solana resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SolanaArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Solana resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param SolanaArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SolanaArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connection: Optional[pulumi.Input[Union['_ssh.ConnectionArgs', '_ssh.ConnectionArgsDict']]] = None,
                 flags: Optional[pulumi.Input[Union['_solana.GenesisFlagsArgs', '_solana.GenesisFlagsArgsDict']]] = None,
                 primordial: Optional[pulumi.Input[Sequence[pulumi.Input[Union['PrimorialEntryArgs', 'PrimorialEntryArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SolanaArgs.__new__(SolanaArgs)

            if connection is None and not opts.urn:
                raise TypeError("Missing required property 'connection'")
            __props__.__dict__["connection"] = connection
            if flags is None and not opts.urn:
                raise TypeError("Missing required property 'flags'")
            __props__.__dict__["flags"] = flags
            if primordial is None and not opts.urn:
                raise TypeError("Missing required property 'primordial'")
            __props__.__dict__["primordial"] = primordial
            __props__.__dict__["genesis_hash"] = None
        super(Solana, __self__).__init__(
            'svmkit:genesis:Solana',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Solana':
        """
        Get an existing Solana resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SolanaArgs.__new__(SolanaArgs)

        __props__.__dict__["connection"] = None
        __props__.__dict__["flags"] = None
        __props__.__dict__["genesis_hash"] = None
        __props__.__dict__["primordial"] = None
        return Solana(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def connection(self) -> pulumi.Output['_ssh.outputs.Connection']:
        return pulumi.get(self, "connection")

    @property
    @pulumi.getter
    def flags(self) -> pulumi.Output['_solana.outputs.GenesisFlags']:
        return pulumi.get(self, "flags")

    @property
    @pulumi.getter(name="genesisHash")
    def genesis_hash(self) -> pulumi.Output[str]:
        return pulumi.get(self, "genesis_hash")

    @property
    @pulumi.getter
    def primordial(self) -> pulumi.Output[Sequence['outputs.PrimorialEntry']]:
        return pulumi.get(self, "primordial")

