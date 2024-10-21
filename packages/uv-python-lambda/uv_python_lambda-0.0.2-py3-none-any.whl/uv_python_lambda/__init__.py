r'''
# uv-python-lambda

CDK Construct for Python Lambda Functions using [uv](https://docs.astral.sh/uv/)

## Goals

* ⚡️ Package and deploy Lambda Functions faster with `uv`'s speed
* 📦 Support workspaces in a monorepo with [uv workspaces](https://docs.astral.sh/uv/concepts/workspaces/)

`uv-python-lambda` is based on [aws-lambda-python-alpha](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-lambda-python-alpha-readme.html) with some differences:

* It only supports `uv` for packaging - there is no Poetry or pip support
* It supports workspaces so you can build multiple Lambda functions from different uv workspaces and have their dependencies included correctly. This is useful for, but not limited to, monorepos.

## API

See [API.md](API.md)

## Example

```python
from uv_python_lambda import PythonFunction
from constructs import Construct

# The root path should be relative to your CDK source file
root_path = Path(__file__).parent.parent.parent


class CdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        fn = PythonFunction(
          self,
          "fn",
          root_dir=str(root_path),
          index="fetcher_lambda.py",
          workspace_package="fetcher",  # Use a workspace package as the top-level Lambda entry point.
          handler="handle_event",
          bundling={
              "asset_excludes": [
                  ".venv/",
                  "node_modules/",
                  "cdk/",
                  ".git/",
                  ".idea/",
                  "dist/",
              ]
          },
          timeout=Duration.seconds(30),
        )
```
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

import aws_cdk as _aws_cdk_ceddda9d
import aws_cdk.aws_codeguruprofiler as _aws_cdk_aws_codeguruprofiler_ceddda9d
import aws_cdk.aws_ec2 as _aws_cdk_aws_ec2_ceddda9d
import aws_cdk.aws_iam as _aws_cdk_aws_iam_ceddda9d
import aws_cdk.aws_kms as _aws_cdk_aws_kms_ceddda9d
import aws_cdk.aws_lambda as _aws_cdk_aws_lambda_ceddda9d
import aws_cdk.aws_logs as _aws_cdk_aws_logs_ceddda9d
import aws_cdk.aws_sns as _aws_cdk_aws_sns_ceddda9d
import aws_cdk.aws_sqs as _aws_cdk_aws_sqs_ceddda9d
import constructs as _constructs_77d1e7e8


class Bundling(metaclass=jsii.JSIIMeta, jsii_type="uv-python-lambda.Bundling"):
    '''Bundling options for Python Lambda assets.'''

    def __init__(
        self,
        *,
        root_dir: builtins.str,
        runtime: _aws_cdk_aws_lambda_ceddda9d.Runtime,
        architecture: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.Architecture] = None,
        skip: typing.Optional[builtins.bool] = None,
        workspace_package: typing.Optional[builtins.str] = None,
        asset_excludes: typing.Optional[typing.Sequence[builtins.str]] = None,
        asset_hash: typing.Optional[builtins.str] = None,
        asset_hash_type: typing.Optional[_aws_cdk_ceddda9d.AssetHashType] = None,
        build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        bundling_file_access: typing.Optional[_aws_cdk_ceddda9d.BundlingFileAccess] = None,
        command_hooks: typing.Optional["ICommandHooks"] = None,
        image: typing.Optional[_aws_cdk_ceddda9d.DockerImage] = None,
        output_path_suffix: typing.Optional[builtins.str] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        entrypoint: typing.Optional[typing.Sequence[builtins.str]] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        network: typing.Optional[builtins.str] = None,
        platform: typing.Optional[builtins.str] = None,
        security_opt: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
        volumes: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_ceddda9d.DockerVolume, typing.Dict[builtins.str, typing.Any]]]] = None,
        volumes_from: typing.Optional[typing.Sequence[builtins.str]] = None,
        working_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param root_dir: uv project root (workspace root).
        :param runtime: Lambda runtime (must be one of the Python runtimes).
        :param architecture: Lambda CPU architecture. Default: Architecture.ARM_64
        :param skip: Skip bundling process. Default: false
        :param workspace_package: uv package to use for the Lambda Function.
        :param asset_excludes: List of file patterns to exclude when copying assets from source for bundling. Default: - DEFAULT_ASSET_EXCLUDES
        :param asset_hash: Specify a custom hash for this asset. If ``assetHashType`` is set it must be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will need to make sure it is updated every time the asset changes, or otherwise it is possible that some deployments will not be invalidated. Default: - Based on ``assetHashType``
        :param asset_hash_type: Determines how asset hash is calculated. Assets will get rebuild and uploaded only if their hash has changed. If asset hash is set to ``SOURCE`` (default), then only changes to the source directory will cause the asset to rebuild. This means, for example, that in order to pick up a new dependency version, a change must be made to the source tree. Ideally, this can be implemented by including a dependency lockfile in your source tree or using fixed dependencies. If the asset hash is set to ``OUTPUT``, the hash is calculated after bundling. This means that any change in the output will cause the asset to be invalidated and uploaded. Bear in mind that ``pip`` adds timestamps to dependencies it installs, which implies that in this mode Python bundles will *always* get rebuild and uploaded. Normally this is an anti-pattern since build Default: AssetHashType.SOURCE By default, hash is calculated based on the contents of the source directory. This means that only updates to the source will cause the asset to rebuild.
        :param build_args: Optional build arguments to pass to the default container. This can be used to customize the index URLs used for installing dependencies. This is not used if a custom image is provided. Default: - No build arguments.
        :param bundling_file_access: Which option to use to copy the source files to the docker container and output files back. Default: - BundlingFileAccess.BIND_MOUNT
        :param command_hooks: Command hooks. Default: - do not run additional commands
        :param image: Docker image to use for bundling. If no options are provided, the default bundling image will be used. Dependencies will be installed using the default packaging commands and copied over from into the Lambda asset. Default: - Default bundling image.
        :param output_path_suffix: Output path suffix: the suffix for the directory into which the bundled output is written. Default: - 'python' for a layer, empty string otherwise.
        :param command: The command to run in the container. Default: - run the command defined in the image
        :param entrypoint: The entrypoint to run in the container. Default: - run the entrypoint defined in the image
        :param environment: The environment variables to pass to the container. Default: - no environment variables.
        :param network: Docker `Networking options <https://docs.docker.com/engine/reference/commandline/run/#connect-a-container-to-a-network---network>`_. Default: - no networking options
        :param platform: Set platform if server is multi-platform capable. *Requires Docker Engine API v1.38+*. Example value: ``linux/amd64`` Default: - no platform specified
        :param security_opt: `Security configuration <https://docs.docker.com/engine/reference/run/#security-configuration>`_ when running the docker container. Default: - no security options
        :param user: The user to use when running the container. Default: - root or image default
        :param volumes: Docker volumes to mount. Default: - no volumes are mounted
        :param volumes_from: Where to mount the specified volumes from. Default: - no containers are specified to mount volumes from
        :param working_directory: Working directory inside the container. Default: - image default
        '''
        props = BundlingProps(
            root_dir=root_dir,
            runtime=runtime,
            architecture=architecture,
            skip=skip,
            workspace_package=workspace_package,
            asset_excludes=asset_excludes,
            asset_hash=asset_hash,
            asset_hash_type=asset_hash_type,
            build_args=build_args,
            bundling_file_access=bundling_file_access,
            command_hooks=command_hooks,
            image=image,
            output_path_suffix=output_path_suffix,
            command=command,
            entrypoint=entrypoint,
            environment=environment,
            network=network,
            platform=platform,
            security_opt=security_opt,
            user=user,
            volumes=volumes,
            volumes_from=volumes_from,
            working_directory=working_directory,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bundle")
    @builtins.classmethod
    def bundle(
        cls,
        *,
        root_dir: builtins.str,
        runtime: _aws_cdk_aws_lambda_ceddda9d.Runtime,
        architecture: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.Architecture] = None,
        skip: typing.Optional[builtins.bool] = None,
        workspace_package: typing.Optional[builtins.str] = None,
        asset_excludes: typing.Optional[typing.Sequence[builtins.str]] = None,
        asset_hash: typing.Optional[builtins.str] = None,
        asset_hash_type: typing.Optional[_aws_cdk_ceddda9d.AssetHashType] = None,
        build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        bundling_file_access: typing.Optional[_aws_cdk_ceddda9d.BundlingFileAccess] = None,
        command_hooks: typing.Optional["ICommandHooks"] = None,
        image: typing.Optional[_aws_cdk_ceddda9d.DockerImage] = None,
        output_path_suffix: typing.Optional[builtins.str] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        entrypoint: typing.Optional[typing.Sequence[builtins.str]] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        network: typing.Optional[builtins.str] = None,
        platform: typing.Optional[builtins.str] = None,
        security_opt: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
        volumes: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_ceddda9d.DockerVolume, typing.Dict[builtins.str, typing.Any]]]] = None,
        volumes_from: typing.Optional[typing.Sequence[builtins.str]] = None,
        working_directory: typing.Optional[builtins.str] = None,
    ) -> _aws_cdk_aws_lambda_ceddda9d.AssetCode:
        '''
        :param root_dir: uv project root (workspace root).
        :param runtime: Lambda runtime (must be one of the Python runtimes).
        :param architecture: Lambda CPU architecture. Default: Architecture.ARM_64
        :param skip: Skip bundling process. Default: false
        :param workspace_package: uv package to use for the Lambda Function.
        :param asset_excludes: List of file patterns to exclude when copying assets from source for bundling. Default: - DEFAULT_ASSET_EXCLUDES
        :param asset_hash: Specify a custom hash for this asset. If ``assetHashType`` is set it must be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will need to make sure it is updated every time the asset changes, or otherwise it is possible that some deployments will not be invalidated. Default: - Based on ``assetHashType``
        :param asset_hash_type: Determines how asset hash is calculated. Assets will get rebuild and uploaded only if their hash has changed. If asset hash is set to ``SOURCE`` (default), then only changes to the source directory will cause the asset to rebuild. This means, for example, that in order to pick up a new dependency version, a change must be made to the source tree. Ideally, this can be implemented by including a dependency lockfile in your source tree or using fixed dependencies. If the asset hash is set to ``OUTPUT``, the hash is calculated after bundling. This means that any change in the output will cause the asset to be invalidated and uploaded. Bear in mind that ``pip`` adds timestamps to dependencies it installs, which implies that in this mode Python bundles will *always* get rebuild and uploaded. Normally this is an anti-pattern since build Default: AssetHashType.SOURCE By default, hash is calculated based on the contents of the source directory. This means that only updates to the source will cause the asset to rebuild.
        :param build_args: Optional build arguments to pass to the default container. This can be used to customize the index URLs used for installing dependencies. This is not used if a custom image is provided. Default: - No build arguments.
        :param bundling_file_access: Which option to use to copy the source files to the docker container and output files back. Default: - BundlingFileAccess.BIND_MOUNT
        :param command_hooks: Command hooks. Default: - do not run additional commands
        :param image: Docker image to use for bundling. If no options are provided, the default bundling image will be used. Dependencies will be installed using the default packaging commands and copied over from into the Lambda asset. Default: - Default bundling image.
        :param output_path_suffix: Output path suffix: the suffix for the directory into which the bundled output is written. Default: - 'python' for a layer, empty string otherwise.
        :param command: The command to run in the container. Default: - run the command defined in the image
        :param entrypoint: The entrypoint to run in the container. Default: - run the entrypoint defined in the image
        :param environment: The environment variables to pass to the container. Default: - no environment variables.
        :param network: Docker `Networking options <https://docs.docker.com/engine/reference/commandline/run/#connect-a-container-to-a-network---network>`_. Default: - no networking options
        :param platform: Set platform if server is multi-platform capable. *Requires Docker Engine API v1.38+*. Example value: ``linux/amd64`` Default: - no platform specified
        :param security_opt: `Security configuration <https://docs.docker.com/engine/reference/run/#security-configuration>`_ when running the docker container. Default: - no security options
        :param user: The user to use when running the container. Default: - root or image default
        :param volumes: Docker volumes to mount. Default: - no volumes are mounted
        :param volumes_from: Where to mount the specified volumes from. Default: - no containers are specified to mount volumes from
        :param working_directory: Working directory inside the container. Default: - image default
        '''
        options = BundlingProps(
            root_dir=root_dir,
            runtime=runtime,
            architecture=architecture,
            skip=skip,
            workspace_package=workspace_package,
            asset_excludes=asset_excludes,
            asset_hash=asset_hash,
            asset_hash_type=asset_hash_type,
            build_args=build_args,
            bundling_file_access=bundling_file_access,
            command_hooks=command_hooks,
            image=image,
            output_path_suffix=output_path_suffix,
            command=command,
            entrypoint=entrypoint,
            environment=environment,
            network=network,
            platform=platform,
            security_opt=security_opt,
            user=user,
            volumes=volumes,
            volumes_from=volumes_from,
            working_directory=working_directory,
        )

        return typing.cast(_aws_cdk_aws_lambda_ceddda9d.AssetCode, jsii.sinvoke(cls, "bundle", [options]))

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> _aws_cdk_ceddda9d.DockerImage:
        return typing.cast(_aws_cdk_ceddda9d.DockerImage, jsii.get(self, "image"))

    @builtins.property
    @jsii.member(jsii_name="bundlingFileAccess")
    def bundling_file_access(
        self,
    ) -> typing.Optional[_aws_cdk_ceddda9d.BundlingFileAccess]:
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.BundlingFileAccess], jsii.get(self, "bundlingFileAccess"))

    @builtins.property
    @jsii.member(jsii_name="command")
    def command(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "command"))

    @builtins.property
    @jsii.member(jsii_name="entrypoint")
    def entrypoint(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "entrypoint"))

    @builtins.property
    @jsii.member(jsii_name="environment")
    def environment(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "environment"))

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "network"))

    @builtins.property
    @jsii.member(jsii_name="securityOpt")
    def security_opt(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityOpt"))

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "user"))

    @builtins.property
    @jsii.member(jsii_name="volumes")
    def volumes(self) -> typing.Optional[typing.List[_aws_cdk_ceddda9d.DockerVolume]]:
        return typing.cast(typing.Optional[typing.List[_aws_cdk_ceddda9d.DockerVolume]], jsii.get(self, "volumes"))

    @builtins.property
    @jsii.member(jsii_name="volumesFrom")
    def volumes_from(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "volumesFrom"))

    @builtins.property
    @jsii.member(jsii_name="workingDirectory")
    def working_directory(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workingDirectory"))


@jsii.data_type(
    jsii_type="uv-python-lambda.BundlingOptions",
    jsii_struct_bases=[_aws_cdk_ceddda9d.DockerRunOptions],
    name_mapping={
        "command": "command",
        "entrypoint": "entrypoint",
        "environment": "environment",
        "network": "network",
        "platform": "platform",
        "security_opt": "securityOpt",
        "user": "user",
        "volumes": "volumes",
        "volumes_from": "volumesFrom",
        "working_directory": "workingDirectory",
        "asset_excludes": "assetExcludes",
        "asset_hash": "assetHash",
        "asset_hash_type": "assetHashType",
        "build_args": "buildArgs",
        "bundling_file_access": "bundlingFileAccess",
        "command_hooks": "commandHooks",
        "image": "image",
        "output_path_suffix": "outputPathSuffix",
    },
)
class BundlingOptions(_aws_cdk_ceddda9d.DockerRunOptions):
    def __init__(
        self,
        *,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        entrypoint: typing.Optional[typing.Sequence[builtins.str]] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        network: typing.Optional[builtins.str] = None,
        platform: typing.Optional[builtins.str] = None,
        security_opt: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
        volumes: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_ceddda9d.DockerVolume, typing.Dict[builtins.str, typing.Any]]]] = None,
        volumes_from: typing.Optional[typing.Sequence[builtins.str]] = None,
        working_directory: typing.Optional[builtins.str] = None,
        asset_excludes: typing.Optional[typing.Sequence[builtins.str]] = None,
        asset_hash: typing.Optional[builtins.str] = None,
        asset_hash_type: typing.Optional[_aws_cdk_ceddda9d.AssetHashType] = None,
        build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        bundling_file_access: typing.Optional[_aws_cdk_ceddda9d.BundlingFileAccess] = None,
        command_hooks: typing.Optional["ICommandHooks"] = None,
        image: typing.Optional[_aws_cdk_ceddda9d.DockerImage] = None,
        output_path_suffix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Options for bundling.

        :param command: The command to run in the container. Default: - run the command defined in the image
        :param entrypoint: The entrypoint to run in the container. Default: - run the entrypoint defined in the image
        :param environment: The environment variables to pass to the container. Default: - no environment variables.
        :param network: Docker `Networking options <https://docs.docker.com/engine/reference/commandline/run/#connect-a-container-to-a-network---network>`_. Default: - no networking options
        :param platform: Set platform if server is multi-platform capable. *Requires Docker Engine API v1.38+*. Example value: ``linux/amd64`` Default: - no platform specified
        :param security_opt: `Security configuration <https://docs.docker.com/engine/reference/run/#security-configuration>`_ when running the docker container. Default: - no security options
        :param user: The user to use when running the container. Default: - root or image default
        :param volumes: Docker volumes to mount. Default: - no volumes are mounted
        :param volumes_from: Where to mount the specified volumes from. Default: - no containers are specified to mount volumes from
        :param working_directory: Working directory inside the container. Default: - image default
        :param asset_excludes: List of file patterns to exclude when copying assets from source for bundling. Default: - DEFAULT_ASSET_EXCLUDES
        :param asset_hash: Specify a custom hash for this asset. If ``assetHashType`` is set it must be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will need to make sure it is updated every time the asset changes, or otherwise it is possible that some deployments will not be invalidated. Default: - Based on ``assetHashType``
        :param asset_hash_type: Determines how asset hash is calculated. Assets will get rebuild and uploaded only if their hash has changed. If asset hash is set to ``SOURCE`` (default), then only changes to the source directory will cause the asset to rebuild. This means, for example, that in order to pick up a new dependency version, a change must be made to the source tree. Ideally, this can be implemented by including a dependency lockfile in your source tree or using fixed dependencies. If the asset hash is set to ``OUTPUT``, the hash is calculated after bundling. This means that any change in the output will cause the asset to be invalidated and uploaded. Bear in mind that ``pip`` adds timestamps to dependencies it installs, which implies that in this mode Python bundles will *always* get rebuild and uploaded. Normally this is an anti-pattern since build Default: AssetHashType.SOURCE By default, hash is calculated based on the contents of the source directory. This means that only updates to the source will cause the asset to rebuild.
        :param build_args: Optional build arguments to pass to the default container. This can be used to customize the index URLs used for installing dependencies. This is not used if a custom image is provided. Default: - No build arguments.
        :param bundling_file_access: Which option to use to copy the source files to the docker container and output files back. Default: - BundlingFileAccess.BIND_MOUNT
        :param command_hooks: Command hooks. Default: - do not run additional commands
        :param image: Docker image to use for bundling. If no options are provided, the default bundling image will be used. Dependencies will be installed using the default packaging commands and copied over from into the Lambda asset. Default: - Default bundling image.
        :param output_path_suffix: Output path suffix: the suffix for the directory into which the bundled output is written. Default: - 'python' for a layer, empty string otherwise.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c127a9f1315f71ef946f978c90bac639ec3fc1d9efcaa70c8b9e86ce62f88283)
            check_type(argname="argument command", value=command, expected_type=type_hints["command"])
            check_type(argname="argument entrypoint", value=entrypoint, expected_type=type_hints["entrypoint"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument platform", value=platform, expected_type=type_hints["platform"])
            check_type(argname="argument security_opt", value=security_opt, expected_type=type_hints["security_opt"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
            check_type(argname="argument volumes", value=volumes, expected_type=type_hints["volumes"])
            check_type(argname="argument volumes_from", value=volumes_from, expected_type=type_hints["volumes_from"])
            check_type(argname="argument working_directory", value=working_directory, expected_type=type_hints["working_directory"])
            check_type(argname="argument asset_excludes", value=asset_excludes, expected_type=type_hints["asset_excludes"])
            check_type(argname="argument asset_hash", value=asset_hash, expected_type=type_hints["asset_hash"])
            check_type(argname="argument asset_hash_type", value=asset_hash_type, expected_type=type_hints["asset_hash_type"])
            check_type(argname="argument build_args", value=build_args, expected_type=type_hints["build_args"])
            check_type(argname="argument bundling_file_access", value=bundling_file_access, expected_type=type_hints["bundling_file_access"])
            check_type(argname="argument command_hooks", value=command_hooks, expected_type=type_hints["command_hooks"])
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument output_path_suffix", value=output_path_suffix, expected_type=type_hints["output_path_suffix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if command is not None:
            self._values["command"] = command
        if entrypoint is not None:
            self._values["entrypoint"] = entrypoint
        if environment is not None:
            self._values["environment"] = environment
        if network is not None:
            self._values["network"] = network
        if platform is not None:
            self._values["platform"] = platform
        if security_opt is not None:
            self._values["security_opt"] = security_opt
        if user is not None:
            self._values["user"] = user
        if volumes is not None:
            self._values["volumes"] = volumes
        if volumes_from is not None:
            self._values["volumes_from"] = volumes_from
        if working_directory is not None:
            self._values["working_directory"] = working_directory
        if asset_excludes is not None:
            self._values["asset_excludes"] = asset_excludes
        if asset_hash is not None:
            self._values["asset_hash"] = asset_hash
        if asset_hash_type is not None:
            self._values["asset_hash_type"] = asset_hash_type
        if build_args is not None:
            self._values["build_args"] = build_args
        if bundling_file_access is not None:
            self._values["bundling_file_access"] = bundling_file_access
        if command_hooks is not None:
            self._values["command_hooks"] = command_hooks
        if image is not None:
            self._values["image"] = image
        if output_path_suffix is not None:
            self._values["output_path_suffix"] = output_path_suffix

    @builtins.property
    def command(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The command to run in the container.

        :default: - run the command defined in the image
        '''
        result = self._values.get("command")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def entrypoint(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The entrypoint to run in the container.

        :default: - run the entrypoint defined in the image
        '''
        result = self._values.get("entrypoint")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The environment variables to pass to the container.

        :default: - no environment variables.
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def network(self) -> typing.Optional[builtins.str]:
        '''Docker `Networking options <https://docs.docker.com/engine/reference/commandline/run/#connect-a-container-to-a-network---network>`_.

        :default: - no networking options
        '''
        result = self._values.get("network")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def platform(self) -> typing.Optional[builtins.str]:
        '''Set platform if server is multi-platform capable. *Requires Docker Engine API v1.38+*.

        Example value: ``linux/amd64``

        :default: - no platform specified
        '''
        result = self._values.get("platform")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_opt(self) -> typing.Optional[builtins.str]:
        '''`Security configuration <https://docs.docker.com/engine/reference/run/#security-configuration>`_ when running the docker container.

        :default: - no security options
        '''
        result = self._values.get("security_opt")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user(self) -> typing.Optional[builtins.str]:
        '''The user to use when running the container.

        :default: - root or image default
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volumes(self) -> typing.Optional[typing.List[_aws_cdk_ceddda9d.DockerVolume]]:
        '''Docker volumes to mount.

        :default: - no volumes are mounted
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_ceddda9d.DockerVolume]], result)

    @builtins.property
    def volumes_from(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Where to mount the specified volumes from.

        :default: - no containers are specified to mount volumes from

        :see: https://docs.docker.com/engine/reference/commandline/run/#mount-volumes-from-container---volumes-from
        '''
        result = self._values.get("volumes_from")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def working_directory(self) -> typing.Optional[builtins.str]:
        '''Working directory inside the container.

        :default: - image default
        '''
        result = self._values.get("working_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def asset_excludes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of file patterns to exclude when copying assets from source for bundling.

        :default: - DEFAULT_ASSET_EXCLUDES
        '''
        result = self._values.get("asset_excludes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def asset_hash(self) -> typing.Optional[builtins.str]:
        '''Specify a custom hash for this asset.

        If ``assetHashType`` is set it must
        be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will
        be SHA256 hashed and encoded as hex. The resulting hash will be the asset
        hash.

        NOTE: the hash is used in order to identify a specific revision of the asset, and
        used for optimizing and caching deployment activities related to this asset such as
        packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will
        need to make sure it is updated every time the asset changes, or otherwise it is
        possible that some deployments will not be invalidated.

        :default: - Based on ``assetHashType``
        '''
        result = self._values.get("asset_hash")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def asset_hash_type(self) -> typing.Optional[_aws_cdk_ceddda9d.AssetHashType]:
        '''Determines how asset hash is calculated. Assets will get rebuild and uploaded only if their hash has changed.

        If asset hash is set to ``SOURCE`` (default), then only changes to the source
        directory will cause the asset to rebuild. This means, for example, that in
        order to pick up a new dependency version, a change must be made to the
        source tree. Ideally, this can be implemented by including a dependency
        lockfile in your source tree or using fixed dependencies.

        If the asset hash is set to ``OUTPUT``, the hash is calculated after
        bundling. This means that any change in the output will cause the asset to
        be invalidated and uploaded. Bear in mind that ``pip`` adds timestamps to
        dependencies it installs, which implies that in this mode Python bundles
        will *always* get rebuild and uploaded. Normally this is an anti-pattern
        since build

        :default:

        AssetHashType.SOURCE By default, hash is calculated based on the
        contents of the source directory. This means that only updates to the
        source will cause the asset to rebuild.
        '''
        result = self._values.get("asset_hash_type")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.AssetHashType], result)

    @builtins.property
    def build_args(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional build arguments to pass to the default container.

        This can be used to customize
        the index URLs used for installing dependencies.
        This is not used if a custom image is provided.

        :default: - No build arguments.
        '''
        result = self._values.get("build_args")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def bundling_file_access(
        self,
    ) -> typing.Optional[_aws_cdk_ceddda9d.BundlingFileAccess]:
        '''Which option to use to copy the source files to the docker container and output files back.

        :default: - BundlingFileAccess.BIND_MOUNT
        '''
        result = self._values.get("bundling_file_access")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.BundlingFileAccess], result)

    @builtins.property
    def command_hooks(self) -> typing.Optional["ICommandHooks"]:
        '''Command hooks.

        :default: - do not run additional commands
        '''
        result = self._values.get("command_hooks")
        return typing.cast(typing.Optional["ICommandHooks"], result)

    @builtins.property
    def image(self) -> typing.Optional[_aws_cdk_ceddda9d.DockerImage]:
        '''Docker image to use for bundling.

        If no options are provided, the default bundling image
        will be used. Dependencies will be installed using the default packaging commands
        and copied over from into the Lambda asset.

        :default: - Default bundling image.
        '''
        result = self._values.get("image")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.DockerImage], result)

    @builtins.property
    def output_path_suffix(self) -> typing.Optional[builtins.str]:
        '''Output path suffix: the suffix for the directory into which the bundled output is written.

        :default: - 'python' for a layer, empty string otherwise.
        '''
        result = self._values.get("output_path_suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BundlingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="uv-python-lambda.BundlingProps",
    jsii_struct_bases=[BundlingOptions],
    name_mapping={
        "command": "command",
        "entrypoint": "entrypoint",
        "environment": "environment",
        "network": "network",
        "platform": "platform",
        "security_opt": "securityOpt",
        "user": "user",
        "volumes": "volumes",
        "volumes_from": "volumesFrom",
        "working_directory": "workingDirectory",
        "asset_excludes": "assetExcludes",
        "asset_hash": "assetHash",
        "asset_hash_type": "assetHashType",
        "build_args": "buildArgs",
        "bundling_file_access": "bundlingFileAccess",
        "command_hooks": "commandHooks",
        "image": "image",
        "output_path_suffix": "outputPathSuffix",
        "root_dir": "rootDir",
        "runtime": "runtime",
        "architecture": "architecture",
        "skip": "skip",
        "workspace_package": "workspacePackage",
    },
)
class BundlingProps(BundlingOptions):
    def __init__(
        self,
        *,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        entrypoint: typing.Optional[typing.Sequence[builtins.str]] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        network: typing.Optional[builtins.str] = None,
        platform: typing.Optional[builtins.str] = None,
        security_opt: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
        volumes: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_ceddda9d.DockerVolume, typing.Dict[builtins.str, typing.Any]]]] = None,
        volumes_from: typing.Optional[typing.Sequence[builtins.str]] = None,
        working_directory: typing.Optional[builtins.str] = None,
        asset_excludes: typing.Optional[typing.Sequence[builtins.str]] = None,
        asset_hash: typing.Optional[builtins.str] = None,
        asset_hash_type: typing.Optional[_aws_cdk_ceddda9d.AssetHashType] = None,
        build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        bundling_file_access: typing.Optional[_aws_cdk_ceddda9d.BundlingFileAccess] = None,
        command_hooks: typing.Optional["ICommandHooks"] = None,
        image: typing.Optional[_aws_cdk_ceddda9d.DockerImage] = None,
        output_path_suffix: typing.Optional[builtins.str] = None,
        root_dir: builtins.str,
        runtime: _aws_cdk_aws_lambda_ceddda9d.Runtime,
        architecture: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.Architecture] = None,
        skip: typing.Optional[builtins.bool] = None,
        workspace_package: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param command: The command to run in the container. Default: - run the command defined in the image
        :param entrypoint: The entrypoint to run in the container. Default: - run the entrypoint defined in the image
        :param environment: The environment variables to pass to the container. Default: - no environment variables.
        :param network: Docker `Networking options <https://docs.docker.com/engine/reference/commandline/run/#connect-a-container-to-a-network---network>`_. Default: - no networking options
        :param platform: Set platform if server is multi-platform capable. *Requires Docker Engine API v1.38+*. Example value: ``linux/amd64`` Default: - no platform specified
        :param security_opt: `Security configuration <https://docs.docker.com/engine/reference/run/#security-configuration>`_ when running the docker container. Default: - no security options
        :param user: The user to use when running the container. Default: - root or image default
        :param volumes: Docker volumes to mount. Default: - no volumes are mounted
        :param volumes_from: Where to mount the specified volumes from. Default: - no containers are specified to mount volumes from
        :param working_directory: Working directory inside the container. Default: - image default
        :param asset_excludes: List of file patterns to exclude when copying assets from source for bundling. Default: - DEFAULT_ASSET_EXCLUDES
        :param asset_hash: Specify a custom hash for this asset. If ``assetHashType`` is set it must be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will need to make sure it is updated every time the asset changes, or otherwise it is possible that some deployments will not be invalidated. Default: - Based on ``assetHashType``
        :param asset_hash_type: Determines how asset hash is calculated. Assets will get rebuild and uploaded only if their hash has changed. If asset hash is set to ``SOURCE`` (default), then only changes to the source directory will cause the asset to rebuild. This means, for example, that in order to pick up a new dependency version, a change must be made to the source tree. Ideally, this can be implemented by including a dependency lockfile in your source tree or using fixed dependencies. If the asset hash is set to ``OUTPUT``, the hash is calculated after bundling. This means that any change in the output will cause the asset to be invalidated and uploaded. Bear in mind that ``pip`` adds timestamps to dependencies it installs, which implies that in this mode Python bundles will *always* get rebuild and uploaded. Normally this is an anti-pattern since build Default: AssetHashType.SOURCE By default, hash is calculated based on the contents of the source directory. This means that only updates to the source will cause the asset to rebuild.
        :param build_args: Optional build arguments to pass to the default container. This can be used to customize the index URLs used for installing dependencies. This is not used if a custom image is provided. Default: - No build arguments.
        :param bundling_file_access: Which option to use to copy the source files to the docker container and output files back. Default: - BundlingFileAccess.BIND_MOUNT
        :param command_hooks: Command hooks. Default: - do not run additional commands
        :param image: Docker image to use for bundling. If no options are provided, the default bundling image will be used. Dependencies will be installed using the default packaging commands and copied over from into the Lambda asset. Default: - Default bundling image.
        :param output_path_suffix: Output path suffix: the suffix for the directory into which the bundled output is written. Default: - 'python' for a layer, empty string otherwise.
        :param root_dir: uv project root (workspace root).
        :param runtime: Lambda runtime (must be one of the Python runtimes).
        :param architecture: Lambda CPU architecture. Default: Architecture.ARM_64
        :param skip: Skip bundling process. Default: false
        :param workspace_package: uv package to use for the Lambda Function.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81d59fe1ee0f2977c9b3195e16a1f5ec90d137ed13842e74353e0938e809140f)
            check_type(argname="argument command", value=command, expected_type=type_hints["command"])
            check_type(argname="argument entrypoint", value=entrypoint, expected_type=type_hints["entrypoint"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument platform", value=platform, expected_type=type_hints["platform"])
            check_type(argname="argument security_opt", value=security_opt, expected_type=type_hints["security_opt"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
            check_type(argname="argument volumes", value=volumes, expected_type=type_hints["volumes"])
            check_type(argname="argument volumes_from", value=volumes_from, expected_type=type_hints["volumes_from"])
            check_type(argname="argument working_directory", value=working_directory, expected_type=type_hints["working_directory"])
            check_type(argname="argument asset_excludes", value=asset_excludes, expected_type=type_hints["asset_excludes"])
            check_type(argname="argument asset_hash", value=asset_hash, expected_type=type_hints["asset_hash"])
            check_type(argname="argument asset_hash_type", value=asset_hash_type, expected_type=type_hints["asset_hash_type"])
            check_type(argname="argument build_args", value=build_args, expected_type=type_hints["build_args"])
            check_type(argname="argument bundling_file_access", value=bundling_file_access, expected_type=type_hints["bundling_file_access"])
            check_type(argname="argument command_hooks", value=command_hooks, expected_type=type_hints["command_hooks"])
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument output_path_suffix", value=output_path_suffix, expected_type=type_hints["output_path_suffix"])
            check_type(argname="argument root_dir", value=root_dir, expected_type=type_hints["root_dir"])
            check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
            check_type(argname="argument skip", value=skip, expected_type=type_hints["skip"])
            check_type(argname="argument workspace_package", value=workspace_package, expected_type=type_hints["workspace_package"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "root_dir": root_dir,
            "runtime": runtime,
        }
        if command is not None:
            self._values["command"] = command
        if entrypoint is not None:
            self._values["entrypoint"] = entrypoint
        if environment is not None:
            self._values["environment"] = environment
        if network is not None:
            self._values["network"] = network
        if platform is not None:
            self._values["platform"] = platform
        if security_opt is not None:
            self._values["security_opt"] = security_opt
        if user is not None:
            self._values["user"] = user
        if volumes is not None:
            self._values["volumes"] = volumes
        if volumes_from is not None:
            self._values["volumes_from"] = volumes_from
        if working_directory is not None:
            self._values["working_directory"] = working_directory
        if asset_excludes is not None:
            self._values["asset_excludes"] = asset_excludes
        if asset_hash is not None:
            self._values["asset_hash"] = asset_hash
        if asset_hash_type is not None:
            self._values["asset_hash_type"] = asset_hash_type
        if build_args is not None:
            self._values["build_args"] = build_args
        if bundling_file_access is not None:
            self._values["bundling_file_access"] = bundling_file_access
        if command_hooks is not None:
            self._values["command_hooks"] = command_hooks
        if image is not None:
            self._values["image"] = image
        if output_path_suffix is not None:
            self._values["output_path_suffix"] = output_path_suffix
        if architecture is not None:
            self._values["architecture"] = architecture
        if skip is not None:
            self._values["skip"] = skip
        if workspace_package is not None:
            self._values["workspace_package"] = workspace_package

    @builtins.property
    def command(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The command to run in the container.

        :default: - run the command defined in the image
        '''
        result = self._values.get("command")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def entrypoint(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The entrypoint to run in the container.

        :default: - run the entrypoint defined in the image
        '''
        result = self._values.get("entrypoint")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The environment variables to pass to the container.

        :default: - no environment variables.
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def network(self) -> typing.Optional[builtins.str]:
        '''Docker `Networking options <https://docs.docker.com/engine/reference/commandline/run/#connect-a-container-to-a-network---network>`_.

        :default: - no networking options
        '''
        result = self._values.get("network")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def platform(self) -> typing.Optional[builtins.str]:
        '''Set platform if server is multi-platform capable. *Requires Docker Engine API v1.38+*.

        Example value: ``linux/amd64``

        :default: - no platform specified
        '''
        result = self._values.get("platform")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_opt(self) -> typing.Optional[builtins.str]:
        '''`Security configuration <https://docs.docker.com/engine/reference/run/#security-configuration>`_ when running the docker container.

        :default: - no security options
        '''
        result = self._values.get("security_opt")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user(self) -> typing.Optional[builtins.str]:
        '''The user to use when running the container.

        :default: - root or image default
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volumes(self) -> typing.Optional[typing.List[_aws_cdk_ceddda9d.DockerVolume]]:
        '''Docker volumes to mount.

        :default: - no volumes are mounted
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_ceddda9d.DockerVolume]], result)

    @builtins.property
    def volumes_from(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Where to mount the specified volumes from.

        :default: - no containers are specified to mount volumes from

        :see: https://docs.docker.com/engine/reference/commandline/run/#mount-volumes-from-container---volumes-from
        '''
        result = self._values.get("volumes_from")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def working_directory(self) -> typing.Optional[builtins.str]:
        '''Working directory inside the container.

        :default: - image default
        '''
        result = self._values.get("working_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def asset_excludes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of file patterns to exclude when copying assets from source for bundling.

        :default: - DEFAULT_ASSET_EXCLUDES
        '''
        result = self._values.get("asset_excludes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def asset_hash(self) -> typing.Optional[builtins.str]:
        '''Specify a custom hash for this asset.

        If ``assetHashType`` is set it must
        be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will
        be SHA256 hashed and encoded as hex. The resulting hash will be the asset
        hash.

        NOTE: the hash is used in order to identify a specific revision of the asset, and
        used for optimizing and caching deployment activities related to this asset such as
        packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will
        need to make sure it is updated every time the asset changes, or otherwise it is
        possible that some deployments will not be invalidated.

        :default: - Based on ``assetHashType``
        '''
        result = self._values.get("asset_hash")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def asset_hash_type(self) -> typing.Optional[_aws_cdk_ceddda9d.AssetHashType]:
        '''Determines how asset hash is calculated. Assets will get rebuild and uploaded only if their hash has changed.

        If asset hash is set to ``SOURCE`` (default), then only changes to the source
        directory will cause the asset to rebuild. This means, for example, that in
        order to pick up a new dependency version, a change must be made to the
        source tree. Ideally, this can be implemented by including a dependency
        lockfile in your source tree or using fixed dependencies.

        If the asset hash is set to ``OUTPUT``, the hash is calculated after
        bundling. This means that any change in the output will cause the asset to
        be invalidated and uploaded. Bear in mind that ``pip`` adds timestamps to
        dependencies it installs, which implies that in this mode Python bundles
        will *always* get rebuild and uploaded. Normally this is an anti-pattern
        since build

        :default:

        AssetHashType.SOURCE By default, hash is calculated based on the
        contents of the source directory. This means that only updates to the
        source will cause the asset to rebuild.
        '''
        result = self._values.get("asset_hash_type")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.AssetHashType], result)

    @builtins.property
    def build_args(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional build arguments to pass to the default container.

        This can be used to customize
        the index URLs used for installing dependencies.
        This is not used if a custom image is provided.

        :default: - No build arguments.
        '''
        result = self._values.get("build_args")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def bundling_file_access(
        self,
    ) -> typing.Optional[_aws_cdk_ceddda9d.BundlingFileAccess]:
        '''Which option to use to copy the source files to the docker container and output files back.

        :default: - BundlingFileAccess.BIND_MOUNT
        '''
        result = self._values.get("bundling_file_access")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.BundlingFileAccess], result)

    @builtins.property
    def command_hooks(self) -> typing.Optional["ICommandHooks"]:
        '''Command hooks.

        :default: - do not run additional commands
        '''
        result = self._values.get("command_hooks")
        return typing.cast(typing.Optional["ICommandHooks"], result)

    @builtins.property
    def image(self) -> typing.Optional[_aws_cdk_ceddda9d.DockerImage]:
        '''Docker image to use for bundling.

        If no options are provided, the default bundling image
        will be used. Dependencies will be installed using the default packaging commands
        and copied over from into the Lambda asset.

        :default: - Default bundling image.
        '''
        result = self._values.get("image")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.DockerImage], result)

    @builtins.property
    def output_path_suffix(self) -> typing.Optional[builtins.str]:
        '''Output path suffix: the suffix for the directory into which the bundled output is written.

        :default: - 'python' for a layer, empty string otherwise.
        '''
        result = self._values.get("output_path_suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_dir(self) -> builtins.str:
        '''uv project root (workspace root).'''
        result = self._values.get("root_dir")
        assert result is not None, "Required property 'root_dir' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def runtime(self) -> _aws_cdk_aws_lambda_ceddda9d.Runtime:
        '''Lambda runtime (must be one of the Python runtimes).'''
        result = self._values.get("runtime")
        assert result is not None, "Required property 'runtime' is missing"
        return typing.cast(_aws_cdk_aws_lambda_ceddda9d.Runtime, result)

    @builtins.property
    def architecture(
        self,
    ) -> typing.Optional[_aws_cdk_aws_lambda_ceddda9d.Architecture]:
        '''Lambda CPU architecture.

        :default: Architecture.ARM_64
        '''
        result = self._values.get("architecture")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_ceddda9d.Architecture], result)

    @builtins.property
    def skip(self) -> typing.Optional[builtins.bool]:
        '''Skip bundling process.

        :default: false
        '''
        result = self._values.get("skip")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def workspace_package(self) -> typing.Optional[builtins.str]:
        '''uv package to use for the Lambda Function.'''
        result = self._values.get("workspace_package")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BundlingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="uv-python-lambda.ICommandHooks")
