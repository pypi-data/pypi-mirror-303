from kabinet.funcs import execute, aexecute
from typing import List, Any, Optional, Tuple, Literal
from rath.scalars import ID
from pydantic import Field, BaseModel, ConfigDict
from enum import Enum
from datetime import datetime
from kabinet.rath import KabinetRath


class PodStatus(str, Enum):
    """The state of a dask cluster"""

    PENDING = "PENDING"
    RUNNING = "RUNNING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    FAILED = "FAILED"
    UNKOWN = "UNKOWN"


class ContainerType(str, Enum):
    """The state of a dask cluster"""

    APPTAINER = "APPTAINER"
    DOCKER = "DOCKER"


class OffsetPaginationInput(BaseModel):
    offset: int
    limit: int
    model_config = ConfigDict(frozen=True, extra="forbid", use_enum_values=True)


class EnvironmentInput(BaseModel):
    """Which environment do you want to match against?"""

    features: Optional[Tuple["DeviceFeature", ...]] = None
    container_type: ContainerType = Field(alias="containerType")
    model_config = ConfigDict(frozen=True, extra="forbid", use_enum_values=True)


class DeviceFeature(BaseModel):
    """The Feature you are trying to match"""

    kind: str
    cpu_count: str = Field(alias="cpuCount")
    model_config = ConfigDict(frozen=True, extra="forbid", use_enum_values=True)


class ResourceFilter(BaseModel):
    """Filter for Resources"""

    ids: Optional[Tuple[ID, ...]] = None
    search: Optional[str] = None
    and_: Optional["ResourceFilter"] = Field(alias="AND", default=None)
    or_: Optional["ResourceFilter"] = Field(alias="OR", default=None)
    not_: Optional["ResourceFilter"] = Field(alias="NOT", default=None)
    model_config = ConfigDict(frozen=True, extra="forbid", use_enum_values=True)


class BackendFilter(BaseModel):
    """Filter for Resources"""

    ids: Optional[Tuple[ID, ...]] = None
    search: Optional[str] = None
    and_: Optional["BackendFilter"] = Field(alias="AND", default=None)
    or_: Optional["BackendFilter"] = Field(alias="OR", default=None)
    not_: Optional["BackendFilter"] = Field(alias="NOT", default=None)
    model_config = ConfigDict(frozen=True, extra="forbid", use_enum_values=True)


class Deployment(BaseModel):
    typename: Optional[Literal["Deployment"]] = Field(
        alias="__typename", default="Deployment", exclude=True
    )
    id: ID
    local_id: ID = Field(alias="localId")
    model_config = ConfigDict(frozen=True)


class ListDeployment(BaseModel):
    typename: Optional[Literal["Deployment"]] = Field(
        alias="__typename", default="Deployment", exclude=True
    )
    id: ID
    local_id: ID = Field(alias="localId")
    model_config = ConfigDict(frozen=True)


class GithubRepoFlavoursDefinitions(BaseModel):
    """Nodes are abstraction of RPC Tasks. They provide a common API to deal with creating tasks.

    See online Documentation"""

    typename: Optional[Literal["Definition"]] = Field(
        alias="__typename", default="Definition", exclude=True
    )
    id: ID
    hash: ID
    "The hash of the Node (completely unique)"
    model_config = ConfigDict(frozen=True)


class GithubRepoFlavours(BaseModel):
    """A user of the bridge server. Maps to an authentikate user"""

    typename: Optional[Literal["Flavour"]] = Field(
        alias="__typename", default="Flavour", exclude=True
    )
    definitions: Tuple[GithubRepoFlavoursDefinitions, ...]
    "The flavours this Definition belongs to"
    model_config = ConfigDict(frozen=True)


class GithubRepo(BaseModel):
    typename: Optional[Literal["GithubRepo"]] = Field(
        alias="__typename", default="GithubRepo", exclude=True
    )
    id: ID
    branch: str
    user: str
    repo: str
    flavours: Tuple[GithubRepoFlavours, ...]
    model_config = ConfigDict(frozen=True)


class ReleaseApp(BaseModel):
    """A user of the bridge server. Maps to an authentikate user"""

    typename: Optional[Literal["App"]] = Field(
        alias="__typename", default="App", exclude=True
    )
    identifier: str
    model_config = ConfigDict(frozen=True)


class ReleaseFlavours(BaseModel):
    """A user of the bridge server. Maps to an authentikate user"""

    typename: Optional[Literal["Flavour"]] = Field(
        alias="__typename", default="Flavour", exclude=True
    )
    id: ID
    name: str
    image: str
    manifest: Any
    requirements: Any
    model_config = ConfigDict(frozen=True)


class Release(BaseModel):
    typename: Optional[Literal["Release"]] = Field(
        alias="__typename", default="Release", exclude=True
    )
    id: ID
    version: str
    app: ReleaseApp
    scopes: Tuple[str, ...]
    colour: str
    "Is this release deployed"
    description: str
    "Is this release deployed"
    flavours: Tuple[ReleaseFlavours, ...]
    model_config = ConfigDict(frozen=True)


class ListReleaseApp(BaseModel):
    """A user of the bridge server. Maps to an authentikate user"""

    typename: Optional[Literal["App"]] = Field(
        alias="__typename", default="App", exclude=True
    )
    identifier: str
    model_config = ConfigDict(frozen=True)


class ListRelease(BaseModel):
    typename: Optional[Literal["Release"]] = Field(
        alias="__typename", default="Release", exclude=True
    )
    id: ID
    version: str
    app: ListReleaseApp
    installed: bool
    "Is this release deployed"
    scopes: Tuple[str, ...]
    flavours: Tuple["ListFlavour", ...]
    colour: str
    "Is this release deployed"
    description: str
    "Is this release deployed"
    model_config = ConfigDict(frozen=True)


class ListPod(BaseModel):
    typename: Optional[Literal["Pod"]] = Field(
        alias="__typename", default="Pod", exclude=True
    )
    id: ID
    pod_id: str = Field(alias="podId")
    model_config = ConfigDict(frozen=True)


class PodDeployment(BaseModel):
    """A user of the bridge server. Maps to an authentikate user"""

    typename: Optional[Literal["Deployment"]] = Field(
        alias="__typename", default="Deployment", exclude=True
    )
    flavour: "Flavour"
    model_config = ConfigDict(frozen=True)


class Pod(BaseModel):
    typename: Optional[Literal["Pod"]] = Field(
        alias="__typename", default="Pod", exclude=True
    )
    id: ID
    pod_id: str = Field(alias="podId")
    deployment: PodDeployment
    model_config = ConfigDict(frozen=True)


