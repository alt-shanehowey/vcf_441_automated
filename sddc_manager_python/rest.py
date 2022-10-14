import requests
from loguru import logger
from sddc_manager_python.rest_data import get_uri, edge_data, avn_data, token_data, vrslcm_data

logger.level("REST", no=37, color="<magenta>")


class VCFRest:
    def __init__(self):
        self.sddc_url = 'localhost:8080'
        self.headers = {'content-type': 'application/json'}
        self.uri = dict()
        self.generate_uri()

    def generate_uri(self):
        v1_rest = '{}/v1'.format(self.sddc_url)
        uri = get_uri()
        for u in uri:
            uri[u] = uri[u].format(v1_rest)
        self.uri = uri

    def post_edge_validation(self, edge_cluster_name, edge_cluster_type, edge_cluster_root_password,
                             edge_cluster_admin_password,
                             edge_cluster_audit_password, edge_node0_name, edge_node0_mgmt_ip, edge_node0_mgmt_gateway,
                             edge_node0_tep_gateway, edge_node0_tep_ip1, edge_node0_tep_ip2, sddc_dc_id,
                             edge_node0_uplink_interface0_ip, edge_node0_uplink_interface1_ip, edge_node0_peer1_ip,
                             edge_node1_name,
                             edge_node1_mgmt_ip, edge_node1_mgmt_gateway, edge_node1_tep_gateway, edge_node1_tep_ip1,
                             edge_node1_tep_ip2, edge_node1_uplink_interface0_ip, edge_node1_peer0_ip,
                             edge_node1_uplink_interface1_ip, edge_node1_peer1_ip, edge_node_tier0_routing_type,
                             edge_node_tier0_name,
                             edge_node_tier1_name):

        edge_validate = edge_data(edge_cluster_name, edge_cluster_type, edge_cluster_root_password,
                                  edge_cluster_admin_password,
                                  edge_cluster_audit_password, edge_node0_name, edge_node0_mgmt_ip,
                                  edge_node0_mgmt_gateway,
                                  edge_node0_tep_gateway, edge_node0_tep_ip1, edge_node0_tep_ip2, sddc_dc_id,
                                  edge_node0_uplink_interface0_ip, edge_node0_uplink_interface1_ip, edge_node0_peer1_ip,
                                  edge_node1_name,
                                  edge_node1_mgmt_ip, edge_node1_mgmt_gateway, edge_node1_tep_gateway,
                                  edge_node1_tep_ip1,
                                  edge_node1_tep_ip2, edge_node1_uplink_interface0_ip, edge_node1_peer0_ip,
                                  edge_node1_uplink_interface1_ip, edge_node1_peer1_ip, edge_node_tier0_routing_type,
                                  edge_node_tier0_name,
                                  edge_node_tier1_name)

        create_response = requests.post(self.uri['edge_validate'], json=edge_validate, headers=self.headers)
        if create_response.status_code != 200:
            logger.log('REST', 'Edge validation POST failed')
            return None

    def deploy_edge(self, edge_cluster_name, edge_cluster_type, edge_cluster_root_password, edge_cluster_admin_password,
                    edge_cluster_audit_password, edge_node0_name, edge_node0_mgmt_ip, edge_node0_mgmt_gateway,
                    edge_node0_tep_gateway, edge_node0_tep_ip1, edge_node0_tep_ip2, sddc_dc_id,
                    edge_node0_uplink_interface0_ip, edge_node0_uplink_interface1_ip, edge_node0_peer1_ip,
                    edge_node1_name,
                    edge_node1_mgmt_ip, edge_node1_mgmt_gateway, edge_node1_tep_gateway, edge_node1_tep_ip1,
                    edge_node1_tep_ip2, edge_node1_uplink_interface0_ip, edge_node1_peer0_ip,
                    edge_node1_uplink_interface1_ip, edge_node1_peer1_ip, edge_node_tier0_routing_type,
                    edge_node_tier0_name,
                    edge_node_tier1_name):

        edge_deploy = edge_data(edge_cluster_name, edge_cluster_type, edge_cluster_root_password,
                                edge_cluster_admin_password,
                                edge_cluster_audit_password, edge_node0_name, edge_node0_mgmt_ip,
                                edge_node0_mgmt_gateway,
                                edge_node0_tep_gateway, edge_node0_tep_ip1, edge_node0_tep_ip2, sddc_dc_id,
                                edge_node0_uplink_interface0_ip, edge_node0_uplink_interface1_ip, edge_node0_peer1_ip,
                                edge_node1_name,
                                edge_node1_mgmt_ip, edge_node1_mgmt_gateway, edge_node1_tep_gateway, edge_node1_tep_ip1,
                                edge_node1_tep_ip2, edge_node1_uplink_interface0_ip, edge_node1_peer0_ip,
                                edge_node1_uplink_interface1_ip, edge_node1_peer1_ip, edge_node_tier0_routing_type,
                                edge_node_tier0_name,
                                edge_node_tier1_name)

        create_response = requests.post(self.uri['edge_deploy'], json=edge_deploy, headers=self.headers)
        if create_response.status_code != 200:
            logger.log('REST', 'Edge deploy POST failed')
            return None

    def validate_avn(self, sddc_ec_id, avn0_name, avn0_region, avn0_subnet, avn0_subnet_mask, avn0_gateway,
                     avn0_router_name,
                     avn1_name, avn1_region, avn1_subnet, avn1_subnet_mask, avn1_gateway, avn1_router_name):

        avn_validate = avn_data(sddc_ec_id, avn0_name, avn0_region, avn0_subnet, avn0_subnet_mask, avn0_gateway,
                                avn0_router_name,
                                avn1_name, avn1_region, avn1_subnet, avn1_subnet_mask, avn1_gateway, avn1_router_name)

        create_response = requests.post(self.uri['avn_validate'], json=avn_validate, headers=self.headers)
        if create_response.status_code != 200:
            logger.log('REST', 'AVN validate POST failed')
            return None

    def deploy_avn(self, sddc_ec_id, avn0_name, avn0_region, avn0_subnet, avn0_subnet_mask, avn0_gateway,
                   avn0_router_name,
                   avn1_name, avn1_region, avn1_subnet, avn1_subnet_mask, avn1_gateway, avn1_router_name):

        avn_deploy = avn_data(sddc_ec_id, avn0_name, avn0_region, avn0_subnet, avn0_subnet_mask, avn0_gateway,
                              avn0_router_name,
                              avn1_name, avn1_region, avn1_subnet, avn1_subnet_mask, avn1_gateway, avn1_router_name)

        create_response = requests.post(self.uri['avn_deploy'], json=avn_deploy, headers=self.headers)
        if create_response.status_code != 200:
            logger.log('REST', 'AVN deploy POST failed')
            return None

    def create_token(self, token_password):

        create_token = token_data(token_password)

        create_response = requests.post(self.uri['create_token'], json=create_token, headers=self.headers)
        if create_response.status_code != 200:
            logger.log('REST', 'Toked creation POST failed')
            return None

    def get_clusters(self):
        clusters = requests.get(self.uri['clusters'], headers=self.headers)
        if clusters.status_code != 200:
            logger.log('REST', 'Clusters GET failed')
        return clusters.content, None

    def get_edge_clusters(self):
        edge_clusters = requests.get(self.uri['edge_clusters'], headers=self.headers)
        if edge_clusters.status_code != 200:
            logger.log('REST', 'Edge clusters GET failed')
        return edge_clusters.content, None
