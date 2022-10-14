import requests
from loguru import logger
from cloudbuilder_python.rest_data import get_uri, sddc_data

logger.level("REST", no=37, color="<magenta>")


class VCFRest:
    def __init__(self):
        self.cb_url = 'localhost:8080'
        self.headers = {'content-type': 'application/json'}
        self.uri = dict()
        self.generate_uri()

    def generate_uri(self):
        v1_rest = '{}/v1/sddcs'.format(self.cb_url)
        uri = get_uri()
        for u in uri:
            uri[u] = uri[u].format(v1_rest)
        self.uri = uri

    def post_sddc_validation(self, np1_mgmt, complex_password, sddcm_ip, sddcm_subnet, sddcm_host_short, sddcm_licensekey,
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

        sddc_validate = sddc_data(np1_mgmt, complex_password, sddcm_ip, sddcm_subnet, sddcm_host_short, sddcm_licensekey,
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
                       host4_server_id)

        create_response = requests.post(self.uri['sddc_validate'], json=sddc_validate, headers=self.headers)
        if create_response.status_code != 200:
            logger.log('REST', 'SDDC validation failed')
            return None

    def get_validate_sddc(self, validation_id):
        validate_sddc = requests.get(f"{self.uri['sddc_validate']}{validation_id}", headers=self.headers)
        if validate_sddc.status_code != 200:
            logger.log('REST', 'Failed to get sddc validation')
        return validate_sddc.content, None

    def deploy_sddc(self, np1_mgmt, complex_password, sddcm_ip, sddcm_subnet, sddcm_host_short, sddcm_licensekey,
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

        sddc_validate = sddc_data(np1_mgmt, complex_password, sddcm_ip, sddcm_subnet, sddcm_host_short,
                                           sddcm_licensekey,
                                           simple_password, mgmt_vc_id, sddcm_sddcid, esxi_license, set_ceip, set_fips,
                                           ntps_primary,
                                           ntps_secondary, dns_secondaryns, dns_subdomain, dns_domainname,
                                           dns_primaryns, net_mgmt_subnet,
                                           net_mgmt_gateway, net_mgmt_vlan, net_mgmt_mtu, net_mgmt_pg_name,
                                           net_vmotion_subnet,
                                           net_vmotion_gateway, net_vmotion_vlanid, net_vmotion_mtu,
                                           net_vmotion_pg_name,
                                           vc_datacenter_name,
                                           net_vmotion_ipend, net_vmotion_ipstart, net_vsan_subnet, net_vsan_gateway,
                                           net_vsan_vlanid,
                                           net_vsan_mtu, psc_spec_name, net_vsan_pg_name, net_vsan_ipend,
                                           net_vsan_ipstart, nsxt_m_size,
                                           nsxt_m1_hostname_short, nsxt_m1_ip, nsxt_m2_hostname_short, nsxt_m2_ip,
                                           nsxt_m3_hostname_short,
                                           nsxt_m3_ip, nsxt_tz_overlayname, nsxt_tz_overlaynetworkname,
                                           nsxt_tz_vlanname,
                                           nsxt_tz_vlannetworkname, nsxt_vip_name, nsxt_vip_fqdn, nsxt_licensekey,
                                           nsxt_htep_vlanid,
                                           nsxt_np2_htep_name, nsxt_np2_htep_desc, net_htep_ipstart, net_htep_ipend,
                                           net_htep_cidr,
                                           net_htep_gateway, vsan_spec_name, vsan_licensekey, set_vsan_dedupe,
                                           vsan_dsname, vds1_version,
                                           vds1_dvsname, vds1_vcenterid, vds1_mtu, vds1_set_isnsxt, vc_mgmt_clustername,
                                           vc_spec_name,
                                           vc_evcmode,
                                           vmfolder_mgmt, vmfolder_net, vmfolder_edge, rps_mgmt_name, rps_mgmt_net,
                                           rp_usr_edge, rp_usr_vm,
                                           vc_mgmt_ip, vc_mgmt_hostname_short, vc_licensekey, vc_vmsize, vc_storagesize,
                                           host1_mgmt_ip,
                                           host1_hostname_short, esxi_vss_name, host1_server_id, host2_mgmt_ip,
                                           host2_hostname_short,
                                           host2_server_id,
                                           host3_mgmt_ip, host3_hostname_short, host3_server_id, host4_mgmt_ip,
                                           host4_hostname_short,
                                           host4_server_id)

        create_response = requests.post(self.uri['deploy'], json=sddc_validate, headers=self.headers)
        if create_response.status_code != 200:
            logger.log('REST', 'SDDC deploy failed')
            return None