class ListFlavour(BaseModel):
    typename: Optional[Literal["Flavour"]] = Field(
        alias="__typename", default="Flavour", exclude=True
    )
    id: ID
    name: str
    manifest: Any
    model_config = ConfigDict(frozen=True)


class Flavour(BaseModel):
    typename: Optional[Literal["Flavour"]] = Field(
        alias="__typename", default="Flavour", exclude=True
    )
    release: Release
    manifest: Any
    model_config = ConfigDict(frozen=True)


class ResourceBackend(BaseModel):
    """A user of the bridge server. Maps to an authentikate user"""

    typename: Optional[Literal["Backend"]] = Field(
        alias="__typename", default="Backend", exclude=True
    )
    id: ID
    name: str
    model_config = ConfigDict(frozen=True)


class ResourcePods(BaseModel):
    """A user of the bridge server. Maps to an authentikate user"""

    typename: Optional[Literal["Pod"]] = Field(
        alias="__typename", default="Pod", exclude=True
    )
    id: ID
    pod_id: str = Field(alias="podId")
    model_config = ConfigDict(frozen=True)


class Resource(BaseModel):
    typename: Optional[Literal["Resource"]] = Field(
        alias="__typename", default="Resource", exclude=True
    )
    id: ID
    name: str
    qualifiers: Optional[Any] = Field(default=None)
    backend: ResourceBackend
    pods: Tuple[ResourcePods, ...]
    model_config = ConfigDict(frozen=True)


class ListResourceBackend(BaseModel):
    """A user of the bridge server. Maps to an authentikate user"""

    typename: Optional[Literal["Backend"]] = Field(
        alias="__typename", default="Backend", exclude=True
    )
    id: ID
    name: str
    model_config = ConfigDict(frozen=True)


class ListResource(BaseModel):
    typename: Optional[Literal["Resource"]] = Field(
        alias="__typename", default="Resource", exclude=True
    )
    id: ID
    name: str
    qualifiers: Optional[Any] = Field(default=None)
    backend: ListResourceBackend
    model_config = ConfigDict(frozen=True)


class ListDefinition(BaseModel):
    typename: Optional[Literal["Definition"]] = Field(
        alias="__typename", default="Definition", exclude=True
    )
    id: ID
    name: str
    "The cleartext name of this Node"
    hash: ID
    "The hash of the Node (completely unique)"
    description: Optional[str] = Field(default=None)
    "A description for the Node"
    model_config = ConfigDict(frozen=True)


class Definition(BaseModel):
    typename: Optional[Literal["Definition"]] = Field(
        alias="__typename", default="Definition", exclude=True
    )
    id: ID
    name: str
    "The cleartext name of this Node"
    model_config = ConfigDict(frozen=True)


class Backend(BaseModel):
    typename: Optional[Literal["Backend"]] = Field(
        alias="__typename", default="Backend", exclude=True
    )
    id: ID
    name: str
    model_config = ConfigDict(frozen=True)


class ListBackend(BaseModel):
    typename: Optional[Literal["Backend"]] = Field(
        alias="__typename", default="Backend", exclude=True
    )
    id: ID
    name: str
    model_config = ConfigDict(frozen=True)


class CreateDeploymentMutation(BaseModel):
    create_deployment: Deployment = Field(alias="createDeployment")
    "Create a new dask cluster on a bridge server"

    class Arguments(BaseModel):
        flavour: ID
        instance_id: str = Field(alias="instanceId")
        local_id: ID = Field(alias="localId")
        last_pulled: Optional[datetime] = Field(alias="lastPulled", default=None)
        secret_params: Optional[Any] = Field(alias="secretParams", default=None)

    class Meta:
        document = "fragment Deployment on Deployment {\n  id\n  localId\n}\n\nmutation CreateDeployment($flavour: ID!, $instanceId: String!, $localId: ID!, $lastPulled: DateTime, $secretParams: UntypedParams) {\n  createDeployment(\n    input: {flavour: $flavour, lastPulled: $lastPulled, secretParams: $secretParams, instanceId: $instanceId, localId: $localId}\n  ) {\n    ...Deployment\n  }\n}"


class CreatePodMutation(BaseModel):
    create_pod: Pod = Field(alias="createPod")
    "Create a new dask cluster on a bridge server"

    class Arguments(BaseModel):
        deployment: ID
        instance_id: str = Field(alias="instanceId")
        local_id: ID = Field(alias="localId")
        resource: Optional[ID] = Field(default=None)
        client_id: Optional[str] = Field(alias="clientId", default=None)

    class Meta:
        document = "fragment Release on Release {\n  id\n  version\n  app {\n    identifier\n  }\n  scopes\n  colour\n  description\n  flavours {\n    id\n    name\n    image\n    manifest\n    requirements\n  }\n}\n\nfragment Flavour on Flavour {\n  release {\n    ...Release\n  }\n  manifest\n}\n\nfragment Pod on Pod {\n  id\n  podId\n  deployment {\n    flavour {\n      ...Flavour\n    }\n  }\n}\n\nmutation CreatePod($deployment: ID!, $instanceId: String!, $localId: ID!, $resource: ID, $clientId: String) {\n  createPod(\n    input: {deployment: $deployment, instanceId: $instanceId, localId: $localId, resource: $resource, clientId: $clientId}\n  ) {\n    ...Pod\n  }\n}"


class UpdatePodMutation(BaseModel):
    update_pod: Pod = Field(alias="updatePod")
    "Create a new dask cluster on a bridge server"

    class Arguments(BaseModel):
        status: PodStatus
        instance_id: str = Field(alias="instanceId")
        pod: Optional[ID] = Field(default=None)
        local_id: Optional[ID] = Field(alias="localId", default=None)

    class Meta:
        document = "fragment Release on Release {\n  id\n  version\n  app {\n    identifier\n  }\n  scopes\n  colour\n  description\n  flavours {\n    id\n    name\n    image\n    manifest\n    requirements\n  }\n}\n\nfragment Flavour on Flavour {\n  release {\n    ...Release\n  }\n  manifest\n}\n\nfragment Pod on Pod {\n  id\n  podId\n  deployment {\n    flavour {\n      ...Flavour\n    }\n  }\n}\n\nmutation UpdatePod($status: PodStatus!, $instanceId: String!, $pod: ID, $localId: ID) {\n  updatePod(\n    input: {pod: $pod, localId: $localId, status: $status, instanceId: $instanceId}\n  ) {\n    ...Pod\n  }\n}"


class DeletePodMutation(BaseModel):
    delete_pod: ID = Field(alias="deletePod")
    "Create a new dask cluster on a bridge server"

    class Arguments(BaseModel):
        id: ID

    class Meta:
        document = "mutation DeletePod($id: ID!) {\n  deletePod(input: {id: $id})\n}"


