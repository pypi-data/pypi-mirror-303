from abc import ABCMeta

from robotcloud.api import APIEndPointAuthenticated


class ServiceInstanceEndpoint(APIEndPointAuthenticated, metaclass=ABCMeta):
    def __init__(self, token: str, project_id: str, service_type: str, instance_id: str = None):
        self.project_id = project_id
        self.service_type = service_type
        self.instance_id = instance_id
        super().__init__(token)


class APICallServiceInstanceData(ServiceInstanceEndpoint):
    """
        Implement GET
    """

    def get_endpoint(self):
        if self.instance_id is None:
            return f'projects/{self.project_id}/services/{self.service_type}/data'
        else:
            return f'projects/{self.project_id}/services/{self.service_type}/instances/{self.instance_id}/data'


class APICallServiceInstanceConfig(ServiceInstanceEndpoint):
    """
        Implement GET, PUT methods
    """

    def get_endpoint(self):
        if self.instance_id is None:
            return f'projects/{self.project_id}/services/{self.service_type}/configuration'
        else:
            return f'projects/{self.project_id}/services/{self.service_type}/instances/{self.instance_id}/configuration'


class APICallServiceInstanceAlert(ServiceInstanceEndpoint):
    """
        Implement GET
    """

    def get_endpoint(self):
        if self.instance_id is None:
            return f'projects/{self.project_id}/services/{self.service_type}/alert'
        else:
            return f'projects/{self.project_id}/services/{self.service_type}/instances/{self.instance_id}/alert'


class ServiceInstanceActionAPIEndpoint(ServiceInstanceEndpoint):
    def get_endpoint(self):
        if self.instance_id is None:
            raise Exception("RobotCloud endpoint bad usage")
        return f'projects/{self.project_id}/services/{self.service_type}/instances/{self.instance_id}/action'


class ServiceInstanceHistoricDataAPIEndpoint(ServiceInstanceEndpoint):
    def get_endpoint(self):
        if self.instance_id is None:
            raise Exception("RobotCloud endpoint bad usage")
        return f'projects/{self.project_id}/services/{self.service_type}/instances/{self.instance_id}/historic/data'


class ServiceInstanceHistoricDataAggregateAPIEndpoint(ServiceInstanceEndpoint):
    def get_endpoint(self):
        if self.instance_id is None:
            raise Exception("RobotCloud endpoint bad usage")
        return (f'projects/{self.project_id}/services/{self.service_type}/instances/{self.instance_id}/historic/data'
                f'/aggregate')
