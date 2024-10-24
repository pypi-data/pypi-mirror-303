###--------------------------###
###----- manager module -----###
###--------------------------###

'''
This module contains three classes:
    - ApiUser: Parent class
    - ApiAdmin: Child class and parent class, inherits from ApiUser
    - ApiRoot: Child class, inherits from ApiAdmin

These classes are used for interacting with the database through the API.
'''

### load modules
import json
import datetime as dt
from copy import deepcopy

import requests


#---------------------------------------------------------------------------#
#---------------------------------------------------------------------------#

###-------------------------###
###----- ApiUser class -----###

class ApiUser:

    def __init__(self, username, password, ip):
        self.session = requests.Session()

        self._user = username
        self._password = password
        self._ip = ip

        self._token, self._headers = self._get_token()

        self._role = self._get_user_role()
        self._organization = self._get_user_organization()

        self._url = None


    def _get_token(self):

        ret = self.session.post(
            f"{self._ip}/auth/token",
            data={
                "username": self._user,
                "password": self._password
            }
        )
        response = ret.json()

        if ret.status_code != 200:
            raise ValueError(response['detail'])
        
        token = response["access_token"]
        headers = {"Authorization": f"Bearer {token}"}
    
        return (token, headers)
    

    def _check_status_code(self, ret, status_code):
        '''
        Checks if the status code of the response is the expected one.
        If token has expired, it gets a new one.
        '''

        if ret.status_code != status_code:
            if ret.status_code == 401:
                self._token, self._headers = self._get_token()
                return 1
            else:
                error_message = {"status_code": ret.status_code, "detail": ret.json()['detail']}
                raise ValueError(error_message)
        else:
            return 0
    

    def _get_user_role(self):
        '''
        Returns the role of the user.
        '''

        url = f"{self._ip}/users/role"

        ret = self.session.get(url, headers=self._headers)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, headers=self._headers)
        
        self._url = ret.url
        jsonret = ret.json()

        return jsonret
    

    def _get_user_organization(self):
        '''
        Returns user's organization.
        '''

        url = f"{self._ip}/users/organization"

        ret = self.session.get(url, headers=self._headers)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, headers=self._headers)
        
        self._url = ret.url
        jsonret = ret.json()

        return jsonret
    

    def _get_datasetname(self, title, scenario, organization=None):
        '''
        Returns the datasetname of the given title and scenario.
        '''

        if organization is None:
            organization = self._organization

        url = f"{self._ip}/organization/{organization}/datasetname"
        params = {
            "title": title,
            "scenario": scenario
        }

        ret = self.session.get(url, params=params, headers=self._headers)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, params=params, headers=self._headers)

        self._url = ret.url
        jsonret = ret.json()

        return jsonret['datasetname']
    

    def _select_datasetname(self, dataset=None, title=None, scenario=None, organization=None):
        '''
        Checks if dataset is None, if so, it returns the datasetname of the given title and scenario.
        '''
        if dataset is None:
            if (title is not None) and (scenario is not None):
                return self._get_datasetname(title, scenario, organization)
            else:
                raise ValueError("Either 'dataset' or both 'title' and 'scenario' are needed.")
        else:
            return dataset


    def _get_polygons_layer_id(self, layer, scenario, organization=None):
        '''
        Returns the id of the given layer.
        '''

        if organization is None:
            organization = self._organization

        url = f"{self._ip}/organization/{organization}/polygons/layer_id"
        params = {
            "layer": layer,
            "scenario": scenario
        }

        ret = self.session.get(url, params=params, headers=self._headers)
        
        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, params=params, headers=self._headers)
        
        jsonret = ret.json()

        return jsonret['layer_id']
    

    def _select_polygon_layer_id(self, layer_id=None, layer=None, scenario=None, organization=None):
        '''
        Checks if layer_id is None, if so, it returns the id of the given layer.
        '''
        if layer_id is None:
            if (layer is not None) and (scenario is not None):
                return self._get_polygons_layer_id(layer, scenario, organization)
            else:
                raise ValueError("Either 'layer_id' or both 'layer' and 'scenario' are needed.")
        else:
            return layer_id
        

    def _get_polygon_geomtry_ids(self, names, layer_id, organization=None):
        '''
        Returns the ids of the polygons with the given names.
        '''

        if organization is None:
            organization = self._organization

        url = f"{self._ip}/organization/{organization}/polygons/geometry_ids"
        params = {
            "layer_id": layer_id,
            "names": names
        }

        ret = self.session.get(url, params=params, headers=self._headers)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, params=params, headers=self._headers)
        
        jsonret = ret.json()

        return jsonret['geom_ids']
    

    def _select_polygon_geometry_ids(self, geom_ids=None, names=None, layer_id=None, organization=None):
        """
        Checks if geom_ids is None, if so, it returns the ids of the polygons with the given names in the given layer_id.
        """
        if geom_ids is None:
            if (names is not None) and (layer_id is not None):
                return self._get_polygon_geomtry_ids(names, layer_id, organization)
            else:
                return []
        else:
            return geom_ids


    ###----------------------º
    ##--------------------
    #--- usable methods
    def get_metadata_all(self, organization=None):
        '''
        Returns a list of metadata dictionaries.
        '''

        if organization is None:
            organization = self._organization
        
        url = f"{self._ip}/organization/{organization}/datasets"

        ret = self.session.get(url, headers=self._headers)
        
        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, headers=self._headers)

        self._url = ret.url
        jsonret = ret.json()

        return jsonret

    
    def _get_tables_scheme(self, organization=None):
        '''
        Returns a dictionary with all the point and polygons scenarios and datasets.
        '''

        if organization is None:
            organization = self._organization

        scenarios_list = self.list_scenarios(organization)
        polygons_scenarios_list = self.list_polygons_scenarios(organization)

        tables_dict = {'points': {}, 'polygons': {}}
        
        for scenario in scenarios_list:
            tables_dict['points'][scenario] = []
            
            for dataset in self.list_datasets(scenario, organization):
                tables_dict['points'][scenario].append(dataset)

        for polygons_scenario in polygons_scenarios_list:
            tables_dict['polygons'][polygons_scenario] = []
            
            for polygons_dataset in self.list_polygons_datasets(polygons_scenario, organization):
                tables_dict['polygons'][polygons_scenario].append(polygons_dataset) 

        return tables_dict


    ###----------------------------------###
    ###----- points dataset methods -----###
    def list_scenarios(self, organization=None):
        '''
        Returns a list of scenarios names.
        '''

        if organization is None:
            organization = self._organization

        url = f"{self._ip}/organization/{organization}/datasets"

        ret = self.session.get(url, headers=self._headers)
        
        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, headers=self._headers)

        self._url = ret.url
        jsonret = ret.json()
            
        scenario_list = list(set([data['scenario'] for data in jsonret]))

        return scenario_list


    def list_datasets(self, scenario, organization=None):
        '''
        Returns a list of dataset names.
        '''

        if organization is None:
            organization = self._organization

        url = f"{self._ip}/organization/{organization}/datasets"

        ret = self.session.get(url, headers=self._headers)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, headers=self._headers)

        self._url = ret.url
        jsonret = ret.json()

        dataset_list = list(set([data['datasetname'] for data in jsonret if data['scenario'] == scenario]))

        return dataset_list


    def get_metadata(self, dataset=None, title=None, scenario=None, organization=None):
        '''
        Returns the metadata of the dataset.
        '''

        if organization is None:
            organization = self._organization
            
        dataset = self._select_datasetname(dataset, title, scenario, organization)
        
        url = f"{self._ip}/organization/{organization}/datasets/{dataset}/metadata"

        ret = self.session.get(url, headers=self._headers)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, headers=self._headers)

        self._url = ret.url
        jsonret = ret.json()

        return jsonret


    #-----------------------#
    #--- manage datasets ---#
    def modify_metadata(self, dataset, metadata, organization=None):
        """
        This method changes the metadata of the dataset. 
        'metadata' contains the values to be changed:
            - scenario
            - title
            - heading_angle
            - inc_angle
            - orbit
            - swath
            - geometry
            - pre_process
            - process
            - lon_ref
            - lat_ref
            - user_boundary
        It is not necessary to include all the values, only the ones to be changed.
        If other different values are included, they will be ignored.
        """
        
        if organization is None:
            organization = self._organization

        url = f"{self._ip}/organization/{organization}/datasets/{dataset}/metadata"

        ret = self.session.post(url, json=metadata, headers=self._headers)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.post(url, json=metadata, headers=self._headers)

        self._url = ret.url

        return {"status_code": ret.status_code, "detail": ret.json()}



    ###------------------------------###
    ###----- point data methods -----###
    def get_dates(self, dataset=None, title=None, scenario=None, organization=None):
        '''
        Returns a dictionary with the dates.
        '''

        if organization is None:
            organization = self._organization

        dataset = self._select_datasetname(dataset, title, scenario, organization)
        
        url = f"{self._ip}/organization/{organization}/datasets/{dataset}/metadata"

        ret = self.session.get(url, headers=self._headers)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, headers=self._headers)

        self._url = ret.url
        jsonret = ret.json()

        days_list = jsonret['dates']
        dates_dict = {(dt.date(1, 1, 1) + dt.timedelta(days=int(days)-365)).strftime("%Y-%m-%d"): days for days in days_list}

        return dates_dict


    def get_data(self, dataset=None, title=None, scenario=None, polygon=None, date_span=None, organization=None):
        '''
        Returns data in a json object including velocities and the displacements within the date span, limits are included.
            - date_span has to be a list of the form [date_start, date_end].
                If date_span is None, the whole dataset is returned.
                If date_span is not None, the velocities are recalculated for the given date span.
        '''

        if organization is None:
            organization = self._organization

        dataset = self._select_datasetname(dataset, title, scenario, organization)

        if date_span is None:
            dates = self.get_metadata(dataset=dataset, organization=organization)['dates']
            params = {'date_span': (dates[0], dates[-1])}
        else:
            params = {'date_span': (date_span[0], date_span[1])}

        if polygon is not None:
            params['polygon'] = json.dumps(polygon)

        url = f"{self._ip}/organization/{organization}/datasets/{dataset}"

        ret = self.session.get(url, headers=self._headers, params = params)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, headers=self._headers, params = params)

        self._url = ret.url
        jsonret = ret.json()

        return jsonret


    def get_complete_json(self, dataset=None, title=None, scenario=None, organization=None):
        '''
        Returns data (with all dates) and metadata together in a json.
        '''

        if organization is None:
            organization = self._organization

        dataset = self._select_datasetname(dataset, title, scenario, organization)
        
        metadata = self.get_metadata(dataset=dataset, organization=organization)

        dates = metadata['dates']
        date_span = [dates[0], dates[-1]]

        data = self.get_data(dataset, date_span=date_span, organization=organization)

        complete_json = json.loads(json.dumps({"metadata": metadata, "data": data}))

        return complete_json


    def get_velocities(self, dataset=None, title=None, scenario=None, polygon=None, extended=False, organization=None):
        '''
        Returns data in a json format with the velocities stored in the database.
            - polygon: if not None, set the polygon to filter the data spatially.
            - extended: if True, returns the velocities of the points together with the extended values.
        '''

        if organization is None:
            organization = self._organization

        dataset = self._select_datasetname(dataset, title, scenario, organization)
        
        params = {}
        if polygon is not None:
            params['polygon'] = json.dumps(polygon)

        if extended:
            params['extended'] = extended

        url = f"{self._ip}/organization/{organization}/datasets/{dataset}"

        ret = self.session.get(url, headers=self._headers, params=params)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, headers=self._headers, params=params)

        self._url = ret.url
        jsonret = ret.json()

        return jsonret


    def get_point_ids(self, dataset=None, title=None, scenario=None, polygon=None, organization=None):
        '''
        Returns points ids of the given dataset.
        '''

        if organization is None:
            organization = self._organization

        dataset = self._select_datasetname(dataset, title, scenario, organization)

        url = f"{self._ip}/organization/{organization}/datasets/{dataset}"
        if polygon is None:
            params = {}
        else:
            params = {'polygon': polygon}

        ret = self.session.get(url, headers=self._headers, params=params)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, headers=self._headers, params=params)

        self._url = ret.url
        jsonret = ret.json()

        point_ids = [point['id'] for point in jsonret['features']]

        return point_ids


    def get_data_details(self, ids, dataset=None, title=None, scenario=None, organization=None):
        '''
        Returns details of the data points labelled the given ids.
        '''

        if organization is None:
            organization = self._organization

        dataset = self._select_datasetname(dataset, title, scenario, organization)
        
        if len(ids) != 0:
            url = f"{self._ip}/organization/{organization}/datasets/{dataset}/details"
            params = {"ids": ids}

            ret = self.session.get(url, headers=self._headers, params=params)

            if self._check_status_code(ret, 200) == 1:
                ret = self.session.get(url, headers=self._headers, params=params)

            self._url = ret.url
            jsonret = ret.json()

            return jsonret
        
        else:
            raise ValueError("No point id is provided")


    #-----------------------#
    #--- manage extended ---#
    def get_extended_metadata(self, dataset=None, title=None, scenario=None, organization=None):
        '''
        Returns the extended metadata table of a given dataset.
        '''

        if organization is None:
            organization = self._organization

        dataset = self._select_datasetname(dataset, title, scenario, organization)

        url = f"{self._ip}/organization/{organization}/extended/{dataset}/metadata"

        ret = self.session.get(url, headers=self._headers)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, headers=self._headers)

        self._url = ret.url
        jsonret = ret.json()
        
        return jsonret


    def get_extended_names(self, dataset=None, title=None, scenario=None, organization=None):
        '''
        Returns the list of the extended keys.
        '''

        if organization is None:
            organization = self._organization

        dataset = self._select_datasetname(dataset, title, scenario, organization)

        jsonret = self.get_extended_metadata(dataset, organization=organization)
        
        return [metadata['key'] for metadata in jsonret]


    def get_extended(self, key, dataset=None, title=None, scenario=None, organization=None):
        '''
        Returns extended values with indices in a json format.
        '''

        if organization is None:
            organization = self._organization

        dataset = self._select_datasetname(dataset, title, scenario, organization)

        url = f"{self._ip}/organization/{organization}/datasets/{dataset}/extended"
        params = {'key': key}

        ret = self.session.get(url, params=params, headers=self._headers)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, params=params, headers=self._headers)

        self._url = ret.url
        jsonret = ret.json()
        
        return jsonret


    #------------------------#
    #--- polygons methods ---#
    def get_polygons_layers(self, organization=None):
        '''
        Returns a list of polygons layers.
        '''

        if organization is None:
            organization = self._organization

        url = f"{self._ip}/organization/{organization}/polygons/layers"

        ret = self.session.get(url, headers=self._headers)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, headers=self._headers)

        self._url = ret.url
        jsonret = ret.json()

        return jsonret
    

    def get_polygons_geometries(self, layer_id=None, layer=None, scenario=None, geom_ids=None, names=None, polygon=None, organization=None):
        '''
        Returns the polygons geometries that satify the conditions passed in the arguments.
        '''

        if organization is None:
            organization = self._organization

        layer_id = self._select_polygon_layer_id(layer_id, layer, scenario, organization)
        geom_ids = self._select_polygon_geometry_ids(geom_ids, names, layer_id, organization)

        url = f"{self._ip}/organization/{organization}/polygons/geometries/{layer_id}"
        params = {}
        if polygon is not None:
            params['polygon'] = json.dumps(polygon)
        if len(geom_ids) != 0:
            params['geom_ids'] = geom_ids

        ret = self.session.get(url, headers=self._headers, params=params)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, headers=self._headers, params=params)

        self._url = ret.url
        jsonret = ret.json()
        
        return jsonret
       
    

    def get_polygons_metrics(self, layer_id=None, layer=None, scenario=None, type=None, metric=None, organization=None):
        '''
        Returns the polygons metrics that satify the conditions passed in the arguments.
        '''

        if organization is None:
            organization = self._organization

        if layer_id is None and layer is None and scenario is None:
            layer_id = None
        else:
            layer_id = self._select_polygon_layer_id(layer_id, layer, scenario, organization=organization)

        url = f"{self._ip}/organization/{organization}/polygons/metrics"
        params = {'layer_id': layer_id, 'type': type, 'metric': metric}

        ret = self.session.get(url, headers=self._headers, params=params)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, headers=self._headers, params=params)

        self._url = ret.url
        jsonret = ret.json()

        return jsonret
    

    def get_polygons_metrics_complete_json(self, metric=None, organization=None):
        '''
        Returns the polygons metrics complete json, ready for uploading it to another database.
        '''

        if organization is None:
            organization = self._organization

        url = f"{self._ip}/organization/{organization}/polygons/metrics/{metric}"

        ret = self.session.get(url, headers=self._headers)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, headers=self._headers)

        self._url = ret.url
        jsonret = ret.json()

        return jsonret
    

    def get_polygons_relations(self, metric=None, layer_id=None, layer=None, scenario=None, organization=None):
        '''
        Returns the polygons relation that satify the conditions passed in the arguments.
        '''

        if organization is None:
            organization = self._organization

        layer_id = self._select_polygon_layer_id(layer_id, layer, scenario, organization=organization)

        url = f"{self._ip}/organization/{organization}/polygons/relations"
        params = {}
        if metric is not None:
            params['metric'] = metric
        if layer_id is not None:
            params['layer_id'] = layer_id

        ret = self.session.get(url, headers=self._headers, params=params)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, headers=self._headers, params=params)

        self._url = ret.url
        jsonret = ret.json()

        return jsonret


    def get_polygons_data(self, metric, time_format="stamps", layer_id=None, layer=None, scenario=None, geom_ids=None, names=None, polygon=None, date_span=None, organization=None):
        '''
        Returns the polygons data that satify the conditions passed in the arguments.
        '''

        if organization is None:
            organization = self._organization

        layer_id = self._select_polygon_layer_id(layer_id, layer, scenario, organization=organization)
        geom_ids = self._select_polygon_geometry_ids(geom_ids, names, layer_id, organization)
        
        url = f"{self._ip}/organization/{organization}/polygons/data/{layer_id}/{metric}"
        params = {'time_format': time_format}
        if len(geom_ids) != 0:
            params['geom_ids'] = geom_ids
        if polygon is not None:
            params['polygon'] = json.dumps(polygon)
        if date_span is not None:
            params['date_span'] = date_span
        
        ret = self.session.get(url, headers=self._headers, params=params)
        
        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, headers=self._headers, params=params)

        self._url = ret.url
        jsonret = ret.json()

        return jsonret


    def get_polygons_time_series(self, metric, time_format="stamps", parent_process_dates='first', layer_id=None, layer=None, scenario=None, geom_ids=None, names=None, polygon=None, date_span=None, organization=None):
        '''
        Returns the polygons time series that satify the conditions passed in the arguments.
        '''

        if organization is None:
            organization = self._organization

        layer_id = self._select_polygon_layer_id(layer_id, layer, scenario, organization=organization)
        geom_ids = self._select_polygon_geometry_ids(geom_ids, names, layer_id, organization)

        url = f"{self._ip}/organization/{organization}/polygons/time_series/{layer_id}/{metric}"
        params = {'parent_process_dates': parent_process_dates, 'time_format': time_format}
        if len(geom_ids) != 0:
            params['geom_ids'] = geom_ids
        if polygon is not None:
            params['polygon'] = json.dumps(polygon)
        if date_span is not None:
            params['date_span'] = date_span

        ret = self.session.get(url, headers=self._headers, params=params)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, headers=self._headers, params=params)

        self._url = ret.url
        jsonret = ret.json()

        return jsonret


    #------------------------#
    #--- old polygons methods ---#
    def _list_polygons_scenarios(self, organization=None):
        '''
        Returns a list of scenarios names.
        '''

        if organization is None:
            organization = self._organization

        url = f"{self._ip}/organization/{organization}/_polygons"

        ret = self.session.get(url, headers=self._headers)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, headers=self._headers)

        self._url = ret.url
        jsonret = ret.json()

        scenario_list = [data['scenario'] for data in jsonret]

        return scenario_list


    def _list_polygons_datasets(self, scenario, organization=None):
        '''
        Returns a list of the loaded polygons metadata in this organization and scenario.
        '''

        if organization is None:
            organization = self._organization

        url = f"{self._ip}/organization/{organization}/_polygons"

        ret = self.session.get(url, headers=self._headers)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, headers=self._headers)

        self._url = ret.url
        jsonret = ret.json()

        dataset_list = [data['datasetname'] for data in jsonret if data['scenario'] == scenario]

        return dataset_list


    def _get_polygons(self, polygon_dataset, organization=None):
        '''
        Returns a json object with the polygons and indices loaded in polygon_dataset.
        '''

        if organization is None:
            organization = self._organization

        url = f"{self._ip}/organization/{organization}/_polygons/{polygon_dataset}"

        ret = self.session.get(url, headers=self._headers)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, headers=self._headers)

        self._url = ret.url
        jsonret = ret.json()

        return jsonret


    def _get_polygons_metadata(self, polygon_dataset, organization=None):
        '''
        Returns a json object with the polygons metadata loaded in polygon_dataset.
        '''

        if organization is None:
            organization = self._organization

        url = f"{self._ip}/organization/{organization}/_polygons/{polygon_dataset}/metadata"

        ret = self.session.get(url, headers=self._headers)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, headers=self._headers)

        self._url = ret.url
        jsonret = ret.json()

        return jsonret
    

    def _get_polygons_metadata_all(self, organization=None):
        '''
        Returns a json object with all the polygons metadata.
        '''

        if organization is None:
            organization = self._organization

        url = f"{self._ip}/organization/{organization}/_polygons"

        ret = self.session.get(url, headers=self._headers)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, headers=self._headers)

        self._url = ret.url
        jsonret = ret.json()

        return jsonret


    def _get_indices_metadata(self, polygon_dataset, index_types=None, date_span=None, organization=None):
        """
        Returns the indices metadata of polygon_dataset and organization
        """

        if organization is None:
            organization = self._organization

        url = f"{self._ip}/organization/{organization}/indices/{polygon_dataset}/metadata"

        params = {}
        if date_span is not None:
            params['date_span'] = (date_span[0], date_span[1])
            if index_types is not None:
                params['index_types'] = index_types
        else:
            if index_types is not None:
                params['index_types'] = index_types

        ret = self.session.get(url, headers=self._headers, params=params)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, headers=self._headers, params=params)

        self._url = ret.url
        jsonret = ret.json()

        return jsonret


    def _get_polygons_time_series(self, polygon_dataset, ids, index_types=None, date_span=None, organization=None):
        '''
        Returns polygons time series of type 'index_type' labelled by the given ids in between the dates in 'date_span'.
        '''

        if organization is None:
            organization = self._organization
        
        if len(ids) != 0:
            indices_json_list = self._get_indices_metadata(polygon_dataset, index_types=index_types, date_span=date_span, organization=organization)
            if index_types is None: # if is None, then get all the index_types 
                index_types = list(set(row['index_type'] for row in indices_json_list))

            #--- index dict
            index_dict = {}
            for index_type in index_types:
                index_dict[index_type] = {}

            for indices_json in indices_json_list:
                index = indices_json['index']
                index_dict[indices_json['index_type']][index] = indices_json['date']

            #--- empty response
            response = {
                'type': 'FeatureCollection',
                'features': [],
                'bbox': None
            }

            #--- loop over index types
            for index_type in index_types:

                #--- query
                url = f"{self._ip}/organization/{organization}/_polygons/{polygon_dataset}/details"
                params = {"ids": ids, "indices": list(index_dict[index_type].keys())}

                ret = self.session.get(url, headers=self._headers, params=params)

                if self._check_status_code(ret, 200) == 1:
                    ret = self.session.get(url, headers=self._headers, params=params)

                self._url = ret.url
                jsonret = ret.json()

                #--- rename indices
                for js in jsonret['features']:
                    properties = js['properties']
                    id = properties['id']

                    properties = {str(v): properties[k] for k, v in index_dict[index_type].items()}
                    js['properties'] = properties
                    js['id'] = id
                    js['index_type'] = index_type

                    response['features'].append(js)

            return response
            
        else:
            raise ValueError("No polygon id is provided")


    #-------------------#
    #--- use plugins ---#
    def use_plugin(self, plugin_name, parameters_dict, dataset=None, title=None, scenario=None, organization=None):
        '''
        Uses the plugin "plugin_name" which requires the parameters "parameters_dict" in a dictionary form.
        '''

        if organization is None:
            organization = self._organization

        dataset = self._select_datasetname(dataset, title, scenario, organization)

        url = f"{self._ip}/organization/{organization}/datasets/{dataset}/process"
        _json={
            "name": plugin_name,
            "data": parameters_dict
        }

        ret = self.session.put(url, headers=self._headers, json=_json)
        
        if self._check_status_code(ret, 200) == 1:
            ret = self.session.put(url, headers=self._headers, json=_json)

        self._url = ret.url
        jsonret = ret.json()

        return jsonret



