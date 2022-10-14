class URI(object):
    url_template = '{}/v1/sddcs'
    base_url = url_template

    def __init__(self, cb_url='localhost:8080'):
        self.cb_url = cb_url
        self.set_base_url()

    def set_base_url(self):
        self.base_url = self.url_template.format(self.cb_url)


def get_uri():
    return {
        'sddc_validate': '{}/validations/',  # GET, POST
        'deploy': '{}/'  # POST

    }


def sddc_data(np1_mgmt, complex_password, sddcm_ip, sddcm_subnet, sddcm_host_short, sddcm_licensekey,
              simple_password, mgmt_vc_id, sddcm_sddcid, esxi_license, set_ceip, set_fips, ntps_primary,
              ntps_secondary, dns_secondaryns, dns_subdomain, dns_domainname, dns_primaryns, net_mgmt_subnet,
              net_mgmt_gateway, net_mgmt_vlan, net_mgmt_mtu, net_mgmt_pg_name, net_vmotion_subnet,
              net_vmotion_gateway, net_vmotion_vlanid, net_vmotion_mtu, net_vmotion_pg_name,
              vc_datacenter_name,
              net_vmotion_ipend, net_vmotion_ipstart, net_vsan_subnet, net_vsan_gateway, net_vsan_vlanid,
              net_vsan_mtu, psc_spec_name, net_vsan_pg_name, net_vsan_ipend, net_vsan_ipstart, nsxt_m_size,
              nsxt_m1_hostname_short, nsxt_m1_ip, nsxt_m2_hostname_short, nsxt_m2_ip, nsxt_m3_hostname_short,
              nsxt_m3_ip, nsxt_tz_overlayname, nsxt_tz_overlaynetworkname, nsxt_tz_vlanname,
              nsxt_tz_vlannetworkname, nsxt_vip_name, nsxt_vip_fqdn, nsxt_licensekey, nsxt_htep_vlanid,
              nsxt_np2_htep_name, nsxt_np2_htep_desc, net_htep_ipstart, net_htep_ipend, net_htep_cidr,
              net_htep_gateway, vsan_spec_name, vsan_licensekey, set_vsan_dedupe, vsan_dsname, vds1_version,
              vds1_dvsname, vds1_vcenterid, vds1_mtu, vds1_set_isnsxt, vc_mgmt_clustername, vc_spec_name,
              vc_evcmode,
              vmfolder_mgmt, vmfolder_net, vmfolder_edge, rps_mgmt_name, rps_mgmt_net, rp_usr_edge, rp_usr_vm,
              vc_mgmt_ip, vc_mgmt_hostname_short, vc_licensekey, vc_vmsize, vc_storagesize, host1_mgmt_ip,
              host1_hostname_short, esxi_vss_name, host1_server_id, host2_mgmt_ip, host2_hostname_short,
              host2_server_id,
              host3_mgmt_ip, host3_hostname_short, host3_server_id, host4_mgmt_ip, host4_hostname_short,
              host4_server_id):
    return {
        "skipEsxThumbprintValidation": True,
        "managementPoolName": np1_mgmt,
        "sddcManagerSpec": {
            "secondUserCredentials": {
                "username": "vcf",
                "password": complex_password
            },
            "ipAddress": sddcm_ip,
            "netmask": sddcm_subnet,
            "hostname": sddcm_host_short,
            "licenseKey": sddcm_licensekey,
            "rootUserCredentials": {
                "username": "root",
                "password": simple_password
            },
            "localUserPassword": simple_password,
            "vcenterId": mgmt_vc_id
        },
        "sddcId": sddcm_sddcid,
        "esxLicense": esxi_license,
        "taskName": "workflowconfig/workflowspec-ems.json",
        "ceipEnabled": set_ceip,
        "fipsEnabled": set_fips,
        "ntpServers": [ntps_primary, ntps_secondary],
        "dnsSpec": {
            "secondaryNameserver": dns_secondaryns,
            "subdomain": dns_subdomain,
            "domain": dns_domainname,
            "nameserver": dns_primaryns
        },
        "networkSpecs": [
            {
                "networkType": "MANAGEMENT",
                "subnet": net_mgmt_subnet,
                "gateway": net_mgmt_gateway,
                "vlanId": net_mgmt_vlan,
                "mtu": net_mgmt_mtu,
                "portGroupKey": net_mgmt_pg_name,
                "standbyUplinks": [],
                "activeUplinks": [
                    "uplink1",
                    "uplink2"
                ]
            },
            {
                "networkType": "VMOTION",
                "subnet": net_vmotion_subnet,
                "gateway": net_vmotion_gateway,
                "vlanId": net_vmotion_vlanid,
                "mtu": net_vmotion_mtu,
                "portGroupKey": net_vmotion_pg_name,
                "association": vc_datacenter_name,
                "includeIpAddressRanges": [{"endIpAddress": net_vmotion_ipend, "startIpAddress": net_vmotion_ipstart}],
                "standbyUplinks": [],
                "activeUplinks": [
                    "uplink1",
                    "uplink2"
                ]
            },
            {
                "networkType": "VSAN",
                "subnet": net_vsan_subnet,
                "gateway": net_vsan_gateway,
                "vlanId": net_vsan_vlanid,
                "mtu": net_vsan_mtu,
                "portGroupKey": net_vsan_pg_name,
                "includeIpAddressRanges": [{"endIpAddress": net_vsan_ipend, "startIpAddress": net_vsan_ipstart}],
                "standbyUplinks": [],
                "activeUplinks": [
                    "uplink1",
                    "uplink2"
                ]
            }
        ],
        "nsxtSpec":
            {
                "nsxtManagerSize": nsxt_m_size,
                "nsxtManagers": [
                    {
                        "hostname": nsxt_m1_hostname_short,
                        "ip": nsxt_m1_ip
                    },
                    {
                        "hostname": nsxt_m2_hostname_short,
                        "ip": nsxt_m2_ip
                    },
                    {
                        "hostname": nsxt_m3_hostname_short,
                        "ip": nsxt_m3_ip
                    }
                ],
                "rootNsxtManagerPassword": complex_password,
                "nsxtAdminPassword": complex_password,
                "nsxtAuditPassword": complex_password,
                "rootLoginEnabledForNsxtManager": "true",
                "sshEnabledForNsxtManager": "true",
                "overLayTransportZone": {
                    "zoneName": nsxt_tz_overlayname,
                    "networkName": nsxt_tz_overlaynetworkname
                },
                "vlanTransportZone": {
                    "zoneName": nsxt_tz_vlanname,
                    "networkName": nsxt_tz_vlannetworkname
                },
                "vip": nsxt_vip_name,
                "vipFqdn": nsxt_vip_fqdn,
                "nsxtLicense": nsxt_licensekey,
                "transportVlanId": nsxt_htep_vlanid,
                "ipAddressPoolSpec": {
                    "name": nsxt_np2_htep_name,
                    "description": nsxt_np2_htep_desc,
                    "subnets": [
                        {
                            "ipAddressPoolRanges": [
                                {
                                    "start": net_htep_ipstart,
                                    "end": net_htep_ipend
                                }
                            ],
                            "cidr": net_htep_cidr,
                            "gateway": net_htep_gateway
                        }
                    ]
                }
            },
        "vsanSpec": {
            "vsanName": vsan_spec_name,
            "licenseFile": vsan_licensekey,
            "vsanDedup": set_vsan_dedupe,
            "datastoreName": vsan_dsname
        },
        "dvSwitchVersion": vds1_version,
        "dvsSpecs": [
            {
                "dvsName": vds1_dvsname,
                "vcenterId": vds1_vcenterid,
                "vmnics": [
                    "vmnic0",
                    "vmnic1"
                ],
                "mtu": vds1_mtu,
                "networks": [
                    "MANAGEMENT",
                    "VMOTION",
                    "VSAN"
                ],
                "niocSpecs": [
                    {
                        "trafficType": "VSAN",
                        "value": "HIGH"
                    },
                    {
                        "trafficType": "VMOTION",
                        "value": "LOW"
                    },
                    {
                        "trafficType": "VDP",
                        "value": "LOW"
                    },
                    {
                        "trafficType": "VIRTUALMACHINE",
                        "value": "HIGH"
                    },
                    {
                        "trafficType": "MANAGEMENT",
                        "value": "NORMAL"
                    },
                    {
                        "trafficType": "NFS",
                        "value": "LOW"
                    },
                    {
                        "trafficType": "HBR",
                        "value": "LOW"
                    },
                    {
                        "trafficType": "FAULTTOLERANCE",
                        "value": "LOW"
                    },
                    {
                        "trafficType": "ISCSI",
                        "value": "LOW"
                    }
                ],
                "isUsedByNsxt": vds1_set_isnsxt
            }
        ],
        "clusterSpec":
            {
                "clusterName": vc_mgmt_clustername,
                "vcenterName": vc_spec_name,
                "clusterEvcMode": vc_evcmode,
                "vmFolders": {
                    "MANAGEMENT": vmfolder_mgmt,
                    "NETWORKING": vmfolder_net,
                    "EDGENODES": vmfolder_edge
                },
                "resourcePoolSpecs": [{
                    "name": rps_mgmt_name,
                    "type": "management",
                    "cpuReservationPercentage": 0,
                    "cpuLimit": -1,
                    "cpuReservationExpandable": True,
                    "cpuSharesLevel": "normal",
                    "cpuSharesValue": 0,
                    "memoryReservationMb": 0,
                    "memoryLimit": -1,
                    "memoryReservationExpandable": True,
                    "memorySharesLevel": "normal",
                    "memorySharesValue": 0
                }, {
                    "name": rps_mgmt_net,
                    "type": "network",
                    "cpuReservationPercentage": 0,
                    "cpuLimit": -1,
                    "cpuReservationExpandable": True,
                    "cpuSharesLevel": "normal",
                    "cpuSharesValue": 0,
                    "memoryReservationPercentage": 0,
                    "memoryLimit": -1,
                    "memoryReservationExpandable": True,
                    "memorySharesLevel": "normal",
                    "memorySharesValue": 0
                }, {
                    "name": rp_usr_edge,
                    "type": "compute",
                    "cpuReservationPercentage": 0,
                    "cpuLimit": -1,
                    "cpuReservationExpandable": True,
                    "cpuSharesLevel": "normal",
                    "cpuSharesValue": 0,
                    "memoryReservationPercentage": 0,
                    "memoryLimit": -1,
                    "memoryReservationExpandable": True,
                    "memorySharesLevel": "normal",
                    "memorySharesValue": 0
                }, {
                    "name": rp_usr_vm,
                    "type": "compute",
                    "cpuReservationPercentage": 0,
                    "cpuLimit": -1,
                    "cpuReservationExpandable": True,
                    "cpuSharesLevel": "normal",
                    "cpuSharesValue": 0,
                    "memoryReservationPercentage": 0,
                    "memoryLimit": -1,
                    "memoryReservationExpandable": True,
                    "memorySharesLevel": "normal",
                    "memorySharesValue": 0
                }]
            },
        "pscSpecs": [
            {
                "pscId": psc_spec_name,
                "vcenterId": vc_spec_name,
                "adminUserSsoPassword": simple_password,
                "pscSsoSpec": {
                    "ssoDomain": "vsphere.local"
                }
            }
        ],
        "vcenterSpec": {
            "vcenterIp": vc_mgmt_ip,
            "vcenterHostname": vc_mgmt_hostname_short,
            "vcenterId": vc_spec_name,
            "licenseFile": vc_licensekey,
            "vmSize": vc_vmsize,
            "storageSize": vc_storagesize,
            "rootVcenterPassword": simple_password
        },
        "hostSpecs": [
            {
                "association": vc_datacenter_name,
                "ipAddressPrivate": {
                    "ipAddress": host1_mgmt_ip
                },
                "hostname": host1_hostname_short,
                "credentials": {
                    "username": "root",
                    "password": simple_password
                },
                "vSwitch": esxi_vss_name,
                "serverId": host1_server_id
            },
            {
                "association": vc_datacenter_name,
                "ipAddressPrivate": {
                    "ipAddress": host2_mgmt_ip
                },
                "hostname": host2_hostname_short,
                "credentials": {
                    "username": "root",
                    "password": simple_password
                },
                "vSwitch": esxi_vss_name,
                "serverId": host2_server_id
            },
            {
                "association": vc_datacenter_name,
                "ipAddressPrivate": {
                    "ipAddress": host3_mgmt_ip
                },
                "hostname": host3_hostname_short,
                "credentials": {
                    "username": "root",
                    "password": simple_password
                },
                "vSwitch": esxi_vss_name,
                "serverId": host3_server_id
            },
            {
                "association": vc_datacenter_name,
                "ipAddressPrivate": {
                    "ipAddress": host4_mgmt_ip
                },
                "hostname": host4_hostname_short,
                "credentials": {
                    "username": "root",
                    "password": simple_password
                },
                "vSwitch": esxi_vss_name,
                "serverId": host4_server_id
            }
        ],
        "excludedComponents": ["AVN", "EBGP"]
    }
