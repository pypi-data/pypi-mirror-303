from amsdal_data.application import DataApplication

from amsdal_server.apps.healthcheck.enums import StatusEnum
from amsdal_server.apps.healthcheck.serializers.healthcheck_result import HealthcheckServiceResult
from amsdal_server.apps.healthcheck.services.checkers.base import BaseHealthchecker


class ConnectionsHealthchecker(BaseHealthchecker):
    async def check(self) -> HealthcheckServiceResult:
        data_app = DataApplication()

        for connection in data_app.connections_statuses:
            if not connection.is_connected:
                return HealthcheckServiceResult(
                    status=StatusEnum.error,
                    service=self.__class__.__name__,
                    message='Connection is not established',
                )

            if not connection.is_alive:
                return HealthcheckServiceResult(
                    status=StatusEnum.error,
                    service=self.__class__.__name__,
                    message='Connection is not alive',
                )

        return HealthcheckServiceResult(
            status=StatusEnum.success,
            service=self.__class__.__name__,
            message='Connection is alive',
        )
