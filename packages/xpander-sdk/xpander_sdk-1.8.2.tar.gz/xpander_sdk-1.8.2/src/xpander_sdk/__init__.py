r'''
# xpander SDK Documentation

Welcome to the xpander SDK documentation.

This document will help you get started with using the SDK in various programming languages.

## Overview

xpander SDK is a tool designed to work seamlessly with the [app.xpander.ai](http://app.xpander.ai) platform. The xpander platform enables building AI Apps with reliable Agentic tools, allowing you to integrate advanced functionalities into your applications without worrying about the complexities of function calling and system integration. The platform provides Connectors that have been enriched and adjusted for tool calling, and it supports the creation of custom connectors for any target system, such as home-grown systems.

### Key Features of xpander platform

1. **AI Apps**: AI Apps act as the interface between xpander AI-ready connectors and your AI Agents or Conversational AI solutions. They allow for easy integration with pre-built or custom connectors.
2. **Connectors**: Pre-built integrations that facilitate communication between xpander AI Apps and third-party systems, including SaaS applications and home-grown systems. Custom connectors can be generated using OpenAPI Specs, Postman collections, or browsing session examples.
3. **AI App Builder**: A chat interface that lets you interact with your APIs by selecting connectors and operators, and then transform the chat into Agentic automation workflows.

## Quick Start Guides

Choose your preferred language to get started quickly:

<div style="display: flex; flex-wrap: wrap; gap: 20px;">
  <a href="https://docs.xpander.ai/reference/getting-started#pre-requisite"><img src="https://files.readme.io/f356d48-python.png" alt="Python" height="80"></a>
  <a href="https://docs.xpander.ai/reference/getting-started#pre-requisite"><img src="https://files.readme.io/bf25a52-node.png" alt="Node.js" height="80"></a>
  <a href="https://docs.xpander.ai/reference/getting-started#pre-requisite"><img src="https://files.readme.io/63217d9-c-sharp_dot_net.png" alt=".NET" height="80"></a>
  <a href="https://docs.xpander.ai/reference/getting-started#pre-requisite"><img src="https://files.readme.io/6426bc7-java.png" alt="Java" height="80"></a>
</div>

## Further Reading

For more detailed information, please refer to the following sections:

* [Xpander SDK Overview](docs/overview): Learn more about the features and capabilities of the Xpander SDK.
* [API Reference](docs/api-reference): Detailed documentation of the SDK's API endpoints and usage.
* [Guides](docs/guides): Step-by-step guides to help you implement specific functionalities.
* [Troubleshooting](docs/troubleshooting): Solutions to common issues and problems.

## Contributing

We welcome contributions! Please refer to our [Contributing Guide](docs/contributing) for more information on how to get involved. Whether you want to report a bug, suggest a new feature, or contribute code, your help is greatly appreciated.

## License

This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE) file for details.

## Contact

For further questions or support, please contact us at [opensource@xpander.ai](mailto:opensource@xpander.ai).

## What's Next?

After finishing this page, explore the Quick Start Guides for your preferred programming language or delve into the API Reference for a comprehensive understanding of the SDK's capabilities. Happy coding with Xpander SDK!
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

import typeguard
from importlib.metadata import version as _metadata_package_version
TYPEGUARD_MAJOR_VERSION = int(_metadata_package_version('typeguard').split('.')[0])

def check_type(argname: str, value: object, expected_type: typing.Any) -> typing.Any:
    if TYPEGUARD_MAJOR_VERSION <= 2:
        return typeguard.check_type(argname=argname, value=value, expected_type=expected_type) # type:ignore
    else:
        if isinstance(value, jsii._reference_map.InterfaceDynamicProxy): # pyright: ignore [reportAttributeAccessIssue]
           pass
        else:
            if TYPEGUARD_MAJOR_VERSION == 3:
                typeguard.config.collection_check_strategy = typeguard.CollectionCheckStrategy.ALL_ITEMS # type:ignore
                typeguard.check_type(value=value, expected_type=expected_type) # type:ignore
            else:
                typeguard.check_type(value=value, expected_type=expected_type, collection_check_strategy=typeguard.CollectionCheckStrategy.ALL_ITEMS) # type:ignore

from ._jsii import *


class AmazonBedrockSupportedModels(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="xpander-sdk.AmazonBedrockSupportedModels",
):
    '''
    :class: AmazonBedrockSupportedModels
    :description: A class containing constants representing various supported models in Amazon Bedrock.
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.python.classproperty
    @jsii.member(jsii_name="ANTHROPIC_CLAUDE_3_5_SONNET_20240620")
    def ANTHROPIC_CLAUDE_3_5_SONNET_20240620(cls) -> builtins.str:
        '''
        :constant: true
        :description: Anthropocene Claude 3.5 Sonnet model with a version date of 2024-06-20.
        :type: {string}
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ANTHROPIC_CLAUDE_3_5_SONNET_20240620"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ANTHROPIC_CLAUDE_3_HAIKU_20240307")
    def ANTHROPIC_CLAUDE_3_HAIKU_20240307(cls) -> builtins.str:
        '''
        :constant: true
        :description: Anthropocene Claude 3 Haiku model with a version date of 2024-03-07.
        :type: {string}
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ANTHROPIC_CLAUDE_3_HAIKU_20240307"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="COHERE_COMMAND_R")
    def COHERE_COMMAND_R(cls) -> builtins.str:
        '''
        :constant: true
        :description: Cohere Command R model.
        :type: {string}
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "COHERE_COMMAND_R"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="COHERE_COMMAND_R_PLUS")
    def COHERE_COMMAND_R_PLUS(cls) -> builtins.str:
        '''
        :constant: true
        :description: Cohere Command R Plus model.
        :type: {string}
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "COHERE_COMMAND_R_PLUS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="META_LLAMA3_1_405B_INSTRUCT")
    def META_LLAMA3_1_405_B_INSTRUCT(cls) -> builtins.str:
        '''
        :constant: true
        :description: Meta Llama 3 1.405B Instruct model.
        :type: {string}
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "META_LLAMA3_1_405B_INSTRUCT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="META_LLAMA3_1_70B_INSTRUCT")
    def META_LLAMA3_1_70_B_INSTRUCT(cls) -> builtins.str:
        '''
        :constant: true
        :description: Meta Llama 3 1.70B Instruct model.
        :type: {string}
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "META_LLAMA3_1_70B_INSTRUCT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="META_LLAMA3_1_8B_INSTRUCT")
    def META_LLAMA3_1_8_B_INSTRUCT(cls) -> builtins.str:
        '''
        :constant: true
        :description: Meta Llama 3 1.8B Instruct model.
        :type: {string}
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "META_LLAMA3_1_8B_INSTRUCT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="MISTRAL_MISTRAL_LARGE_2402")
    def MISTRAL_MISTRAL_LARGE_2402(cls) -> builtins.str:
        '''
        :constant: true
        :description: Mistral Large 2402 model.
        :type: {string}
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "MISTRAL_MISTRAL_LARGE_2402"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="MISTRAL_MISTRAL_LARGE_2407")
    def MISTRAL_MISTRAL_LARGE_2407(cls) -> builtins.str:
        '''
        :constant: true
        :description: Mistral Large 2407 model.
        :type: {string}
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "MISTRAL_MISTRAL_LARGE_2407"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="MISTRAL_MISTRAL_SMALL_2402")
    def MISTRAL_MISTRAL_SMALL_2402(cls) -> builtins.str:
        '''
        :constant: true
        :description: Mistral Small 2402 model.
        :type: {string}
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "MISTRAL_MISTRAL_SMALL_2402"))


class _AmazonBedrockSupportedModelsProxy(AmazonBedrockSupportedModels):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, AmazonBedrockSupportedModels).__jsii_proxy_class__ = lambda : _AmazonBedrockSupportedModelsProxy


@jsii.interface(jsii_type="xpander-sdk.IBedrockTool")
class IBedrockTool(typing_extensions.Protocol):
    '''Interface representing a Bedrock tool.'''

    @builtins.property
    @jsii.member(jsii_name="toolSpec")
    def tool_spec(self) -> "IBedrockToolSpec":
        '''The tool specification of the Bedrock tool.'''
        ...

    @tool_spec.setter
    def tool_spec(self, value: "IBedrockToolSpec") -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="execute")
    def execute(self) -> typing.Any:
        '''Function to execute the Bedrock tool.'''
        ...

    @execute.setter
    def execute(self, value: typing.Any) -> None:
        ...


