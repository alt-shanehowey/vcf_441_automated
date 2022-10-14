class URI(object):
    url_template = '{}/v1'
    base_url = url_template

    def __init__(self, sddc_url='localhost:8080'):
        self.sddc_url = sddc_url
        self.set_base_url()

    def set_base_url(self):
        self.base_url = self.url_template.format(self.sddc_url)


def get_uri():
    return {
        'edge_validate': '{}/edge-clusters/validations/',  # POST
        'edge_deploy': '{}/edge-clusters/',  # POST
        'avn_validate': '{}/avns/validations',  # POST
        'avn_deploy': '{}/avns/',  # POST
        'create_token': '{}/tokens',  # POST
        'clusters': '{}/clusters',  # GET
        'edge_clusters': '{}/edge-clusters',  # GET
        'vrslcm_deploy': '{}'  # GET

    }


def edge_data(edge_cluster_name, edge_cluster_type, edge_cluster_root_password, edge_cluster_admin_password,
              edge_cluster_audit_password, edge_node0_name, edge_node0_mgmt_ip, edge_node0_mgmt_gateway,
              edge_node0_tep_gateway, edge_node0_tep_ip1, edge_node0_tep_ip2, sddc_dc_id,
              edge_node0_uplink_interface0_ip, edge_node0_uplink_interface1_ip, edge_node0_peer1_ip, edge_node1_name,
              edge_node1_mgmt_ip, edge_node1_mgmt_gateway, edge_node1_tep_gateway, edge_node1_tep_ip1,
              edge_node1_tep_ip2, edge_node1_uplink_interface0_ip, edge_node1_peer0_ip,
              edge_node1_uplink_interface1_ip, edge_node1_peer1_ip, edge_node_tier0_routing_type, edge_node_tier0_name,
              edge_node_tier1_name):
    return {
        "edgeClusterName": edge_cluster_name,
        "edgeClusterType": edge_cluster_type,
        "edgeRootPassword": edge_cluster_root_password,
        "edgeAdminPassword": edge_cluster_admin_password,
        "edgeAuditPassword": edge_cluster_audit_password,
        "edgeFormFactor": "LARGE",
        "tier0ServicesHighAvailability": "ACTIVE_ACTIVE",
        "mtu": 9000,
        "asn": 65532,
        "edgeNodeSpecs": [{
            "edgeNodeName": edge_node0_name,
            "managementIP": edge_node0_mgmt_ip,
            "managementGateway": edge_node0_mgmt_gateway,
            "edgeTepGateway": edge_node0_tep_gateway,
            "edgeTep1IP": edge_node0_tep_ip1,
            "edgeTep2IP": edge_node0_tep_ip2,
            "edgeTepVlan": 1006,
            "clusterId": sddc_dc_id,
            "interRackCluster": False,
            "uplinkNetwork": [{
                "uplinkVlan": 1004,
                "uplinkInterfaceIP": edge_node0_uplink_interface0_ip,
                "peerIP": "{{edge_node0_peer0_ip}}",
                "asnPeer": 65530,
                "bgpPeerPassword": ""
            }, {
                "uplinkVlan": 1005,
                "uplinkInterfaceIP": edge_node0_uplink_interface1_ip,
                "peerIP": edge_node0_peer1_ip,
                "asnPeer": 65530,
                "bgpPeerPassword": ""
            }]
        }, {
            "edgeNodeName": edge_node1_name,
            "managementIP": edge_node1_mgmt_ip,
            "managementGateway": edge_node1_mgmt_gateway,
            "edgeTepGateway": edge_node1_tep_gateway,
            "edgeTep1IP": edge_node1_tep_ip1,
            "edgeTep2IP": edge_node1_tep_ip2,
            "edgeTepVlan": 1006,
            "clusterId": sddc_dc_id,
            "interRackCluster": False,
            "uplinkNetwork": [{
                "uplinkVlan": 1004,
                "uplinkInterfaceIP": edge_node1_uplink_interface0_ip,
                "peerIP": edge_node1_peer0_ip,
                "asnPeer": 65530,
                "bgpPeerPassword": ""
            }, {
                "uplinkVlan": 1005,
                "uplinkInterfaceIP": edge_node1_uplink_interface1_ip,
                "peerIP": edge_node1_peer1_ip,
                "asnPeer": 65530,
                "bgpPeerPassword": ""
            }]
        }],
        "tier0RoutingType": edge_node_tier0_routing_type,
        "tier0Name": edge_node_tier0_name,
        "tier1Name": edge_node_tier1_name,
        "edgeClusterProfileType": "DEFAULT"
    }


def avn_data(sddc_ec_id, avn0_name, avn0_region, avn0_subnet, avn0_subnet_mask, avn0_gateway, avn0_router_name,
             avn1_name, avn1_region, avn1_subnet, avn1_subnet_mask, avn1_gateway, avn1_router_name):
    return {
        "edgeClusterId": sddc_ec_id,
        "avns": [{
            "name": avn0_name,
            "regionType": avn0_region,
            "subnet": avn0_subnet,
            "subnetMask": avn0_subnet_mask,
            "gateway": avn0_gateway,
            "mtu": 9000,
            "routerName": avn0_router_name
        }, {
            "name": avn1_name,
            "regionType": avn1_region,
            "subnet": avn1_subnet,
            "subnetMask": avn1_subnet_mask,
            "gateway": avn1_gateway,
            "mtu": 9000,
            "routerName": avn1_router_name
        }]
    }


def token_data(token_password):
    return {
        "username": "administrator@vsphere.local",
        "password": token_password
    }


def vrslcm_data(default_password, vrslcm_url, vrslcm_tier1_ip):
    return {
        "apiPassword": default_password,
        "fqdn": vrslcm_url,
        "nsxtStandaloneTier1Ip": vrslcm_tier1_ip,
        "sshPassword": default_password
    }
