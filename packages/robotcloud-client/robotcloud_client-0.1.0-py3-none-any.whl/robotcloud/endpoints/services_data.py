from typing import List

from robotcloud.typing import RobotCloudServiceInstanceMeasurement, HistoricAggregateFunction

from robotcloud.endpoints.endpoint_classes.services_data import *


def get_service_instance_data(token,
                              project_id, service_type, instance_id=None) -> RobotCloudServiceInstanceMeasurement:
    """
    If instance_id is None then return data from all project service_type instances
    otherwise, only return the data from the specified instance.

    :param token:
    :param project_id:
    :param service_type:
    :param instance_id:
    :raises:
    :return:
    """
    api_response = APICallServiceInstanceData(token, project_id, service_type, instance_id).get()
    if type(api_response) is dict:
        return api_response  # Single data

    response = {}
    for data in api_response:
        response[data['instance']] = data

    return response


def get_service_instance_config(token, project_id, service_type, instance_id) -> dict:
    """
    If instance_id is None then return data from all project service_type instances
    otherwise, only return the data from the specified instance.

    :param token:
    :param project_id:
    :param service_type:
    :param instance_id:
    :return:
    """
    return APICallServiceInstanceConfig(token, project_id, service_type, instance_id).get()


def update_service_instance_config(token, project_id, service_type, instance_id, data):
    """
    Update the specified service instance configuration.

    :param token:
    :param project_id:
    :param service_type:
    :param instance_id:
    :param data: Data to update
    :return:
    """
    return APICallServiceInstanceConfig(token, project_id, service_type, instance_id).put(data)


def get_service_instance_alert(token, project_id, service_type, instance_id=None
                               ) -> RobotCloudServiceInstanceMeasurement:
    """
    If instance_id is None then return data from all project service_type instances
    otherwise, only return the data from the specified instance.

    :param token:
    :param project_id:
    :param service_type:
    :param instance_id:
    :return:
    """
    api_response = APICallServiceInstanceAlert(token, project_id, service_type, instance_id).get()
    if type(api_response) is dict:
        return api_response  # Single data

    response = {}
    for data in api_response:
        response[data['instance']] = data

    return response


def apply_service_instance_action(token, project_id, service_type, instance_id, command: str,
                                  arguments: List[str]) -> dict:
    """
    Apply an action on a server instance.
    Program which call this function would validate if commands and arguments are valid and allowed.


    :param token:
    :param project_id:
    :param service_type:
    :param instance_id:
    :param command:
    :param arguments:

    :return:
    """
    api_response = ServiceInstanceActionAPIEndpoint(token, project_id, service_type, instance_id).put(data={
        "command": command,
        "arguments": arguments
    })
    if type(api_response) is dict:
        return api_response  # Single data

    response = {}
    for data in api_response:
        response[data['instance']] = data

    return response


def get_service_instance_historic_data(token, project_id, service_type, instance_id, start_time, end_time,
                                       query_params: dict = None) -> List[RobotCloudServiceInstanceMeasurement]:
    params = {'start_time': start_time, 'end_time': end_time}
    if query_params is not None:
        params.update(query_params)
    return ServiceInstanceHistoricDataAPIEndpoint(token, project_id, service_type, instance_id).get(params=params)


def get_service_instance_historic_data_aggregate(token, project_id, service_type, instance_id,
                                                 start_time, end_time, function: HistoricAggregateFunction,
                                                 periode: str,
                                                 query_params: dict = None
                                                 ) -> List[RobotCloudServiceInstanceMeasurement]:
    params = {'start_time': start_time, 'end_time': end_time, 'function': function, 'periode': periode}
    if query_params is not None:
        params.update(query_params)
    return (ServiceInstanceHistoricDataAggregateAPIEndpoint(token, project_id, service_type, instance_id)
            .get(params=params))
