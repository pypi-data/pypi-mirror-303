# Copyright 2018 Red Hat, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_log import log as logging
from oslo_utils import netutils
import swiftclient.exceptions

from ironic.common import exception
from ironic.common import swift
from ironic.conf import CONF
from ironic import objects
from ironic.objects import node_inventory

LOG = logging.getLogger(__name__)
_OBJECT_NAME_PREFIX = 'inspector_data'


def create_ports_if_not_exist(task, macs):
    """Create ironic ports from MAC addresses data dict.

    Creates ironic ports from MAC addresses data returned with inspection or
    as requested by operator. Helper argument to detect the MAC address
    ``get_mac_address`` defaults to 'value' part of MAC address dict key-value
    pair.

    :param task: A TaskManager instance.
    :param macs: A sequence of MAC addresses.
    """
    node = task.node
    for mac in macs:
        if not netutils.is_valid_mac(mac):
            LOG.warning("Ignoring NIC address %(address)s for node %(node)s "
                        "because it is not a valid MAC",
                        {'address': mac, 'node': node.uuid})
            continue

        port_dict = {'address': mac, 'node_id': node.id}
        port = objects.Port(task.context, **port_dict)

        try:
            port.create()
            LOG.info("Port created for MAC address %(address)s for node "
                     "%(node)s", {'address': mac, 'node': node.uuid})
        except exception.MACAlreadyExists:
            LOG.info("Port already exists for MAC address %(address)s "
                     "for node %(node)s", {'address': mac, 'node': node.uuid})


def clean_up_swift_entries(task):
    """Delete swift entries containing introspection data.

    Delete swift entries related to the node in task.node containing
    introspection data. The entries are
    ``inspector_data-<task.node.uuid>-inventory`` for hardware inventory and
    similar for ``-plugin`` containing the rest of the introspection data.

    :param task: A TaskManager instance.
    """
    if CONF.inventory.data_backend != 'swift':
        return
    swift_api = swift.SwiftAPI()
    swift_object_name = '%s-%s' % (_OBJECT_NAME_PREFIX, task.node.uuid)
    container = CONF.inventory.swift_data_container
    inventory_obj_name = swift_object_name + '-inventory'
    plugin_obj_name = swift_object_name + '-plugin'
    try:
        swift_api.delete_object(inventory_obj_name, container)
    except swiftclient.exceptions.ClientException as e:
        if e.http_status == 404:
            # 404 -> entry did not exist - acceptable.
            pass
        else:
            LOG.error("Object %(obj)s related to node %(node)s "
                      "failed to be deleted with expection: %(e)s",
                      {'obj': inventory_obj_name, 'node': task.node.uuid,
                       'e': e})
            raise exception.SwiftObjectStillExists(obj=inventory_obj_name,
                                                   node=task.node.uuid)
    try:
        swift_api.delete_object(plugin_obj_name, container)
    except swiftclient.exceptions.ClientException as e:
        if e.http_status == 404:
            # 404 -> entry did not exist - acceptable.
            pass
        else:
            LOG.error("Object %(obj)s related to node %(node)s "
                      "failed to be deleted with exception: %(e)s",
                      {'obj': plugin_obj_name, 'node': task.node.uuid,
                       'e': e})
            raise exception.SwiftObjectStillExists(obj=plugin_obj_name,
                                                   node=task.node.uuid)


def store_introspection_data(node, introspection_data, context):
    """Store introspection data.

    Store the introspection data for a node. Either to database
    or swift as configured.

    :param node: the Ironic node that the introspection data is about
    :param introspection_data: the data to store
    :param context: an admin context
    """
    # If store_data == 'none', do not store the data
    store_data = CONF.inventory.data_backend
    if store_data == 'none':
        LOG.debug('Introspection data storage is disabled, the data will '
                  'not be saved for node %(node)s', {'node': node.uuid})
        return
    inventory_data = introspection_data.pop("inventory")
    plugin_data = introspection_data
    if store_data == 'database':
        node_inventory.NodeInventory(
            context,
            node_id=node.id,
            inventory_data=inventory_data,
            plugin_data=plugin_data).create()
        LOG.info('Introspection data was stored in database for node '
                 '%(node)s', {'node': node.uuid})
    if store_data == 'swift':
        swift_object_name = _store_introspection_data_in_swift(
            node_uuid=node.uuid,
            inventory_data=inventory_data,
            plugin_data=plugin_data)
        LOG.info('Introspection data was stored for node %(node)s in Swift'
                 ' object %(obj_name)s-inventory and %(obj_name)s-plugin',
                 {'node': node.uuid, 'obj_name': swift_object_name})


def _node_inventory_convert(node_inventory):
    inventory_data = node_inventory['inventory_data']
    plugin_data = node_inventory['plugin_data']
    return {"inventory": inventory_data, "plugin_data": plugin_data}


def get_introspection_data(node, context):
    """Get introspection data.

    Retrieve the introspection data for a node. Either from database
    or swift as configured.

    :param node_id: the Ironic node that the required data is about
    :param context: an admin context
    :returns: dictionary with ``inventory`` and ``plugin_data`` fields
    """
    store_data = CONF.inventory.data_backend
    if store_data == 'none':
        raise exception.NodeInventoryNotFound(node=node.uuid)
    if store_data == 'database':
        node_inventory = objects.NodeInventory.get_by_node_id(
            context, node.id)
        return _node_inventory_convert(node_inventory)
    if store_data == 'swift':
        try:
            node_inventory = _get_introspection_data_from_swift(node.uuid)
        except exception.SwiftObjectNotFoundError:
            raise exception.NodeInventoryNotFound(node=node.uuid)
        return node_inventory


def _store_introspection_data_in_swift(node_uuid, inventory_data, plugin_data):
    """Uploads introspection data to Swift.

    :param data: data to store in Swift
    :param node_id: ID of the Ironic node that the data came from
    :returns: name of the Swift object that the data is stored in
    """
    swift_api = swift.SwiftAPI()
    swift_object_name = '%s-%s' % (_OBJECT_NAME_PREFIX, node_uuid)
    container = CONF.inventory.swift_data_container
    swift_api.create_object_from_data(swift_object_name + '-inventory',
                                      inventory_data,
                                      container)
    swift_api.create_object_from_data(swift_object_name + '-plugin',
                                      plugin_data,
                                      container)
    return swift_object_name


def _get_introspection_data_from_swift(node_uuid):
    """Get introspection data from Swift.

    :param node_uuid: UUID of the Ironic node that the data came from
    :returns: dictionary with ``inventory`` and ``plugin_data`` fields
    """
    swift_api = swift.SwiftAPI()
    swift_object_name = '%s-%s' % (_OBJECT_NAME_PREFIX, node_uuid)
    container = CONF.inventory.swift_data_container
    inv_obj = swift_object_name + '-inventory'
    plug_obj = swift_object_name + '-plugin'
    try:
        inventory_data = swift_api.get_object(inv_obj, container)
    except exception.SwiftOperationError:
        LOG.error("Failed to retrieve object %(obj)s from swift",
                  {'obj': inv_obj})
        raise exception.SwiftObjectNotFoundError(obj=inv_obj,
                                                 container=container,
                                                 operation='get')
    try:
        plugin_data = swift_api.get_object(plug_obj, container)
    except exception.SwiftOperationError:
        LOG.error("Failed to retrieve object %(obj)s from swift",
                  {'obj': plug_obj})
        raise exception.SwiftObjectNotFoundError(obj=plug_obj,
                                                 container=container,
                                                 operation='get')
    return {"inventory": inventory_data, "plugin_data": plugin_data}