class DumpLogsMutationDumplogsPod(BaseModel):
    """A user of the bridge server. Maps to an authentikate user"""

    typename: Optional[Literal["Pod"]] = Field(
        alias="__typename", default="Pod", exclude=True
    )
    id: ID
    model_config = ConfigDict(frozen=True)


class DumpLogsMutationDumplogs(BaseModel):
    """The logs of a pod"""

    typename: Optional[Literal["LogDump"]] = Field(
        alias="__typename", default="LogDump", exclude=True
    )
    pod: DumpLogsMutationDumplogsPod
    logs: str
    model_config = ConfigDict(frozen=True)


class DumpLogsMutation(BaseModel):
    dump_logs: DumpLogsMutationDumplogs = Field(alias="dumpLogs")
    "Create a new dask cluster on a bridge server"

    class Arguments(BaseModel):
        pod: ID
        logs: str

    class Meta:
        document = "mutation DumpLogs($pod: ID!, $logs: String!) {\n  dumpLogs(input: {pod: $pod, logs: $logs}) {\n    pod {\n      id\n    }\n    logs\n  }\n}"


class CreateGithubRepoMutation(BaseModel):
    create_github_repo: GithubRepo = Field(alias="createGithubRepo")
    "Create a new Github repository on a bridge server"

    class Arguments(BaseModel):
        user: str
        repo: str
        branch: str
        name: str

    class Meta:
        document = "fragment GithubRepo on GithubRepo {\n  id\n  branch\n  user\n  repo\n  flavours {\n    definitions {\n      id\n      hash\n    }\n  }\n}\n\nmutation CreateGithubRepo($user: String!, $repo: String!, $branch: String!, $name: String!) {\n  createGithubRepo(\n    input: {user: $user, repo: $repo, branch: $branch, name: $name}\n  ) {\n    ...GithubRepo\n  }\n}"


class DeclareResourceMutation(BaseModel):
    declare_resource: Resource = Field(alias="declareResource")
    "Create a new resource for your backend"

    class Arguments(BaseModel):
        instance_id: str = Field(alias="instanceId")
        name: str
        resource_id: str = Field(alias="resourceId")
        qualifiers: Optional[Any] = Field(default=None)

    class Meta:
        document = "fragment Resource on Resource {\n  id\n  name\n  qualifiers\n  backend {\n    id\n    name\n  }\n  pods {\n    id\n    podId\n  }\n}\n\nmutation DeclareResource($instanceId: String!, $name: String!, $resourceId: String!, $qualifiers: UntypedParams) {\n  declareResource(\n    input: {instanceId: $instanceId, name: $name, resourceId: $resourceId, qualifiers: $qualifiers}\n  ) {\n    ...Resource\n  }\n}"


class DeclareBackendMutation(BaseModel):
    declare_backend: Backend = Field(alias="declareBackend")
    "Create a new dask cluster on a bridge server"

    class Arguments(BaseModel):
        instance_id: str = Field(alias="instanceId")
        kind: str
        name: str

    class Meta:
        document = "fragment Backend on Backend {\n  id\n  name\n}\n\nmutation DeclareBackend($instanceId: String!, $kind: String!, $name: String!) {\n  declareBackend(input: {kind: $kind, instanceId: $instanceId, name: $name}) {\n    ...Backend\n  }\n}"


class ListReleasesQuery(BaseModel):
    releases: Tuple[ListRelease, ...]

    class Arguments(BaseModel):
        pass

    class Meta:
        document = "fragment ListFlavour on Flavour {\n  id\n  name\n  manifest\n}\n\nfragment ListRelease on Release {\n  id\n  version\n  app {\n    identifier\n  }\n  installed\n  scopes\n  flavours {\n    ...ListFlavour\n  }\n  colour\n  description\n}\n\nquery ListReleases {\n  releases {\n    ...ListRelease\n  }\n}"


class GetReleaseQuery(BaseModel):
    release: Release
    "Return all dask clusters"

    class Arguments(BaseModel):
        id: ID

    class Meta:
        document = "fragment Release on Release {\n  id\n  version\n  app {\n    identifier\n  }\n  scopes\n  colour\n  description\n  flavours {\n    id\n    name\n    image\n    manifest\n    requirements\n  }\n}\n\nquery GetRelease($id: ID!) {\n  release(id: $id) {\n    ...Release\n  }\n}"


class SearchReleasesQueryOptions(BaseModel):
    """A user of the bridge server. Maps to an authentikate user"""

    typename: Optional[Literal["Release"]] = Field(
        alias="__typename", default="Release", exclude=True
    )
    value: ID
    label: str
    "Is this release deployed"
    model_config = ConfigDict(frozen=True)


class SearchReleasesQuery(BaseModel):
    options: Tuple[SearchReleasesQueryOptions, ...]

    class Arguments(BaseModel):
        search: Optional[str] = Field(default=None)
        values: Optional[List[ID]] = Field(default=None)

    class Meta:
        document = "query SearchReleases($search: String, $values: [ID!]) {\n  options: releases(\n    filters: {search: $search, ids: $values}\n    pagination: {limit: 10}\n  ) {\n    value: id\n    label: name\n  }\n}"


class GetDeploymentQuery(BaseModel):
    deployment: Deployment
    "Return all dask clusters"

    class Arguments(BaseModel):
        id: ID

    class Meta:
        document = "fragment Deployment on Deployment {\n  id\n  localId\n}\n\nquery GetDeployment($id: ID!) {\n  deployment(id: $id) {\n    ...Deployment\n  }\n}"


class ListDeploymentsQuery(BaseModel):
    deployments: Tuple[ListDeployment, ...]

    class Arguments(BaseModel):
        pass

    class Meta:
        document = "fragment ListDeployment on Deployment {\n  id\n  localId\n}\n\nquery ListDeployments {\n  deployments {\n    ...ListDeployment\n  }\n}"


class SearchDeploymentsQueryOptions(BaseModel):
    """A user of the bridge server. Maps to an authentikate user"""

    typename: Optional[Literal["Deployment"]] = Field(
        alias="__typename", default="Deployment", exclude=True
    )
    value: ID
    label: str
    model_config = ConfigDict(frozen=True)


class SearchDeploymentsQuery(BaseModel):
    options: Tuple[SearchDeploymentsQueryOptions, ...]

    class Arguments(BaseModel):
        search: Optional[str] = Field(default=None)
        values: Optional[List[ID]] = Field(default=None)

    class Meta:
        document = "query SearchDeployments($search: String, $values: [ID!]) {\n  options: deployments(\n    filters: {search: $search, ids: $values}\n    pagination: {limit: 10}\n  ) {\n    value: id\n    label: name\n  }\n}"


