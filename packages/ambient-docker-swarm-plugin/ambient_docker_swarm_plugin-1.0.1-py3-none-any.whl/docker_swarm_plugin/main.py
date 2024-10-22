from logging import Logger
from typing import Any, Optional, Union

import aiohttp
from ambient_backend_api_client import ApiClient, Cluster, ClustersApi, Configuration
from ambient_backend_api_client import NodeOutput as Node
from ambient_base_plugin import BasePlugin
from ambient_base_plugin.models.configuration import ConfigPayload
from ambient_base_plugin.models.message import Message
from docker_swarm_plugin.services.cluster_config_service import (
    ClusterConfigService,
    DockerClusterConfigService,
)

from ambient_client_common import config
from ambient_client_common.repositories.docker_repo import DockerRepo
from ambient_client_common.repositories.node_repo import NodeRepo

logger: Optional[Logger] = None


class DockerSwarmPlugin(BasePlugin):
    def __init__(self) -> None:
        self.node_repo: Optional[NodeRepo] = None
        self.docker_repo: Optional[DockerRepo] = None
        self.api_config: Optional[Configuration] = None
        self.logger: Optional[Logger] = None
        self.cluster_config_service: Optional[ClusterConfigService] = None

    async def configure(
        self, config: ConfigPayload, logger: Union[Logger, Any] = None
    ) -> None:
        self.node_repo = config.node_repo
        self.docker_repo = config.docker_repo
        self.api_config = config.api_config
        self.set_logger(logger)
        self.cluster_config_service = DockerClusterConfigService(
            docker_repo=self.docker_repo,
            node_repo=self.node_repo,
            api_config=self.api_config,
        )
        logger.info("Configured DockerSwarmPlugin")

    def set_logger(self, logger_: Logger) -> None:
        global logger
        logger = logger_
        self.logger = logger_

    async def handle_event(self, message: Message) -> None:
        logger.info("Handling cluster event [from plugin handler] ...")
        logger.debug(f"Handling cluster event: {message.model_dump_json(indent=4)}")

        # fetch node from from backend
        try:
            current_node_data: Node = self.node_repo.get_node_data(strict=True)
            logger.info("retrieved node data from local repo")
            fetched_node_data = await fetch_node_data(
                current_node_data.id, self.api_config
            )
            logger.info("fetched node data from backend")
            self.node_repo.save_node_data(fetched_node_data)
            logger.debug(
                f"Fetched node data: {fetched_node_data.model_dump_json(indent=4)}"
            )
        except Exception as e:
            logger.error(f"Failed to fetch node data: {e}")
            return

        # create diff
        try:
            diff_result = await self.cluster_config_service.generate_diff(
                cluster_id=fetched_node_data.cluster_id
            )
            if diff_result.is_err():
                logger.error(f"Failed to generate diff: {diff_result.unwrap_err()}")
                return
            diff = diff_result.unwrap()
            logger.debug(f"Generated diff: {diff.model_dump_json(indent=4)}")

            # generate plan
            logger.debug("Generating reconciliation plan ...")
            plan_result = await self.cluster_config_service.plan_reconciliation(diff)
            if plan_result.is_err():
                logger.error(f"Failed to generate plan: {plan_result.unwrap_err()}")
                return
            plan = plan_result.unwrap()
            logger.debug(f"Generated plan: {plan}")

            # execute plan
            logger.debug("Executing reconciliation plan ...")
            await self.cluster_config_service.reconcile(plan=plan)
        except Exception as e:
            logger.error(f"Failed to reconcile cluster: {e}")
            return


async def fetch_node_data(node_id: int, api_config: Configuration) -> Node:
    logger.info("Fetching node data from backend [Node ID: {}]", node_id)
    logger.debug("api_config token: {}", api_config.access_token)
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"{config.settings.backend_api_url}/nodes/{node_id}",
            headers={
                "Authorization": f"Bearer {api_config.access_token}",
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
        ) as response:
            response.raise_for_status()
            node_data = await response.json()
            return Node.model_validate(node_data)


async def fetch_cluster_data(cluster_id: str, api_config: Configuration) -> Cluster:
    async with ApiClient(api_config) as api_client:
        clusters_api = ClustersApi(api_client)
        cluster = await clusters_api.get_cluster_clusters_cluster_id_get(cluster_id)
        return cluster