class _IBedrockToolProxy:
    '''Interface representing a Bedrock tool.'''

    __jsii_type__: typing.ClassVar[str] = "xpander-sdk.IBedrockTool"

    @builtins.property
    @jsii.member(jsii_name="toolSpec")
    def tool_spec(self) -> "IBedrockToolSpec":
        '''The tool specification of the Bedrock tool.'''
        return typing.cast("IBedrockToolSpec", jsii.get(self, "toolSpec"))

    @tool_spec.setter
    def tool_spec(self, value: "IBedrockToolSpec") -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__686bee2f9cc4cb8e5e46bd20309c912c48752fa01feec49d211288fe414d9879)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "toolSpec", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="execute")
    def execute(self) -> typing.Any:
        '''Function to execute the Bedrock tool.'''
        return typing.cast(typing.Any, jsii.get(self, "execute"))

    @execute.setter
    def execute(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50442d45bad8e7fa927b6be3feac263e79712091c62056e831a391b5a17c13bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "execute", value) # pyright: ignore[reportArgumentType]

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBedrockTool).__jsii_proxy_class__ = lambda : _IBedrockToolProxy


@jsii.interface(jsii_type="xpander-sdk.IBedrockToolOutput")
class IBedrockToolOutput(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="toolSpec")
    def tool_spec(self) -> "IBedrockToolSpec":
        '''The tool specification of the Bedrock tool.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="execute")
    def execute(self) -> typing.Any:
        '''Function to execute the Bedrock tool.'''
        ...


class _IBedrockToolOutputProxy:
    __jsii_type__: typing.ClassVar[str] = "xpander-sdk.IBedrockToolOutput"

    @builtins.property
    @jsii.member(jsii_name="toolSpec")
    def tool_spec(self) -> "IBedrockToolSpec":
        '''The tool specification of the Bedrock tool.'''
        return typing.cast("IBedrockToolSpec", jsii.get(self, "toolSpec"))

    @builtins.property
    @jsii.member(jsii_name="execute")
    def execute(self) -> typing.Any:
        '''Function to execute the Bedrock tool.'''
        return typing.cast(typing.Any, jsii.get(self, "execute"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBedrockToolOutput).__jsii_proxy_class__ = lambda : _IBedrockToolOutputProxy


@jsii.interface(jsii_type="xpander-sdk.IBedrockToolSpec")
class IBedrockToolSpec(typing_extensions.Protocol):
    '''Interface representing a Bedrock tool specification.'''

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''The description of the Bedrock tool.'''
        ...

    @description.setter
    def description(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="inputSchema")
    def input_schema(self) -> "IBedrockToolSpecInputSchema":
        '''Input schema of the Bedrock tool.'''
        ...

    @input_schema.setter
    def input_schema(self, value: "IBedrockToolSpecInputSchema") -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the Bedrock tool.'''
        ...

    @name.setter
    def name(self, value: builtins.str) -> None:
        ...


class _IBedrockToolSpecProxy:
    '''Interface representing a Bedrock tool specification.'''

    __jsii_type__: typing.ClassVar[str] = "xpander-sdk.IBedrockToolSpec"

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''The description of the Bedrock tool.'''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bab15f7ad29e9cbdf37869d4d12b1eca4937a0130eb1409bb74f1149d0dfc26b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="inputSchema")
    def input_schema(self) -> "IBedrockToolSpecInputSchema":
        '''Input schema of the Bedrock tool.'''
        return typing.cast("IBedrockToolSpecInputSchema", jsii.get(self, "inputSchema"))

    @input_schema.setter
    def input_schema(self, value: "IBedrockToolSpecInputSchema") -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39dfbf6fa195f65cf55b428cbf9c7e700af738bcd9c47ebdda318cfedf78e70a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputSchema", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the Bedrock tool.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0534d2b1daae9caffc87b99f4b6cc09e1a9eac3888374c04e9c619375c2f1b35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBedrockToolSpec).__jsii_proxy_class__ = lambda : _IBedrockToolSpecProxy


@jsii.interface(jsii_type="xpander-sdk.IBedrockToolSpecInputSchema")
class IBedrockToolSpecInputSchema(typing_extensions.Protocol):
    '''Interface representing the input schema for a Bedrock tool specification.'''

    @builtins.property
    @jsii.member(jsii_name="json")
    def json(self) -> typing.Mapping[builtins.str, "IToolParameter"]:
        '''JSON schema of the tool parameters.'''
        ...

    @json.setter
    def json(self, value: typing.Mapping[builtins.str, "IToolParameter"]) -> None:
        ...


class _IBedrockToolSpecInputSchemaProxy:
    '''Interface representing the input schema for a Bedrock tool specification.'''

    __jsii_type__: typing.ClassVar[str] = "xpander-sdk.IBedrockToolSpecInputSchema"

    @builtins.property
    @jsii.member(jsii_name="json")
    def json(self) -> typing.Mapping[builtins.str, "IToolParameter"]:
        '''JSON schema of the tool parameters.'''
        return typing.cast(typing.Mapping[builtins.str, "IToolParameter"], jsii.get(self, "json"))

    @json.setter
    def json(self, value: typing.Mapping[builtins.str, "IToolParameter"]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1454322c6f1b39bdf36a5d88226526fce2d55d1e13ada58cf00d44f12fd64366)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "json", value) # pyright: ignore[reportArgumentType]

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBedrockToolSpecInputSchema).__jsii_proxy_class__ = lambda : _IBedrockToolSpecInputSchemaProxy


@jsii.interface(jsii_type="xpander-sdk.IConnector")
class IConnector(typing_extensions.Protocol):
    '''Interface representing a connector.'''

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''Unique connector ID.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="operationIds")
    def operation_ids(self) -> typing.List[builtins.str]:
        '''List of operation IDs for the connector.'''
        ...


class _IConnectorProxy:
    '''Interface representing a connector.'''

    __jsii_type__: typing.ClassVar[str] = "xpander-sdk.IConnector"

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''Unique connector ID.'''
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="operationIds")
    def operation_ids(self) -> typing.List[builtins.str]:
        '''List of operation IDs for the connector.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "operationIds"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConnector).__jsii_proxy_class__ = lambda : _IConnectorProxy