class ListPodQuery(BaseModel):
    pods: Tuple[ListPod, ...]

    class Arguments(BaseModel):
        pass

    class Meta:
        document = "fragment ListPod on Pod {\n  id\n  podId\n}\n\nquery ListPod {\n  pods {\n    ...ListPod\n  }\n}"


class GetPodQuery(BaseModel):
    pod: Pod
    "Return all dask clusters"

    class Arguments(BaseModel):
        id: ID

    class Meta:
        document = "fragment Release on Release {\n  id\n  version\n  app {\n    identifier\n  }\n  scopes\n  colour\n  description\n  flavours {\n    id\n    name\n    image\n    manifest\n    requirements\n  }\n}\n\nfragment Flavour on Flavour {\n  release {\n    ...Release\n  }\n  manifest\n}\n\nfragment Pod on Pod {\n  id\n  podId\n  deployment {\n    flavour {\n      ...Flavour\n    }\n  }\n}\n\nquery GetPod($id: ID!) {\n  pod(id: $id) {\n    ...Pod\n  }\n}"


class SearchPodsQueryOptions(BaseModel):
    """A user of the bridge server. Maps to an authentikate user"""

    typename: Optional[Literal["Pod"]] = Field(
        alias="__typename", default="Pod", exclude=True
    )
    value: ID
    label: str
    model_config = ConfigDict(frozen=True)


class SearchPodsQuery(BaseModel):
    options: Tuple[SearchPodsQueryOptions, ...]

    class Arguments(BaseModel):
        search: Optional[str] = Field(default=None)
        values: Optional[List[ID]] = Field(default=None)
        backend: Optional[ID] = Field(default=None)

    class Meta:
        document = "query SearchPods($search: String, $values: [ID!], $backend: ID) {\n  options: pods(\n    filters: {search: $search, ids: $values, backend: $backend}\n    pagination: {limit: 10}\n  ) {\n    value: id\n    label: name\n  }\n}"


class ListDefinitionsQuery(BaseModel):
    definitions: Tuple[ListDefinition, ...]

    class Arguments(BaseModel):
        pass

    class Meta:
        document = "fragment ListDefinition on Definition {\n  id\n  name\n  hash\n  description\n}\n\nquery ListDefinitions {\n  definitions {\n    ...ListDefinition\n  }\n}"


class GetDefinitionQuery(BaseModel):
    definition: Definition
    "Return all dask clusters"

    class Arguments(BaseModel):
        hash: Optional[ID] = Field(default=None)

    class Meta:
        document = "fragment Definition on Definition {\n  id\n  name\n}\n\nquery GetDefinition($hash: NodeHash) {\n  definition(hash: $hash) {\n    ...Definition\n  }\n}"


class SearchDefinitionsQueryOptions(BaseModel):
    """Nodes are abstraction of RPC Tasks. They provide a common API to deal with creating tasks.

    See online Documentation"""

    typename: Optional[Literal["Definition"]] = Field(
        alias="__typename", default="Definition", exclude=True
    )
    value: ID
    label: str
    "The cleartext name of this Node"
    model_config = ConfigDict(frozen=True)


class SearchDefinitionsQuery(BaseModel):
    options: Tuple[SearchDefinitionsQueryOptions, ...]

    class Arguments(BaseModel):
        search: Optional[str] = Field(default=None)
        values: Optional[List[ID]] = Field(default=None)

    class Meta:
        document = "query SearchDefinitions($search: String, $values: [ID!]) {\n  options: definitions(\n    filters: {search: $search, ids: $values}\n    pagination: {limit: 10}\n  ) {\n    value: id\n    label: name\n  }\n}"


class MatchFlavourQueryMatchflavour(BaseModel):
    """A user of the bridge server. Maps to an authentikate user"""

    typename: Optional[Literal["Flavour"]] = Field(
        alias="__typename", default="Flavour", exclude=True
    )
    id: ID
    image: str
    model_config = ConfigDict(frozen=True)


class MatchFlavourQuery(BaseModel):
    match_flavour: MatchFlavourQueryMatchflavour = Field(alias="matchFlavour")
    "Return the currently logged in user"

    class Arguments(BaseModel):
        nodes: Optional[List[ID]] = Field(default=None)
        environment: Optional[EnvironmentInput] = Field(default=None)

    class Meta:
        document = "query MatchFlavour($nodes: [NodeHash!], $environment: EnvironmentInput) {\n  matchFlavour(input: {nodes: $nodes, environment: $environment}) {\n    id\n    image\n  }\n}"


class ListResourcesQuery(BaseModel):
    resources: Tuple[ListResource, ...]

    class Arguments(BaseModel):
        filters: Optional[ResourceFilter] = Field(default=None)
        pagination: Optional[OffsetPaginationInput] = Field(default=None)

    class Meta:
        document = "fragment ListResource on Resource {\n  id\n  name\n  qualifiers\n  backend {\n    id\n    name\n  }\n}\n\nquery ListResources($filters: ResourceFilter, $pagination: OffsetPaginationInput) {\n  resources(filters: $filters, pagination: $pagination) {\n    ...ListResource\n  }\n}"


class GeResourceQuery(BaseModel):
    resource: Resource
    "Return all dask clusters"

    class Arguments(BaseModel):
        id: ID

    class Meta:
        document = "fragment Resource on Resource {\n  id\n  name\n  qualifiers\n  backend {\n    id\n    name\n  }\n  pods {\n    id\n    podId\n  }\n}\n\nquery GeResource($id: ID!) {\n  resource(id: $id) {\n    ...Resource\n  }\n}"


class SearchResourcesQueryOptions(BaseModel):
    """A resource on a backend. Resource define allocated resources on a backend. E.g a computational node"""

    typename: Optional[Literal["Resource"]] = Field(
        alias="__typename", default="Resource", exclude=True
    )
    value: ID
    label: str
    model_config = ConfigDict(frozen=True)


class SearchResourcesQuery(BaseModel):
    options: Tuple[SearchResourcesQueryOptions, ...]

    class Arguments(BaseModel):
        search: Optional[str] = Field(default=None)
        values: Optional[List[ID]] = Field(default=None)

    class Meta:
        document = "query SearchResources($search: String, $values: [ID!]) {\n  options: resources(\n    filters: {search: $search, ids: $values}\n    pagination: {limit: 10}\n  ) {\n    value: id\n    label: name\n  }\n}"


class ListBackendsQuery(BaseModel):
    backends: Tuple[ListBackend, ...]

    class Arguments(BaseModel):
        filters: Optional[BackendFilter] = Field(default=None)
        pagination: Optional[OffsetPaginationInput] = Field(default=None)

    class Meta:
        document = "fragment ListBackend on Backend {\n  id\n  name\n}\n\nquery ListBackends($filters: BackendFilter, $pagination: OffsetPaginationInput) {\n  backends(filters: $filters, pagination: $pagination) {\n    ...ListBackend\n  }\n}"


