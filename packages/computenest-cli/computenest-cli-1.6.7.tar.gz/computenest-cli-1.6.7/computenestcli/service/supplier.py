# -*- coding: utf-8 -*-
import json
from alibabacloud_computenestsupplier20210521 import models as compute_nest_supplier_20210521_models
from computenestcli.common.util import Util
from computenestcli.common import constant
from computenestcli.service.base import Service


def _json_dumps_adapt_none(obj):
    if obj is None:
        return None
    return json.dumps(obj)


class SupplierService(Service):

    @classmethod
    def create_service(cls, context, service_config, service_id=''):
        # 提取配置信息
        service_info_config = service_config.get(constant.SERVICE_INFO)
        deploy_metadata_config = service_config.get(constant.DEPLOY_METADATA)

        # 处理操作元数据
        operation_metadata = service_config.get(constant.OPERATION_METADATA, '{}')
        if operation_metadata != '{}':
            operation_metadata = json.dumps(operation_metadata)

        # 处理版本名称及部署元数据, 指定了版本名称时，不再加随机数
        version_name = service_config.get(constant.VERSION_NAME)
        if version_name is None:
            version_name = Util.add_timestamp_to_version_name(service_config.get(constant.VERSION_NAME))
        deploy_metadata = json.dumps(deploy_metadata_config)

        # 创建服务信息对象
        service_info_init = compute_nest_supplier_20210521_models.CreateServiceRequestServiceInfo(
            locale=service_info_config.get(constant.LOCALE),
            short_description=service_info_config.get(constant.SHORT_DESCRIPTION),
            image=service_info_config.get(constant.IMAGE),
            name=service_info_config.get(constant.NAME)
        )

        # 生成创建服务请求参数
        create_service_request_params = {
            'region_id': context.region_id,
            'deploy_type': service_config.get(constant.DEPLOY_TYPE),
            'operation_metadata': operation_metadata,
            'version_name': version_name,
            'service_type': service_config.get(constant.SERVICE_TYPE),
            'service_info': [service_info_init],
            'deploy_metadata': deploy_metadata,
            'is_support_operated': service_config.get(constant.IS_SUPPORT_OPERATED),
            'policy_names': service_config.get(constant.POLICY_NAMES),
            'alarm_metadata': _json_dumps_adapt_none(service_config.get(constant.ALARM_METADATA)),
            'duration': service_config.get(constant.DURATION),
            'license_metadata': _json_dumps_adapt_none(service_config.get(constant.LICENSE_METADATA)),
            'log_metadata': _json_dumps_adapt_none(service_config.get(constant.LOG_METADATA)),
            'resource_group_id': service_config.get(constant.RESOURCE_GROUP_ID),
            'source_service_id': service_config.get(constant.SOURCE_SERVICE_ID),
            'source_service_version': service_config.get(constant.SOURCE_SERVICE_VERSION),
            'tenant_type': service_config.get(constant.TENANT_TYPE),
            'trial_duration': service_config.get(constant.TRIAL_DURATION),
            'upgrade_metadata': _json_dumps_adapt_none(service_config.get(constant.UPGRADE_METADATA)),
        }

        # 如果有 service_id，则添加到请求参数中
        if service_id:
            create_service_request_params['service_id'] = service_id

        # 创建服务请求对象
        create_service_request = compute_nest_supplier_20210521_models.CreateServiceRequest(
            **create_service_request_params)

        # 调用客户端创建服务
        client = cls._get_computenest_client(context)
        response = client.create_service(create_service_request)

        return response

    @classmethod
    def update_service(cls, context, service_config, service_id):
        service_info = service_config.get(constant.SERVICE_INFO)
        deploy_meta_data = service_config.get(constant.DEPLOY_METADATA)
        operation_metadata = service_config.get(constant.OPERATION_METADATA)
        if operation_metadata is None:
            operation_metadata = '{}'
        else:
            operation_metadata = json.dumps(operation_metadata)

        version_name = service_config.get(constant.VERSION_NAME)
        if version_name is None:
            version_name = Util.add_timestamp_to_version_name(service_config.get(constant.VERSION_NAME))
        deploy_metadata = service_config.get(constant.DEPLOY_METADATA)
        if deploy_metadata and deploy_metadata.get(constant.TEMPLATE_CONFIGS):
            for template in deploy_metadata.get(constant.TEMPLATE_CONFIGS):
                template[constant.PREDEFINED_PARAMETERS] = template.get(constant.PREDEFINED_PARAMETERS) or []
                template[constant.HIDDEN_PARAMETER_KEYS] = template.get(constant.HIDDEN_PARAMETER_KEYS) or []
        json_data = json.dumps(deploy_meta_data)
        service_info_init = compute_nest_supplier_20210521_models.UpdateServiceRequestServiceInfo(
            name=service_info.get(constant.NAME),
            image=service_info.get(constant.IMAGE),
            short_description=service_info.get(constant.SHORT_DESCRIPTION),
            locale=service_info.get(constant.LOCALE)
        )
        update_service_request = compute_nest_supplier_20210521_models.UpdateServiceRequest(
            region_id=context.region_id,
            deploy_type=service_config.get(constant.DEPLOY_TYPE),
            operation_metadata=operation_metadata,
            version_name=version_name,
            service_id=service_id,
            service_info=[service_info_init],
            deploy_metadata=json_data,
            service_type=service_config.get(constant.SERVICE_TYPE),
            is_support_operated=service_config.get(constant.IS_SUPPORT_OPERATED),
            policy_names=service_config.get(constant.POLICY_NAMES),
            alarm_metadata=_json_dumps_adapt_none(service_config.get(constant.ALARM_METADATA)),
            duration=service_config.get(constant.DURATION),
            license_metadata=_json_dumps_adapt_none(service_config.get(constant.LICENSE_METADATA)),
            log_metadata=_json_dumps_adapt_none(service_config.get(constant.LOG_METADATA)),
            tenant_type=service_config.get(constant.TENANT_TYPE),
            trial_duration=service_config.get(constant.TRIAL_DURATION),
            upgrade_metadata=_json_dumps_adapt_none(service_config.get(constant.UPGRADE_METADATA)),
        )
        client = cls._get_computenest_client(context)
        response = client.update_service(update_service_request)
        return response

    @classmethod
    def list_service(cls, context, service_name, service_versions):
        filter_query = []
        filter_service_name = compute_nest_supplier_20210521_models.ListServicesRequestFilter(
            name=constant.NAME,
            value=[service_name]
        )
        filter_query.append(filter_service_name)
        if service_versions:
            filter_service_versions = compute_nest_supplier_20210521_models.ListServicesRequestFilter(
                name=constant.VERSION,
                value=service_versions
            )
            filter_query.append(filter_service_versions)

        list_services_request = compute_nest_supplier_20210521_models.ListServicesRequest(
            region_id=context.region_id,
            all_versions=True,
            filter=filter_query
        )
        client = cls._get_computenest_client(context)
        response = client.list_services(list_services_request)
        return response

    @classmethod
    def get_service(cls, context, service_id, service_version):
        get_service_request = compute_nest_supplier_20210521_models.GetServiceRequest(
            region_id=context.region_id,
            service_id=service_id,
            service_version=service_version
        )
        client = cls._get_computenest_client(context)
        response = client.get_service(get_service_request)
        return response
