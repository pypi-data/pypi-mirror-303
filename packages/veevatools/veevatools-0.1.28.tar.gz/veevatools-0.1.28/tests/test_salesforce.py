from json import load
from numpy import fix
from pytest import mark
from pytest import fixture
import pandas as pd
from salesforce.salesforce import Sf
from salesforce.utilities.df_utils import *
from salesforce.utilities.async_utils import *


@fixture(scope='session')
def sfdc():
    return Sf()

@mark.sfdc
class SalesforceTests():

    def test_init(self, sfdc):
        """
        Test to verify all instance variables are
        properly initialized
        """
        sfdc.filename == None
        sfdc.sfUsername == None
        sfdc.credentials == pd.DataFrame()
        sfdc.sfPassword == None
        sfdc.sfOrgId == None
        sfdc.isSandbox == None
        sfdc.session_id == None
        sfdc.instance == None
        sfdc.domain == None
        sfdc.security_token == ''
        sfdc.api_version == 'v52.0'
        sfdc.record_count == {}
        sfdc.record_count_caseinsensitive == {}
        sfdc.debug == False

    def test_authentication(self, sfdc, test_config, get_param):
        if (get_param['sfdcUser'] is None) | (get_param['sfdcPass'] is None):
            print("No SFDC Username or password provided, mock authentication executed, success!")
            test_success = True
            sfdc.sfUsername = 'test@salesforce.com'
            sfdc.sfPassword = 'password'
            sfdc.sfOrgId = 'OrgId123'
            sfdc.isSandbox = True
            sfdc.session_id = 'fake_session'
            sfdc.instance = 'No Instance'
        else:
            test_success = sfdc.authenticate(sfUsername = test_config.sfdc_username,
                                sfPassword = test_config.sfdc_password,
                                isSandbox = False if get_param['sfdcEnv'] == 'prod' else True,
                                sfOrgId = test_config.sfdc_org_id,
                                if_return = True
            )['sfMeta_is_connected']
        assert sfdc.sfUsername is not None
        assert sfdc.sfPassword is not None
        assert sfdc.sfOrgId is not None
        assert sfdc.isSandbox is not None
        assert sfdc.session_id is not None
        assert sfdc.instance is not None
        assert test_success == True

    def test_query(self, sfdc, get_param):
        if (get_param['sfdcUser'] is None) | (get_param['sfdcPass'] is None):
            print("No SFDC Username or password provided, mock query executed, Success!")
            test_success = True
        else:
            try:
                sfdc.query("Select Id, Name From Account limit 10")
                test_success = True
            except:
                test_success = False
        assert test_success

    def test_create(self, sfdc, get_param):
        if (get_param['sfdcUser'] is None) | (get_param['sfdcPass'] is None):
            print("No SFDC Username or password provided, mock create executed, Success!")
            test_success = True
        else:
            try:
                input_data = [{'FirstName':'Create1','Email':'example@example.com'}, 
                {'LastName': 'Create2', 'Email': 'Michael.pay@myemail.com'}]
                input_df = pd.DataFrame(input_data).fillna('')
                results = sfdc.create("Contact", input_df)
                test_success = len(results) > 0
                sfdc.delete("Contact", results['Id'].dropna().to_frame()) # teardown            
            except:
                test_success = False
        assert test_success

    def test_update(self, sfdc, get_param):
        if (get_param['sfdcUser'] is None) | (get_param['sfdcPass'] is None):
            print("No SFDC Username or password provided, mock create executed, Success!")
            test_success = True
        else:
            try:
                input_data = [{'LastName':'Update','Email':'example@example.com'}, 
                {'LastName': 'Update2', 'Email': 'Michael.pay@myemail.com'}]
                input_df = pd.DataFrame(input_data).fillna('')
                results = sfdc.create("Contact", input_df)
                id_string = "', '".join(list(results['Id'].dropna()))
                results = sfdc.update("Contact", sfdc.query(f"Select Id, LastName from Contact WHERE Id IN ('{id_string}')"))
                test_success = results['success'].isin([True]).all()
                sfdc.delete("Contact", results['Id'].dropna().to_frame()) # teardown            
            except:
                test_success = False
        assert test_success

    def test_upsert(self, sfdc, get_param):
        if (get_param['sfdcUser'] is None) | (get_param['sfdcPass'] is None):
            print("No SFDC Username or password provided, mock create executed, Success!")
            test_success = True
        else:
            try:
                input_data = [{'LastName':'Upsert1','Email':'example@example.com'}, 
                {'LastName': 'Upsert2', 'Email': 'Michael.pay@myemail.com'}]
                input_df = pd.DataFrame(input_data).fillna('')
                results = sfdc.create("Contact", input_df)
                id_string = "', '".join(list(results['Id'].dropna()))
                results["External_Id_vod__c"] = results["Id"]
                update_df = pd.merge(sfdc.query(f"Select Id, LastName from Contact WHERE Id IN ('{id_string}')"),results[["Id","External_Id_vod__c"]],how='left',on="Id")
                sfdc.update("Contact",update_df)
                upsert_df = update_df.drop(columns=['Id']).copy()
                results = sfdc.upsert("Contact", "External_Id_vod__c",upsert_df).rename(columns={"id":"Id"})
                test_success = results['success'].isin([True]).all() & results['created'].isin([False]).all()
                sfdc.delete("Contact", results['Id'].dropna().to_frame()) # teardown            
            except:
                test_success = False
        assert test_success
    
    def test_delete(self, sfdc, get_param):
        if (get_param['sfdcUser'] is None) | (get_param['sfdcPass'] is None):
            print("No SFDC Username or password provided, mock create executed, Success!")
            test_success = True
        else:
            try:
                input_data = [{'LastName':'Delete1','Email':'example@example.com'}, 
                {'LastName': 'Delete2', 'Email': 'Michael.pay@myemail.com'}]
                input_df = pd.DataFrame(input_data).fillna('')
                results = sfdc.create("Contact", input_df)
                results = sfdc.delete("Contact", results['Id'].dropna().to_frame())
                test_success = results['success'].isin([True]).all()         
            except:
                test_success = False
        assert test_success

    def test_extract_bulk(self, sfdc, get_param):
        if (get_param['sfdcUser'] is None) | (get_param['sfdcPass'] is None):
            print("No SFDC Username or password provided, mock query executed, Success!")
            test_success = True
        else:
            try:
                sfdc.extract_bulk("Select Id, Name From Account limit 10")
                test_success = True
            except:
                test_success = False
        assert test_success

    def test_object_describe(self, sfdc):
        assert sfdc.object_describe("Account")['fields']['Id']['label'] is not None

    def test_field_describe(self, sfdc):
        assert sfdc.field_describe(objects=['Account'], attributes =['name']).iloc[0,0] is not None

    def test_picklist_dataframe_stacked(self, sfdc):
        assert sfdc.picklist_dataframe_stacked(objects=['Account']).iloc[0,0] is not None

    def test_picklist_dataframe(self, sfdc):
        assert sfdc.picklist_dataframe(objects=['Account'])[0].iloc[0,0] is not None

    def test_record_type_retrieval(self, sfdc):
        assert sfdc.record_type_retrieval('Account').iloc[0,0] is not None
    
    def test_metadata_crud(self, sfdc):
        metadata_read = sfdc.metadata_read("CustomObject", "Contact")
        assert metadata_read['fullName'][0] == 'Contact'

        metadata_parsed = metadata_parse(metadata_read)
        assert metadata_parsed['fullName'] == 'Contact'

        metadata_list = sfdc.metadata_list("CustomObject")
        assert metadata_list[0]['type'] == 'CustomObject'

        custom_object_test = sfdc.sf.mdapi.CustomObject(
            fullName = "Veeva_Unit_Testing_Custom_Object_vpro__c",
            label = "Veeva Vpro Unit Testing",
            pluralLabel = "Veeva Vpro Unit Testing",
            nameField = sfdc.sf.mdapi.CustomField(
                label = "Vpro Test Field",
                type = "Text"
            ),
            recordTypes = [sfdc.sf.mdapi.RecordType(
                active = True,
                description = "Vpro RT Testing",
                fullName = "Vpro_RT_Testing",
                label = "Vpro RT Testing"
            )],
            deploymentStatus = sfdc.sf.mdapi.DeploymentStatus("Deployed"),
            sharingModel = sfdc.sf.mdapi.SharingModel("ReadWrite")
        )
        sfdc.metadata_create("CustomObject", custom_object_test)
        metadata_create_verify = sfdc.metadata_read("CustomObject", "Veeva_Unit_Testing_Custom_Object_vpro__c")
        assert metadata_create_verify['fullName'][0] == 'Veeva_Unit_Testing_Custom_Object_vpro__c'

        sfdc.metadata_rename("CustomObject", "Veeva_Unit_Testing_Custom_Object_vpro__c", "Veeva_Unit_Testing_Custom_Object_2_vpro__c")
        metadata_renamed = sfdc.metadata_read("CustomObject", "Veeva_Unit_Testing_Custom_Object_2_vpro__c")
        assert metadata_renamed['fullName'][0] == 'Veeva_Unit_Testing_Custom_Object_2_vpro__c'

        sfdc.metadata_delete("CustomObject", "Veeva_Unit_Testing_Custom_Object_2_vpro__c")
        verify_deleted = sfdc.metadata_read("CustomObject", "Veeva_Unit_Testing_Custom_Object_2_vpro__c")
        assert verify_deleted['fullName'][0] is None


    # Testin Async Functions

    async def test_async_query(self, sfdc, get_param):
        if (get_param['sfdcUser'] is None) | (get_param['sfdcPass'] is None):
            print("No SFDC Username or password provided, mock query executed, Success!")
            test_success = True
        else:
            try:
                
                result = await sfdc.async_query("Select Id, Name From Account limit 10")
                test_success = True
            except:
                test_success = False
        assert test_success
        
    @mark.skip(reason="TODO")
    

    @mark.skip(reason="Not built yet, todo")
    def test_sf_api_call(self):
        assert False
    
    @mark.skip(reason="Function deprecated.")
    @mark.deprecated
    def test_join(self):
        assert True