class GetBackendQuery(BaseModel):
    backend: Backend
    "Return all dask clusters"

    class Arguments(BaseModel):
        id: ID

    class Meta:
        document = "fragment Backend on Backend {\n  id\n  name\n}\n\nquery GetBackend($id: ID!) {\n  backend(id: $id) {\n    ...Backend\n  }\n}"


class SearchBackendsQueryOptions(BaseModel):
    """A user of the bridge server. Maps to an authentikate user"""

    typename: Optional[Literal["Backend"]] = Field(
        alias="__typename", default="Backend", exclude=True
    )
    value: ID
    label: str
    model_config = ConfigDict(frozen=True)


class SearchBackendsQuery(BaseModel):
    options: Tuple[SearchBackendsQueryOptions, ...]

    class Arguments(BaseModel):
        search: Optional[str] = Field(default=None)
        values: Optional[List[ID]] = Field(default=None)

    class Meta:
        document = "query SearchBackends($search: String, $values: [ID!]) {\n  options: backends(\n    filters: {search: $search, ids: $values}\n    pagination: {limit: 10}\n  ) {\n    value: id\n    label: name\n  }\n}"


async def acreate_deployment(
    flavour: ID,
    instance_id: str,
    local_id: ID,
    last_pulled: Optional[datetime] = None,
    secret_params: Optional[Any] = None,
    rath: Optional[KabinetRath] = None,
) -> Deployment:
    """CreateDeployment


     createDeployment: A user of the bridge server. Maps to an authentikate user


    Arguments:
        flavour (ID): flavour
        instance_id (str): instanceId
        local_id (ID): localId
        last_pulled (Optional[datetime], optional): lastPulled.
        secret_params (Optional[Any], optional): secretParams.
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        Deployment"""
    return (
        await aexecute(
            CreateDeploymentMutation,
            {
                "flavour": flavour,
                "instanceId": instance_id,
                "localId": local_id,
                "lastPulled": last_pulled,
                "secretParams": secret_params,
            },
            rath=rath,
        )
    ).create_deployment


def create_deployment(
    flavour: ID,
    instance_id: str,
    local_id: ID,
    last_pulled: Optional[datetime] = None,
    secret_params: Optional[Any] = None,
    rath: Optional[KabinetRath] = None,
) -> Deployment:
    """CreateDeployment


     createDeployment: A user of the bridge server. Maps to an authentikate user


    Arguments:
        flavour (ID): flavour
        instance_id (str): instanceId
        local_id (ID): localId
        last_pulled (Optional[datetime], optional): lastPulled.
        secret_params (Optional[Any], optional): secretParams.
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        Deployment"""
    return execute(
        CreateDeploymentMutation,
        {
            "flavour": flavour,
            "instanceId": instance_id,
            "localId": local_id,
            "lastPulled": last_pulled,
            "secretParams": secret_params,
        },
        rath=rath,
    ).create_deployment


async def acreate_pod(
    deployment: ID,
    instance_id: str,
    local_id: ID,
    resource: Optional[ID] = None,
    client_id: Optional[str] = None,
    rath: Optional[KabinetRath] = None,
) -> Pod:
    """CreatePod


     createPod: A user of the bridge server. Maps to an authentikate user


    Arguments:
        deployment (ID): deployment
        instance_id (str): instanceId
        local_id (ID): localId
        resource (Optional[ID], optional): resource.
        client_id (Optional[str], optional): clientId.
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        Pod"""
    return (
        await aexecute(
            CreatePodMutation,
            {
                "deployment": deployment,
                "instanceId": instance_id,
                "localId": local_id,
                "resource": resource,
                "clientId": client_id,
            },
            rath=rath,
        )
    ).create_pod


def create_pod(
    deployment: ID,
    instance_id: str,
    local_id: ID,
    resource: Optional[ID] = None,
    client_id: Optional[str] = None,
    rath: Optional[KabinetRath] = None,
) -> Pod:
    """CreatePod


     createPod: A user of the bridge server. Maps to an authentikate user


    Arguments:
        deployment (ID): deployment
        instance_id (str): instanceId
        local_id (ID): localId
        resource (Optional[ID], optional): resource.
        client_id (Optional[str], optional): clientId.
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        Pod"""
    return execute(
        CreatePodMutation,
        {
            "deployment": deployment,
            "instanceId": instance_id,
            "localId": local_id,
            "resource": resource,
            "clientId": client_id,
        },
        rath=rath,
    ).create_pod


async def aupdate_pod(
    status: PodStatus,
    instance_id: str,
    pod: Optional[ID] = None,
    local_id: Optional[ID] = None,
    rath: Optional[KabinetRath] = None,
) -> Pod:
    """UpdatePod


     updatePod: A user of the bridge server. Maps to an authentikate user


    Arguments:
        status (PodStatus): status
        instance_id (str): instanceId
        pod (Optional[ID], optional): pod.
        local_id (Optional[ID], optional): localId.
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        Pod"""
    return (
        await aexecute(
            UpdatePodMutation,
            {
                "status": status,
                "instanceId": instance_id,
                "pod": pod,
                "localId": local_id,
            },
            rath=rath,
        )
    ).update_pod


def update_pod(
    status: PodStatus,
    instance_id: str,
    pod: Optional[ID] = None,
    local_id: Optional[ID] = None,
    rath: Optional[KabinetRath] = None,
) -> Pod:
    """UpdatePod


     updatePod: A user of the bridge server. Maps to an authentikate user


    Arguments:
        status (PodStatus): status
        instance_id (str): instanceId
        pod (Optional[ID], optional): pod.
        local_id (Optional[ID], optional): localId.
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        Pod"""
    return execute(
        UpdatePodMutation,
        {"status": status, "instanceId": instance_id, "pod": pod, "localId": local_id},
        rath=rath,
    ).update_pod


async def adelete_pod(id: ID, rath: Optional[KabinetRath] = None) -> ID:
    """DeletePod


     deletePod: The `ID` scalar type represents a unique identifier, often used to refetch an object or as key for a cache. The ID type appears in a JSON response as a String; however, it is not intended to be human-readable. When expected as an input type, any string (such as `"4"`) or integer (such as `4`) input value will be accepted as an ID.


    Arguments:
        id (ID): id
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        ID"""
    return (await aexecute(DeletePodMutation, {"id": id}, rath=rath)).delete_pod