class ICommandHooks(typing_extensions.Protocol):
    '''Command hooks.

    These commands will run in the environment in which bundling occurs: inside
    the container for Docker bundling or on the host OS for local bundling.

    Commands are chained with ``&&``::

       {
         // Run tests prior to bundling
         beforeBundling(inputDir: string, outputDir: string): string[] {
           return [`pytest`];
         }
         // ...
       }
    '''

    @jsii.member(jsii_name="afterBundling")
    def after_bundling(
        self,
        input_dir: builtins.str,
        output_dir: builtins.str,
    ) -> typing.List[builtins.str]:
        '''Returns commands to run after bundling.

        Commands are chained with ``&&``.

        :param input_dir: -
        :param output_dir: -
        '''
        ...

    @jsii.member(jsii_name="beforeBundling")
    def before_bundling(
        self,
        input_dir: builtins.str,
        output_dir: builtins.str,
    ) -> typing.List[builtins.str]:
        '''Returns commands to run before bundling.

        Commands are chained with ``&&``.

        :param input_dir: -
        :param output_dir: -
        '''
        ...


class _ICommandHooksProxy:
    '''Command hooks.

    These commands will run in the environment in which bundling occurs: inside
    the container for Docker bundling or on the host OS for local bundling.

    Commands are chained with ``&&``::

       {
         // Run tests prior to bundling
         beforeBundling(inputDir: string, outputDir: string): string[] {
           return [`pytest`];
         }
         // ...
       }
    '''

    __jsii_type__: typing.ClassVar[str] = "uv-python-lambda.ICommandHooks"

    @jsii.member(jsii_name="afterBundling")
    def after_bundling(
        self,
        input_dir: builtins.str,
        output_dir: builtins.str,
    ) -> typing.List[builtins.str]:
        '''Returns commands to run after bundling.

        Commands are chained with ``&&``.

        :param input_dir: -
        :param output_dir: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__488db7d12e1ab44fd5779f576fc5cd00cb9e85710a675cd96533b44d5c3b3135)
            check_type(argname="argument input_dir", value=input_dir, expected_type=type_hints["input_dir"])
            check_type(argname="argument output_dir", value=output_dir, expected_type=type_hints["output_dir"])
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "afterBundling", [input_dir, output_dir]))

    @jsii.member(jsii_name="beforeBundling")
    def before_bundling(
        self,
        input_dir: builtins.str,
        output_dir: builtins.str,
    ) -> typing.List[builtins.str]:
        '''Returns commands to run before bundling.

        Commands are chained with ``&&``.

        :param input_dir: -
        :param output_dir: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a84729a70b154d4dbb345742f5239044f1bb9c86e4f5efb63576535d4d8b4d6f)
            check_type(argname="argument input_dir", value=input_dir, expected_type=type_hints["input_dir"])
            check_type(argname="argument output_dir", value=output_dir, expected_type=type_hints["output_dir"])
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "beforeBundling", [input_dir, output_dir]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICommandHooks).__jsii_proxy_class__ = lambda : _ICommandHooksProxy