@jsii.interface(jsii_type="xpander-sdk.ICustomParams")
class ICustomParams(typing_extensions.Protocol):
    '''Interface representing custom parameters.'''

    @builtins.property
    @jsii.member(jsii_name="connectors")
    def connectors(self) -> typing.List[IConnector]:
        '''List of connectors associated with the organization.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="organizationId")
    def organization_id(self) -> builtins.str:
        '''Organization ID associated with the custom.'''
        ...


class _ICustomParamsProxy:
    '''Interface representing custom parameters.'''

    __jsii_type__: typing.ClassVar[str] = "xpander-sdk.ICustomParams"

    @builtins.property
    @jsii.member(jsii_name="connectors")
    def connectors(self) -> typing.List[IConnector]:
        '''List of connectors associated with the organization.'''
        return typing.cast(typing.List[IConnector], jsii.get(self, "connectors"))

    @builtins.property
    @jsii.member(jsii_name="organizationId")
    def organization_id(self) -> builtins.str:
        '''Organization ID associated with the custom.'''
        return typing.cast(builtins.str, jsii.get(self, "organizationId"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICustomParams).__jsii_proxy_class__ = lambda : _ICustomParamsProxy


@jsii.interface(jsii_type="xpander-sdk.IGraph")
class IGraph(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="allowAllOperations")
    def allow_all_operations(self) -> builtins.bool:
        ...

    @allow_all_operations.setter
    def allow_all_operations(self, value: builtins.bool) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="graphs")
    def graphs(self) -> typing.List["IGraphItem"]:
        ...

    @graphs.setter
    def graphs(self, value: typing.List["IGraphItem"]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="organizationId")
    def organization_id(self) -> builtins.bool:
        ...

    @organization_id.setter
    def organization_id(self, value: builtins.bool) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="pgSwitchAllowed")
    def pg_switch_allowed(self) -> builtins.bool:
        ...

    @pg_switch_allowed.setter
    def pg_switch_allowed(self, value: builtins.bool) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="spec")
    def spec(self) -> typing.Any:
        ...

    @spec.setter
    def spec(self, value: typing.Any) -> None:
        ...


class _IGraphProxy:
    __jsii_type__: typing.ClassVar[str] = "xpander-sdk.IGraph"

    @builtins.property
    @jsii.member(jsii_name="allowAllOperations")
    def allow_all_operations(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "allowAllOperations"))

    @allow_all_operations.setter
    def allow_all_operations(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__749dc09e74837091b743b20b44a7b3d650b22053af60f7190f6967162b0ce86a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowAllOperations", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="graphs")
    def graphs(self) -> typing.List["IGraphItem"]:
        return typing.cast(typing.List["IGraphItem"], jsii.get(self, "graphs"))

    @graphs.setter
    def graphs(self, value: typing.List["IGraphItem"]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__716ced89905278f67f812ac3e2a90a587568bbaaad3f65e614e638500f0a8879)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "graphs", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="organizationId")
    def organization_id(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "organizationId"))

    @organization_id.setter
    def organization_id(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f8b6a560e7ca3dd7becbfdd776fa40b4c1a0421caf2d7e32cf7d3b20237db27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="pgSwitchAllowed")
    def pg_switch_allowed(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "pgSwitchAllowed"))

    @pg_switch_allowed.setter
    def pg_switch_allowed(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc94fcdd7c82d34b33d4fef5adb26a8b703ba811f07b94c755cecfd7ccf827f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pgSwitchAllowed", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="spec")
    def spec(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "spec"))

    @spec.setter
    def spec(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f9e512f5abf3ed78aa692496e890765157ef21fe2ca4e70e7c65491156ba438)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spec", value) # pyright: ignore[reportArgumentType]

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGraph).__jsii_proxy_class__ = lambda : _IGraphProxy


@jsii.interface(jsii_type="xpander-sdk.IGraphItem")
class IGraphItem(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="enrichedPrompts")
    def enriched_prompts(self) -> typing.List[builtins.str]:
        ...

    @enriched_prompts.setter
    def enriched_prompts(self, value: typing.List[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="graph")
    def graph(self) -> typing.Mapping[builtins.str, typing.List[builtins.str]]:
        ...

    @graph.setter
    def graph(
        self,
        value: typing.Mapping[builtins.str, typing.List[builtins.str]],
    ) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="prompts")
    def prompts(self) -> typing.List[builtins.str]:
        ...

    @prompts.setter
    def prompts(self, value: typing.List[builtins.str]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="startingNode")
    def starting_node(self) -> builtins.str:
        ...

    @starting_node.setter
    def starting_node(self, value: builtins.str) -> None:
        ...


class _IGraphItemProxy:
    __jsii_type__: typing.ClassVar[str] = "xpander-sdk.IGraphItem"

    @builtins.property
    @jsii.member(jsii_name="enrichedPrompts")
    def enriched_prompts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "enrichedPrompts"))

    @enriched_prompts.setter
    def enriched_prompts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63dac3f67c0f52d800dcd097be9ddb6eb98f70c71ea8289dbaad0e94a58d47f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enrichedPrompts", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="graph")
    def graph(self) -> typing.Mapping[builtins.str, typing.List[builtins.str]]:
        return typing.cast(typing.Mapping[builtins.str, typing.List[builtins.str]], jsii.get(self, "graph"))

    @graph.setter
    def graph(
        self,
        value: typing.Mapping[builtins.str, typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53cbdb3cb6871f560d5a0a78bd2ceff7528297ba8da6e71aa3da216d1c0284f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "graph", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="prompts")
    def prompts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "prompts"))

    @prompts.setter
    def prompts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42a9c3fc5cff09316502fc55db2175287af1ef6831a515963059bd6de019711a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prompts", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="startingNode")
    def starting_node(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startingNode"))

    @starting_node.setter
    def starting_node(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57c77329d9ea483c6111ccb444f6e30c3a08d7baf27c81a55cc015bb38ed9369)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startingNode", value) # pyright: ignore[reportArgumentType]

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGraphItem).__jsii_proxy_class__ = lambda : _IGraphItemProxy


@jsii.interface(jsii_type="xpander-sdk.IGraphSession")
class IGraphSession(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="previousNode")
    def previous_node(self) -> builtins.str:
        ...

    @previous_node.setter
    def previous_node(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="prompt")
    def prompt(self) -> builtins.str:
        ...

    @prompt.setter
    def prompt(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="promptGroup")
    def prompt_group(self) -> typing.Any:
        ...

    @prompt_group.setter
    def prompt_group(self, value: typing.Any) -> None:
        ...


class _IGraphSessionProxy:
    __jsii_type__: typing.ClassVar[str] = "xpander-sdk.IGraphSession"

    @builtins.property
    @jsii.member(jsii_name="previousNode")
    def previous_node(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "previousNode"))

    @previous_node.setter
    def previous_node(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__436460a38c0c401a5ac0cc40ee38a8569b50fcd9c0d74756e93fc405e57b4999)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "previousNode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="prompt")
    def prompt(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prompt"))

    @prompt.setter
    def prompt(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80f4ac1b21803bf084bc5d3fa5ecbc38ccdbf3c98eda8c5f9b373c3c454a9986)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prompt", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="promptGroup")
    def prompt_group(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "promptGroup"))

    @prompt_group.setter
    def prompt_group(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae86dd288186a83788bd74bbe23efbaf93b927d68170d1c441873dafce300f31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "promptGroup", value) # pyright: ignore[reportArgumentType]

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGraphSession).__jsii_proxy_class__ = lambda : _IGraphSessionProxy


@jsii.interface(jsii_type="xpander-sdk.ILLMProviderHandler")
class ILLMProviderHandler(typing_extensions.Protocol):
    '''Interface representing a LLM (Large Language Model) provider handler.'''

    @builtins.property
    @jsii.member(jsii_name="toolsNamesMapping")
    def tools_names_mapping(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Mapping of tool names.'''
        ...

    @tools_names_mapping.setter
    def tools_names_mapping(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        ...

    @jsii.member(jsii_name="getTools")
    def get_tools(
        self,
        functionize: typing.Optional[builtins.bool] = None,
    ) -> typing.List[typing.Any]:
        '''Retrieves tools.

        :param functionize: - Whether to functionize the tools.

        :return: Array of tools.
        '''
        ...

    @jsii.member(jsii_name="invokeTools")
    def invoke_tools(self, tool_selector_response: typing.Any) -> typing.Any:
        '''Invokes tools based on the tool selector response.

        :param tool_selector_response: - The response from the tool selector.

        :return: Result of the invoked tools.
        '''
        ...

    @jsii.member(jsii_name="singleToolInvoke")
    def single_tool_invoke(
        self,
        tool_id: builtins.str,
        payload: typing.Any,
    ) -> builtins.str:
        '''Invokes a single tool with the provided payload.

        :param tool_id: - The ID of the tool to invoke.
        :param payload: - The payload to send to the tool.

        :return: Result of the invoked tool as a string.
        '''
        ...


class _ILLMProviderHandlerProxy:
    '''Interface representing a LLM (Large Language Model) provider handler.'''

    __jsii_type__: typing.ClassVar[str] = "xpander-sdk.ILLMProviderHandler"

    @builtins.property
    @jsii.member(jsii_name="toolsNamesMapping")
    def tools_names_mapping(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Mapping of tool names.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "toolsNamesMapping"))

    @tools_names_mapping.setter
    def tools_names_mapping(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2abb4fa17493a619c62da93fd4891ab5d776cbbf34890a94704d9ab98af249d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "toolsNamesMapping", value) # pyright: ignore[reportArgumentType]

    @jsii.member(jsii_name="getTools")
    def get_tools(
        self,
        functionize: typing.Optional[builtins.bool] = None,
    ) -> typing.List[typing.Any]:
        '''Retrieves tools.

        :param functionize: - Whether to functionize the tools.

        :return: Array of tools.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e990337f22ef47b5f40d9401058956b9c4bea64a9bafe926858ea6869074251)
            check_type(argname="argument functionize", value=functionize, expected_type=type_hints["functionize"])
        return typing.cast(typing.List[typing.Any], jsii.invoke(self, "getTools", [functionize]))

    @jsii.member(jsii_name="invokeTools")
    def invoke_tools(self, tool_selector_response: typing.Any) -> typing.Any:
        '''Invokes tools based on the tool selector response.

        :param tool_selector_response: - The response from the tool selector.

        :return: Result of the invoked tools.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6eabf11d97b19da7ed9046ad2b6f0a43749a3b5d1cf7fa11d5ec2390b04bffc9)
            check_type(argname="argument tool_selector_response", value=tool_selector_response, expected_type=type_hints["tool_selector_response"])
        return typing.cast(typing.Any, jsii.invoke(self, "invokeTools", [tool_selector_response]))

    @jsii.member(jsii_name="singleToolInvoke")
    def single_tool_invoke(
        self,
        tool_id: builtins.str,
        payload: typing.Any,
    ) -> builtins.str:
        '''Invokes a single tool with the provided payload.

        :param tool_id: - The ID of the tool to invoke.
        :param payload: - The payload to send to the tool.

        :return: Result of the invoked tool as a string.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae6f34e8c01f6a6c9c281834bc9bf889895f559d21de59a7b05271a82ba77196)
            check_type(argname="argument tool_id", value=tool_id, expected_type=type_hints["tool_id"])
            check_type(argname="argument payload", value=payload, expected_type=type_hints["payload"])
        return typing.cast(builtins.str, jsii.invoke(self, "singleToolInvoke", [tool_id, payload]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILLMProviderHandler).__jsii_proxy_class__ = lambda : _ILLMProviderHandlerProxy


@jsii.interface(jsii_type="xpander-sdk.ILocalTool")
class ILocalTool(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="function")
    def function(self) -> "ILocalToolFunction":
        ...

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        ...


class _ILocalToolProxy:
    __jsii_type__: typing.ClassVar[str] = "xpander-sdk.ILocalTool"

    @builtins.property
    @jsii.member(jsii_name="function")
    def function(self) -> "ILocalToolFunction":
        return typing.cast("ILocalToolFunction", jsii.get(self, "function"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILocalTool).__jsii_proxy_class__ = lambda : _ILocalToolProxy


@jsii.interface(jsii_type="xpander-sdk.ILocalToolFunction")
class ILocalToolFunction(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        ...

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        ...

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Any:
        ...


class _ILocalToolFunctionProxy:
    __jsii_type__: typing.ClassVar[str] = "xpander-sdk.ILocalToolFunction"

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "parameters"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILocalToolFunction).__jsii_proxy_class__ = lambda : _ILocalToolFunctionProxy


@jsii.interface(jsii_type="xpander-sdk.IMessage")
class IMessage(typing_extensions.Protocol):
    '''Interface representing a message.'''

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        '''The content of the message.'''
        ...

    @content.setter
    def content(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        '''The role of the message sender.'''
        ...

    @role.setter
    def role(self, value: builtins.str) -> None:
        ...


class _IMessageProxy:
    '''Interface representing a message.'''

    __jsii_type__: typing.ClassVar[str] = "xpander-sdk.IMessage"

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        '''The content of the message.'''
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afcc8b3292657cf39d4883d2f4c5f804a04f2bf61a3a6d58fc200181f1613b2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        '''The role of the message sender.'''
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ceabb1f28442b22fad8c23d587d18b3058d760f8679016135ab59fdde96b125)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value) # pyright: ignore[reportArgumentType]

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMessage).__jsii_proxy_class__ = lambda : _IMessageProxy


@jsii.interface(jsii_type="xpander-sdk.IOpenAIToolFunctionOutput")
class IOpenAIToolFunctionOutput(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''The description of the tool.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the tool.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="execute")
    def execute(self) -> typing.Any:
        '''Function to execute the Bedrock tool.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="func")
    def func(self) -> typing.Any:
        '''Function to execute the tool.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Optional["IToolParameter"]:
        '''Parameters of the tool.'''
        ...


class _IOpenAIToolFunctionOutputProxy:
    __jsii_type__: typing.ClassVar[str] = "xpander-sdk.IOpenAIToolFunctionOutput"

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''The description of the tool.'''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the tool.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="execute")
    def execute(self) -> typing.Any:
        '''Function to execute the Bedrock tool.'''
        return typing.cast(typing.Any, jsii.get(self, "execute"))

    @builtins.property
    @jsii.member(jsii_name="func")
    def func(self) -> typing.Any:
        '''Function to execute the tool.'''
        return typing.cast(typing.Any, jsii.get(self, "func"))

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Optional["IToolParameter"]:
        '''Parameters of the tool.'''
        return typing.cast(typing.Optional["IToolParameter"], jsii.get(self, "parameters"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOpenAIToolFunctionOutput).__jsii_proxy_class__ = lambda : _IOpenAIToolFunctionOutputProxy


@jsii.interface(jsii_type="xpander-sdk.IOpenAIToolOutput")
class IOpenAIToolOutput(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="function")
    def function(self) -> IOpenAIToolFunctionOutput:
        ...

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        ...


class _IOpenAIToolOutputProxy:
    __jsii_type__: typing.ClassVar[str] = "xpander-sdk.IOpenAIToolOutput"

    @builtins.property
    @jsii.member(jsii_name="function")
    def function(self) -> IOpenAIToolFunctionOutput:
        return typing.cast(IOpenAIToolFunctionOutput, jsii.get(self, "function"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOpenAIToolOutput).__jsii_proxy_class__ = lambda : _IOpenAIToolOutputProxy


@jsii.interface(jsii_type="xpander-sdk.ITool")
class ITool(typing_extensions.Protocol):
    '''Interface representing a tool.'''

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''The description of the tool.'''
        ...

    @description.setter
    def description(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the tool.'''
        ...

    @name.setter
    def name(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="func")
    def func(self) -> typing.Any:
        '''Function to execute the tool.'''
        ...

    @func.setter
    def func(self, value: typing.Any) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, "IToolParameter"]]:
        '''Parameters of the tool.'''
        ...

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, "IToolParameter"]],
    ) -> None:
        ...