def delete_pod(id: ID, rath: Optional[KabinetRath] = None) -> ID:
    """DeletePod


     deletePod: The `ID` scalar type represents a unique identifier, often used to refetch an object or as key for a cache. The ID type appears in a JSON response as a String; however, it is not intended to be human-readable. When expected as an input type, any string (such as `"4"`) or integer (such as `4`) input value will be accepted as an ID.


    Arguments:
        id (ID): id
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        ID"""
    return execute(DeletePodMutation, {"id": id}, rath=rath).delete_pod


async def adump_logs(
    pod: ID, logs: str, rath: Optional[KabinetRath] = None
) -> DumpLogsMutationDumplogs:
    """DumpLogs


     dumpLogs: The logs of a pod


    Arguments:
        pod (ID): pod
        logs (str): logs
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        DumpLogsMutationDumplogs"""
    return (
        await aexecute(DumpLogsMutation, {"pod": pod, "logs": logs}, rath=rath)
    ).dump_logs


def dump_logs(
    pod: ID, logs: str, rath: Optional[KabinetRath] = None
) -> DumpLogsMutationDumplogs:
    """DumpLogs


     dumpLogs: The logs of a pod


    Arguments:
        pod (ID): pod
        logs (str): logs
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        DumpLogsMutationDumplogs"""
    return execute(DumpLogsMutation, {"pod": pod, "logs": logs}, rath=rath).dump_logs


async def acreate_github_repo(
    user: str, repo: str, branch: str, name: str, rath: Optional[KabinetRath] = None
) -> GithubRepo:
    """CreateGithubRepo


     createGithubRepo: A user of the bridge server. Maps to an authentikate user


    Arguments:
        user (str): user
        repo (str): repo
        branch (str): branch
        name (str): name
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        GithubRepo"""
    return (
        await aexecute(
            CreateGithubRepoMutation,
            {"user": user, "repo": repo, "branch": branch, "name": name},
            rath=rath,
        )
    ).create_github_repo


def create_github_repo(
    user: str, repo: str, branch: str, name: str, rath: Optional[KabinetRath] = None
) -> GithubRepo:
    """CreateGithubRepo


     createGithubRepo: A user of the bridge server. Maps to an authentikate user


    Arguments:
        user (str): user
        repo (str): repo
        branch (str): branch
        name (str): name
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        GithubRepo"""
    return execute(
        CreateGithubRepoMutation,
        {"user": user, "repo": repo, "branch": branch, "name": name},
        rath=rath,
    ).create_github_repo


async def adeclare_resource(
    instance_id: str,
    name: str,
    resource_id: str,
    qualifiers: Optional[Any] = None,
    rath: Optional[KabinetRath] = None,
) -> Resource:
    """DeclareResource


     declareResource: A resource on a backend. Resource define allocated resources on a backend. E.g a computational node


    Arguments:
        instance_id (str): instanceId
        name (str): name
        resource_id (str): resourceId
        qualifiers (Optional[Any], optional): qualifiers.
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        Resource"""
    return (
        await aexecute(
            DeclareResourceMutation,
            {
                "instanceId": instance_id,
                "name": name,
                "resourceId": resource_id,
                "qualifiers": qualifiers,
            },
            rath=rath,
        )
    ).declare_resource


def declare_resource(
    instance_id: str,
    name: str,
    resource_id: str,
    qualifiers: Optional[Any] = None,
    rath: Optional[KabinetRath] = None,
) -> Resource:
    """DeclareResource


     declareResource: A resource on a backend. Resource define allocated resources on a backend. E.g a computational node


    Arguments:
        instance_id (str): instanceId
        name (str): name
        resource_id (str): resourceId
        qualifiers (Optional[Any], optional): qualifiers.
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        Resource"""
    return execute(
        DeclareResourceMutation,
        {
            "instanceId": instance_id,
            "name": name,
            "resourceId": resource_id,
            "qualifiers": qualifiers,
        },
        rath=rath,
    ).declare_resource


async def adeclare_backend(
    instance_id: str, kind: str, name: str, rath: Optional[KabinetRath] = None
) -> Backend:
    """DeclareBackend


     declareBackend: A user of the bridge server. Maps to an authentikate user


    Arguments:
        instance_id (str): instanceId
        kind (str): kind
        name (str): name
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        Backend"""
    return (
        await aexecute(
            DeclareBackendMutation,
            {"instanceId": instance_id, "kind": kind, "name": name},
            rath=rath,
        )
    ).declare_backend


def declare_backend(
    instance_id: str, kind: str, name: str, rath: Optional[KabinetRath] = None
) -> Backend:
    """DeclareBackend


     declareBackend: A user of the bridge server. Maps to an authentikate user


    Arguments:
        instance_id (str): instanceId
        kind (str): kind
        name (str): name
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        Backend"""
    return execute(
        DeclareBackendMutation,
        {"instanceId": instance_id, "kind": kind, "name": name},
        rath=rath,
    ).declare_backend


async def alist_releases(rath: Optional[KabinetRath] = None) -> List[ListRelease]:
    """ListReleases


     releases: A user of the bridge server. Maps to an authentikate user


    Arguments:
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[ListRelease]"""
    return (await aexecute(ListReleasesQuery, {}, rath=rath)).releases


def list_releases(rath: Optional[KabinetRath] = None) -> List[ListRelease]:
    """ListReleases


     releases: A user of the bridge server. Maps to an authentikate user


    Arguments:
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[ListRelease]"""
    return execute(ListReleasesQuery, {}, rath=rath).releases


async def aget_release(id: ID, rath: Optional[KabinetRath] = None) -> Release:
    """GetRelease


     release: A user of the bridge server. Maps to an authentikate user


    Arguments:
        id (ID): id
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        Release"""
    return (await aexecute(GetReleaseQuery, {"id": id}, rath=rath)).release


def get_release(id: ID, rath: Optional[KabinetRath] = None) -> Release:
    """GetRelease


     release: A user of the bridge server. Maps to an authentikate user


    Arguments:
        id (ID): id
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        Release"""
    return execute(GetReleaseQuery, {"id": id}, rath=rath).release


async def asearch_releases(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[KabinetRath] = None,
) -> List[SearchReleasesQueryOptions]:
    """SearchReleases


     options: A user of the bridge server. Maps to an authentikate user


    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[SearchReleasesQueryReleases]"""
    return (
        await aexecute(
            SearchReleasesQuery, {"search": search, "values": values}, rath=rath
        )
    ).options


def search_releases(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[KabinetRath] = None,
) -> List[SearchReleasesQueryOptions]:
    """SearchReleases


     options: A user of the bridge server. Maps to an authentikate user


    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[SearchReleasesQueryReleases]"""
    return execute(
        SearchReleasesQuery, {"search": search, "values": values}, rath=rath
    ).options


async def aget_deployment(id: ID, rath: Optional[KabinetRath] = None) -> Deployment:
    """GetDeployment


     deployment: A user of the bridge server. Maps to an authentikate user


    Arguments:
        id (ID): id
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        Deployment"""
    return (await aexecute(GetDeploymentQuery, {"id": id}, rath=rath)).deployment


def get_deployment(id: ID, rath: Optional[KabinetRath] = None) -> Deployment:
    """GetDeployment


     deployment: A user of the bridge server. Maps to an authentikate user


    Arguments:
        id (ID): id
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        Deployment"""
    return execute(GetDeploymentQuery, {"id": id}, rath=rath).deployment


async def alist_deployments(rath: Optional[KabinetRath] = None) -> List[ListDeployment]:
    """ListDeployments


     deployments: A user of the bridge server. Maps to an authentikate user


    Arguments:
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[ListDeployment]"""
    return (await aexecute(ListDeploymentsQuery, {}, rath=rath)).deployments


def list_deployments(rath: Optional[KabinetRath] = None) -> List[ListDeployment]:
    """ListDeployments


     deployments: A user of the bridge server. Maps to an authentikate user


    Arguments:
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[ListDeployment]"""
    return execute(ListDeploymentsQuery, {}, rath=rath).deployments


async def asearch_deployments(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[KabinetRath] = None,
) -> List[SearchDeploymentsQueryOptions]:
    """SearchDeployments


     options: A user of the bridge server. Maps to an authentikate user


    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[SearchDeploymentsQueryDeployments]"""
    return (
        await aexecute(
            SearchDeploymentsQuery, {"search": search, "values": values}, rath=rath
        )
    ).options


def search_deployments(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[KabinetRath] = None,
) -> List[SearchDeploymentsQueryOptions]:
    """SearchDeployments


     options: A user of the bridge server. Maps to an authentikate user


    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[SearchDeploymentsQueryDeployments]"""
    return execute(
        SearchDeploymentsQuery, {"search": search, "values": values}, rath=rath
    ).options


async def alist_pod(rath: Optional[KabinetRath] = None) -> List[ListPod]:
    """ListPod


     pods: A user of the bridge server. Maps to an authentikate user


    Arguments:
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[ListPod]"""
    return (await aexecute(ListPodQuery, {}, rath=rath)).pods


def list_pod(rath: Optional[KabinetRath] = None) -> List[ListPod]:
    """ListPod


     pods: A user of the bridge server. Maps to an authentikate user


    Arguments:
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[ListPod]"""
    return execute(ListPodQuery, {}, rath=rath).pods


async def aget_pod(id: ID, rath: Optional[KabinetRath] = None) -> Pod:
    """GetPod


     pod: A user of the bridge server. Maps to an authentikate user


    Arguments:
        id (ID): id
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        Pod"""
    return (await aexecute(GetPodQuery, {"id": id}, rath=rath)).pod


def get_pod(id: ID, rath: Optional[KabinetRath] = None) -> Pod:
    """GetPod


     pod: A user of the bridge server. Maps to an authentikate user


    Arguments:
        id (ID): id
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        Pod"""
    return execute(GetPodQuery, {"id": id}, rath=rath).pod


async def asearch_pods(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    backend: Optional[ID] = None,
    rath: Optional[KabinetRath] = None,
) -> List[SearchPodsQueryOptions]:
    """SearchPods


     options: A user of the bridge server. Maps to an authentikate user


    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        backend (Optional[ID], optional): backend.
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[SearchPodsQueryPods]"""
    return (
        await aexecute(
            SearchPodsQuery,
            {"search": search, "values": values, "backend": backend},
            rath=rath,
        )
    ).options


def search_pods(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    backend: Optional[ID] = None,
    rath: Optional[KabinetRath] = None,
) -> List[SearchPodsQueryOptions]:
    """SearchPods


     options: A user of the bridge server. Maps to an authentikate user


    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        backend (Optional[ID], optional): backend.
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[SearchPodsQueryPods]"""
    return execute(
        SearchPodsQuery,
        {"search": search, "values": values, "backend": backend},
        rath=rath,
    ).options


async def alist_definitions(rath: Optional[KabinetRath] = None) -> List[ListDefinition]:
    """ListDefinitions


     definitions: Nodes are abstraction of RPC Tasks. They provide a common API to deal with creating tasks.

    See online Documentation


    Arguments:
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[ListDefinition]"""
    return (await aexecute(ListDefinitionsQuery, {}, rath=rath)).definitions


def list_definitions(rath: Optional[KabinetRath] = None) -> List[ListDefinition]:
    """ListDefinitions


     definitions: Nodes are abstraction of RPC Tasks. They provide a common API to deal with creating tasks.

    See online Documentation


    Arguments:
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[ListDefinition]"""
    return execute(ListDefinitionsQuery, {}, rath=rath).definitions


async def aget_definition(
    hash: Optional[ID] = None, rath: Optional[KabinetRath] = None
) -> Definition:
    """GetDefinition


     definition: Nodes are abstraction of RPC Tasks. They provide a common API to deal with creating tasks.

    See online Documentation


    Arguments:
        hash (Optional[ID], optional): hash.
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        Definition"""
    return (await aexecute(GetDefinitionQuery, {"hash": hash}, rath=rath)).definition


def get_definition(
    hash: Optional[ID] = None, rath: Optional[KabinetRath] = None
) -> Definition:
    """GetDefinition


     definition: Nodes are abstraction of RPC Tasks. They provide a common API to deal with creating tasks.

    See online Documentation


    Arguments:
        hash (Optional[ID], optional): hash.
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        Definition"""
    return execute(GetDefinitionQuery, {"hash": hash}, rath=rath).definition


async def asearch_definitions(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[KabinetRath] = None,
) -> List[SearchDefinitionsQueryOptions]:
    """SearchDefinitions


     options: Nodes are abstraction of RPC Tasks. They provide a common API to deal with creating tasks.

    See online Documentation


    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[SearchDefinitionsQueryDefinitions]"""
    return (
        await aexecute(
            SearchDefinitionsQuery, {"search": search, "values": values}, rath=rath
        )
    ).options


def search_definitions(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[KabinetRath] = None,
) -> List[SearchDefinitionsQueryOptions]:
    """SearchDefinitions


     options: Nodes are abstraction of RPC Tasks. They provide a common API to deal with creating tasks.

    See online Documentation


    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[SearchDefinitionsQueryDefinitions]"""
    return execute(
        SearchDefinitionsQuery, {"search": search, "values": values}, rath=rath
    ).options


async def amatch_flavour(
    nodes: Optional[List[ID]] = None,
    environment: Optional[EnvironmentInput] = None,
    rath: Optional[KabinetRath] = None,
) -> MatchFlavourQueryMatchflavour:
    """MatchFlavour


     matchFlavour: A user of the bridge server. Maps to an authentikate user


    Arguments:
        nodes (Optional[List[ID]], optional): nodes.
        environment (Optional[EnvironmentInput], optional): environment.
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        MatchFlavourQueryMatchflavour"""
    return (
        await aexecute(
            MatchFlavourQuery, {"nodes": nodes, "environment": environment}, rath=rath
        )
    ).match_flavour


def match_flavour(
    nodes: Optional[List[ID]] = None,
    environment: Optional[EnvironmentInput] = None,
    rath: Optional[KabinetRath] = None,
) -> MatchFlavourQueryMatchflavour:
    """MatchFlavour


     matchFlavour: A user of the bridge server. Maps to an authentikate user


    Arguments:
        nodes (Optional[List[ID]], optional): nodes.
        environment (Optional[EnvironmentInput], optional): environment.
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        MatchFlavourQueryMatchflavour"""
    return execute(
        MatchFlavourQuery, {"nodes": nodes, "environment": environment}, rath=rath
    ).match_flavour


async def alist_resources(
    filters: Optional[ResourceFilter] = None,
    pagination: Optional[OffsetPaginationInput] = None,
    rath: Optional[KabinetRath] = None,
) -> List[ListResource]:
    """ListResources


     resources: A resource on a backend. Resource define allocated resources on a backend. E.g a computational node


    Arguments:
        filters (Optional[ResourceFilter], optional): filters.
        pagination (Optional[OffsetPaginationInput], optional): pagination.
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[ListResource]"""
    return (
        await aexecute(
            ListResourcesQuery,
            {"filters": filters, "pagination": pagination},
            rath=rath,
        )
    ).resources


def list_resources(
    filters: Optional[ResourceFilter] = None,
    pagination: Optional[OffsetPaginationInput] = None,
    rath: Optional[KabinetRath] = None,
) -> List[ListResource]:
    """ListResources


     resources: A resource on a backend. Resource define allocated resources on a backend. E.g a computational node


    Arguments:
        filters (Optional[ResourceFilter], optional): filters.
        pagination (Optional[OffsetPaginationInput], optional): pagination.
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[ListResource]"""
    return execute(
        ListResourcesQuery, {"filters": filters, "pagination": pagination}, rath=rath
    ).resources


async def age_resource(id: ID, rath: Optional[KabinetRath] = None) -> Resource:
    """GeResource


     resource: A resource on a backend. Resource define allocated resources on a backend. E.g a computational node


    Arguments:
        id (ID): id
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        Resource"""
    return (await aexecute(GeResourceQuery, {"id": id}, rath=rath)).resource


def ge_resource(id: ID, rath: Optional[KabinetRath] = None) -> Resource:
    """GeResource


     resource: A resource on a backend. Resource define allocated resources on a backend. E.g a computational node


    Arguments:
        id (ID): id
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        Resource"""
    return execute(GeResourceQuery, {"id": id}, rath=rath).resource


async def asearch_resources(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[KabinetRath] = None,
) -> List[SearchResourcesQueryOptions]:
    """SearchResources


     options: A resource on a backend. Resource define allocated resources on a backend. E.g a computational node


    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[SearchResourcesQueryResources]"""
    return (
        await aexecute(
            SearchResourcesQuery, {"search": search, "values": values}, rath=rath
        )
    ).options


def search_resources(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[KabinetRath] = None,
) -> List[SearchResourcesQueryOptions]:
    """SearchResources


     options: A resource on a backend. Resource define allocated resources on a backend. E.g a computational node


    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[SearchResourcesQueryResources]"""
    return execute(
        SearchResourcesQuery, {"search": search, "values": values}, rath=rath
    ).options


async def alist_backends(
    filters: Optional[BackendFilter] = None,
    pagination: Optional[OffsetPaginationInput] = None,
    rath: Optional[KabinetRath] = None,
) -> List[ListBackend]:
    """ListBackends


     backends: A user of the bridge server. Maps to an authentikate user


    Arguments:
        filters (Optional[BackendFilter], optional): filters.
        pagination (Optional[OffsetPaginationInput], optional): pagination.
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[ListBackend]"""
    return (
        await aexecute(
            ListBackendsQuery, {"filters": filters, "pagination": pagination}, rath=rath
        )
    ).backends


def list_backends(
    filters: Optional[BackendFilter] = None,
    pagination: Optional[OffsetPaginationInput] = None,
    rath: Optional[KabinetRath] = None,
) -> List[ListBackend]:
    """ListBackends


     backends: A user of the bridge server. Maps to an authentikate user


    Arguments:
        filters (Optional[BackendFilter], optional): filters.
        pagination (Optional[OffsetPaginationInput], optional): pagination.
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[ListBackend]"""
    return execute(
        ListBackendsQuery, {"filters": filters, "pagination": pagination}, rath=rath
    ).backends


async def aget_backend(id: ID, rath: Optional[KabinetRath] = None) -> Backend:
    """GetBackend


     backend: A user of the bridge server. Maps to an authentikate user


    Arguments:
        id (ID): id
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        Backend"""
    return (await aexecute(GetBackendQuery, {"id": id}, rath=rath)).backend


def get_backend(id: ID, rath: Optional[KabinetRath] = None) -> Backend:
    """GetBackend


     backend: A user of the bridge server. Maps to an authentikate user


    Arguments:
        id (ID): id
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        Backend"""
    return execute(GetBackendQuery, {"id": id}, rath=rath).backend


async def asearch_backends(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[KabinetRath] = None,
) -> List[SearchBackendsQueryOptions]:
    """SearchBackends


     options: A user of the bridge server. Maps to an authentikate user


    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[SearchBackendsQueryBackends]"""
    return (
        await aexecute(
            SearchBackendsQuery, {"search": search, "values": values}, rath=rath
        )
    ).options


def search_backends(
    search: Optional[str] = None,
    values: Optional[List[ID]] = None,
    rath: Optional[KabinetRath] = None,
) -> List[SearchBackendsQueryOptions]:
    """SearchBackends


     options: A user of the bridge server. Maps to an authentikate user


    Arguments:
        search (Optional[str], optional): search.
        values (Optional[List[ID]], optional): values.
        rath (kabinet.rath.KabinetRath, optional): The client we want to use (defaults to the currently active client)

    Returns:
        List[SearchBackendsQueryBackends]"""
    return execute(
        SearchBackendsQuery, {"search": search, "values": values}, rath=rath
    ).options


BackendFilter.model_rebuild()
EnvironmentInput.model_rebuild()
ListRelease.model_rebuild()
PodDeployment.model_rebuild()
ResourceFilter.model_rebuild()