class PythonFunction(
    _aws_cdk_aws_lambda_ceddda9d.Function,
    metaclass=jsii.JSIIMeta,
    jsii_type="uv-python-lambda.PythonFunction",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        root_dir: builtins.str,
        bundling: typing.Optional[typing.Union[BundlingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        handler: typing.Optional[builtins.str] = None,
        index: typing.Optional[builtins.str] = None,
        runtime: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.Runtime] = None,
        workspace_package: typing.Optional[builtins.str] = None,
        adot_instrumentation: typing.Optional[typing.Union[_aws_cdk_aws_lambda_ceddda9d.AdotInstrumentationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        allow_all_ipv6_outbound: typing.Optional[builtins.bool] = None,
        allow_all_outbound: typing.Optional[builtins.bool] = None,
        allow_public_subnet: typing.Optional[builtins.bool] = None,
        application_log_level: typing.Optional[builtins.str] = None,
        application_log_level_v2: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.ApplicationLogLevel] = None,
        architecture: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.Architecture] = None,
        code_signing_config: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.ICodeSigningConfig] = None,
        current_version_options: typing.Optional[typing.Union[_aws_cdk_aws_lambda_ceddda9d.VersionOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        dead_letter_queue: typing.Optional[_aws_cdk_aws_sqs_ceddda9d.IQueue] = None,
        dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
        dead_letter_topic: typing.Optional[_aws_cdk_aws_sns_ceddda9d.ITopic] = None,
        description: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        environment_encryption: typing.Optional[_aws_cdk_aws_kms_ceddda9d.IKey] = None,
        ephemeral_storage_size: typing.Optional[_aws_cdk_ceddda9d.Size] = None,
        events: typing.Optional[typing.Sequence[_aws_cdk_aws_lambda_ceddda9d.IEventSource]] = None,
        filesystem: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.FileSystem] = None,
        function_name: typing.Optional[builtins.str] = None,
        initial_policy: typing.Optional[typing.Sequence[_aws_cdk_aws_iam_ceddda9d.PolicyStatement]] = None,
        insights_version: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.LambdaInsightsVersion] = None,
        ipv6_allowed_for_dual_stack: typing.Optional[builtins.bool] = None,
        layers: typing.Optional[typing.Sequence[_aws_cdk_aws_lambda_ceddda9d.ILayerVersion]] = None,
        log_format: typing.Optional[builtins.str] = None,
        logging_format: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.LoggingFormat] = None,
        log_group: typing.Optional[_aws_cdk_aws_logs_ceddda9d.ILogGroup] = None,
        log_retention: typing.Optional[_aws_cdk_aws_logs_ceddda9d.RetentionDays] = None,
        log_retention_retry_options: typing.Optional[typing.Union[_aws_cdk_aws_lambda_ceddda9d.LogRetentionRetryOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        log_retention_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        params_and_secrets: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.ParamsAndSecretsLayerVersion] = None,
        profiling: typing.Optional[builtins.bool] = None,
        profiling_group: typing.Optional[_aws_cdk_aws_codeguruprofiler_ceddda9d.IProfilingGroup] = None,
        recursive_loop: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.RecursiveLoop] = None,
        reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        runtime_management_mode: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.RuntimeManagementMode] = None,
        security_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup]] = None,
        snap_start: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.SnapStartConf] = None,
        system_log_level: typing.Optional[builtins.str] = None,
        system_log_level_v2: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.SystemLogLevel] = None,
        timeout: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        tracing: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.Tracing] = None,
        vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
        vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
        max_event_age: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        on_failure: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.IDestination] = None,
        on_success: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.IDestination] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param root_dir: UV project root directory (workspace root).
        :param bundling: Custom bundling options, including build architecture and bundling container image.
        :param handler: The name of the exported handler function in the #index. Default: handler
        :param index: The path to the index file with the project or (or workspace, if specified) containing the handler. Default: index.py
        :param runtime: The runtime. Default: Runtime.PYTHON_3_12
        :param workspace_package: Optional UV project workspace, used to specify a specific package to be used as a Lambda Function entry.
        :param adot_instrumentation: Specify the configuration of AWS Distro for OpenTelemetry (ADOT) instrumentation. Default: - No ADOT instrumentation
        :param allow_all_ipv6_outbound: Whether to allow the Lambda to send all ipv6 network traffic. If set to true, there will only be a single egress rule which allows all outbound ipv6 traffic. If set to false, you must individually add traffic rules to allow the Lambda to connect to network targets using ipv6. Do not specify this property if the ``securityGroups`` or ``securityGroup`` property is set. Instead, configure ``allowAllIpv6Outbound`` directly on the security group. Default: false
        :param allow_all_outbound: Whether to allow the Lambda to send all network traffic (except ipv6). If set to false, you must individually add traffic rules to allow the Lambda to connect to network targets. Do not specify this property if the ``securityGroups`` or ``securityGroup`` property is set. Instead, configure ``allowAllOutbound`` directly on the security group. Default: true
        :param allow_public_subnet: Lambda Functions in a public subnet can NOT access the internet. Use this property to acknowledge this limitation and still place the function in a public subnet. Default: false
        :param application_log_level: (deprecated) Sets the application log level for the function. Default: "INFO"
        :param application_log_level_v2: Sets the application log level for the function. Default: ApplicationLogLevel.INFO
        :param architecture: The system architectures compatible with this lambda function. Default: Architecture.X86_64
        :param code_signing_config: Code signing config associated with this function. Default: - Not Sign the Code
        :param current_version_options: Options for the ``lambda.Version`` resource automatically created by the ``fn.currentVersion`` method. Default: - default options as described in ``VersionOptions``
        :param dead_letter_queue: The SQS queue to use if DLQ is enabled. If SNS topic is desired, specify ``deadLetterTopic`` property instead. Default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``
        :param dead_letter_queue_enabled: Enabled DLQ. If ``deadLetterQueue`` is undefined, an SQS queue with default options will be defined for your Function. Default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.
        :param dead_letter_topic: The SNS topic to use as a DLQ. Note that if ``deadLetterQueueEnabled`` is set to ``true``, an SQS queue will be created rather than an SNS topic. Using an SNS topic as a DLQ requires this property to be set explicitly. Default: - no SNS topic
        :param description: A description of the function. Default: - No description.
        :param environment: Key-value pairs that Lambda caches and makes available for your Lambda functions. Use environment variables to apply configuration changes, such as test and production environment configurations, without changing your Lambda function source code. Default: - No environment variables.
        :param environment_encryption: The AWS KMS key that's used to encrypt your function's environment variables. Default: - AWS Lambda creates and uses an AWS managed customer master key (CMK).
        :param ephemeral_storage_size: The size of the function’s /tmp directory in MiB. Default: 512 MiB
        :param events: Event sources for this function. You can also add event sources using ``addEventSource``. Default: - No event sources.
        :param filesystem: The filesystem configuration for the lambda function. Default: - will not mount any filesystem
        :param function_name: A name for the function. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the function's name. For more information, see Name Type.
        :param initial_policy: Initial policy statements to add to the created Lambda Role. You can call ``addToRolePolicy`` to the created lambda to add statements post creation. Default: - No policy statements are added to the created Lambda role.
        :param insights_version: Specify the version of CloudWatch Lambda insights to use for monitoring. Default: - No Lambda Insights
        :param ipv6_allowed_for_dual_stack: Allows outbound IPv6 traffic on VPC functions that are connected to dual-stack subnets. Only used if 'vpc' is supplied. Default: false
        :param layers: A list of layers to add to the function's execution environment. You can configure your Lambda function to pull in additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies that can be used by multiple functions. Default: - No layers.
        :param log_format: (deprecated) Sets the logFormat for the function. Default: "Text"
        :param logging_format: Sets the loggingFormat for the function. Default: LoggingFormat.TEXT
        :param log_group: The log group the function sends logs to. By default, Lambda functions send logs to an automatically created default log group named /aws/lambda/<function name>. However you cannot change the properties of this auto-created log group using the AWS CDK, e.g. you cannot set a different log retention. Use the ``logGroup`` property to create a fully customizable LogGroup ahead of time, and instruct the Lambda function to send logs to it. Providing a user-controlled log group was rolled out to commercial regions on 2023-11-16. If you are deploying to another type of region, please check regional availability first. Default: ``/aws/lambda/${this.functionName}`` - default log group created by Lambda
        :param log_retention: The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. This is a legacy API and we strongly recommend you move away from it if you can. Instead create a fully customizable log group with ``logs.LogGroup`` and use the ``logGroup`` property to instruct the Lambda function to send logs to it. Migrating from ``logRetention`` to ``logGroup`` will cause the name of the log group to change. Users and code and referencing the name verbatim will have to adjust. In AWS CDK code, you can access the log group name directly from the LogGroup construct:: import * as logs from 'aws-cdk-lib/aws-logs'; declare const myLogGroup: logs.LogGroup; myLogGroup.logGroupName; Default: logs.RetentionDays.INFINITE
        :param log_retention_retry_options: When log retention is specified, a custom resource attempts to create the CloudWatch log group. These options control the retry policy when interacting with CloudWatch APIs. This is a legacy API and we strongly recommend you migrate to ``logGroup`` if you can. ``logGroup`` allows you to create a fully customizable log group and instruct the Lambda function to send logs to it. Default: - Default AWS SDK retry options.
        :param log_retention_role: The IAM role for the Lambda function associated with the custom resource that sets the retention policy. This is a legacy API and we strongly recommend you migrate to ``logGroup`` if you can. ``logGroup`` allows you to create a fully customizable log group and instruct the Lambda function to send logs to it. Default: - A new role is created.
        :param memory_size: The amount of memory, in MB, that is allocated to your Lambda function. Lambda uses this value to proportionally allocate the amount of CPU power. For more information, see Resource Model in the AWS Lambda Developer Guide. Default: 128
        :param params_and_secrets: Specify the configuration of Parameters and Secrets Extension. Default: - No Parameters and Secrets Extension
        :param profiling: Enable profiling. Default: - No profiling.
        :param profiling_group: Profiling Group. Default: - A new profiling group will be created if ``profiling`` is set.
        :param recursive_loop: Sets the Recursive Loop Protection for Lambda Function. It lets Lambda detect and terminate unintended recusrive loops. Default: RecursiveLoop.Terminate
        :param reserved_concurrent_executions: The maximum of concurrent executions you want to reserve for the function. Default: - No specific limit - account limit.
        :param role: Lambda execution role. This is the role that will be assumed by the function upon execution. It controls the permissions that the function will have. The Role must be assumable by the 'lambda.amazonaws.com' service principal. The default Role automatically has permissions granted for Lambda execution. If you provide a Role, you must add the relevant AWS managed policies yourself. The relevant managed policies are "service-role/AWSLambdaBasicExecutionRole" and "service-role/AWSLambdaVPCAccessExecutionRole". Default: - A unique role will be generated for this lambda function. Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.
        :param runtime_management_mode: Sets the runtime management configuration for a function's version. Default: Auto
        :param security_groups: The list of security groups to associate with the Lambda's network interfaces. Only used if 'vpc' is supplied. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroup prop, a dedicated security group will be created for this function.
        :param snap_start: Enable SnapStart for Lambda Function. SnapStart is currently supported only for Java 11, 17 runtime Default: - No snapstart
        :param system_log_level: (deprecated) Sets the system log level for the function. Default: "INFO"
        :param system_log_level_v2: Sets the system log level for the function. Default: SystemLogLevel.INFO
        :param timeout: The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: Duration.seconds(3)
        :param tracing: Enable AWS X-Ray Tracing for Lambda Function. Default: Tracing.Disabled
        :param vpc: VPC network to place Lambda network interfaces. Specify this if the Lambda function needs to access resources in a VPC. This is required when ``vpcSubnets`` is specified. Default: - Function is not placed within a VPC.
        :param vpc_subnets: Where to place the network interfaces within the VPC. This requires ``vpc`` to be specified in order for interfaces to actually be placed in the subnets. If ``vpc`` is not specify, this will raise an error. Note: Internet access for Lambda Functions requires a NAT Gateway, so picking public subnets is not allowed (unless ``allowPublicSubnet`` is set to ``true``). Default: - the Vpc default strategy if not specified
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: The destination for failed invocations. Default: - no destination
        :param on_success: The destination for successful invocations. Default: - no destination
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f4b27a9e71783873da8f30bb12ae1f28cc9da3f8ddc294f9bd54cf8dabd8506)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = PythonFunctionProps(
            root_dir=root_dir,
            bundling=bundling,
            handler=handler,
            index=index,
            runtime=runtime,
            workspace_package=workspace_package,
            adot_instrumentation=adot_instrumentation,
            allow_all_ipv6_outbound=allow_all_ipv6_outbound,
            allow_all_outbound=allow_all_outbound,
            allow_public_subnet=allow_public_subnet,
            application_log_level=application_log_level,
            application_log_level_v2=application_log_level_v2,
            architecture=architecture,
            code_signing_config=code_signing_config,
            current_version_options=current_version_options,
            dead_letter_queue=dead_letter_queue,
            dead_letter_queue_enabled=dead_letter_queue_enabled,
            dead_letter_topic=dead_letter_topic,
            description=description,
            environment=environment,
            environment_encryption=environment_encryption,
            ephemeral_storage_size=ephemeral_storage_size,
            events=events,
            filesystem=filesystem,
            function_name=function_name,
            initial_policy=initial_policy,
            insights_version=insights_version,
            ipv6_allowed_for_dual_stack=ipv6_allowed_for_dual_stack,
            layers=layers,
            log_format=log_format,
            logging_format=logging_format,
            log_group=log_group,
            log_retention=log_retention,
            log_retention_retry_options=log_retention_retry_options,
            log_retention_role=log_retention_role,
            memory_size=memory_size,
            params_and_secrets=params_and_secrets,
            profiling=profiling,
            profiling_group=profiling_group,
            recursive_loop=recursive_loop,
            reserved_concurrent_executions=reserved_concurrent_executions,
            role=role,
            runtime_management_mode=runtime_management_mode,
            security_groups=security_groups,
            snap_start=snap_start,
            system_log_level=system_log_level,
            system_log_level_v2=system_log_level_v2,
            timeout=timeout,
            tracing=tracing,
            vpc=vpc,
            vpc_subnets=vpc_subnets,
            max_event_age=max_event_age,
            on_failure=on_failure,
            on_success=on_success,
            retry_attempts=retry_attempts,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="uv-python-lambda.PythonFunctionProps",
    jsii_struct_bases=[_aws_cdk_aws_lambda_ceddda9d.FunctionOptions],
    name_mapping={
        "max_event_age": "maxEventAge",
        "on_failure": "onFailure",
        "on_success": "onSuccess",
        "retry_attempts": "retryAttempts",
        "adot_instrumentation": "adotInstrumentation",
        "allow_all_ipv6_outbound": "allowAllIpv6Outbound",
        "allow_all_outbound": "allowAllOutbound",
        "allow_public_subnet": "allowPublicSubnet",
        "application_log_level": "applicationLogLevel",
        "application_log_level_v2": "applicationLogLevelV2",
        "architecture": "architecture",
        "code_signing_config": "codeSigningConfig",
        "current_version_options": "currentVersionOptions",
        "dead_letter_queue": "deadLetterQueue",
        "dead_letter_queue_enabled": "deadLetterQueueEnabled",
        "dead_letter_topic": "deadLetterTopic",
        "description": "description",
        "environment": "environment",
        "environment_encryption": "environmentEncryption",
        "ephemeral_storage_size": "ephemeralStorageSize",
        "events": "events",
        "filesystem": "filesystem",
        "function_name": "functionName",
        "initial_policy": "initialPolicy",
        "insights_version": "insightsVersion",
        "ipv6_allowed_for_dual_stack": "ipv6AllowedForDualStack",
        "layers": "layers",
        "log_format": "logFormat",
        "logging_format": "loggingFormat",
        "log_group": "logGroup",
        "log_retention": "logRetention",
        "log_retention_retry_options": "logRetentionRetryOptions",
        "log_retention_role": "logRetentionRole",
        "memory_size": "memorySize",
        "params_and_secrets": "paramsAndSecrets",
        "profiling": "profiling",
        "profiling_group": "profilingGroup",
        "recursive_loop": "recursiveLoop",
        "reserved_concurrent_executions": "reservedConcurrentExecutions",
        "role": "role",
        "runtime_management_mode": "runtimeManagementMode",
        "security_groups": "securityGroups",
        "snap_start": "snapStart",
        "system_log_level": "systemLogLevel",
        "system_log_level_v2": "systemLogLevelV2",
        "timeout": "timeout",
        "tracing": "tracing",
        "vpc": "vpc",
        "vpc_subnets": "vpcSubnets",
        "root_dir": "rootDir",
        "bundling": "bundling",
        "handler": "handler",
        "index": "index",
        "runtime": "runtime",
        "workspace_package": "workspacePackage",
    },
)
class PythonFunctionProps(_aws_cdk_aws_lambda_ceddda9d.FunctionOptions):
    def __init__(
        self,
        *,
        max_event_age: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        on_failure: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.IDestination] = None,
        on_success: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.IDestination] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        adot_instrumentation: typing.Optional[typing.Union[_aws_cdk_aws_lambda_ceddda9d.AdotInstrumentationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        allow_all_ipv6_outbound: typing.Optional[builtins.bool] = None,
        allow_all_outbound: typing.Optional[builtins.bool] = None,
        allow_public_subnet: typing.Optional[builtins.bool] = None,
        application_log_level: typing.Optional[builtins.str] = None,
        application_log_level_v2: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.ApplicationLogLevel] = None,
        architecture: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.Architecture] = None,
        code_signing_config: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.ICodeSigningConfig] = None,
        current_version_options: typing.Optional[typing.Union[_aws_cdk_aws_lambda_ceddda9d.VersionOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        dead_letter_queue: typing.Optional[_aws_cdk_aws_sqs_ceddda9d.IQueue] = None,
        dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
        dead_letter_topic: typing.Optional[_aws_cdk_aws_sns_ceddda9d.ITopic] = None,
        description: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        environment_encryption: typing.Optional[_aws_cdk_aws_kms_ceddda9d.IKey] = None,
        ephemeral_storage_size: typing.Optional[_aws_cdk_ceddda9d.Size] = None,
        events: typing.Optional[typing.Sequence[_aws_cdk_aws_lambda_ceddda9d.IEventSource]] = None,
        filesystem: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.FileSystem] = None,
        function_name: typing.Optional[builtins.str] = None,
        initial_policy: typing.Optional[typing.Sequence[_aws_cdk_aws_iam_ceddda9d.PolicyStatement]] = None,
        insights_version: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.LambdaInsightsVersion] = None,
        ipv6_allowed_for_dual_stack: typing.Optional[builtins.bool] = None,
        layers: typing.Optional[typing.Sequence[_aws_cdk_aws_lambda_ceddda9d.ILayerVersion]] = None,
        log_format: typing.Optional[builtins.str] = None,
        logging_format: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.LoggingFormat] = None,
        log_group: typing.Optional[_aws_cdk_aws_logs_ceddda9d.ILogGroup] = None,
        log_retention: typing.Optional[_aws_cdk_aws_logs_ceddda9d.RetentionDays] = None,
        log_retention_retry_options: typing.Optional[typing.Union[_aws_cdk_aws_lambda_ceddda9d.LogRetentionRetryOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        log_retention_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        params_and_secrets: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.ParamsAndSecretsLayerVersion] = None,
        profiling: typing.Optional[builtins.bool] = None,
        profiling_group: typing.Optional[_aws_cdk_aws_codeguruprofiler_ceddda9d.IProfilingGroup] = None,
        recursive_loop: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.RecursiveLoop] = None,
        reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        runtime_management_mode: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.RuntimeManagementMode] = None,
        security_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup]] = None,
        snap_start: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.SnapStartConf] = None,
        system_log_level: typing.Optional[builtins.str] = None,
        system_log_level_v2: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.SystemLogLevel] = None,
        timeout: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        tracing: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.Tracing] = None,
        vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
        vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
        root_dir: builtins.str,
        bundling: typing.Optional[typing.Union[BundlingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        handler: typing.Optional[builtins.str] = None,
        index: typing.Optional[builtins.str] = None,
        runtime: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.Runtime] = None,
        workspace_package: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: The destination for failed invocations. Default: - no destination
        :param on_success: The destination for successful invocations. Default: - no destination
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2
        :param adot_instrumentation: Specify the configuration of AWS Distro for OpenTelemetry (ADOT) instrumentation. Default: - No ADOT instrumentation
        :param allow_all_ipv6_outbound: Whether to allow the Lambda to send all ipv6 network traffic. If set to true, there will only be a single egress rule which allows all outbound ipv6 traffic. If set to false, you must individually add traffic rules to allow the Lambda to connect to network targets using ipv6. Do not specify this property if the ``securityGroups`` or ``securityGroup`` property is set. Instead, configure ``allowAllIpv6Outbound`` directly on the security group. Default: false
        :param allow_all_outbound: Whether to allow the Lambda to send all network traffic (except ipv6). If set to false, you must individually add traffic rules to allow the Lambda to connect to network targets. Do not specify this property if the ``securityGroups`` or ``securityGroup`` property is set. Instead, configure ``allowAllOutbound`` directly on the security group. Default: true
        :param allow_public_subnet: Lambda Functions in a public subnet can NOT access the internet. Use this property to acknowledge this limitation and still place the function in a public subnet. Default: false
        :param application_log_level: (deprecated) Sets the application log level for the function. Default: "INFO"
        :param application_log_level_v2: Sets the application log level for the function. Default: ApplicationLogLevel.INFO
        :param architecture: The system architectures compatible with this lambda function. Default: Architecture.X86_64
        :param code_signing_config: Code signing config associated with this function. Default: - Not Sign the Code
        :param current_version_options: Options for the ``lambda.Version`` resource automatically created by the ``fn.currentVersion`` method. Default: - default options as described in ``VersionOptions``
        :param dead_letter_queue: The SQS queue to use if DLQ is enabled. If SNS topic is desired, specify ``deadLetterTopic`` property instead. Default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``
        :param dead_letter_queue_enabled: Enabled DLQ. If ``deadLetterQueue`` is undefined, an SQS queue with default options will be defined for your Function. Default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.
        :param dead_letter_topic: The SNS topic to use as a DLQ. Note that if ``deadLetterQueueEnabled`` is set to ``true``, an SQS queue will be created rather than an SNS topic. Using an SNS topic as a DLQ requires this property to be set explicitly. Default: - no SNS topic
        :param description: A description of the function. Default: - No description.
        :param environment: Key-value pairs that Lambda caches and makes available for your Lambda functions. Use environment variables to apply configuration changes, such as test and production environment configurations, without changing your Lambda function source code. Default: - No environment variables.
        :param environment_encryption: The AWS KMS key that's used to encrypt your function's environment variables. Default: - AWS Lambda creates and uses an AWS managed customer master key (CMK).
        :param ephemeral_storage_size: The size of the function’s /tmp directory in MiB. Default: 512 MiB
        :param events: Event sources for this function. You can also add event sources using ``addEventSource``. Default: - No event sources.
        :param filesystem: The filesystem configuration for the lambda function. Default: - will not mount any filesystem
        :param function_name: A name for the function. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the function's name. For more information, see Name Type.
        :param initial_policy: Initial policy statements to add to the created Lambda Role. You can call ``addToRolePolicy`` to the created lambda to add statements post creation. Default: - No policy statements are added to the created Lambda role.
        :param insights_version: Specify the version of CloudWatch Lambda insights to use for monitoring. Default: - No Lambda Insights
        :param ipv6_allowed_for_dual_stack: Allows outbound IPv6 traffic on VPC functions that are connected to dual-stack subnets. Only used if 'vpc' is supplied. Default: false
        :param layers: A list of layers to add to the function's execution environment. You can configure your Lambda function to pull in additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies that can be used by multiple functions. Default: - No layers.
        :param log_format: (deprecated) Sets the logFormat for the function. Default: "Text"
        :param logging_format: Sets the loggingFormat for the function. Default: LoggingFormat.TEXT
        :param log_group: The log group the function sends logs to. By default, Lambda functions send logs to an automatically created default log group named /aws/lambda/<function name>. However you cannot change the properties of this auto-created log group using the AWS CDK, e.g. you cannot set a different log retention. Use the ``logGroup`` property to create a fully customizable LogGroup ahead of time, and instruct the Lambda function to send logs to it. Providing a user-controlled log group was rolled out to commercial regions on 2023-11-16. If you are deploying to another type of region, please check regional availability first. Default: ``/aws/lambda/${this.functionName}`` - default log group created by Lambda
        :param log_retention: The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. This is a legacy API and we strongly recommend you move away from it if you can. Instead create a fully customizable log group with ``logs.LogGroup`` and use the ``logGroup`` property to instruct the Lambda function to send logs to it. Migrating from ``logRetention`` to ``logGroup`` will cause the name of the log group to change. Users and code and referencing the name verbatim will have to adjust. In AWS CDK code, you can access the log group name directly from the LogGroup construct:: import * as logs from 'aws-cdk-lib/aws-logs'; declare const myLogGroup: logs.LogGroup; myLogGroup.logGroupName; Default: logs.RetentionDays.INFINITE
        :param log_retention_retry_options: When log retention is specified, a custom resource attempts to create the CloudWatch log group. These options control the retry policy when interacting with CloudWatch APIs. This is a legacy API and we strongly recommend you migrate to ``logGroup`` if you can. ``logGroup`` allows you to create a fully customizable log group and instruct the Lambda function to send logs to it. Default: - Default AWS SDK retry options.
        :param log_retention_role: The IAM role for the Lambda function associated with the custom resource that sets the retention policy. This is a legacy API and we strongly recommend you migrate to ``logGroup`` if you can. ``logGroup`` allows you to create a fully customizable log group and instruct the Lambda function to send logs to it. Default: - A new role is created.
        :param memory_size: The amount of memory, in MB, that is allocated to your Lambda function. Lambda uses this value to proportionally allocate the amount of CPU power. For more information, see Resource Model in the AWS Lambda Developer Guide. Default: 128
        :param params_and_secrets: Specify the configuration of Parameters and Secrets Extension. Default: - No Parameters and Secrets Extension
        :param profiling: Enable profiling. Default: - No profiling.
        :param profiling_group: Profiling Group. Default: - A new profiling group will be created if ``profiling`` is set.
        :param recursive_loop: Sets the Recursive Loop Protection for Lambda Function. It lets Lambda detect and terminate unintended recusrive loops. Default: RecursiveLoop.Terminate
        :param reserved_concurrent_executions: The maximum of concurrent executions you want to reserve for the function. Default: - No specific limit - account limit.
        :param role: Lambda execution role. This is the role that will be assumed by the function upon execution. It controls the permissions that the function will have. The Role must be assumable by the 'lambda.amazonaws.com' service principal. The default Role automatically has permissions granted for Lambda execution. If you provide a Role, you must add the relevant AWS managed policies yourself. The relevant managed policies are "service-role/AWSLambdaBasicExecutionRole" and "service-role/AWSLambdaVPCAccessExecutionRole". Default: - A unique role will be generated for this lambda function. Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.
        :param runtime_management_mode: Sets the runtime management configuration for a function's version. Default: Auto
        :param security_groups: The list of security groups to associate with the Lambda's network interfaces. Only used if 'vpc' is supplied. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroup prop, a dedicated security group will be created for this function.
        :param snap_start: Enable SnapStart for Lambda Function. SnapStart is currently supported only for Java 11, 17 runtime Default: - No snapstart
        :param system_log_level: (deprecated) Sets the system log level for the function. Default: "INFO"
        :param system_log_level_v2: Sets the system log level for the function. Default: SystemLogLevel.INFO
        :param timeout: The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: Duration.seconds(3)
        :param tracing: Enable AWS X-Ray Tracing for Lambda Function. Default: Tracing.Disabled
        :param vpc: VPC network to place Lambda network interfaces. Specify this if the Lambda function needs to access resources in a VPC. This is required when ``vpcSubnets`` is specified. Default: - Function is not placed within a VPC.
        :param vpc_subnets: Where to place the network interfaces within the VPC. This requires ``vpc`` to be specified in order for interfaces to actually be placed in the subnets. If ``vpc`` is not specify, this will raise an error. Note: Internet access for Lambda Functions requires a NAT Gateway, so picking public subnets is not allowed (unless ``allowPublicSubnet`` is set to ``true``). Default: - the Vpc default strategy if not specified
        :param root_dir: UV project root directory (workspace root).
        :param bundling: Custom bundling options, including build architecture and bundling container image.
        :param handler: The name of the exported handler function in the #index. Default: handler
        :param index: The path to the index file with the project or (or workspace, if specified) containing the handler. Default: index.py
        :param runtime: The runtime. Default: Runtime.PYTHON_3_12
        :param workspace_package: Optional UV project workspace, used to specify a specific package to be used as a Lambda Function entry.
        '''
        if isinstance(adot_instrumentation, dict):
            adot_instrumentation = _aws_cdk_aws_lambda_ceddda9d.AdotInstrumentationConfig(**adot_instrumentation)
        if isinstance(current_version_options, dict):
            current_version_options = _aws_cdk_aws_lambda_ceddda9d.VersionOptions(**current_version_options)
        if isinstance(log_retention_retry_options, dict):
            log_retention_retry_options = _aws_cdk_aws_lambda_ceddda9d.LogRetentionRetryOptions(**log_retention_retry_options)
        if isinstance(vpc_subnets, dict):
            vpc_subnets = _aws_cdk_aws_ec2_ceddda9d.SubnetSelection(**vpc_subnets)
        if isinstance(bundling, dict):
            bundling = BundlingOptions(**bundling)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9783d4735a5a328474d4c697ce9ae14150d27c171dc16c9970a5f60d92b82410)
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument on_failure", value=on_failure, expected_type=type_hints["on_failure"])
            check_type(argname="argument on_success", value=on_success, expected_type=type_hints["on_success"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument adot_instrumentation", value=adot_instrumentation, expected_type=type_hints["adot_instrumentation"])
            check_type(argname="argument allow_all_ipv6_outbound", value=allow_all_ipv6_outbound, expected_type=type_hints["allow_all_ipv6_outbound"])
            check_type(argname="argument allow_all_outbound", value=allow_all_outbound, expected_type=type_hints["allow_all_outbound"])
            check_type(argname="argument allow_public_subnet", value=allow_public_subnet, expected_type=type_hints["allow_public_subnet"])
            check_type(argname="argument application_log_level", value=application_log_level, expected_type=type_hints["application_log_level"])
            check_type(argname="argument application_log_level_v2", value=application_log_level_v2, expected_type=type_hints["application_log_level_v2"])
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
            check_type(argname="argument code_signing_config", value=code_signing_config, expected_type=type_hints["code_signing_config"])
            check_type(argname="argument current_version_options", value=current_version_options, expected_type=type_hints["current_version_options"])
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument dead_letter_queue_enabled", value=dead_letter_queue_enabled, expected_type=type_hints["dead_letter_queue_enabled"])
            check_type(argname="argument dead_letter_topic", value=dead_letter_topic, expected_type=type_hints["dead_letter_topic"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument environment_encryption", value=environment_encryption, expected_type=type_hints["environment_encryption"])
            check_type(argname="argument ephemeral_storage_size", value=ephemeral_storage_size, expected_type=type_hints["ephemeral_storage_size"])
            check_type(argname="argument events", value=events, expected_type=type_hints["events"])
            check_type(argname="argument filesystem", value=filesystem, expected_type=type_hints["filesystem"])
            check_type(argname="argument function_name", value=function_name, expected_type=type_hints["function_name"])
            check_type(argname="argument initial_policy", value=initial_policy, expected_type=type_hints["initial_policy"])
            check_type(argname="argument insights_version", value=insights_version, expected_type=type_hints["insights_version"])
            check_type(argname="argument ipv6_allowed_for_dual_stack", value=ipv6_allowed_for_dual_stack, expected_type=type_hints["ipv6_allowed_for_dual_stack"])
            check_type(argname="argument layers", value=layers, expected_type=type_hints["layers"])
            check_type(argname="argument log_format", value=log_format, expected_type=type_hints["log_format"])
            check_type(argname="argument logging_format", value=logging_format, expected_type=type_hints["logging_format"])
            check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
            check_type(argname="argument log_retention", value=log_retention, expected_type=type_hints["log_retention"])
            check_type(argname="argument log_retention_retry_options", value=log_retention_retry_options, expected_type=type_hints["log_retention_retry_options"])
            check_type(argname="argument log_retention_role", value=log_retention_role, expected_type=type_hints["log_retention_role"])
            check_type(argname="argument memory_size", value=memory_size, expected_type=type_hints["memory_size"])
            check_type(argname="argument params_and_secrets", value=params_and_secrets, expected_type=type_hints["params_and_secrets"])
            check_type(argname="argument profiling", value=profiling, expected_type=type_hints["profiling"])
            check_type(argname="argument profiling_group", value=profiling_group, expected_type=type_hints["profiling_group"])
            check_type(argname="argument recursive_loop", value=recursive_loop, expected_type=type_hints["recursive_loop"])
            check_type(argname="argument reserved_concurrent_executions", value=reserved_concurrent_executions, expected_type=type_hints["reserved_concurrent_executions"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument runtime_management_mode", value=runtime_management_mode, expected_type=type_hints["runtime_management_mode"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument snap_start", value=snap_start, expected_type=type_hints["snap_start"])
            check_type(argname="argument system_log_level", value=system_log_level, expected_type=type_hints["system_log_level"])
            check_type(argname="argument system_log_level_v2", value=system_log_level_v2, expected_type=type_hints["system_log_level_v2"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument tracing", value=tracing, expected_type=type_hints["tracing"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
            check_type(argname="argument root_dir", value=root_dir, expected_type=type_hints["root_dir"])
            check_type(argname="argument bundling", value=bundling, expected_type=type_hints["bundling"])
            check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
            check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
            check_type(argname="argument workspace_package", value=workspace_package, expected_type=type_hints["workspace_package"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "root_dir": root_dir,
        }
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if on_failure is not None:
            self._values["on_failure"] = on_failure
        if on_success is not None:
            self._values["on_success"] = on_success
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if adot_instrumentation is not None:
            self._values["adot_instrumentation"] = adot_instrumentation
        if allow_all_ipv6_outbound is not None:
            self._values["allow_all_ipv6_outbound"] = allow_all_ipv6_outbound
        if allow_all_outbound is not None:
            self._values["allow_all_outbound"] = allow_all_outbound
        if allow_public_subnet is not None:
            self._values["allow_public_subnet"] = allow_public_subnet
        if application_log_level is not None:
            self._values["application_log_level"] = application_log_level
        if application_log_level_v2 is not None:
            self._values["application_log_level_v2"] = application_log_level_v2
        if architecture is not None:
            self._values["architecture"] = architecture
        if code_signing_config is not None:
            self._values["code_signing_config"] = code_signing_config
        if current_version_options is not None:
            self._values["current_version_options"] = current_version_options
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if dead_letter_queue_enabled is not None:
            self._values["dead_letter_queue_enabled"] = dead_letter_queue_enabled
        if dead_letter_topic is not None:
            self._values["dead_letter_topic"] = dead_letter_topic
        if description is not None:
            self._values["description"] = description
        if environment is not None:
            self._values["environment"] = environment
        if environment_encryption is not None:
            self._values["environment_encryption"] = environment_encryption
        if ephemeral_storage_size is not None:
            self._values["ephemeral_storage_size"] = ephemeral_storage_size
        if events is not None:
            self._values["events"] = events
        if filesystem is not None:
            self._values["filesystem"] = filesystem
        if function_name is not None:
            self._values["function_name"] = function_name
        if initial_policy is not None:
            self._values["initial_policy"] = initial_policy
        if insights_version is not None:
            self._values["insights_version"] = insights_version
        if ipv6_allowed_for_dual_stack is not None:
            self._values["ipv6_allowed_for_dual_stack"] = ipv6_allowed_for_dual_stack
        if layers is not None:
            self._values["layers"] = layers
        if log_format is not None:
            self._values["log_format"] = log_format
        if logging_format is not None:
            self._values["logging_format"] = logging_format
        if log_group is not None:
            self._values["log_group"] = log_group
        if log_retention is not None:
            self._values["log_retention"] = log_retention
        if log_retention_retry_options is not None:
            self._values["log_retention_retry_options"] = log_retention_retry_options
        if log_retention_role is not None:
            self._values["log_retention_role"] = log_retention_role
        if memory_size is not None:
            self._values["memory_size"] = memory_size
        if params_and_secrets is not None:
            self._values["params_and_secrets"] = params_and_secrets
        if profiling is not None:
            self._values["profiling"] = profiling
        if profiling_group is not None:
            self._values["profiling_group"] = profiling_group
        if recursive_loop is not None:
            self._values["recursive_loop"] = recursive_loop
        if reserved_concurrent_executions is not None:
            self._values["reserved_concurrent_executions"] = reserved_concurrent_executions
        if role is not None:
            self._values["role"] = role
        if runtime_management_mode is not None:
            self._values["runtime_management_mode"] = runtime_management_mode
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if snap_start is not None:
            self._values["snap_start"] = snap_start
        if system_log_level is not None:
            self._values["system_log_level"] = system_log_level
        if system_log_level_v2 is not None:
            self._values["system_log_level_v2"] = system_log_level_v2
        if timeout is not None:
            self._values["timeout"] = timeout
        if tracing is not None:
            self._values["tracing"] = tracing
        if vpc is not None:
            self._values["vpc"] = vpc
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets
        if bundling is not None:
            self._values["bundling"] = bundling
        if handler is not None:
            self._values["handler"] = handler
        if index is not None:
            self._values["index"] = index
        if runtime is not None:
            self._values["runtime"] = runtime
        if workspace_package is not None:
            self._values["workspace_package"] = workspace_package

    @builtins.property
    def max_event_age(self) -> typing.Optional[_aws_cdk_ceddda9d.Duration]:
        '''The maximum age of a request that Lambda sends to a function for processing.

        Minimum: 60 seconds
        Maximum: 6 hours

        :default: Duration.hours(6)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.Duration], result)

    @builtins.property
    def on_failure(self) -> typing.Optional[_aws_cdk_aws_lambda_ceddda9d.IDestination]:
        '''The destination for failed invocations.

        :default: - no destination
        '''
        result = self._values.get("on_failure")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_ceddda9d.IDestination], result)

    @builtins.property
    def on_success(self) -> typing.Optional[_aws_cdk_aws_lambda_ceddda9d.IDestination]:
        '''The destination for successful invocations.

        :default: - no destination
        '''
        result = self._values.get("on_success")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_ceddda9d.IDestination], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the function returns an error.

        Minimum: 0
        Maximum: 2

        :default: 2
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def adot_instrumentation(
        self,
    ) -> typing.Optional[_aws_cdk_aws_lambda_ceddda9d.AdotInstrumentationConfig]:
        '''Specify the configuration of AWS Distro for OpenTelemetry (ADOT) instrumentation.

        :default: - No ADOT instrumentation

        :see: https://aws-otel.github.io/docs/getting-started/lambda
        '''
        result = self._values.get("adot_instrumentation")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_ceddda9d.AdotInstrumentationConfig], result)

    @builtins.property
    def allow_all_ipv6_outbound(self) -> typing.Optional[builtins.bool]:
        '''Whether to allow the Lambda to send all ipv6 network traffic.

        If set to true, there will only be a single egress rule which allows all
        outbound ipv6 traffic. If set to false, you must individually add traffic rules to allow the
        Lambda to connect to network targets using ipv6.

        Do not specify this property if the ``securityGroups`` or ``securityGroup`` property is set.
        Instead, configure ``allowAllIpv6Outbound`` directly on the security group.

        :default: false
        '''
        result = self._values.get("allow_all_ipv6_outbound")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def allow_all_outbound(self) -> typing.Optional[builtins.bool]:
        '''Whether to allow the Lambda to send all network traffic (except ipv6).

        If set to false, you must individually add traffic rules to allow the
        Lambda to connect to network targets.

        Do not specify this property if the ``securityGroups`` or ``securityGroup`` property is set.
        Instead, configure ``allowAllOutbound`` directly on the security group.

        :default: true
        '''
        result = self._values.get("allow_all_outbound")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def allow_public_subnet(self) -> typing.Optional[builtins.bool]:
        '''Lambda Functions in a public subnet can NOT access the internet.

        Use this property to acknowledge this limitation and still place the function in a public subnet.

        :default: false

        :see: https://stackoverflow.com/questions/52992085/why-cant-an-aws-lambda-function-inside-a-public-subnet-in-a-vpc-connect-to-the/52994841#52994841
        '''
        result = self._values.get("allow_public_subnet")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def application_log_level(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Sets the application log level for the function.

        :default: "INFO"

        :deprecated: Use ``applicationLogLevelV2`` as a property instead.

        :stability: deprecated
        '''
        result = self._values.get("application_log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def application_log_level_v2(
        self,
    ) -> typing.Optional[_aws_cdk_aws_lambda_ceddda9d.ApplicationLogLevel]:
        '''Sets the application log level for the function.

        :default: ApplicationLogLevel.INFO
        '''
        result = self._values.get("application_log_level_v2")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_ceddda9d.ApplicationLogLevel], result)

    @builtins.property
    def architecture(
        self,
    ) -> typing.Optional[_aws_cdk_aws_lambda_ceddda9d.Architecture]:
        '''The system architectures compatible with this lambda function.

        :default: Architecture.X86_64
        '''
        result = self._values.get("architecture")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_ceddda9d.Architecture], result)

    @builtins.property
    def code_signing_config(
        self,
    ) -> typing.Optional[_aws_cdk_aws_lambda_ceddda9d.ICodeSigningConfig]:
        '''Code signing config associated with this function.

        :default: - Not Sign the Code
        '''
        result = self._values.get("code_signing_config")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_ceddda9d.ICodeSigningConfig], result)

    @builtins.property
    def current_version_options(
        self,
    ) -> typing.Optional[_aws_cdk_aws_lambda_ceddda9d.VersionOptions]:
        '''Options for the ``lambda.Version`` resource automatically created by the ``fn.currentVersion`` method.

        :default: - default options as described in ``VersionOptions``
        '''
        result = self._values.get("current_version_options")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_ceddda9d.VersionOptions], result)

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_aws_cdk_aws_sqs_ceddda9d.IQueue]:
        '''The SQS queue to use if DLQ is enabled.

        If SNS topic is desired, specify ``deadLetterTopic`` property instead.

        :default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_aws_cdk_aws_sqs_ceddda9d.IQueue], result)

    @builtins.property
    def dead_letter_queue_enabled(self) -> typing.Optional[builtins.bool]:
        '''Enabled DLQ.

        If ``deadLetterQueue`` is undefined,
        an SQS queue with default options will be defined for your Function.

        :default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.
        '''
        result = self._values.get("dead_letter_queue_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def dead_letter_topic(self) -> typing.Optional[_aws_cdk_aws_sns_ceddda9d.ITopic]:
        '''The SNS topic to use as a DLQ.

        Note that if ``deadLetterQueueEnabled`` is set to ``true``, an SQS queue will be created
        rather than an SNS topic. Using an SNS topic as a DLQ requires this property to be set explicitly.

        :default: - no SNS topic
        '''
        result = self._values.get("dead_letter_topic")
        return typing.cast(typing.Optional[_aws_cdk_aws_sns_ceddda9d.ITopic], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the function.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Key-value pairs that Lambda caches and makes available for your Lambda functions.

        Use environment variables to apply configuration changes, such
        as test and production environment configurations, without changing your
        Lambda function source code.

        :default: - No environment variables.
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def environment_encryption(self) -> typing.Optional[_aws_cdk_aws_kms_ceddda9d.IKey]:
        '''The AWS KMS key that's used to encrypt your function's environment variables.

        :default: - AWS Lambda creates and uses an AWS managed customer master key (CMK).
        '''
        result = self._values.get("environment_encryption")
        return typing.cast(typing.Optional[_aws_cdk_aws_kms_ceddda9d.IKey], result)

    @builtins.property
    def ephemeral_storage_size(self) -> typing.Optional[_aws_cdk_ceddda9d.Size]:
        '''The size of the function’s /tmp directory in MiB.

        :default: 512 MiB
        '''
        result = self._values.get("ephemeral_storage_size")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.Size], result)

    @builtins.property
    def events(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_lambda_ceddda9d.IEventSource]]:
        '''Event sources for this function.

        You can also add event sources using ``addEventSource``.

        :default: - No event sources.
        '''
        result = self._values.get("events")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_lambda_ceddda9d.IEventSource]], result)

    @builtins.property
    def filesystem(self) -> typing.Optional[_aws_cdk_aws_lambda_ceddda9d.FileSystem]:
        '''The filesystem configuration for the lambda function.

        :default: - will not mount any filesystem
        '''
        result = self._values.get("filesystem")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_ceddda9d.FileSystem], result)

    @builtins.property
    def function_name(self) -> typing.Optional[builtins.str]:
        '''A name for the function.

        :default:

        - AWS CloudFormation generates a unique physical ID and uses that
        ID for the function's name. For more information, see Name Type.
        '''
        result = self._values.get("function_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initial_policy(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_iam_ceddda9d.PolicyStatement]]:
        '''Initial policy statements to add to the created Lambda Role.

        You can call ``addToRolePolicy`` to the created lambda to add statements post creation.

        :default: - No policy statements are added to the created Lambda role.
        '''
        result = self._values.get("initial_policy")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_iam_ceddda9d.PolicyStatement]], result)

    @builtins.property
    def insights_version(
        self,
    ) -> typing.Optional[_aws_cdk_aws_lambda_ceddda9d.LambdaInsightsVersion]:
        '''Specify the version of CloudWatch Lambda insights to use for monitoring.

        :default: - No Lambda Insights

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights-Getting-Started-docker.html
        '''
        result = self._values.get("insights_version")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_ceddda9d.LambdaInsightsVersion], result)

    @builtins.property
    def ipv6_allowed_for_dual_stack(self) -> typing.Optional[builtins.bool]:
        '''Allows outbound IPv6 traffic on VPC functions that are connected to dual-stack subnets.

        Only used if 'vpc' is supplied.

        :default: false
        '''
        result = self._values.get("ipv6_allowed_for_dual_stack")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def layers(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_lambda_ceddda9d.ILayerVersion]]:
        '''A list of layers to add to the function's execution environment.

        You can configure your Lambda function to pull in
        additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies
        that can be used by multiple functions.

        :default: - No layers.
        '''
        result = self._values.get("layers")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_lambda_ceddda9d.ILayerVersion]], result)

    @builtins.property
    def log_format(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Sets the logFormat for the function.

        :default: "Text"

        :deprecated: Use ``loggingFormat`` as a property instead.

        :stability: deprecated
        '''
        result = self._values.get("log_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_format(
        self,
    ) -> typing.Optional[_aws_cdk_aws_lambda_ceddda9d.LoggingFormat]:
        '''Sets the loggingFormat for the function.

        :default: LoggingFormat.TEXT
        '''
        result = self._values.get("logging_format")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_ceddda9d.LoggingFormat], result)

    @builtins.property
    def log_group(self) -> typing.Optional[_aws_cdk_aws_logs_ceddda9d.ILogGroup]:
        '''The log group the function sends logs to.

        By default, Lambda functions send logs to an automatically created default log group named /aws/lambda/.
        However you cannot change the properties of this auto-created log group using the AWS CDK, e.g. you cannot set a different log retention.

        Use the ``logGroup`` property to create a fully customizable LogGroup ahead of time, and instruct the Lambda function to send logs to it.

        Providing a user-controlled log group was rolled out to commercial regions on 2023-11-16.
        If you are deploying to another type of region, please check regional availability first.

        :default: ``/aws/lambda/${this.functionName}`` - default log group created by Lambda
        '''
        result = self._values.get("log_group")
        return typing.cast(typing.Optional[_aws_cdk_aws_logs_ceddda9d.ILogGroup], result)

    @builtins.property
    def log_retention(
        self,
    ) -> typing.Optional[_aws_cdk_aws_logs_ceddda9d.RetentionDays]:
        '''The number of days log events are kept in CloudWatch Logs.

        When updating
        this property, unsetting it doesn't remove the log retention policy. To
        remove the retention policy, set the value to ``INFINITE``.

        This is a legacy API and we strongly recommend you move away from it if you can.
        Instead create a fully customizable log group with ``logs.LogGroup`` and use the ``logGroup`` property
        to instruct the Lambda function to send logs to it.
        Migrating from ``logRetention`` to ``logGroup`` will cause the name of the log group to change.
        Users and code and referencing the name verbatim will have to adjust.

        In AWS CDK code, you can access the log group name directly from the LogGroup construct::

           import * as logs from 'aws-cdk-lib/aws-logs';

           declare const myLogGroup: logs.LogGroup;
           myLogGroup.logGroupName;

        :default: logs.RetentionDays.INFINITE
        '''
        result = self._values.get("log_retention")
        return typing.cast(typing.Optional[_aws_cdk_aws_logs_ceddda9d.RetentionDays], result)

    @builtins.property
    def log_retention_retry_options(
        self,
    ) -> typing.Optional[_aws_cdk_aws_lambda_ceddda9d.LogRetentionRetryOptions]:
        '''When log retention is specified, a custom resource attempts to create the CloudWatch log group.

        These options control the retry policy when interacting with CloudWatch APIs.

        This is a legacy API and we strongly recommend you migrate to ``logGroup`` if you can.
        ``logGroup`` allows you to create a fully customizable log group and instruct the Lambda function to send logs to it.

        :default: - Default AWS SDK retry options.
        '''
        result = self._values.get("log_retention_retry_options")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_ceddda9d.LogRetentionRetryOptions], result)

    @builtins.property
    def log_retention_role(self) -> typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole]:
        '''The IAM role for the Lambda function associated with the custom resource that sets the retention policy.

        This is a legacy API and we strongly recommend you migrate to ``logGroup`` if you can.
        ``logGroup`` allows you to create a fully customizable log group and instruct the Lambda function to send logs to it.

        :default: - A new role is created.
        '''
        result = self._values.get("log_retention_role")
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole], result)

    @builtins.property
    def memory_size(self) -> typing.Optional[jsii.Number]:
        '''The amount of memory, in MB, that is allocated to your Lambda function.

        Lambda uses this value to proportionally allocate the amount of CPU
        power. For more information, see Resource Model in the AWS Lambda
        Developer Guide.

        :default: 128
        '''
        result = self._values.get("memory_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def params_and_secrets(
        self,
    ) -> typing.Optional[_aws_cdk_aws_lambda_ceddda9d.ParamsAndSecretsLayerVersion]:
        '''Specify the configuration of Parameters and Secrets Extension.

        :default: - No Parameters and Secrets Extension

        :see: https://docs.aws.amazon.com/systems-manager/latest/userguide/ps-integration-lambda-extensions.html
        '''
        result = self._values.get("params_and_secrets")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_ceddda9d.ParamsAndSecretsLayerVersion], result)

    @builtins.property
    def profiling(self) -> typing.Optional[builtins.bool]:
        '''Enable profiling.

        :default: - No profiling.

        :see: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/setting-up-lambda.html
        '''
        result = self._values.get("profiling")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def profiling_group(
        self,
    ) -> typing.Optional[_aws_cdk_aws_codeguruprofiler_ceddda9d.IProfilingGroup]:
        '''Profiling Group.

        :default: - A new profiling group will be created if ``profiling`` is set.

        :see: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/setting-up-lambda.html
        '''
        result = self._values.get("profiling_group")
        return typing.cast(typing.Optional[_aws_cdk_aws_codeguruprofiler_ceddda9d.IProfilingGroup], result)

    @builtins.property
    def recursive_loop(
        self,
    ) -> typing.Optional[_aws_cdk_aws_lambda_ceddda9d.RecursiveLoop]:
        '''Sets the Recursive Loop Protection for Lambda Function.

        It lets Lambda detect and terminate unintended recusrive loops.

        :default: RecursiveLoop.Terminate
        '''
        result = self._values.get("recursive_loop")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_ceddda9d.RecursiveLoop], result)

    @builtins.property
    def reserved_concurrent_executions(self) -> typing.Optional[jsii.Number]:
        '''The maximum of concurrent executions you want to reserve for the function.

        :default: - No specific limit - account limit.

        :see: https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html
        '''
        result = self._values.get("reserved_concurrent_executions")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def role(self) -> typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole]:
        '''Lambda execution role.

        This is the role that will be assumed by the function upon execution.
        It controls the permissions that the function will have. The Role must
        be assumable by the 'lambda.amazonaws.com' service principal.

        The default Role automatically has permissions granted for Lambda execution. If you
        provide a Role, you must add the relevant AWS managed policies yourself.

        The relevant managed policies are "service-role/AWSLambdaBasicExecutionRole" and
        "service-role/AWSLambdaVPCAccessExecutionRole".

        :default:

        - A unique role will be generated for this lambda function.
        Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole], result)

    @builtins.property
    def runtime_management_mode(
        self,
    ) -> typing.Optional[_aws_cdk_aws_lambda_ceddda9d.RuntimeManagementMode]:
        '''Sets the runtime management configuration for a function's version.

        :default: Auto
        '''
        result = self._values.get("runtime_management_mode")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_ceddda9d.RuntimeManagementMode], result)

    @builtins.property
    def security_groups(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup]]:
        '''The list of security groups to associate with the Lambda's network interfaces.

        Only used if 'vpc' is supplied.

        :default:

        - If the function is placed within a VPC and a security group is
        not specified, either by this or securityGroup prop, a dedicated security
        group will be created for this function.
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup]], result)

    @builtins.property
    def snap_start(self) -> typing.Optional[_aws_cdk_aws_lambda_ceddda9d.SnapStartConf]:
        '''Enable SnapStart for Lambda Function.

        SnapStart is currently supported only for Java 11, 17 runtime

        :default: - No snapstart
        '''
        result = self._values.get("snap_start")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_ceddda9d.SnapStartConf], result)

    @builtins.property
    def system_log_level(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Sets the system log level for the function.

        :default: "INFO"

        :deprecated: Use ``systemLogLevelV2`` as a property instead.

        :stability: deprecated
        '''
        result = self._values.get("system_log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def system_log_level_v2(
        self,
    ) -> typing.Optional[_aws_cdk_aws_lambda_ceddda9d.SystemLogLevel]:
        '''Sets the system log level for the function.

        :default: SystemLogLevel.INFO
        '''
        result = self._values.get("system_log_level_v2")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_ceddda9d.SystemLogLevel], result)

    @builtins.property
    def timeout(self) -> typing.Optional[_aws_cdk_ceddda9d.Duration]:
        '''The function execution time (in seconds) after which Lambda terminates the function.

        Because the execution time affects cost, set this value
        based on the function's expected execution time.

        :default: Duration.seconds(3)
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.Duration], result)

    @builtins.property
    def tracing(self) -> typing.Optional[_aws_cdk_aws_lambda_ceddda9d.Tracing]:
        '''Enable AWS X-Ray Tracing for Lambda Function.

        :default: Tracing.Disabled
        '''
        result = self._values.get("tracing")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_ceddda9d.Tracing], result)

    @builtins.property
    def vpc(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc]:
        '''VPC network to place Lambda network interfaces.

        Specify this if the Lambda function needs to access resources in a VPC.
        This is required when ``vpcSubnets`` is specified.

        :default: - Function is not placed within a VPC.
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection]:
        '''Where to place the network interfaces within the VPC.

        This requires ``vpc`` to be specified in order for interfaces to actually be
        placed in the subnets. If ``vpc`` is not specify, this will raise an error.

        Note: Internet access for Lambda Functions requires a NAT Gateway, so picking
        public subnets is not allowed (unless ``allowPublicSubnet`` is set to ``true``).

        :default: - the Vpc default strategy if not specified
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection], result)

    @builtins.property
    def root_dir(self) -> builtins.str:
        '''UV project root directory (workspace root).'''
        result = self._values.get("root_dir")
        assert result is not None, "Required property 'root_dir' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bundling(self) -> typing.Optional[BundlingOptions]:
        '''Custom bundling options, including build architecture and bundling container image.'''
        result = self._values.get("bundling")
        return typing.cast(typing.Optional[BundlingOptions], result)

    @builtins.property
    def handler(self) -> typing.Optional[builtins.str]:
        '''The name of the exported handler function in the #index.

        :default: handler
        '''
        result = self._values.get("handler")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def index(self) -> typing.Optional[builtins.str]:
        '''The path to the index file with the project or (or workspace, if specified) containing the handler.

        :default: index.py
        '''
        result = self._values.get("index")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def runtime(self) -> typing.Optional[_aws_cdk_aws_lambda_ceddda9d.Runtime]:
        '''The runtime.

        :default: Runtime.PYTHON_3_12
        '''
        result = self._values.get("runtime")
        return typing.cast(typing.Optional[_aws_cdk_aws_lambda_ceddda9d.Runtime], result)

    @builtins.property
    def workspace_package(self) -> typing.Optional[builtins.str]:
        '''Optional UV project workspace, used to specify a specific package to be used as a Lambda Function entry.'''
        result = self._values.get("workspace_package")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PythonFunctionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Bundling",
    "BundlingOptions",
    "BundlingProps",
    "ICommandHooks",
    "PythonFunction",
    "PythonFunctionProps",
]

publication.publish()

def _typecheckingstub__c127a9f1315f71ef946f978c90bac639ec3fc1d9efcaa70c8b9e86ce62f88283(
    *,
    command: typing.Optional[typing.Sequence[builtins.str]] = None,
    entrypoint: typing.Optional[typing.Sequence[builtins.str]] = None,
    environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    network: typing.Optional[builtins.str] = None,
    platform: typing.Optional[builtins.str] = None,
    security_opt: typing.Optional[builtins.str] = None,
    user: typing.Optional[builtins.str] = None,
    volumes: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_ceddda9d.DockerVolume, typing.Dict[builtins.str, typing.Any]]]] = None,
    volumes_from: typing.Optional[typing.Sequence[builtins.str]] = None,
    working_directory: typing.Optional[builtins.str] = None,
    asset_excludes: typing.Optional[typing.Sequence[builtins.str]] = None,
    asset_hash: typing.Optional[builtins.str] = None,
    asset_hash_type: typing.Optional[_aws_cdk_ceddda9d.AssetHashType] = None,
    build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    bundling_file_access: typing.Optional[_aws_cdk_ceddda9d.BundlingFileAccess] = None,
    command_hooks: typing.Optional[ICommandHooks] = None,
    image: typing.Optional[_aws_cdk_ceddda9d.DockerImage] = None,
    output_path_suffix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81d59fe1ee0f2977c9b3195e16a1f5ec90d137ed13842e74353e0938e809140f(
    *,
    command: typing.Optional[typing.Sequence[builtins.str]] = None,
    entrypoint: typing.Optional[typing.Sequence[builtins.str]] = None,
    environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    network: typing.Optional[builtins.str] = None,
    platform: typing.Optional[builtins.str] = None,
    security_opt: typing.Optional[builtins.str] = None,
    user: typing.Optional[builtins.str] = None,
    volumes: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_ceddda9d.DockerVolume, typing.Dict[builtins.str, typing.Any]]]] = None,
    volumes_from: typing.Optional[typing.Sequence[builtins.str]] = None,
    working_directory: typing.Optional[builtins.str] = None,
    asset_excludes: typing.Optional[typing.Sequence[builtins.str]] = None,
    asset_hash: typing.Optional[builtins.str] = None,
    asset_hash_type: typing.Optional[_aws_cdk_ceddda9d.AssetHashType] = None,
    build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    bundling_file_access: typing.Optional[_aws_cdk_ceddda9d.BundlingFileAccess] = None,
    command_hooks: typing.Optional[ICommandHooks] = None,
    image: typing.Optional[_aws_cdk_ceddda9d.DockerImage] = None,
    output_path_suffix: typing.Optional[builtins.str] = None,
    root_dir: builtins.str,
    runtime: _aws_cdk_aws_lambda_ceddda9d.Runtime,
    architecture: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.Architecture] = None,
    skip: typing.Optional[builtins.bool] = None,
    workspace_package: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__488db7d12e1ab44fd5779f576fc5cd00cb9e85710a675cd96533b44d5c3b3135(
    input_dir: builtins.str,
    output_dir: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a84729a70b154d4dbb345742f5239044f1bb9c86e4f5efb63576535d4d8b4d6f(
    input_dir: builtins.str,
    output_dir: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f4b27a9e71783873da8f30bb12ae1f28cc9da3f8ddc294f9bd54cf8dabd8506(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    root_dir: builtins.str,
    bundling: typing.Optional[typing.Union[BundlingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    handler: typing.Optional[builtins.str] = None,
    index: typing.Optional[builtins.str] = None,
    runtime: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.Runtime] = None,
    workspace_package: typing.Optional[builtins.str] = None,
    adot_instrumentation: typing.Optional[typing.Union[_aws_cdk_aws_lambda_ceddda9d.AdotInstrumentationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    allow_all_ipv6_outbound: typing.Optional[builtins.bool] = None,
    allow_all_outbound: typing.Optional[builtins.bool] = None,
    allow_public_subnet: typing.Optional[builtins.bool] = None,
    application_log_level: typing.Optional[builtins.str] = None,
    application_log_level_v2: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.ApplicationLogLevel] = None,
    architecture: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.Architecture] = None,
    code_signing_config: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.ICodeSigningConfig] = None,
    current_version_options: typing.Optional[typing.Union[_aws_cdk_aws_lambda_ceddda9d.VersionOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    dead_letter_queue: typing.Optional[_aws_cdk_aws_sqs_ceddda9d.IQueue] = None,
    dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
    dead_letter_topic: typing.Optional[_aws_cdk_aws_sns_ceddda9d.ITopic] = None,
    description: typing.Optional[builtins.str] = None,
    environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    environment_encryption: typing.Optional[_aws_cdk_aws_kms_ceddda9d.IKey] = None,
    ephemeral_storage_size: typing.Optional[_aws_cdk_ceddda9d.Size] = None,
    events: typing.Optional[typing.Sequence[_aws_cdk_aws_lambda_ceddda9d.IEventSource]] = None,
    filesystem: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.FileSystem] = None,
    function_name: typing.Optional[builtins.str] = None,
    initial_policy: typing.Optional[typing.Sequence[_aws_cdk_aws_iam_ceddda9d.PolicyStatement]] = None,
    insights_version: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.LambdaInsightsVersion] = None,
    ipv6_allowed_for_dual_stack: typing.Optional[builtins.bool] = None,
    layers: typing.Optional[typing.Sequence[_aws_cdk_aws_lambda_ceddda9d.ILayerVersion]] = None,
    log_format: typing.Optional[builtins.str] = None,
    logging_format: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.LoggingFormat] = None,
    log_group: typing.Optional[_aws_cdk_aws_logs_ceddda9d.ILogGroup] = None,
    log_retention: typing.Optional[_aws_cdk_aws_logs_ceddda9d.RetentionDays] = None,
    log_retention_retry_options: typing.Optional[typing.Union[_aws_cdk_aws_lambda_ceddda9d.LogRetentionRetryOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    log_retention_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    memory_size: typing.Optional[jsii.Number] = None,
    params_and_secrets: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.ParamsAndSecretsLayerVersion] = None,
    profiling: typing.Optional[builtins.bool] = None,
    profiling_group: typing.Optional[_aws_cdk_aws_codeguruprofiler_ceddda9d.IProfilingGroup] = None,
    recursive_loop: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.RecursiveLoop] = None,
    reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
    role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    runtime_management_mode: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.RuntimeManagementMode] = None,
    security_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup]] = None,
    snap_start: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.SnapStartConf] = None,
    system_log_level: typing.Optional[builtins.str] = None,
    system_log_level_v2: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.SystemLogLevel] = None,
    timeout: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    tracing: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.Tracing] = None,
    vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
    vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
    max_event_age: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    on_failure: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.IDestination] = None,
    on_success: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.IDestination] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9783d4735a5a328474d4c697ce9ae14150d27c171dc16c9970a5f60d92b82410(
    *,
    max_event_age: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    on_failure: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.IDestination] = None,
    on_success: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.IDestination] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    adot_instrumentation: typing.Optional[typing.Union[_aws_cdk_aws_lambda_ceddda9d.AdotInstrumentationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    allow_all_ipv6_outbound: typing.Optional[builtins.bool] = None,
    allow_all_outbound: typing.Optional[builtins.bool] = None,
    allow_public_subnet: typing.Optional[builtins.bool] = None,
    application_log_level: typing.Optional[builtins.str] = None,
    application_log_level_v2: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.ApplicationLogLevel] = None,
    architecture: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.Architecture] = None,
    code_signing_config: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.ICodeSigningConfig] = None,
    current_version_options: typing.Optional[typing.Union[_aws_cdk_aws_lambda_ceddda9d.VersionOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    dead_letter_queue: typing.Optional[_aws_cdk_aws_sqs_ceddda9d.IQueue] = None,
    dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
    dead_letter_topic: typing.Optional[_aws_cdk_aws_sns_ceddda9d.ITopic] = None,
    description: typing.Optional[builtins.str] = None,
    environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    environment_encryption: typing.Optional[_aws_cdk_aws_kms_ceddda9d.IKey] = None,
    ephemeral_storage_size: typing.Optional[_aws_cdk_ceddda9d.Size] = None,
    events: typing.Optional[typing.Sequence[_aws_cdk_aws_lambda_ceddda9d.IEventSource]] = None,
    filesystem: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.FileSystem] = None,
    function_name: typing.Optional[builtins.str] = None,
    initial_policy: typing.Optional[typing.Sequence[_aws_cdk_aws_iam_ceddda9d.PolicyStatement]] = None,
    insights_version: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.LambdaInsightsVersion] = None,
    ipv6_allowed_for_dual_stack: typing.Optional[builtins.bool] = None,
    layers: typing.Optional[typing.Sequence[_aws_cdk_aws_lambda_ceddda9d.ILayerVersion]] = None,
    log_format: typing.Optional[builtins.str] = None,
    logging_format: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.LoggingFormat] = None,
    log_group: typing.Optional[_aws_cdk_aws_logs_ceddda9d.ILogGroup] = None,
    log_retention: typing.Optional[_aws_cdk_aws_logs_ceddda9d.RetentionDays] = None,
    log_retention_retry_options: typing.Optional[typing.Union[_aws_cdk_aws_lambda_ceddda9d.LogRetentionRetryOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    log_retention_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    memory_size: typing.Optional[jsii.Number] = None,
    params_and_secrets: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.ParamsAndSecretsLayerVersion] = None,
    profiling: typing.Optional[builtins.bool] = None,
    profiling_group: typing.Optional[_aws_cdk_aws_codeguruprofiler_ceddda9d.IProfilingGroup] = None,
    recursive_loop: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.RecursiveLoop] = None,
    reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
    role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    runtime_management_mode: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.RuntimeManagementMode] = None,
    security_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup]] = None,
    snap_start: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.SnapStartConf] = None,
    system_log_level: typing.Optional[builtins.str] = None,
    system_log_level_v2: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.SystemLogLevel] = None,
    timeout: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    tracing: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.Tracing] = None,
    vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
    vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
    root_dir: builtins.str,
    bundling: typing.Optional[typing.Union[BundlingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    handler: typing.Optional[builtins.str] = None,
    index: typing.Optional[builtins.str] = None,
    runtime: typing.Optional[_aws_cdk_aws_lambda_ceddda9d.Runtime] = None,
    workspace_package: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