class _IToolProxy:
    '''Interface representing a tool.'''

    __jsii_type__: typing.ClassVar[str] = "xpander-sdk.ITool"

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''The description of the tool.'''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f56ea2b548b4cdfe22f0f80bf2c3f88697c04aedd2bf7fe61755b4eb9cee55b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the tool.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5396ff1ffb06161e7b92840a35a663b1f418ffdcc7dde0e2593addf6ca31936a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="func")
    def func(self) -> typing.Any:
        '''Function to execute the tool.'''
        return typing.cast(typing.Any, jsii.get(self, "func"))

    @func.setter
    def func(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__682720a04a90eb0d29239c0baf8e36b53b239f76f1079edf9cd418a69ddb97ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "func", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, "IToolParameter"]]:
        '''Parameters of the tool.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, "IToolParameter"]], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, "IToolParameter"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bf23d7676e5d1c7e307b10d99651d3e323b4741175a001eec3d04daa9f6a063)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value) # pyright: ignore[reportArgumentType]

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITool).__jsii_proxy_class__ = lambda : _IToolProxy


@jsii.interface(jsii_type="xpander-sdk.IToolParameter")
class IToolParameter(typing_extensions.Protocol):
    '''Interface representing a tool parameter.'''

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, "IToolParameter"]:
        '''Properties of the parameter.'''
        ...

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, "IToolParameter"]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of the parameter.'''
        ...

    @type.setter
    def type(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="required")
    def required(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of required properties.'''
        ...

    @required.setter
    def required(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        ...


class _IToolParameterProxy:
    '''Interface representing a tool parameter.'''

    __jsii_type__: typing.ClassVar[str] = "xpander-sdk.IToolParameter"

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, IToolParameter]:
        '''Properties of the parameter.'''
        return typing.cast(typing.Mapping[builtins.str, IToolParameter], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, IToolParameter]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__187dae4a63a6fee1ee6e1cb395b2f91742bd245c20c13ab04570590726c5ef61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of the parameter.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16039ce6185f742cd5865e412fc0342905a7a6d458331abeea0c8aea52fd0eb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="required")
    def required(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of required properties.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "required"))

    @required.setter
    def required(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52b13164b7161ac045d14f7c4212e2fc304cf9b4c0234c2221c11807a860fee0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "required", value) # pyright: ignore[reportArgumentType]

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IToolParameter).__jsii_proxy_class__ = lambda : _IToolParameterProxy