#---------------------------------------------------------------------------#
#---------------------------------------------------------------------------#

###--------------------------###
###----- ApiAdmin class -----###


class ApiAdmin(ApiUser):
    '''
    This class can be created only as a admin user.
    '''

    def __init__(self, username, password, ip):
        super().__init__(username, password, ip)

        if self._role < 1:
            raise ValueError("User is not admin")


    def _reformat_polygons(self, polygons_json):
        """
        This function checks if the polygon json has the right format, if not is is modified as needed.
        """

        reformated_polygons_json = deepcopy(polygons_json)

        for i, d in enumerate(reformated_polygons_json['data']['features']):
            if 'id' in d['properties'].keys():
                d['properties']['id'] = int(d['properties']['id']) # make sure that 'id' in 'properties' is an integer.
            else:
                d['properties']['id'] = i

            if 'uid' not in d['properties'].keys():
                d['properties']['uid'] = d['properties']['id']
            
            if d['geometry']['type'] == 'MultiPolygon':
                d['geometry']['type'] = 'Polygon'
                d['geometry']['coordinates'] = d['geometry']['coordinates'][0]
                
        return reformated_polygons_json


    ###----------------------
    ##--------------------
    #--- usable methods

    #-----------------------#
    #--- manage datasets ---#
    def add_dataset(self, dataset_json, title, scenario, organization=None):
        '''
        This method adds new dataset data and metadata tables from the dataset_json object.
        '''

        if organization is None:
            organization = self._organization

        dataset_json['metadata']['title'] = title
        dataset_json['metadata']['scenario'] = scenario
        
        url = f"{self._ip}/organization/{organization}/datasets"

        ret = self.session.put(url, json=dataset_json, headers=self._headers)

        if  self._check_status_code(ret, 201) == 1:
            ret = self.session.put(url, json=dataset_json, headers=self._headers)

        return ret.status_code
    

    def delete_dataset(self, dataset=None, title=None, scenario=None, organization=None):
        '''
        This method deletes a complete dataset.
        '''

        if organization is None:
            organization = self._organization

        dataset = self._select_datasetname(dataset, title, scenario, organization)

        url = f"{self._ip}/organization/{organization}/datasets/{dataset}"

        ret = self.session.delete(url, headers=self._headers)

        if self._check_status_code(ret, 204) == 1:
            ret = self.session.delete(url, headers=self._headers)

        return ret.status_code


    #-----------------------#
    #--- manage extended ---#
    def add_extended(self, extended_dict, dataset=None, title=None, scenario=None, organization=None):
        '''
        This methods adds an extended_dict in the extended table of dataset.
        '''

        if organization is None:
            organization = self._organization

        dataset = self._select_datasetname(dataset, title, scenario, organization)

        url = f"{self._ip}/organization/{organization}/datasets/{dataset}/extended"

        ret = self.session.patch(url, json=extended_dict, headers=self._headers)
        
        if self._check_status_code(ret, 200) == 1:
            ret = self.session.patch(url, json=extended_dict, headers=self._headers)

        return ret.status_code
    
    
    def delete_extended(self, key, dataset=None, title=None, scenario=None, organization=None):
        '''
        This method deletes the extended values with key 'key' in the dataset 'dataset'.
        '''

        if organization is None:
            organization = self._organization

        dataset = self._select_datasetname(dataset, title, scenario, organization)
        
        url = f"{self._ip}/organization/{organization}/datasets/{dataset}/extended"
        params={'key': key}

        ret = self.session.delete(url, params=params, headers=self._headers)

        if self._check_status_code(ret, 204) == 1:
            ret = self.session.delete(url, params=params, headers=self._headers)

        return ret.status_code
        

    #-----------------------#
    #--- manage polygons ---#
    def add_polygons_geometries(self, geometries_json, organization=None):
        '''
        This method adds polygons geometries.
            - Table polygons_layer: if one of the polygons belongs to a new layer, it is created.
            - Table polygons_geometry: if one of the polygons is new, it is created.
        '''

        if organization is None:
            organization = self._organization

        url = f"{self._ip}/organization/{organization}/polygons/geometry"

        ret = self.session.patch(url, json=geometries_json, headers=self._headers)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.patch(url, json=geometries_json, headers=self._headers)

        return {"status_code": ret.status_code, "detail": ret.json()}
    

    def add_polygons_metric(self, metrics_json, organization=None):
        '''
        This method adds polygons metrics and data.
            - Table polygons_metrics: if the metric does not exist, a new row is added.
            - Table polygons_data: if there is data for that metric and for an existing polygon, rows are added.
            - Table polygons_relation: if data is added to polygons_data table, rows are added.
        '''

        if organization is None:
            organization = self._organization

        url = f"{self._ip}/organization/{organization}/polygons/metric"

        ret = self.session.patch(url, json=metrics_json, headers=self._headers)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.patch(url, json=metrics_json, headers=self._headers)

        return {"status_code": ret.status_code, "detail": ret.json()}
    

    def delete_polygons_layer(self, layer_id=None, layer=None, scenario=None, organization=None):
        '''
        This method deletes the polygons layer with id 'layer_id', its geometries and its data associated, together with the corresponding polygons_relation rows.
        '''

        if organization is None:
            organization = self._organization

        layer_id = self._select_polygon_layer_id(layer_id, layer, scenario, organization)

        url = f"{self._ip}/organization/{organization}/polygons/layer/{layer_id}"

        ret = self.session.delete(url, headers=self._headers)

        if self._check_status_code(ret, 204) == 1:
            ret = self.session.delete(url, headers=self._headers)

        return ret.status_code


    def delete_polygons_geometries(self, geom_ids, layer_id=None, layer=None, scenario=None, organization=None):
        """
        This method deletes the polygons geometries with ids 'geom_ids' in the layer with id 'layer_id', together with its associeted data and polygons_relation table rows.
        """

        if organization is None:
            organization = self._organization

        layer_id = self._select_polygon_layer_id(layer_id, layer, scenario, organization)

        url = f"{self._ip}/organization/{organization}/polygons/geometries/{layer_id}"
        _json = geom_ids

        ret = self.session.delete(url, headers=self._headers, json=_json)

        if self._check_status_code(ret, 204) == 1:
            ret = self.session.delete(url, headers=self._headers, json=_json)
        
        return ret.status_code


    def delete_polygons_metric(self, metric, organization=None):
        '''
        This method deletes the polygons metric with name 'metric', together with its data and polygons_relation table rows.
        '''

        if organization is None:
            organization = self._organization

        url = f"{self._ip}/organization/{organization}/polygons/metric/{metric}"

        ret = self.session.delete(url, headers=self._headers)

        if self._check_status_code(ret, 204) == 1:
            ret = self.session.delete(url, headers=self._headers)

        return ret.status_code
    

    def delete_polygons_data(self, ids=None, data_ids=None, geom_ids=None, layer_id=None, layer=None, scenario=None, metric=None, organization=None):
        '''
        This method deletes the polygons data with the given conditions.
        '''

        if organization is None:
            organization = self._organization

        layer_id = self._select_polygon_layer_id(layer_id, layer, scenario, organization)

        url = f"{self._ip}/organization/{organization}/polygons/data"
        json_data = {"ids": ids, "data_ids": data_ids, "geom_ids": geom_ids, "layer_id": layer_id, "metric": metric}

        ret = self.session.delete(url, headers=self._headers, json=json_data)

        if self._check_status_code(ret, 204) == 1:
            ret = self.session.delete(url, headers=self._headers, json=json_data)

        return ret.status_code


    #---------------------------#
    #--- manage old polygons ---#
    def _add_polygons(self, polygons_dataset, polygons_json, organization=None):
        '''
        This method adds polygons to the dataset with name dataset_name.
        '''

        if organization is None:
            organization = self._organization

        url = f"{self._ip}/organization/{organization}/_polygons/{polygons_dataset}"
        polygons_json = self._reformat_polygons(polygons_json)

        ret = self.session.put(url, json=polygons_json, headers=self._headers)

        if self._check_status_code(ret, 201) == 1:
            ret = self.session.put(url, json=polygons_json, headers=self._headers)

        return ret.status_code


    def _delete_polygons(self, polygons_dataset, organization=None):
        '''
        This method delete polygons of dataset with name polygons_dataset.
        '''

        if organization is None:
            organization = self._organization

        url = f"{self._ip}/organization/{organization}/_polygons/{polygons_dataset}"

        ret = self.session.delete(url, headers=self._headers)

        if self._check_status_code(ret, 204) == 1:
            ret = self.session.delete(url, headers=self._headers)

        return ret.status_code


    #-------------#
    #--- quota ---#
    def get_assigned_quota(self, organization=None):
        '''
        Returns the assigned quota of the selected organization.
        '''

        if organization is None:
            organization = self._organization

        url = f"{self._ip}/organization/{organization}/quota/assigned"

        ret = self.session.get(url, headers=self._headers)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, headers=self._headers)

        self._url = ret.url
        jsonret = ret.json()

        return jsonret
    

    def get_consumed_quota(self, organization=None):
        '''
        Returns the consumed quota of the selected organization.
        '''

        if organization is None:
            organization = self._organization

        url = f"{self._ip}/organization/{organization}/quota/consumed"

        ret = self.session.get(url, headers=self._headers)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, headers=self._headers)

        self._url = ret.url
        jsonret = ret.json()

        return jsonret



