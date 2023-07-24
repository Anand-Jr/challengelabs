from result_output import *
import sys
import json
import importlib.util
import urllib.request
from googleapiclient import discovery
from google.oauth2 import service_account
from pprint import pprint
from google.cloud import compute_v1


class Activity():

    def testcase_check_first_vpc(self,test_object,credentials,project_id):
        testcase_description="Check first VPC name"
        expected_result='my-vpc-1' 
        
        try:
            is_present = False
            actual = 'VPC name is not '+ expected_result
            compute_client = compute_v1.NetworksClient(credentials=credentials)
            logging.info(f"{testcase_description} started")
            try:
                vpcs = compute_client.list(project=project_id)
                for vpc in vpcs:
                    if vpc.name == expected_result:
                        is_present=True
                        actual=expected_result
                        break
                    else:
                        logging.info("")
                        actual= vpc.name      

            except Exception as e:
                logging.info("exception:",str(e))
                is_present = False

            test_object.update_pre_result(testcase_description,expected_result)
            if is_present==True:
                test_object.update_result(1,expected_result,actual,"Congrats! You have done it right!"," ") 
            else:
                return test_object.update_result(0,expected_result,actual,"Check VPC name","https://cloud.google.com/vpc/docs/create-modify-vpc-networks")   

        except Exception as e:    
            test_object.update_result(-1,expected_result,"Internal Server error","Please check with Admin","")
            test_object.eval_message["testcase_check_first_vpc"]=str(e)                



    def testcase_check_second_vpc(self,test_object,credentials,project_id):
        testcase_description="Check second VPC name"
        expected_result='my-vpc-2' 
        
        try:
            is_present = False
            actual = 'VPC name is not '+ expected_result
            compute_client = compute_v1.NetworksClient(credentials=credentials)
            try:
                vpcs = compute_client.list(project=project_id)
                for vpc in vpcs:
                    if vpc.name == expected_result:
                        is_present=True
                        actual=expected_result
                        break
                    else:
                        actual= vpc.name      

            except Exception as e:
                is_present = False

            test_object.update_pre_result(testcase_description,expected_result)
            if is_present==True:
                test_object.update_result(1,expected_result,actual,"Congrats! You have done it right!"," ") 
            else:
                test_object.update_result(0,expected_result,actual,"Check VPC name","https://cloud.google.com/vpc/docs/create-modify-vpc-networks")   

        except Exception as e:    
            test_object.update_result(-1,expected_result,"Internal Server error","Please check with Admin","")
            test_object.eval_message["testcase_check_second_vpc"]=str(e)  



    def testcase_check_first_subnet_name_and_region(self,test_object,credentials,project_id):
        testcase_description="Check first subnet name and region"
        expected_result='us-central1/subnetworks/subnet-1' 
        
        try:
            is_present = False
            actual = 'Subnet is not present in '+ expected_result
            compute_client = compute_v1.NetworksClient(credentials=credentials)
            try:
                vpcs = compute_client.list(project=project_id)
                for vpc in vpcs:
                    for subnets in vpc.subnetworks:
                        if subnets.endswith(expected_result):
                            is_present=True
                            actual=expected_result
                            break
                        else:
                            # actual= subnets 
                            pass   

            except Exception as e:
                is_present = False

            test_object.update_pre_result(testcase_description,expected_result)
            if is_present==True:
                test_object.update_result(1,expected_result,actual,"Congrats! You have done it right!"," ") 
            else:
                test_object.update_result(0,expected_result,actual,"Check Subnet name and region","https://cloud.google.com/vpc/docs/create-modify-vpc-networks")   

        except Exception as e:    
            test_object.update_result(-1,expected_result,"Internal Server error","Please check with Admin","")
            test_object.eval_message["testcase_check_first_subnet_name_and_region"]=str(e)


    def testcase_check_second_subnet_name_and_region(self,test_object,credentials,project_id):
        testcase_description="Check second subnet name and region"
        expected_result='europe-north1/subnetworks/subnet-2' 
        
        try:
            is_present = False
            actual = 'Subnet is not present in'+ expected_result
            compute_client = compute_v1.NetworksClient(credentials=credentials)
            try:
                vpcs = compute_client.list(project=project_id)
                for vpc in vpcs:
                    for subnets in vpc.subnetworks:
                        if subnets.endswith(expected_result):
                            is_present=True
                            actual=expected_result
                            break
                        else:
                            # actual= subnets 
                            pass   

            except Exception as e:
                is_present = False

            test_object.update_pre_result(testcase_description,expected_result)
            if is_present==True:
                test_object.update_result(1,expected_result,actual,"Congrats! You have done it right!"," ") 
            else:
                test_object.update_result(0,expected_result,actual,"Check Subnet name and region","https://cloud.google.com/vpc/docs/create-modify-vpc-networks")   

        except Exception as e:    
            test_object.update_result(-1,expected_result,"Internal Server error","Please check with Admin","")
            test_object.eval_message["testcase_check_second_subnet_name_and_region"]=str(e)



    def testcase_check_first_peering_connection_name(self,test_object,credentials,project_id):
        testcase_description="Check first peering connection name"
        expected_result='my-vpc1-to-my-vpc2' 
        network1="my-vpc-1"

        try:
            is_present = False
            actual = 'Peering connection name is not'+ expected_result
            compute_client = compute_v1.NetworksClient(credentials=credentials)
            
            try:
                
                network1_response = compute_client.get(project=project_id, network=network1)
                network1_peering = network1_response.peerings

                for peer_data in network1_peering:
                    if peer_data.name == expected_result:
                        is_present= True
                        actual=expected_result
                        break
                    else:
                        actual = peer_data.name
                        pass

            except Exception as e:
                is_present = False

            test_object.update_pre_result(testcase_description,expected_result)
            if is_present==True:
                test_object.update_result(1,expected_result,actual,"Congrats! You have done it right!"," ") 
            else:
                test_object.update_result(0,expected_result,actual,"Check VPC peeering connection name","https://cloud.google.com/vpc/docs/using-vpc-peering")   

        except Exception as e:    
            test_object.update_result(-1,expected_result,"Internal Server error","Please check with Admin","")
            test_object.eval_message["testcase_check_first_peering_connection_name"]=str(e)



    def testcase_check_second_peering_connection_name(self,test_object,credentials,project_id):
        testcase_description="Check second peering connection name"
        expected_result='my-vpc2-to-my-vpc1' 
        network1="my-vpc-2"
        try:
            is_present = False
            actual = 'Peering connection name is not'+ expected_result
            compute_client = compute_v1.NetworksClient(credentials=credentials)
            
            try:
                
                network1_response = compute_client.get(project=project_id, network=network1)
                network1_peering = network1_response.peerings

                for peer_data in network1_peering:
                    if peer_data.name == expected_result:
                        is_present= True
                        actual=expected_result
                        break
                    else:
                        actual = peer_data.name
                        pass

            except Exception as e:
                is_present = False

            test_object.update_pre_result(testcase_description,expected_result)
            if is_present==True:
                test_object.update_result(1,expected_result,actual,"Congrats! You have done it right!"," ") 
            else:
                test_object.update_result(0,expected_result,actual,"Check VPC peeering connection name","https://cloud.google.com/vpc/docs/using-vpc-peering")   

        except Exception as e:    
            test_object.update_result(-1,expected_result,"Internal Server error","Please check with Admin","")
            test_object.eval_message["testcase_check_second_peering_connection_name"]=str(e)


    def testcase_check_vpc_connection_established(self,test_object,credentials,project_id):
        testcase_description="Check VPC connection established"
        network1="my-vpc-1"
        network2="my-vpc-2"
        expected_result="ACTIVE"
        
        try:
            is_present = False
            actual = 'There is no connection between '+ network1 + 'and' + expected_result
            compute_client = compute_v1.NetworksClient(credentials=credentials)
            
            try:
               
                network1_response = compute_client.get(project=project_id, network=network1)
                network1_peering = network1_response.peerings
                network2_response = compute_client.get(project=project_id, network=network2)
                network2_peering = network2_response.peerings

                for peering in network1_peering:
                    if peering.state == expected_result and peering.network.endswith(network2):
                        is_present = True
                        actual=expected_result
                        break
                    else:
                        actual = peering.state
                        pass
                
            except Exception as e:
                is_present = False

            test_object.update_pre_result(testcase_description,expected_result)
            if is_present==True:
                test_object.update_result(1,expected_result,actual,"Congrats! You have done it right!"," ") 
            else:
                test_object.update_result(0,expected_result,actual,"Check VPC connection state","https://cloud.google.com/vpc/docs/using-vpc-peering")   

        except Exception as e:    
            test_object.update_result(-1,expected_result,"Internal Server error","Please check with Admin","")
            test_object.eval_message["testcase_check_second_peering_connection_name"]=str(e)



    def testcase_check_first_firewall(self,test_object,credentials,project_id):
        testcase_description="Check first firewall name"
        expected_result="firewall-1"
        
        try:
            is_present = False
            actual = 'Firewall name is not' + expected_result
            client = compute_v1.FirewallsClient(credentials=credentials)
            
            try:
               
                firewall_rules = client.list(project=project_id)
                for firewall_rule in firewall_rules:
                    if firewall_rule.name == expected_result:
                        is_present= True
                        actual=expected_result
                        break
                    else:
                        actual = firewall_rule.name
                        pass
        
                
            except Exception as e:
                is_present = False

            test_object.update_pre_result(testcase_description,expected_result)
            if is_present==True:
                test_object.update_result(1,expected_result,actual,"Congrats! You have done it right!"," ") 
            else:
                test_object.update_result(0,expected_result,actual,"Check Firewall name","https://cloud.google.com/firewall/docs/using-firewalls")   

        except Exception as e:    
            test_object.update_result(-1,expected_result,"Internal Server error","Please check with Admin","")
            test_object.eval_message["testcase_check_first_firewall"]=str(e)

    def testcase_check_second_firewall(self,test_object,credentials,project_id):
        testcase_description="Check second firewall name"
        expected_result="firewall-2"
        
        try:
            is_present = False
            actual = 'Firewall name is not' + expected_result
            client = compute_v1.FirewallsClient(credentials=credentials)
            
            try:
               
                firewall_rules = client.list(project=project_id)
                for firewall_rule in firewall_rules:
                    if firewall_rule.name == expected_result:
                        is_present= True
                        actual=expected_result
                        break
                    else:
                        actual = firewall_rule.name
                        pass
        
                
            except Exception as e:
                is_present = False

            test_object.update_pre_result(testcase_description,expected_result)
            if is_present==True:
                test_object.update_result(1,expected_result,actual,"Congrats! You have done it right!"," ") 
            else:
                test_object.update_result(0,expected_result,actual,"Check Firewall name","https://cloud.google.com/firewall/docs/using-firewalls")   

        except Exception as e:    
            test_object.update_result(-1,expected_result,"Internal Server error","Please check with Admin","")
            test_object.eval_message["testcase_check_second_firewall"]=str(e)

    def testcase_check_ports_first_firewall(self,test_object,credentials,project_id):
        testcase_description="Check ports allowed by firewall-1"
        expected_result="tcp and icmp"
        
        try:
            is_present = False
            actual = 'Firewall rule does not allow the protocols' + expected_result
            client = compute_v1.FirewallsClient(credentials=credentials)
            
            try:
               
                firewall_rules = client.list(project=project_id)
                for firewall_rule in firewall_rules:
                    if firewall_rule.name == "firewall-1":
                        for rules in firewall_rule.allowed:
                            protocols = rules.I_p_protocol
                            if "tcp" and "icmp" in protocols:
                                is_present= True
                                actual=expected_result
                                break
                            else:
                                actual = protocols
                                pass
                        
                
            except Exception as e:
                is_present = False

            test_object.update_pre_result(testcase_description,expected_result)
            if is_present==True:
                test_object.update_result(1,expected_result,actual,"Congrats! You have done it right!"," ") 
            else:
                test_object.update_result(0,expected_result,actual,"Check Protocols and ports of firewall","https://cloud.google.com/firewall/docs/using-firewalls")   

        except Exception as e:    
            test_object.update_result(-1,expected_result,"Internal Server error","Please check with Admin","")
            test_object.eval_message["testcase_check_ports_first_firewall"]=str(e)


    def testcase_check_ports_second_firewall(self,test_object,credentials,project_id):
        testcase_description="Check ports allowed by firewall-2"
        expected_result="tcp and icmp"
        
        try:
            is_present = False
            actual = 'Firewall rule does not allow the protocols' + expected_result
            client = compute_v1.FirewallsClient(credentials=credentials)
            
            try:
               
                firewall_rules = client.list(project=project_id)
                for firewall_rule in firewall_rules:
                    if firewall_rule.name == "firewall-2":
                        for rules in firewall_rule.allowed:
                            protocols = rules.I_p_protocol
                            if "tcp" and "icmp" in protocols:
                                is_present= True
                                actual=expected_result
                                break
                            else:
                                actual = protocols
                                pass
                        
                
            except Exception as e:
                is_present = False

            test_object.update_pre_result(testcase_description,expected_result)
            if is_present==True:
                test_object.update_result(1,expected_result,actual,"Congrats! You have done it right!"," ") 
            else:
                test_object.update_result(0,expected_result,actual,"Check Protocols and ports of firewall","https://cloud.google.com/firewall/docs/using-firewalls")   

        except Exception as e:    
            test_object.update_result(-1,expected_result,"Internal Server error","Please check with Admin","")
            test_object.eval_message["testcase_check_ports_first_firewall"]=str(e)



def start_tests(credentials, project_id, args):
    
    if "result_output" not in sys.modules:
        importlib.import_module("result_output")
    else:
        importlib.reload(sys.modules[ "result_output"])

    test_object=ResultOutput(args,Activity)
    challenge_test=Activity()
    challenge_test.testcase_check_first_vpc(test_object,credentials,project_id)
    challenge_test.testcase_check_second_vpc(test_object,credentials,project_id)
    challenge_test.testcase_check_first_subnet_name_and_region(test_object,credentials,project_id)
    challenge_test.testcase_check_second_subnet_name_and_region(test_object,credentials,project_id)
    challenge_test.testcase_check_first_peering_connection_name(test_object,credentials,project_id)
    challenge_test.testcase_check_second_peering_connection_name(test_object,credentials,project_id)
    challenge_test.testcase_check_vpc_connection_established(test_object,credentials,project_id)
    challenge_test.testcase_check_first_firewall(test_object,credentials,project_id)
    challenge_test.testcase_check_second_firewall(test_object,credentials,project_id)
    challenge_test.testcase_check_ports_first_firewall(test_object,credentials,project_id)
    challenge_test.testcase_check_ports_second_firewall(test_object,credentials,project_id)
    json.dumps(test_object.result_final(),indent=4)
    return test_object.result_final()


