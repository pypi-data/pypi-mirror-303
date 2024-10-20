import posixpath
import re

from .base import SynchronousMicrosoftApiClient


class Skus:
    entra_id_p2 = 'AAD_PREMIUM_P2'
    exchange_plan_1 = 'EXCHANGESTANDARD'
    exchange_plan_2 = 'EXCHANGEENTERPRISE'
    m365_apps = 'O365_BUSINESS'
    m365_apps_enterprise = 'OFFICESUBSCRIPTION'
    m365_business_standard = 'O365_BUSINESS_PREMIUM'
    m365_e3 = 'SPE_E3'
    m365_e5 = 'SPE_E5'
    m365_f1 = 'M365_F1'
    o365_e1 = 'STANDARDPACK'
    o365_e2 = 'STANDARDWOFFPACK'
    o365_storage = 'SHAREPOINTSTORAGE'
    o365_e3 = 'ENTERPRISEPACK'
    o365_e5 = 'ENTERPRISEPREMIUM'
    values_map = {
        'AAD_PREMIUM_P2': 'entra_id_p2',
        'EXCHANGESTANDARD': 'exchange_plan_1',
        'EXCHANGEENTERPRISE': 'exchange_plan_2',
        'O365_BUSINESS': 'm365_apps',
        'OFFICESUBSCRIPTION': 'm365_apps_enterprise',
        'O365_BUSINESS_PREMIUM': 'm365_business_standard',
        'SPE_E3': 'm365_e3',
        'SPE_E5': 'm365_e5',
        'M365_F1': 'm365_f1',
        'STANDARDPACK': 'o365_e1',
        'STANDARDWOFFPACK': 'o365_e2',
        'SHAREPOINTSTORAGE': 'o365_storage',
        'ENTERPRISEPACK': 'o365_e3',
        'ENTERPRISEPREMIUM': 'o365_e5',
    }


class SynchronousGraphClient(SynchronousMicrosoftApiClient):
    def __init__(
            self,
            tenant_id,
            client_id=None,
            client_secret=None,
            creds=None,
            scope='https://graph.microsoft.com/.default'):
        super().__init__(
            tenant_id,
            client_id,
            client_secret,
            creds,
            scope=scope,
            base_url='https://graph.microsoft.com/v1.0')
        self.beta_url = 'https://graph.microsoft.com/beta'

    def get(self, url, params=None, headers=None, token_retry=False, **kwargs):
        """
        Send a GET request to the specified URL.

        Available OData query parameters for Microsoft Graph API:

        - $filter: Filters the results based on a condition (e.g., "startswith(displayName, 'A')")
        - $select: Narrows the properties returned (e.g., "id,displayName")
        - $orderby: Orders the results based on properties (e.g., "displayName asc")
        - $skip: Skips a specified number of results
        - $top: Limits the number of results returned (up to 999)
        - $search: Performs a full-text search (e.g., "$search="displayName: 'John'")
        - $count: Returns the count of results (true or false)
        - $expand: Expands related entities inline

        Note: Not all parameters are available for all endpoints. Always
        consult Microsoft Graph API documentation for endpoint-specific details.

        :param url: URL for the GET request
        :param headers: Optional headers dictionary
        :param params: Optional dictionary of query parameters
        :param token_retry: Internal flag to ensure we don't enter an infinite
                            loop if there's a token issue
        :return: JSON response from the server
        """
        headers = self.adjust_headers_for_odata(params, headers)
        return super().get(
            url, params, headers=headers,
            token_retry=token_retry, **kwargs)

    def post_headers(self):
        return {
            'accept': 'application/json',
        }

    def post(self, url, params=None, headers=None, token_retry=False,
             json_data=None, **kwargs):
        post_headers = self.post_headers()
        if headers:  # pragma: no cover
            post_headers.update(headers)
        return super().post(
            url, params=params, json=json_data, headers=headers,
            token_retry=token_retry, **kwargs)

    def patch(self, url, params=None, headers=None, token_retry=False,
              json_data=None, **kwargs):
        post_headers = self.post_headers()
        if headers:  # pragma: no cover
            post_headers.update(headers)
        return super().patch(
            url, params=params, json=json_data, headers=headers,
            token_retry=token_retry, **kwargs)

    def whoami(self, raw=False, **kwargs):
        url = f'{self.base_url}/me'
        result = self.get(url, raw=raw, **kwargs)
        return result

    def get_users(self, select=None, params=None):
        """
        fetch a list of users from the microsoft graph api.

        available odata query parameters for the /users endpoint:

        - $filter: filters the results based on a condition (e.g., "accountEnabled eq true")
        - $select: narrows the properties returned (e.g., "id,displayName,mail")
        - $orderby: orders the results based on properties (e.g., "displayName asc")
        - $skip: skips a specified number of results
        - $top: limits the number of results returned (up to 999)
        - $count: returns the count of results (true or false)
        - $expand: expands related entities inline (e.g., "manager,memberOf")
        - $search: performs a full-text search on specific properties
                   (requires 'ConsistencyLevel' header to be set to 'eventual')

        for detailed information and additional query options, consult the
        official microsoft graph api documentation for the /users endpoint:
        https://docs.microsoft.com/en-us/graph/api/user-list?view=graph-rest-1.0

        :param params: optional dictionary of query parameters
        :param select: list of user properties to include
        :return: list of users
        """
        select = select or [
            'id',
            'userPrincipalName',
            'displayName',
            'mail',
            'accountEnabled',
            'assignedLicenses',
            'identities',
            'lastPasswordChangeDateTime',
            'onPremisesDistinguishedName',
            'onPremisesDomainName',
            'onPremisesImmutableId',
            'onPremisesLastSyncDateTime',
            'onPremisesSamAccountName',
            'onPremisesSyncEnabled',
            'otherMails',
            'proxyAddresses',
            'userType',
        ]
        params = params or {}
        params['$select'] = ','.join(select)
        endpoint = f'{self.base_url}/users'
        return list(self.yield_result(endpoint, params))

    @classmethod
    def escape_upn(cls, upn):
        return upn.replace('#', '%23')

    def get_user(self, n_id=None, select=None):
        """
        returns the specified user, select should be a list of strings
        that include 1+ properties from https://docs.microsoft.com/en-us/graph/api/user-list?view=graph-rest-1.0
        """
        n_id = self.escape_upn(n_id)
        endpoint = f"{self.base_url}/users('{n_id}')"
        select = select or [
            'id',
            'userPrincipalName',
            'displayName',
            'mail',
            'accountEnabled',
            'assignedLicenses',
            'identities',
            'lastPasswordChangeDateTime',
            'onPremisesDistinguishedName',
            'onPremisesDomainName',
            'onPremisesImmutableId',
            'onPremisesLastSyncDateTime',
            'onPremisesSamAccountName',
            'onPremisesSyncEnabled',
            'otherMails',
            'proxyAddresses',
            'userType',
        ]
        params = {
            '$select': ','.join(select),
        }
        result = self.get(endpoint, params=params)
        return result

    def subscribed_skus(self, **kwargs):
        url = f'{self.base_url}/subscribedSkus'
        return list(self.yield_result(url, **kwargs))

    def subscribed_skus_map(self, **kwargs):
        return {
            x['skuId']: x['skuPartNumber']
            for x in self.subscribed_skus(params={
                '$select': 'skuId,skuPartNumber',
            })
        }

    def reverse_skus_map(self, **kwargs):
        """
        for a reference to sku part numbers, please see
        https://learn.microsoft.com/en-us/entra/identity/users/licensing-service-plan-reference
        """
        params = {
            '$select': 'skuId,skuPartNumber',
        }
        rg = self.subscribed_skus(params=params)
        rg = list(rg)
        rg.sort(key=lambda lx: lx['skuPartNumber'].lower())
        return {
            x['skuPartNumber']: x['skuId']
            for x in rg
        }

    def resolve_skus(self, user, sku_map=None):
        if not sku_map:
            sku_map = self.subscribed_skus_map()
        licenses = user.get('assignedLicenses') or []
        for x in licenses:
            sku_id = x.get('skuId')
            sku = sku_map[sku_id]
            x['skuPartNumber'] = sku

    def change_licenses(self, user_id, add_skus=None, remove_skus=None,
                        reverse_sku_map=None):
        add_licenses = []
        remove_licenses = []
        add_skus = add_skus or []
        remove_skus = remove_skus or []
        guid_re = r'^[a-f0-9]{8}\-[a-f0-9]{4}\-[a-f0-9]{4}\-[a-f0-9]{4}\-[a-f0-9]{12}$'
        guid_matcher = re.compile(guid_re)
        for x in add_skus:
            if isinstance(x, dict):
                add_licenses.append(x)
            elif guid_matcher.match(x):
                add_licenses.append({
                    'disabledPlans': [],
                    'skuId': x,
                })
            else:
                reverse_sku_map = reverse_sku_map or self.reverse_skus_map()
                sku_id = reverse_sku_map[x]
                add_licenses.append({
                    'disabledPlans': [],
                    'skuId': sku_id,
                })
        for x in remove_skus:
            if guid_matcher.match(x):
                remove_licenses.append(x)
            else:
                reverse_sku_map = reverse_sku_map or self.reverse_skus_map()
                sku_id = reverse_sku_map[x]
                remove_licenses.append(sku_id)
        json_data = {}
        json_data['addLicenses'] = add_licenses
        json_data['removeLicenses'] = remove_licenses
        url = f"{self.base_url}/users('{user_id}')/assignLicense"
        return self.post(url, json_data=json_data)

    def get_groups(self, params=None, **kwargs):
        """
        https://learn.microsoft.com/en-us/graph/api/group-list?view=graph-rest-1.0&tabs=http
        """
        url = f'{self.base_url}/groups'
        return list(self.yield_result(url, params=params, **kwargs))

    def get_group_members(self, group_id, params=None, **kwargs):
        """
        https://learn.microsoft.com/en-us/graph/api/group-list-members?view=graph-rest-1.0&tabs=http
        """
        url = f'{self.base_url}/groups/{group_id}/members'
        select = [
            'id',
            'userPrincipalName',
            'displayName',
            'mail',
            'accountEnabled',
        ]
        params = params or {}
        params.setdefault('$select', ','.join(select))
        return list(self.yield_result(url, params=params, **kwargs))

    def get_group_app_assignments(self, group_id, params=None, **kwargs):
        """
        https://learn.microsoft.com/en-us/graph/api/group-list?view=graph-rest-1.0&tabs=http
        """
        url = f'{self.base_url}/groups/{group_id}/appRoleAssignments'
        return list(self.yield_result(url, params=params, **kwargs))

    def assign_group_to_app(
            self, group_id,
            service_principal_id=None, app_id=None, app_name=None,
            role_id=None, **kwargs):
        principal = None
        if not service_principal_id and (app_id or app_name):
            principal = self.get_service_principal(app_id=app_id, name=app_name)
            service_principal_id = principal['id']
        if not role_id:
            if not principal:
                principal = self.get_service_principal(service_principal_id)
            roles = principal['appRoles']
            for x in roles:
                name = x['displayName'] or ''
                name = name.lower()
                if name == 'user':
                    role_id = x['id']
                    break
            if not role_id and roles:  # pragma: no cover
                role_id = roles[0]['id']
        data = {
            'resourceId': service_principal_id,
            'principalId': group_id,
            'appRoleId': role_id,
        }
        url = f'{self.base_url}/groups/{group_id}/appRoleAssignments'
        return self.post(url, json_data=data)

    def delete_group_from_app(
            self, group_id, assignment_id=None,
            service_principal_id=None, app_id=None, app_name=None,
            **kwargs):
        if not assignment_id:
            assignments = self.get_group_app_assignments(group_id)
            if not service_principal_id and (app_id or app_name):
                p = self.get_service_principal(app_id=app_id, name=app_name)
                service_principal_id = p['id']
            for x in assignments:
                if x['resourceId'] == service_principal_id:
                    assignment_id = x['id']
                    break
        if not assignment_id:  # pragma: no cover
            return True
        url = '/'.join([
            self.base_url,
            'groups', group_id,
            'appRoleAssignments', assignment_id])
        return self.delete(url, raw=True, **kwargs)

    def search_groups(self, display_name=None, params=None, **kwargs):
        """
        https://learn.microsoft.com/en-us/graph/api/group-list?view=graph-rest-1.0&tabs=http#example-4-use-filter-and-top-to-get-one-group-with-a-display-name-that-starts-with-a-including-a-count-of-returned-objects
        """
        params = params or {}
        if display_name:
            params.setdefault('$search', f'"displayName:{display_name}"')
        return self.get_groups(params=params)

    def create_group(
            self,
            display_name=None,
            mail_enabled=False,
            mail_nickname=None,
            security_enabled=True,
            description=None):
        """
        creates a new group using the microsoft graph api
        """
        data = {}
        if display_name:
            data['displayName'] = display_name
        data['mailEnabled'] = mail_enabled
        data['securityEnabled'] = security_enabled
        data['mailNickname'] = mail_nickname or display_name
        if description:  # pragma: no cover
            data['description'] = description
        url = f'{self.base_url}/groups'
        return self.post(url, json_data=data)

    def delete_group(
            self,
            group_id=None):
        """
        deletes group using the microsoft graph api
        """
        url = f'{self.base_url}/groups/{group_id}'
        return self.delete(url, raw=True)

    def add_group_member(
            self,
            group_id,
            user_id):
        """
        adds a user to a group
        """
        url = f'{self.base_url}/groups/{group_id}/members/$ref'
        data = {
            '@odata.id': f'https://graph.microsoft.com/v1.0/directoryObjects/{user_id}',
        }
        response = self.post(url, json_data=data, raw=True)
        return response.status_code == 204

    def remove_group_member(
            self,
            group_id,
            user_id):
        """
        removes a user from a group
        """
        url = f'{self.base_url}/groups/{group_id}/members/{user_id}/$ref'
        response = self.delete(url, raw=True)
        return response.status_code == 204

    def get_app(self, object_id=None, app_id=None):
        if object_id:
            url = f'{self.base_url}/applications/{object_id}'
        else:
            url = f"{self.base_url}/applications(appId='{app_id}')"
        return self.get(url)

    def get_apps(self, params=None, **kwargs):
        """
        https://learn.microsoft.com/en-us/graph/api/application-list?view=graph-rest-1.0&tabs=http
        """
        url = f'{self.base_url}/applications'
        return list(self.yield_result(url, params=params, **kwargs))

    def search_apps(self, display_name=None, params=None, **kwargs):
        """
        https://learn.microsoft.com/en-us/graph/api/application-list?view=graph-rest-1.0&tabs=http
        """
        params = params or {}
        if display_name:
            params.setdefault('$search', f'"displayName:{display_name}"')
        return self.get_apps(params=params)

    def get_service_principal(self, object_id=None, app_id=None, name=None,
                              params=None, **kwargs):
        """
        https://learn.microsoft.com/en-us/graph/api/serviceprincipal-get?view=graph-rest-1.0&tabs=http
        """
        if object_id:
            url = f'{self.base_url}/servicePrincipals/{object_id}'
            return self.get(url)
        if app_id:
            url = f"{self.base_url}/servicePrincipals(appId='{app_id}')"
            return self.get(url)
        principals = self.search_service_principals(name)
        if len(principals) == 1:
            return principals[0]
        for x in principals:  # pragma: no cover
            if x['displayName'].lower() == name.lower():
                return x
        return None  # pragma: no cover

    def get_service_principals(self, params=None, **kwargs):
        """
        https://learn.microsoft.com/en-us/graph/api/serviceprincipal-list?view=graph-rest-1.0&tabs=http
        """
        url = f'{self.base_url}/servicePrincipals'
        return list(self.yield_result(url, params=params, **kwargs))

    def search_service_principals(self, display_name, params=None):
        params = params or {}
        if display_name:
            params.setdefault('$search', f'"displayName:{display_name}"')
        return self.get_service_principals(params=params)

    def get_service_principal_id(self, app_id=None, app_name=None, **kwargs):
        principal = self.get_service_principal(app_id=app_id, name=app_name)
        return principal['id']

    def get_app_jobs(self, service_principal_id=None,
                     app_id=None, app_name=None, **kwargs):
        if not service_principal_id:
            service_principal_id = self.get_service_principal_id(
                app_id=app_id,
                app_name=app_name,
            )
        url = posixpath.join(
            self.base_url,
            'servicePrincipals', service_principal_id,
            'synchronization', 'jobs'
        )
        return list(self.yield_result(url, **kwargs))

    def get_app_job_schema(
            self, job_id, service_principal_id=None,
            app_id=None, app_name=None, **kwargs):
        if not service_principal_id:
            service_principal_id = self.get_service_principal_id(
                app_id=app_id,
                app_name=app_name,
            )
        url = posixpath.join(
            self.base_url,
            'servicePrincipals', service_principal_id,
            'synchronization', 'jobs', job_id,
            'schema',
        )
        return self.get(url)

    def provision_on_demand(self, subjects, app_name, rule_name=None, **kwargs):
        service_principal = self.get_service_principal(name=app_name)
        service_principal_id = service_principal['id']
        jobs = self.get_app_jobs(service_principal_id=service_principal_id)
        if not jobs:
            return None
        job = jobs[0]
        job_id = job['id']
        schema = self.get_app_job_schema(job_id, service_principal_id)
        rules = schema['synchronizationRules']
        rule_id = 'sesame_meow_cat'
        if rule_name:
            for rule in rules:
                if rule['name'] == rule_name:
                    rule_id = rule['id']
                    break
        else:
            rule_id = rules[0]['id']
        data = {
            'parameters': [{
                'subjects': subjects,
                'ruleId': rule_id,
            }],
        }
        url = posixpath.join(
            self.base_url,
            'servicePrincipals', service_principal_id,
            'synchronization', 'jobs', job_id,
            'provisionOnDemand'
        )
        return self.post(url, json_data=data, **kwargs)

    def provision_group_on_demand(self, group_id, app_name, rule_name=None, **kwargs):
        subjects = [{
            'objectId': group_id,
            'objectTypeName': 'Group',
        }]
        return self.provision_on_demand(subjects, app_name, rule_name, **kwargs)

    def provision_group_members_on_demand(self, group_id, user_ids, app_name, rule_name=None, **kwargs):
        subject = {
            'objectId': group_id,
            'objectTypeName': 'Group',
            'links': {
                'members': [{
                    'objectId': user_id,
                    'objectTypeName': 'User',
                } for user_id in user_ids]
            },
        }
        subjects = [ subject ]
        return self.provision_on_demand(subjects, app_name, rule_name, **kwargs)

    def get_tenant_info(self, tenant_id=None, raw=False, **kwargs):
        """
        https://learn.microsoft.com/en-us/graph/api/resources/tenantinformation?view=graph-rest-1.0
        requires the following permissions:
            CrossTenantInformation.ReadBasic.All
        """
        tenant_id = tenant_id or self.tenant_id
        route = f"findTenantInformationByTenantId(tenantId='{tenant_id}')"
        route = f'{self.base_url}/tenantRelationships/{route}'
        result = self.get(route, raw=raw, **kwargs)
        return result

    def get_sharepoint_site(self, hostname, site_name, raw=False, **kwargs):
        """
        gets the sharepoint site in question.  hostname should be the hostname
        in the sharepoint base url for the tenant, e.g., contoso.sharepoint.com
        """
        route = f'{self.base_url}/sites/{hostname}:/sites/{site_name}'
        return self.get(route, raw=raw, **kwargs)

    def get_sharepoint_site_permissions(self, site_id, raw=False, **kwargs):
        """
        gets the app permissions for the sharepoint site in question.
        """
        route = f'{self.base_url}/sites/{site_id}/permissions'
        return self.get(route, raw=raw, **kwargs)

    def get_sharepoint_site_permission(self, site_id, permission_id, raw=False, **kwargs):
        """
        gets the app permission for the sharepoint site / permission id in question.
        """
        route = f'{self.base_url}/sites/{site_id}/permissions/{permission_id}'
        return self.get(route, raw=raw, **kwargs)

    def update_sharepoint_site_permission(self, site_id, permission_id, roles, **kwargs):
        route = f'{self.base_url}/sites/{site_id}/permissions/{permission_id}'
        data = {
            'roles': roles,
        }
        return self.patch(route, json_data=data, **kwargs)

    def create_sharepoint_site_permission(self, site_id, app_id, app_name, roles, **kwargs):
        route = f'{self.base_url}/sites/{site_id}/permissions'
        data = {
            'roles': roles,
            'grantedToIdentities': [{
                'application': {
                    'id': app_id,
                    'displayName': app_name,
                },
            }, ]
        }
        return self.post(route, json_data=data, **kwargs)

    def delete_sharepoint_site_permission(self, site_id, permission_id, **kwargs):
        route = f'{self.base_url}/sites/{site_id}/permissions/{permission_id}'
        return self.delete(route, **kwargs)

    def list_domains(self, params=None, **kwargs):
        route = f'{self.base_url}/domains'
        response = self.get(route, params=params, **kwargs)
        if not kwargs.get('raw'):
            return response['value']
        return response

    def initial_domain(self, params=None, **kwargs):
        result = self.list_domains(params=params)
        for x in result:
            if x['isInitial']:
                return x
        return result[0]

    def managed_tenants(self, **kwargs):
        route = f'{self.base_url}/tenantRelationships/multiTenantOrganization/tenants'
        response = self.get(route, **kwargs)
        return response