#---------------------------------------------------------------------------#
#---------------------------------------------------------------------------#

###-------------------------###
###----- ApiRoot class -----###


class ApiRoot(ApiAdmin):
    '''
    This class can be created only as a admin user.
    '''

    def __init__(self, username, password, ip):
        ApiUser.__init__(self, username, password, ip)

        if self._role != 2:
            raise ValueError("User is not root")


    ###----------------------
    ##--------------------
    #--- usable methods

    #--------------------#
    #--- manage users ---#
    def get_users_info(self):
        '''
        Returns a list of dictionaries. Each dictionary has the information.
        '''

        url = f"{self._ip}/users"
        
        ret = self.session.get(url, headers=self._headers)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.get(url, headers=self._headers)

        jsonret = ret.json()

        return jsonret


    def get_users_list(self):
        '''
        Returns a list with all the user names.
        '''

        jsonret = self.get_users_info()

        user_list = [user['name'] for user in jsonret]

        return user_list


    def create_user(self, organization, new_user, new_pwd, e_mail=None, _is_admin=False, _root=False, quota=1.0):
        '''
        This mehotd creates a new user.
        '''

        is_admin = "TRUE" if _is_admin else "FALSE" 
        root = "TRUE" if _root else "FALSE"
        email = e_mail or f"{new_user}@detektia.com"

        url = f"{self._ip}/users"
        _json = {
            "organization": organization,
            "name": new_user,
            "password": new_pwd,
            "email": email,
            "is_admin": is_admin,
            "root": root,
            "quota": quota
        }

        ret = self.session.post(url, json=_json, headers=self._headers)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.post(url, json=_json, headers=self._headers)

        return ret.status_code


    def delete_user(self, user_to_delete):
        '''
        This mehotd deletes user.
        '''

        url = f"{self._ip}/users/{user_to_delete}"

        ret = self.session.delete(url, headers=self._headers)

        if self._check_status_code(ret, 204) == 1:
            ret = self.session.delete(url, headers=self._headers)

        return ret.status_code
    

    def modify_role(self, user, is_admin):
        '''
        This method updates the role of the user.
        '''

        url = f"{self._ip}/users/{user}/update/role"
        _json = {
            "role": is_admin
        }

        ret = self.session.post(url, json=_json, headers=self._headers)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.post(url, json=_json, headers=self._headers)

        return ret.json()



    #------------------#
    #----- manage -----#

    def modify_quota(self, organization, quota):
        '''
        This method updates the quota of the organization.
        '''

        url = f"{self._ip}/organization/{organization}/update/quota"
        _json = {
            "quota": quota
        }
        
        ret = self.session.post(url, json=_json, headers=self._headers)

        if self._check_status_code(ret, 200) == 1:
            ret = self.session.put(url, json=_json, headers=self._headers)

        jsonret = ret.json()

        return jsonret
    