@jsii.interface(jsii_type="xpander-sdk.IToolResponse")
class IToolResponse(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="filteredTool")
    def filtered_tool(self) -> typing.Mapping[typing.Any, typing.Any]:
        '''The filtered tool object.'''
        ...

    @filtered_tool.setter
    def filtered_tool(self, value: typing.Mapping[typing.Any, typing.Any]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the tool.'''
        ...

    @name.setter
    def name(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="payloadRequest")
    def payload_request(self) -> builtins.str:
        '''The request payload that sent to tool.'''
        ...

    @payload_request.setter
    def payload_request(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="responseMessage")
    def response_message(self) -> builtins.str:
        '''The response message from the tool.'''
        ...

    @response_message.setter
    def response_message(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        '''The role in the response.'''
        ...

    @role.setter
    def role(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="toolCallId")
    def tool_call_id(self) -> builtins.str:
        '''The ID of the tool call.'''
        ...

    @tool_call_id.setter
    def tool_call_id(self, value: builtins.str) -> None:
        ...


class _IToolResponseProxy:
    __jsii_type__: typing.ClassVar[str] = "xpander-sdk.IToolResponse"

    @builtins.property
    @jsii.member(jsii_name="filteredTool")
    def filtered_tool(self) -> typing.Mapping[typing.Any, typing.Any]:
        '''The filtered tool object.'''
        return typing.cast(typing.Mapping[typing.Any, typing.Any], jsii.get(self, "filteredTool"))

    @filtered_tool.setter
    def filtered_tool(self, value: typing.Mapping[typing.Any, typing.Any]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f73e164c6a44a3b3baeb4c0db588226328547869f802218d70a1011b2423f20e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filteredTool", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the tool.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bef146974c73640980b42683bcc6c7c6fd3e99ce00416797a28824e24ed245b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="payloadRequest")
    def payload_request(self) -> builtins.str:
        '''The request payload that sent to tool.'''
        return typing.cast(builtins.str, jsii.get(self, "payloadRequest"))

    @payload_request.setter
    def payload_request(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__480f8c3a9fe5cce1c76c047e7c85449f3f3b18ac119d429c16fcd668dd9bffa9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "payloadRequest", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="responseMessage")
    def response_message(self) -> builtins.str:
        '''The response message from the tool.'''
        return typing.cast(builtins.str, jsii.get(self, "responseMessage"))

    @response_message.setter
    def response_message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73d18f79c4026ba80502b29d7d377fbe641a12167e31a95dedf72905d238ad06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseMessage", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        '''The role in the response.'''
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f62f1d504eb1a32375eaa547166df13aaedae86863a17762624dad92eac5771)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="toolCallId")
    def tool_call_id(self) -> builtins.str:
        '''The ID of the tool call.'''
        return typing.cast(builtins.str, jsii.get(self, "toolCallId"))

    @tool_call_id.setter
    def tool_call_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4886f85be83c75284f4a0a609075d0f680402dee57ac924df12e39c6dc2a2620)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "toolCallId", value) # pyright: ignore[reportArgumentType]

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IToolResponse).__jsii_proxy_class__ = lambda : _IToolResponseProxy


@jsii.interface(jsii_type="xpander-sdk.IToolResponsePayload")
class IToolResponsePayload(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="property1")
    def property1(self) -> builtins.str:
        '''A string property for the tool response payload.'''
        ...

    @property1.setter
    def property1(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="property2")
    def property2(self) -> jsii.Number:
        '''A numeric property for the tool response payload.'''
        ...

    @property2.setter
    def property2(self, value: jsii.Number) -> None:
        ...


class _IToolResponsePayloadProxy:
    __jsii_type__: typing.ClassVar[str] = "xpander-sdk.IToolResponsePayload"

    @builtins.property
    @jsii.member(jsii_name="property1")
    def property1(self) -> builtins.str:
        '''A string property for the tool response payload.'''
        return typing.cast(builtins.str, jsii.get(self, "property1"))

    @property1.setter
    def property1(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d1cc4753491f22ff1bb5d9814210da53bb4bb3a6fe4d73062b568a69f396d22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "property1", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="property2")
    def property2(self) -> jsii.Number:
        '''A numeric property for the tool response payload.'''
        return typing.cast(jsii.Number, jsii.get(self, "property2"))

    @property2.setter
    def property2(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__855e7764f28c37e54a5301b3a5ae59a5cf33e5b99b7ee9d8af609ec4cbabe816)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "property2", value) # pyright: ignore[reportArgumentType]

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IToolResponsePayload).__jsii_proxy_class__ = lambda : _IToolResponsePayloadProxy


@jsii.enum(jsii_type="xpander-sdk.LLMProvider")
class LLMProvider(enum.Enum):
    '''Enum representing different Large Language Model (LLM) providers.'''

    LANG_CHAIN = "LANG_CHAIN"
    '''Represents the 'langchain' provider.'''
    OPEN_AI = "OPEN_AI"
    '''Represents the 'openai' provider.'''
    NVIDIA_NIM = "NVIDIA_NIM"
    '''Represents the 'nvidiaNim' provider.'''
    AMAZON_BEDROCK = "AMAZON_BEDROCK"
    '''Represents the 'amazonBedrock' provider.'''


class NvidiaNIMSupportedModels(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="xpander-sdk.NvidiaNIMSupportedModels",
):
    '''
    :class: NvidiaNIMSupportedModels
    :description: A class containing constants representing various supported models in Nvidia NIM.
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.python.classproperty
    @jsii.member(jsii_name="LLAMA_3_1_70B_INSTRUCT")
    def LLAMA_3_1_70_B_INSTRUCT(cls) -> builtins.str:
        '''
        :constant: true
        :description: Meta Llama 3.1 70B Instruct model.
        :type: {string}
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "LLAMA_3_1_70B_INSTRUCT"))


class _NvidiaNIMSupportedModelsProxy(NvidiaNIMSupportedModels):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, NvidiaNIMSupportedModels).__jsii_proxy_class__ = lambda : _NvidiaNIMSupportedModelsProxy


class OpenAISupportedModels(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="xpander-sdk.OpenAISupportedModels",
):
    '''
    :class: OpenAISupportedModels
    :description: A class containing constants representing various supported models in OpenAI.
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.python.classproperty
    @jsii.member(jsii_name="GPT_4")
    def GPT_4(cls) -> builtins.str:
        '''
        :constant: true
        :description: OpenAI GPT-4 model.
        :type: {string}
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "GPT_4"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GPT_4_O")
    def GPT_4_O(cls) -> builtins.str:
        '''
        :constant: true
        :description: OpenAI GPT-4o model.
        :type: {string}
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "GPT_4_O"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GPT_4_O_MINI")
    def GPT_4_O_MINI(cls) -> builtins.str:
        '''
        :constant: true
        :description: OpenAI GPT-4o Mini model.
        :type: {string}
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "GPT_4_O_MINI"))


class _OpenAISupportedModelsProxy(OpenAISupportedModels):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, OpenAISupportedModels).__jsii_proxy_class__ = lambda : _OpenAISupportedModelsProxy


@jsii.implements(IToolResponse)
class ToolResponse(metaclass=jsii.JSIIMeta, jsii_type="xpander-sdk.ToolResponse"):
    def __init__(
        self,
        tool_call_id: builtins.str,
        role: builtins.str,
        name: builtins.str,
        response_message: builtins.str,
        filtered_tool: typing.Mapping[typing.Any, typing.Any],
        payload_request: builtins.str,
        local_tool: typing.Optional[typing.Union[IBedrockToolOutput, ILocalTool]] = None,
    ) -> None:
        '''Constructs a new ToolResponse instance.

        :param tool_call_id: - The ID of the tool call.
        :param role: - The role in the response.
        :param name: - The name of the tool.
        :param response_message: - The response message from the tool.
        :param filtered_tool: - The filtered tool object.
        :param payload_request: - The request payload that sent to tool.
        :param local_tool: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e85f84776414e75b23ca0d7ed7d4e074419a70de8997b3fa89b3e717ba2d16b)
            check_type(argname="argument tool_call_id", value=tool_call_id, expected_type=type_hints["tool_call_id"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument response_message", value=response_message, expected_type=type_hints["response_message"])
            check_type(argname="argument filtered_tool", value=filtered_tool, expected_type=type_hints["filtered_tool"])
            check_type(argname="argument payload_request", value=payload_request, expected_type=type_hints["payload_request"])
            check_type(argname="argument local_tool", value=local_tool, expected_type=type_hints["local_tool"])
        jsii.create(self.__class__, self, [tool_call_id, role, name, response_message, filtered_tool, payload_request, local_tool])

    @jsii.member(jsii_name="fromJSON")
    @builtins.classmethod
    def from_json(cls, json: typing.Any) -> "ToolResponse":
        '''Creates a ToolResponse instance from a JSON object.

        :param json: - The JSON object to create the instance from.

        :return: A new ToolResponse instance.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c59e939ed4cdb302e7adbd3d749f4a8fd632cdd13ed91e112788b1bc5ff9c94)
            check_type(argname="argument json", value=json, expected_type=type_hints["json"])
        return typing.cast("ToolResponse", jsii.sinvoke(cls, "fromJSON", [json]))

    @jsii.member(jsii_name="toJSON")
    def to_json(self) -> typing.Mapping[typing.Any, typing.Any]:
        '''Converts the ToolResponse instance to a JSON object.

        :return: A JSON representation of the ToolResponse instance.
        '''
        return typing.cast(typing.Mapping[typing.Any, typing.Any], jsii.invoke(self, "toJSON", []))

    @builtins.property
    @jsii.member(jsii_name="rawResponse")
    def raw_response(self) -> typing.Any:
        '''Gets the response message.

        :return: The response message.
        '''
        return typing.cast(typing.Any, jsii.get(self, "rawResponse"))

    @builtins.property
    @jsii.member(jsii_name="filteredTool")
    def filtered_tool(self) -> typing.Mapping[typing.Any, typing.Any]:
        '''The filtered tool object.'''
        return typing.cast(typing.Mapping[typing.Any, typing.Any], jsii.get(self, "filteredTool"))

    @filtered_tool.setter
    def filtered_tool(self, value: typing.Mapping[typing.Any, typing.Any]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1db45836b482186036af28282ce7a17e90a75b871f10d04414a6e1b162096be1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filteredTool", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the tool.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b47dd0917aa0042a7945f018986b595aafdc255b7d68dccdab7c7059cd806be2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="payloadRequest")
    def payload_request(self) -> builtins.str:
        '''The request payload that sent to tool.'''
        return typing.cast(builtins.str, jsii.get(self, "payloadRequest"))

    @payload_request.setter
    def payload_request(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49643ea0ff919e21e24a0644caba005ea086c83fa97ef4bcae54bc545248dfb3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "payloadRequest", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="responseMessage")
    def response_message(self) -> builtins.str:
        '''The response message from the tool.'''
        return typing.cast(builtins.str, jsii.get(self, "responseMessage"))

    @response_message.setter
    def response_message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de9a33fbf19475ac4ae43975d7e702211d1f6568a662fcddb481de787c1223d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseMessage", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        '''The role in the response.'''
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90f4115fd71d0ee18aaf8914fba42e770875ad5f03c5f8a6e9705ad62d5fbd3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="toolCallId")
    def tool_call_id(self) -> builtins.str:
        '''The ID of the tool call.'''
        return typing.cast(builtins.str, jsii.get(self, "toolCallId"))

    @tool_call_id.setter
    def tool_call_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72d95ac9191b5a3b6832a987b8a5261e3257588cd5f2e4c5cf0cc50be50059f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "toolCallId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="localTool")
    def local_tool(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "localTool"))

    @local_tool.setter
    def local_tool(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d5b3165d80d89d2b04b5e46c254e63da06e5858a40d39921ca98f3cc75fd9c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localTool", value) # pyright: ignore[reportArgumentType]


class XpanderClient(metaclass=jsii.JSIIMeta, jsii_type="xpander-sdk.XpanderClient"):
    '''Class representing the XpanderClient used to interact with xpanderAI tools.'''

    def __init__(
        self,
        agent_key: builtins.str,
        agent_url: builtins.str,
        llm_provider: LLMProvider,
        local_tools: typing.Optional[typing.Sequence[ILocalTool]] = None,
        tools: typing.Optional[typing.Union[typing.Sequence[typing.Any], typing.Sequence[IOpenAIToolOutput], typing.Sequence[IBedrockToolOutput]]] = None,
        custom_params: typing.Any = None,
    ) -> None:
        '''Constructs a new XpanderClient instance.

        :param agent_key: - The API key for the agent.
        :param agent_url: - The URL for the agent.
        :param llm_provider: - The LLM provider to use.
        :param local_tools: - Local tools to append into the tools list.
        :param tools: - Pass existing xpanderAI tools to the client instead of fetching.
        :param custom_params: - Optional custom parameters for enhanced context.

        :throws: Will throw an error if an invalid LLM provider is specified.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ada04f0df01e9b462e0b973aee5f69eda17ab0f22e7345f33423f0acca9ad36)
            check_type(argname="argument agent_key", value=agent_key, expected_type=type_hints["agent_key"])
            check_type(argname="argument agent_url", value=agent_url, expected_type=type_hints["agent_url"])
            check_type(argname="argument llm_provider", value=llm_provider, expected_type=type_hints["llm_provider"])
            check_type(argname="argument local_tools", value=local_tools, expected_type=type_hints["local_tools"])
            check_type(argname="argument tools", value=tools, expected_type=type_hints["tools"])
            check_type(argname="argument custom_params", value=custom_params, expected_type=type_hints["custom_params"])
        jsii.create(self.__class__, self, [agent_key, agent_url, llm_provider, local_tools, tools, custom_params])

    @jsii.member(jsii_name="addLocalTools")
    def add_local_tools(self, tools: typing.Sequence[ILocalTool]) -> None:
        '''Adds local tools to the client.

        :param tools: - Array of local tools to add.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4b1a48b122979793bac1655fd731a7c2e2b3cf3c645f438a6d486a90006820b)
            check_type(argname="argument tools", value=tools, expected_type=type_hints["tools"])
        return typing.cast(None, jsii.invoke(self, "addLocalTools", [tools]))

    @jsii.member(jsii_name="getGraphSessionParam")
    def get_graph_session_param(self, param: builtins.str) -> typing.Any:
        '''Gets a parameter in the current graph session.

        :param param: - The parameter to get, either 'previousNode' or 'prompt'.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5db91ce4f1a6c12048755ac88edd73655b66f8c589fd9d213b66d580ec7adc7)
            check_type(argname="argument param", value=param, expected_type=type_hints["param"])
        return typing.cast(typing.Any, jsii.invoke(self, "getGraphSessionParam", [param]))

    @jsii.member(jsii_name="getToolsForGraphsSession")
    def get_tools_for_graphs_session(
        self,
        tools: typing.Union[typing.Sequence[typing.Any], typing.Sequence[IOpenAIToolOutput], typing.Sequence[IBedrockToolOutput]],
    ) -> typing.Union[typing.List[typing.Any], typing.List[IOpenAIToolOutput], typing.List[IBedrockToolOutput]]:
        '''Retrieves the appropriate tools for the current graph session.

        :param tools: - Array of available tools.

        :return: A subset of tools based on the graph session and prompt group.

        :throws: {Error} If graphs are not loaded or the graph session is not initiated properly.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18f87c7417879c6d58ba1275f3c6dc3cbe6518ab8cc45a112608c2ba48d7890f)
            check_type(argname="argument tools", value=tools, expected_type=type_hints["tools"])
        return typing.cast(typing.Union[typing.List[typing.Any], typing.List[IOpenAIToolOutput], typing.List[IBedrockToolOutput]], jsii.invoke(self, "getToolsForGraphsSession", [tools]))

    @jsii.member(jsii_name="loadXpanderTools")
    def load_xpander_tools(self) -> typing.List[typing.Any]:
        '''Loads the tools available from the xpanderAI agent.

        :return: Array of tools.

        :throws: Will throw an error if the tools cannot be loaded.
        '''
        return typing.cast(typing.List[typing.Any], jsii.invoke(self, "loadXpanderTools", []))

    @jsii.member(jsii_name="setGraphSessionParam")
    def set_graph_session_param(self, param: builtins.str, value: typing.Any) -> None:
        '''Sets a parameter in the current graph session.

        :param param: - The parameter to set, either 'previousNode' or 'prompt'.
        :param value: - The value to assign to the specified parameter.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__533ca20d23cf744702ce059e14658b186611443cff0802973ffca1dd3c3cfc49)
            check_type(argname="argument param", value=param, expected_type=type_hints["param"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "setGraphSessionParam", [param, value]))

    @jsii.member(jsii_name="startSession")
    def start_session(self, prompt: typing.Optional[builtins.str] = None) -> None:
        '''Initializes a new graph session with the provided prompt.

        :param prompt: - The prompt to initialize the session with.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e2d2dde4e8be1794629154f5f5785efd317185e2b79dcff6e50ef0104c288e2)
            check_type(argname="argument prompt", value=prompt, expected_type=type_hints["prompt"])
        return typing.cast(None, jsii.invoke(self, "startSession", [prompt]))

    @jsii.member(jsii_name="tools")
    def tools(
        self,
        llm_provider: typing.Optional[LLMProvider] = None,
    ) -> typing.Union[typing.List[typing.Any], typing.List[IOpenAIToolOutput], typing.List[IBedrockToolOutput]]:
        '''Retrieves the tools for the current or specified LLM provider.

        :param llm_provider: (Optional) The LLM provider to use.

        :return: Array of tools.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f966ec87e3ece5fb630f8589d4ea9d99ed7fea000929df61b60531734c7ce278)
            check_type(argname="argument llm_provider", value=llm_provider, expected_type=type_hints["llm_provider"])
        return typing.cast(typing.Union[typing.List[typing.Any], typing.List[IOpenAIToolOutput], typing.List[IBedrockToolOutput]], jsii.invoke(self, "tools", [llm_provider]))

    @jsii.member(jsii_name="xpanderSingleToolInvoke")
    def xpander_single_tool_invoke(
        self,
        tool_id: builtins.str,
        payload: typing.Any = None,
    ) -> builtins.str:
        '''Invokes a single tool with the given tool ID and payload.

        :param tool_id: - The ID of the tool to invoke.
        :param payload: - The payload to pass to the tool.

        :return: The result of the tool invocation.

        :throws: Will throw an error if the tool implementation is not found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a22edb3e8b5b34cd3d6b792b223e3a6d2ff1c9a97db02d95432302d04135716f)
            check_type(argname="argument tool_id", value=tool_id, expected_type=type_hints["tool_id"])
            check_type(argname="argument payload", value=payload, expected_type=type_hints["payload"])
        return typing.cast(builtins.str, jsii.invoke(self, "xpanderSingleToolInvoke", [tool_id, payload]))

    @jsii.member(jsii_name="xpanderToolCall")
    def xpander_tool_call(
        self,
        tool_selector_response: typing.Any,
        llm_provider: typing.Optional[builtins.str] = None,
    ) -> typing.List[ToolResponse]:
        '''Invokes the tools based on the tool selector response.

        :param tool_selector_response: - The response from the tool selector.
        :param llm_provider: - (Optional) The LLM provider to use.

        :return: Array of tool responses.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__934787f3c0966796972c5e5bf4a28aca4d188aa70632ed29bc6401dc3383596d)
            check_type(argname="argument tool_selector_response", value=tool_selector_response, expected_type=type_hints["tool_selector_response"])
            check_type(argname="argument llm_provider", value=llm_provider, expected_type=type_hints["llm_provider"])
        return typing.cast(typing.List[ToolResponse], jsii.invoke(self, "xpanderToolCall", [tool_selector_response, llm_provider]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="validProviders")
    def valid_providers(cls) -> typing.List[builtins.str]:
        '''Provides a list of valid LLM providers.

        :return: Array of valid provider names.
        '''
        return typing.cast(typing.List[builtins.str], jsii.sget(cls, "validProviders"))

    @builtins.property
    @jsii.member(jsii_name="toolsNamesMapping")
    def tools_names_mapping(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Retrieves the tool names mapping for the current LLM provider.

        :return: A record of tool names mapping.
        '''
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "toolsNamesMapping"))

    @builtins.property
    @jsii.member(jsii_name="agentKey")
    def agent_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "agentKey"))

    @agent_key.setter
    def agent_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec1e4aa01d86350e4e2fa3a8d5fd0dd0b10573e0712e583aebf20df7c99904b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentKey", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="agentUrl")
    def agent_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "agentUrl"))

    @agent_url.setter
    def agent_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03c6a33ed2b1e15f73f6cd1ce2ef1b2c47f2516aff9583e0b468b87a95b92859)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentUrl", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="graphsCache")
    def graphs_cache(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "graphsCache"))

    @graphs_cache.setter
    def graphs_cache(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93d7882c050d951d58dd512563574491c355d278ba3db4b5be8f1e48ae90973c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "graphsCache", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="graphSession")
    def _graph_session(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "graphSession"))

    @_graph_session.setter
    def _graph_session(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43d62092cf9d0124286de42b5169d53613f78e50ea0b5177fa0f187cb31d41ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "graphSession", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="llmProviderHandler")
    def _llm_provider_handler(self) -> ILLMProviderHandler:
        return typing.cast(ILLMProviderHandler, jsii.get(self, "llmProviderHandler"))

    @_llm_provider_handler.setter
    def _llm_provider_handler(self, value: ILLMProviderHandler) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef50ccd539cda95bb415311cc7ddb6b2d6ffef3a7905c703e6d5bea60b5406d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "llmProviderHandler", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="localTools")
    def local_tools(self) -> typing.List[ILocalTool]:
        return typing.cast(typing.List[ILocalTool], jsii.get(self, "localTools"))

    @local_tools.setter
    def local_tools(self, value: typing.List[ILocalTool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89ac314921ee59851df3b7539810145482a18a068c13ebd4e4f4f9cf38d40e2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localTools", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="toolsCache")
    def tools_cache(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "toolsCache"))

    @tools_cache.setter
    def tools_cache(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4685c27686f93e903b9776fd808abb1991bcbc10198a9b97d66846fd79da67d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "toolsCache", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="toolsFromExternal")
    def tools_from_external(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "toolsFromExternal"))

    @tools_from_external.setter
    def tools_from_external(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c157c90274c35a97f6cc1e958c5d93f56b8921e11e66102068c645a4db91b7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "toolsFromExternal", value) # pyright: ignore[reportArgumentType]


__all__ = [
    "AmazonBedrockSupportedModels",
    "IBedrockTool",
    "IBedrockToolOutput",
    "IBedrockToolSpec",
    "IBedrockToolSpecInputSchema",
    "IConnector",
    "ICustomParams",
    "IGraph",
    "IGraphItem",
    "IGraphSession",
    "ILLMProviderHandler",
    "ILocalTool",
    "ILocalToolFunction",
    "IMessage",
    "IOpenAIToolFunctionOutput",
    "IOpenAIToolOutput",
    "ITool",
    "IToolParameter",
    "IToolResponse",
    "IToolResponsePayload",
    "LLMProvider",
    "NvidiaNIMSupportedModels",
    "OpenAISupportedModels",
    "ToolResponse",
    "XpanderClient",
]

publication.publish()

def _typecheckingstub__686bee2f9cc4cb8e5e46bd20309c912c48752fa01feec49d211288fe414d9879(
    value: IBedrockToolSpec,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50442d45bad8e7fa927b6be3feac263e79712091c62056e831a391b5a17c13bc(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bab15f7ad29e9cbdf37869d4d12b1eca4937a0130eb1409bb74f1149d0dfc26b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39dfbf6fa195f65cf55b428cbf9c7e700af738bcd9c47ebdda318cfedf78e70a(
    value: IBedrockToolSpecInputSchema,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0534d2b1daae9caffc87b99f4b6cc09e1a9eac3888374c04e9c619375c2f1b35(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1454322c6f1b39bdf36a5d88226526fce2d55d1e13ada58cf00d44f12fd64366(
    value: typing.Mapping[builtins.str, IToolParameter],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__749dc09e74837091b743b20b44a7b3d650b22053af60f7190f6967162b0ce86a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__716ced89905278f67f812ac3e2a90a587568bbaaad3f65e614e638500f0a8879(
    value: typing.List[IGraphItem],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f8b6a560e7ca3dd7becbfdd776fa40b4c1a0421caf2d7e32cf7d3b20237db27(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc94fcdd7c82d34b33d4fef5adb26a8b703ba811f07b94c755cecfd7ccf827f7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f9e512f5abf3ed78aa692496e890765157ef21fe2ca4e70e7c65491156ba438(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63dac3f67c0f52d800dcd097be9ddb6eb98f70c71ea8289dbaad0e94a58d47f1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53cbdb3cb6871f560d5a0a78bd2ceff7528297ba8da6e71aa3da216d1c0284f2(
    value: typing.Mapping[builtins.str, typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42a9c3fc5cff09316502fc55db2175287af1ef6831a515963059bd6de019711a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57c77329d9ea483c6111ccb444f6e30c3a08d7baf27c81a55cc015bb38ed9369(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__436460a38c0c401a5ac0cc40ee38a8569b50fcd9c0d74756e93fc405e57b4999(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80f4ac1b21803bf084bc5d3fa5ecbc38ccdbf3c98eda8c5f9b373c3c454a9986(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae86dd288186a83788bd74bbe23efbaf93b927d68170d1c441873dafce300f31(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2abb4fa17493a619c62da93fd4891ab5d776cbbf34890a94704d9ab98af249d2(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e990337f22ef47b5f40d9401058956b9c4bea64a9bafe926858ea6869074251(
    functionize: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6eabf11d97b19da7ed9046ad2b6f0a43749a3b5d1cf7fa11d5ec2390b04bffc9(
    tool_selector_response: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae6f34e8c01f6a6c9c281834bc9bf889895f559d21de59a7b05271a82ba77196(
    tool_id: builtins.str,
    payload: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afcc8b3292657cf39d4883d2f4c5f804a04f2bf61a3a6d58fc200181f1613b2a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ceabb1f28442b22fad8c23d587d18b3058d760f8679016135ab59fdde96b125(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f56ea2b548b4cdfe22f0f80bf2c3f88697c04aedd2bf7fe61755b4eb9cee55b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5396ff1ffb06161e7b92840a35a663b1f418ffdcc7dde0e2593addf6ca31936a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__682720a04a90eb0d29239c0baf8e36b53b239f76f1079edf9cd418a69ddb97ac(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bf23d7676e5d1c7e307b10d99651d3e323b4741175a001eec3d04daa9f6a063(
    value: typing.Optional[typing.Mapping[builtins.str, IToolParameter]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__187dae4a63a6fee1ee6e1cb395b2f91742bd245c20c13ab04570590726c5ef61(
    value: typing.Mapping[builtins.str, IToolParameter],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16039ce6185f742cd5865e412fc0342905a7a6d458331abeea0c8aea52fd0eb5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52b13164b7161ac045d14f7c4212e2fc304cf9b4c0234c2221c11807a860fee0(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f73e164c6a44a3b3baeb4c0db588226328547869f802218d70a1011b2423f20e(
    value: typing.Mapping[typing.Any, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bef146974c73640980b42683bcc6c7c6fd3e99ce00416797a28824e24ed245b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__480f8c3a9fe5cce1c76c047e7c85449f3f3b18ac119d429c16fcd668dd9bffa9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73d18f79c4026ba80502b29d7d377fbe641a12167e31a95dedf72905d238ad06(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f62f1d504eb1a32375eaa547166df13aaedae86863a17762624dad92eac5771(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4886f85be83c75284f4a0a609075d0f680402dee57ac924df12e39c6dc2a2620(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d1cc4753491f22ff1bb5d9814210da53bb4bb3a6fe4d73062b568a69f396d22(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__855e7764f28c37e54a5301b3a5ae59a5cf33e5b99b7ee9d8af609ec4cbabe816(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e85f84776414e75b23ca0d7ed7d4e074419a70de8997b3fa89b3e717ba2d16b(
    tool_call_id: builtins.str,
    role: builtins.str,
    name: builtins.str,
    response_message: builtins.str,
    filtered_tool: typing.Mapping[typing.Any, typing.Any],
    payload_request: builtins.str,
    local_tool: typing.Optional[typing.Union[IBedrockToolOutput, ILocalTool]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c59e939ed4cdb302e7adbd3d749f4a8fd632cdd13ed91e112788b1bc5ff9c94(
    json: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1db45836b482186036af28282ce7a17e90a75b871f10d04414a6e1b162096be1(
    value: typing.Mapping[typing.Any, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b47dd0917aa0042a7945f018986b595aafdc255b7d68dccdab7c7059cd806be2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49643ea0ff919e21e24a0644caba005ea086c83fa97ef4bcae54bc545248dfb3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de9a33fbf19475ac4ae43975d7e702211d1f6568a662fcddb481de787c1223d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90f4115fd71d0ee18aaf8914fba42e770875ad5f03c5f8a6e9705ad62d5fbd3f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72d95ac9191b5a3b6832a987b8a5261e3257588cd5f2e4c5cf0cc50be50059f2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d5b3165d80d89d2b04b5e46c254e63da06e5858a40d39921ca98f3cc75fd9c1(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ada04f0df01e9b462e0b973aee5f69eda17ab0f22e7345f33423f0acca9ad36(
    agent_key: builtins.str,
    agent_url: builtins.str,
    llm_provider: LLMProvider,
    local_tools: typing.Optional[typing.Sequence[ILocalTool]] = None,
    tools: typing.Optional[typing.Union[typing.Sequence[typing.Any], typing.Sequence[IOpenAIToolOutput], typing.Sequence[IBedrockToolOutput]]] = None,
    custom_params: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4b1a48b122979793bac1655fd731a7c2e2b3cf3c645f438a6d486a90006820b(
    tools: typing.Sequence[ILocalTool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5db91ce4f1a6c12048755ac88edd73655b66f8c589fd9d213b66d580ec7adc7(
    param: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18f87c7417879c6d58ba1275f3c6dc3cbe6518ab8cc45a112608c2ba48d7890f(
    tools: typing.Union[typing.Sequence[typing.Any], typing.Sequence[IOpenAIToolOutput], typing.Sequence[IBedrockToolOutput]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__533ca20d23cf744702ce059e14658b186611443cff0802973ffca1dd3c3cfc49(
    param: builtins.str,
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e2d2dde4e8be1794629154f5f5785efd317185e2b79dcff6e50ef0104c288e2(
    prompt: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f966ec87e3ece5fb630f8589d4ea9d99ed7fea000929df61b60531734c7ce278(
    llm_provider: typing.Optional[LLMProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a22edb3e8b5b34cd3d6b792b223e3a6d2ff1c9a97db02d95432302d04135716f(
    tool_id: builtins.str,
    payload: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__934787f3c0966796972c5e5bf4a28aca4d188aa70632ed29bc6401dc3383596d(
    tool_selector_response: typing.Any,
    llm_provider: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec1e4aa01d86350e4e2fa3a8d5fd0dd0b10573e0712e583aebf20df7c99904b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03c6a33ed2b1e15f73f6cd1ce2ef1b2c47f2516aff9583e0b468b87a95b92859(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93d7882c050d951d58dd512563574491c355d278ba3db4b5be8f1e48ae90973c(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43d62092cf9d0124286de42b5169d53613f78e50ea0b5177fa0f187cb31d41ca(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef50ccd539cda95bb415311cc7ddb6b2d6ffef3a7905c703e6d5bea60b5406d8(
    value: ILLMProviderHandler,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89ac314921ee59851df3b7539810145482a18a068c13ebd4e4f4f9cf38d40e2d(
    value: typing.List[ILocalTool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4685c27686f93e903b9776fd808abb1991bcbc10198a9b97d66846fd79da67d7(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c157c90274c35a97f6cc1e958c5d93f56b8921e11e66102068c645a4db91b7c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass
