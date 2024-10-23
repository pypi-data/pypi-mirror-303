import json
import os
import re
from datetime import datetime
from pyspark.sql.functions import lit, col, regexp_replace
from delta.tables import *
from adal import AuthenticationContext
import requests
from types import SimpleNamespace
#import dbutils
from pathlib import Path

class Landing:
    """
        A class for landing API ingests and other data into Azure Data Lake Storage (ADLS). Currently can ingest SharePoint Online data and JSON (API-sourced) data.

        Methods:
        - set_static_col
        - set_config
        - set_bronze
        - set_landing_folder
        - set_content_type
        - set_tmp_file_location
        - set_autorename
        - set_distinct
        - set_tab_name
        - set_adls_container
        - set_auto_archive
        - set_sharepoint_location
        - set_sharepoint_auth
        - get_all_sharepoint_files
        - get_sharepoint_file
        - put_json_content
        - put_bronze

    """

    def __init__(self, spark, dbutils, database, bronze_table, target_folder = None, filename = '', catalog = 'default', container = 'bronze'):
        """
        Initializes a Landing object with the specified parameters.

        Parameters:
        - spark:                            SparkSession object to be used for processing.
        - dbutils:                          Databricks utilities object for file operations.
        - database:                         Name of the database where the data should be landed.
        - bronze_table:                     Name of the bronze table where the data should be landed.
        - target_folder (str, optional):    ADLS folder path where files should be stored. If None, it is inferred based on the database and bronze table.
        - filename (str, optional):         Filename with extension for the data to be landed.
        - catalog (str, optional):          Catalog used in Delta Lake (default is 'default').
        - container (str, optional):        ADLS storage container name (default is 'bronze').

        Attributes:
        - _dbutils:             Databricks utilities function for file operations.
        - _spark:               SparkSession object.
        - _container:           ADLS storage container name.
        - _target:              ADLS folder path where files should be stored.
        - _location:            Full path where files need to be stored.
        - _filename:            Cleaned filename with extension for the data.
        - _auto_archive:        Flag indicating whether to archive ingested files.
        - _file_path:           Full file path for the data.
        - _content_type:        Default content type for file upload (default is 'parquet').
        - _catalog:             Catalog used in Delta Lake.
        - _database:            Bronze database name.
        - _bronze_table:        Bronze table name for landing the data.
        - _bronze_table_path:   Complete path of the bronze table.
        - _joincolumns:         Columns to merge on when load type is set to merge.
        - _static_cols:         List of columns with fixed values to be added.
        - _loadtype:            Load type for data insertion (default is 'append').
        - _sharepoint_session:  SharePoint session object for authentication.
        - _timestamp:           Current timestamp.

        Raises:
        - Exception: If the specified location cannot be created.

        Notes:
        - The folder path is created if it does not exist.
        """

        self._dbutils       = dbutils                           # Required. Passes the dbutils function to be used down the line
        self._spark         = spark                             # Required. Passes a sparksession  to be used down the line

        #Ingestion vars
        self._container     = container                         # ADLS Storage container (Name of the blob storage)
        self._target        = target_folder                     # Required. the ADLS folder. Contains the full path after the storage container decleration. Should start with a /. If None or empty, one needs to be inferred.
        if target_folder is None:
            self._target = database + '/' + bronze_table.replace("__", "/").lower()
        self._location      = os.environ.get("ADLS").format(container=self._container,path=self._target)    #full path of where files need to be stored. 

        self._filename      = self._clean_filename(filename)    # Optional. the filename with extension that the data should be landed in

        self._excel_tabnames = []                               # Optional. Tells which tab names should be looked for in an excel file ingested from Sharepoint. If this list is empty, the first tab is used. 
        self._renamefiles   = True                              # Optional. Default behaviour adds a timestamp at the start of the filename in ADLS

        # Construct the full file path
        self._file_path = os.path.join(self._location, self._filename)

        self._content_type  = 'parquet'                         # Default expectation is to upload a Parquet file. change it when needed using the SET function

        #Bronze vars
        self._catalog       = catalog                           # Optional. the catalog used in delta lake. Defaults to prd
        self._database      = database                          # Required. the bronze database  that the data should be landed in
        self._bronze_table  = self.set_bronze(bronze_table, False)          # Required. the bronze tablename that the data should be landed in
        self._bronze_table_path  = f'{self._database}.{self._bronze_table}' # Complete path of the bronze table.

        self._distinct  = False                             # By default the input data is not made distinct
        self._joincolumns   = None                              # When load type is set to merge, this will contain the columns to merge on
        self._static_cols   = []                                # List of columns (dictionaries) that should be added with their fixed value, not in the source data. 
        self._loadtype      = 'append'                          # By default just add it into bronze

        self._column_logic = {}                                 # Optional. Can be used if a column needs to be manipulated before entering into bronze. contains a dictionary with the column name as key and a function as value.

        #Helper vars
        self._sharepoint_session = None
        self._timestamp     = datetime.now()

        
        # Check if the database exists
        databases = [db.name for db in spark.catalog.listDatabases()]
        if database not in databases:
            raise ValueError(f"Database {database} not found in the SparkSession.")

        # Check if the table name is valid
        if not re.match(r'^[a-zA-Z0-9_]+$', self._bronze_table):
            raise ValueError(f"Invalid table name: {self._bronze_table}. Table names can only contain alphanumeric characters and underscores.")

        # Ensure the specified location exists, create it if it doesn't
        if not os.path.exists(self._location):
            print('Folder path did not exist yet. Making the dir now.')
            try:
                os.makedirs(self._location, exist_ok=True)
            except Exception as e:
                raise Exception(f'Failed to create the folder. Error: {e}')

        
        #print(f'location: {self._location} | for the bronze table {self._bronze_table_path}')
    
    ##############################################
    # Basic configuration options for landing.   #
    ##############################################

    def set_static_col(self, cols = {}):
        """
        Set additional static columns for the bronze layer table.
        """
        print(f'Added columns to bronze layer table: {cols}')
        self._static_cols.append(cols)
        
        return self

    def set_config(self, data = {}):
        """
        Store the config on the ingested data that allows us to put it to bronze layer
        """

        if 'loadtype' in data:
            self._loadtype = data['loadtype']
        
        if 'join' in data:
            if isinstance(data['join'], list):
              self._joincolumns = data['join']
            else:
              raise Exception(f'Invalid join columns: {data["join"]}. We expect a stringified list. Error: {e}')

        if self._loadtype == 'merge':
            if self._joincolumns is None:
                raise Exception('Join columns must be specified when load type is set to merge.')

        return self
      
    def set_bronze(self, table, returning = True):
        """
        Sets the destination bronze table for landing the data.

        Args:
        - table (str): The name of the bronze table.
        - returning (bool): Flag to indicate if the function should return the updated object or the table name.

        Returns:
        - object or str: The updated object if returning is True, else returns the table name.
        """
        if not table.startswith("bronze__"):
            table = "bronze__" + table
            print(f'Changing bronze table name to {table}')
        self._bronze_table = table

        if returning:
            return self
        else:
            return table

    def set_landing_folder(self, folder):
        """
        Sets the landing folder path for the data.

        Args:
        - folder (str): The folder path for landing the data.
        """
        self._location = os.environ.get("ADLS").format(container=self._container,path=folder)

    def set_content_type(self, content_type):
        """
        Sets the content type for the data.

        Args:
        - content_type (str): The content type (JSON, CSV, XLSX, PARQUET).

        Raises:
        - ValueError: If the content type is not one of the allowed types.
        """
        allowed_content_types = ['json', 'csv', 'xlsx', 'xls','xlsm', 'parquet']
        if content_type.lower() not in allowed_content_types:
            raise ValueError(f"Invalid content type. Allowed types are: {', '.join(allowed_content_types)}")

        self._content_type = content_type
        return self
    
    def set_tmp_file_location(self, location):
        """
        Sets the temporary file location.

        Args:
        - location (str): The temporary file location.

        Returns:
        - object: The updated object with the temporary file location set.
        """
        self._tmp_file_location = location
        return self

    def set_autorename(self, rename = True):
        """
        Optional function to change the autorename that happens when adding a file to landing. By default the ingested filename is changed (or inferred) and includes the loading timestamp as part of the filename

        Args:
        - rename (bool): Required. True / False flag.
        """

        self._renamefiles = rename

        return self

    def set_adls_container(self, container):
        """
        Sets the ADLS container for the data.

        Args:
        - container (str): The container name.

        Returns:
        - object: The updated object with the container set.
        """
        self._container = container
        return self
    
    def set_auto_archive(self, archive):
        """
        Set the auto archive flag for the SharePoint files.

        Parameters:
        - archive (bool): Flag indicating whether to automatically archive SharePoint files.

        Returns:
        - None
        """
        if not isinstance(archive, bool):
            raise ValueError("The 'archive' parameter must be a boolean value.")

        self._auto_archive = archive

        return self      

    def set_tab_name(self, tabnames):
        """
        Set the standard tab to ingest for excel files collected from the SharePoint files.

        Parameters:
        - tabnames (string): the tab name to look for. Can be an array. if an array then the datatype is expected to be identical and ingests to the same table. 

        Returns:
        - None
        """
        if not isinstance(tabnames, list):
            raise ValueError("The 'tabname' parameter must be a list.")

        self._excel_tabnames = tabnames

        return self      

    ##############################################
    # SharePoint Ingestion to landing function.  #
    ##############################################

    def set_sharepoint_location(self, Resource):
        """
        Sets the SharePoint Source location for the data.

        Args:
        - Resource (str): The SharePoint resource path.

        Returns:
        - object: The updated object with the SharePoint location set.
        """
        
        # Check if the Resource resembles a SharePoint Online URL
        if '.sharepoint.com/sites' not in Resource:
            raise ValueError("Invalid SharePoint Online URL format. Please provide a valid SharePoint Online URL.")

        self._sharepoint_uri = '/'.join(Resource.rstrip('/').split('/')[:3]) + '/'
        parts = Resource.rstrip('/').split('/')
        self._sharepoint_site = parts[4]
        self._sharepoint_folder = '/'.join(parts[5:])
        self._sharepoint_folder_path = os.path.join(self._sharepoint_site, self._sharepoint_folder)

        if not self._sharepoint_folder_path[0] == '/':
            self._sharepoint_folder_path = "/" + self._sharepoint_folder_path

        # Print the values of each variable for verification
        print("SharePoint URI:", self._sharepoint_uri)
        print("SharePoint Folder Path:", self._sharepoint_folder_path)

        return self

    def set_sharepoint_auth(self, UserName, Password, Client_ID):
        """
        Sets the SharePoint authentication credentials.

        Args:
        - UserName (str): The username for SharePoint authentication.
        - Password (str): The password for SharePoint authentication.
        - Client_ID (str): The client ID for SharePoint authentication.

        Returns:
        - object: The updated object with the SharePoint authentication credentials set.

        Raises:
        - ValueError: If any of the input variables (UserName, Password, Client_ID) are empty.
        """
        if not UserName or not Password or not Client_ID:
            raise ValueError("Username, Password, and Client ID cannot be empty.")
        
        self._sharepoint_user      = UserName
        self._sharepoint_pass      = Password
        self._sharepoint_client_id = Client_ID

        return self

    def get_all_sharepoint_files(self, MatchingRegexPattern = '^.*\.(xlsx)$'):
        """
            This function will list all files under a Sharepoint folder and download the ones matched. Finally, it will hook the files into a delta bronze table defined. 
            
            Parameters:
            @MatchingRegexPattern        : Matching criteria on file name as Regex Pattern i.e for xls files '^.*\.(xls)$' or files containing the MASTER word '^.*MASTER*'
            
            Return
            List of SharePoint file objects, use dir(file) to see all properties like file.serverRelativeUrl or file.name
        """  
        
        MyFiles = []

        response = self._sharepoint_apicall()

        if response:
            try:
                jsons = json.loads(response.content)
                jsonvalue = jsons["d"]["results"]
                json_string = json.dumps(jsonvalue)
                files = json.loads(json_string, object_hook=lambda d: SimpleNamespace(**d))

                for file in files:
                    try:
                        if MatchingRegexPattern and re.match(MatchingRegexPattern, file.Name):
                            MyFiles.append(file)

                            print(f"File: {file.Name} - Selected for ingestion")
                            print(f"Downloading file {file.Name}")
                            self._file_path = self.get_sharepoint_file(file)

                            print('Converting to bronze now')
                            self.put_bronze()

                            # print('Archiving landed file')
                            # self._archive_file()

                    except Exception as file_error:
                        print(f"Error processing file {file.Name}: {str(file_error)}")

            except Exception as e:
                print(f"Failed to list all files in folder {self._sharepoint_folder_path}: {str(e)}")
                # Handle the exception gracefully or log it as needed
                # You can choose to raise the exception if it's critical or just continue with the remaining files

        self._sharepoint_files = MyFiles

        print(f'SharePoint folder {self._sharepoint_folder_path} contains {len(files)} files, out of which {len(MyFiles)} file(s) are selected.')

        return True

    def get_sharepoint_file(self, file, destination_filename=None):
        """
            This function will DOWNLOAD a file from a SharePoint, locally to databricks tmp folder first, and copied to a container if needed.
            
            Parameters:
            @FileNameSource: File name to download i.e. 'Master Remapping Table.xlsx'
            
            Return
            DownloadedPath:  Final location of the downloaded file.
        """

        SparkLocation = self._tmp_file_location
        PythonLocation = SparkLocation.replace('/dbfs/', 'dbfs:/')

        # Format all provided paths as needed
        if not self._sharepoint_folder_path.endswith('/'):
            self._sharepoint_folder_path += "/"
        if not self._sharepoint_uri.endswith('/'):
            self._sharepoint_uri += "/"
        if not self._sharepoint_folder_path.startswith('/'):
            self._sharepoint_folder_path = "/" + self._sharepoint_folder_path
        if self._location and not self._location.endswith('/'):
            self._location += "/"
        if self._location and self._location.startswith('/'):
            self._location = self._location[1:]

        if destination_filename is None:
            destination_filename = file.Name
        DownloadedPath = PythonLocation + file.Name

        ContainerPath = os.path.join(self._location, destination_filename)  # Format the Path, ADLS is stored with parameters

        try:
            response = self._sharepoint_apicall(file.Name)
            if response:
                # Generate a new filename based on the current datetime and original filename
                current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
                original_filename, file_extension = os.path.splitext(file.Name)

                if self._renamefiles:
                    new_filename = f"{current_datetime} - {original_filename}{file_extension}"
                else:
                    new_filename = f"{original_filename}{file_extension}"

                with open(SparkLocation + file.Name, "wb") as local_file:
                    local_file.write(response.content)

                # Check if the uploaded file actually exists
                if os.path.exists(SparkLocation + file.Name):
                    # Move the file to ADLS with the new filename
                    new_file_path = os.path.join(self._location, new_filename)
                    self._dbutils.fs.cp(PythonLocation + file.Name, new_file_path, True)
                    self._dbutils.fs.rm(PythonLocation + file.Name)
                    print(f'Successfully uploaded file to: {new_file_path}')

                    self._file_path = new_file_path
                    self._file_name = new_filename

                    return new_file_path
                else:
                    print('Error: Uploaded file does not exist')
                    return ("Error", "Uploaded file does not exist")

            else:
                print(response)
                print(response.text)
                return ("Error", response.text)

        except Exception as e:
            raise e

    ########################################
    # JSON Ingestion to landing function.  #
    ########################################

    def put_json_content(self, json_data):
        """
        Stores JSON data into a JSON file at the specified location with the given filename.

        Args:
        - json_data (dict): The JSON data to be stored in the file.

        Returns:
        str: The full path of the saved JSON file.
        """
        try:

            # Get the row count of the JSON data
            row_count = len(json_data)

            # Write the JSON data to the file
            json_string = json.dumps(json_data, indent=4)
            
            #parquetfile     = self._file_path.replace('.json', '.parquet')
            #parquetfilename = self._filename.replace( '.json', '.parquet')
            try:
                # Write the JSON data to the file in ADLS Gen2
                df = self._spark.read.json(self._spark.sparkContext.parallelize([json_string]))
                # Write the DataFrame to a Parquet file on ADLS Gen2
                df.write.mode("overwrite").parquet(self._file_path)
                #self._dbutils.fs.put(self._file_path, json_string, overwrite=True)
                print("JSON data successfully written to the file.")
            except Exception as e:
                # Handle any exceptions that occur during the file write operation
                error_message = f"Error writing JSON data to file: {e}"
                print(error_message)

            #with open(self._file_path, 'w') as file:
            #    json.dump(json_data, file, indent=4)
            #time.sleep(10)

            # Check if the file was created
            files = self._dbutils.fs.ls(self._location)
            found_files = [file_info.name for file_info in files]

            #if parquetfilename in found_files:
            #return self._file_path, row_count
            #else:
            #    found_files_str = ", ".join(found_files)
            #    raise FileNotFoundError(f"The file was not found in the specified directory. looking for file {parquetfilename}, but files in the listed directory: {found_files_str}")
            
            self._file_name

            return self
        
        except (OSError, IOError) as e:
            # Handle file I/O errors
            error_message = f"Error occurred while writing JSON data to file: {e}"
            raise IOError(error_message)
        except Exception as e:
            # Handle other exceptions
            error_message = f"An error occurred: {e}"
            raise Exception(error_message)
   
    #######################################
    # Databricks bronze layer ingestion.  #
    #######################################

    def set_column_logic(self, column_logic = {}):
        """
        Set the column logic for the bronze layer.
        """
        self._column_logic = column_logic
        return self

    def _check_bronze_ingestion(self):
        """
        Get the distinct delta__sourcefile values from the bronze table self._bronze_table_path
        via self._spark.sql() and check that self._file_name is not ingested already.
        If the file is ingested already, update the bronze table by setting delta__deleted column to 1
        where the file name matches the ingested file.
        """
        # Get the distinct delta__sourcefile values from the bronze table
        distinct_files_df = self._spark.sql(f"SELECT DISTINCT Sourcefile FROM {self._bronze_table_path}")

        # Check if the current file is already ingested
        existing_files = [row.Sourcefile for row in distinct_files_df.collect()]
        if self._file_name in existing_files:
            # Update the bronze table to mark the ingested file as deleted
            self._spark.sql(f"UPDATE {self._bronze_table_path} SET IsDeleted = 1 WHERE Sourcefile = '{self._file_name}'")

    def set_distinct(self):
        self._distinct = True

        return self

    def put_bronze(self):
        """
            Store the landed data into the designated bronze layer table.

            This function loads the landed data into a Spark DataFrame, processes it, and stores it in the designated bronze layer table.

            Returns:
            - bool: True if the data is successfully stored in the bronze layer table.

            Raises:
            - ValueError: If any errors occur during the data loading process.
        """

        print(f"Starting put_bronze function. Trying to load the file located at {self._file_path}.")

        if self._file_name is None:
            return("Ran put_bronze but No filename specified.")

        file_readers = {
            '.parquet': self._spark.read.parquet,
            '.json': self._spark.read.json,
            '.csv':  lambda path: self._spark.read.format('csv').option("header", "true").load(path),
            '.xlsx': lambda path: self._spark.read.format('com.crealytics.spark.excel').option("header", "true").option("useHeader", "true").option('inferSchema',"true").load(path),
            '.xls':  lambda path: self._spark.read.format('com.crealytics.spark.excel').option("useHeader", "true").option('inferSchema',"true").load(path)
        }

        file_extension = os.path.splitext(self._file_name)[1]

        try:
            reader = file_readers.get(file_extension)
            if reader is None:
                return(f"Unsupported file format: {file_extension}")
            stage = reader(self._file_path)

            if file_extension in ['.xlsx', '.xls'] and isinstance(self._excel_tabnames, list) and self._excel_tabnames:
                print(f'Filtering the excel to tabs {self._excel_tabnames}')
                stage = stage.filter(stage['tab_name'].isin(self._excel_tabnames))

        except Exception as e:
            raise Exception(f"Error reading file: {self._file_path} | {str(e)}")

        # Check if any additional static columns are required in bronze, and add them to the dataframe
        if self._static_cols:
            print("Adding static columns to the DataFrame...")
            try:
                for static_col in self._static_cols:
                    for col, value in static_col.items():
                        stage = stage.withColumn(col, lit(value))
            except Exception as e:
                raise Exception(f"Error adding static columns to dataframe: {static_col}")
        
        try:
          columns = [col for col in stage.columns]
        except Exception as e:
          raise Exception(f'Failed to create a column list: {e}. DF head: {stage.head()}')

        #Always make sure the bronze table has DbxCreated, DbxUpdated, IsDeleted, and Sourcefile columns.
        try:
            stage = stage.withColumn('DbxCreated', lit(datetime.now()))\
                         .withColumn('DbxUpdated', lit(datetime.now()))\
                         .withColumn('IsDeleted',  lit(0))\
                         .withColumn('Sourcefile', lit(self._file_name))
        except Exception as e:
            raise Exception(f'Failed to add delta columns: {e}')

        try:
            # Reorder the columns to have delta columns at the start of the table.
            delta_columns     = ['DbxCreated', 'DbxUpdated', 'IsDeleted', 'Sourcefile']
        except Exception as e:
                    raise Exception(f'Failed to make delta column name list: {e}')

        try:
            # Select the columns in the desired order
            stage = stage.select(*delta_columns + columns)
        except Exception as e:
            raise Exception(f'Failed to reshuffle the order: {e}')

        try:
            #Now change column names when needed to because they can't contain invalid characters
            cleaned_columns = [self._clean_column_name(col) for col in stage.columns]

            # Create a mapping of old column names to cleaned column names
            column_mapping = {old_col: new_col for old_col, new_col in zip(stage.columns, cleaned_columns) if old_col != self._clean_column_name(old_col)}

            # Rename columns in the DataFrame with cleaned names if any column names were changed
            if column_mapping:
                stage_cleaned = stage
                for old_col, new_col in column_mapping.items():
                    stage_cleaned = stage_cleaned.withColumnRenamed(old_col, new_col)

                stage = stage_cleaned
        except Exception as e:
            raise Exception(f'Failed to clean column names: {e}')
 
        # Make sure the delta bronze table is there and working
        print(f'Table name to load data to: {self._bronze_table_path}')
 
        table_exists = self._spark.catalog.tableExists(self._bronze_table_path)
 
        if not table_exists:
            print(f'Table {self._bronze_table_path} does not exist; inferring the schema and try to create it.')
            try:
              self._infer_table(stage)
            except Exception as e:
              raise Exception(f'Failed to call infer the schema: {e}')
        else:
            delta_table = DeltaTable.forName(self._spark, self._bronze_table_path)
            delta_schema = delta_table.toDF().schema
            stage_schema = stage.schema
 
            # Update IsDeleted flag if the file had already been ingested.
            try:
              self._check_bronze_ingestion()
            except Exception as e:
              raise Exception(f'Failed to check bronze ingestion: {e}')

            try:
              # Find the exact schema differences
              delta_fields = set((f.name.lower(), f.dataType) for f in delta_schema)
              stage_fields = set((f.name.lower(), f.dataType) for f in stage_schema)

              missing_fields = delta_fields - stage_fields
              extra_fields = stage_fields - delta_fields

              if missing_fields or extra_fields:
                  error_message = "Schema mismatch between stage DataFrame and Delta table.\n"
                  if missing_fields:
                      error_message += "Fields missing in stage DataFrame: {}\n".format(missing_fields)
                  if extra_fields:
                      error_message += "Extra fields in stage DataFrame: {}\n".format(extra_fields)
                  raise ValueError(error_message)
            except Exception as e:
              raise Exception(f'Schemas are misaligned but failed to give a meaningful error: {e}')

        if self._distinct:
            stage = stage.distinct()


        #Column custom logic
        if self._column_logic:
          print("Applying custom logic to columns...")
          try:
              for col, logic_func in self._column_logic.items():
                  stage = stage.withColumn(col, logic_func(col))
          except Exception as e:
              raise Exception(f'Failed to apply custom logic to columns: {e}')


        if self._loadtype =="overwrite":
            #Truncate and overwrite
            try:
                stage.write.format("delta").mode("overwrite").saveAsTable(self._bronze_table_path)
            except Exception as e:
                raise ValueError(f"Error overwriting data: {e}")
 
        elif self._loadtype =="append":
            #Just append the data with a new delta__load_date
            try:
                stage.write.format("delta").mode("append").saveAsTable(self._bronze_table_path)
            except Exception as e:
                raise ValueError(f"Error appending data: {e}")
 
        elif self._loadtype =="merge":
            #Parameters are then required
            if self._joincolumns is None or not isinstance(self._joincolumns, list):
                raise ValueError('No parameters added. A Merge load will need to know which values are used as join condition and it should be a list.')
    
            joinstring = ' AND '.join([f's.{cond} = f.{cond}' for cond in self._joincolumns])
            try:
                final = DeltaTable.forName(self._spark, self._bronze_table_path)
                final.alias('f') \
                     .merge(stage.alias('s'),joinstring) \
                     .whenMatchedUpdateAll() \
                     .whenNotMatchedInsertAll() \
                     .execute()
            except Exception as e:
                raise ValueError(f"Error merging data: {e}")
 
        else:
            raise ValueError(f'Loadtype {self._loadtype} is not supported.')
 
        return True

    ################################################################################################
    # Helper functions. Used internally in the class and not designed for calling them externally. #
    ################################################################################################

    def _clean_column_name(self, column_name):
        """
        Cleans a column name by removing special characters and replacing spaces with underscores.

        Args:
        - column_name (str): The original column name to be cleaned.

        Returns:
        - str: The cleaned column name without special characters and with spaces replaced by underscores.
        """
        # Remove special characters and replace spaces with underscores
        try:
          cleaned_name = re.sub(r'\W+', '', column_name.replace(' ', '_')).lower()
        except Exception as e:
          raise ValueError(f"Error cleaning column name: {e}")

        return cleaned_name
  
    def _archive_file(self):
        """
        Archive the file by moving it to the 'Archive' subfolder.

        Returns:
        - str: The path of the archived file.
        """
        try:
            archive_folder = "Archive"
            archive_path = os.path.join(self._file_path, archive_folder)

            # Create the "Archive" subfolder if it doesn't exist
            if not self._dbutils.fs.ls(archive_path):
                self._dbutils.fs.mkdirs(archive_path)

            # Move the file to the "Archive" subfolder
            archive_file_path = os.path.join(archive_path, os.path.basename(self._file_path))
            self._dbutils.fs.mv(self._file_path, archive_file_path)

            return True

        except Exception as e:
            print(f"Error archiving file {self._file_path} to {archive_path}: {str(e)}")
            raise e

    def _clean_filename(self, filename):
        """
        Cleans the filename by removing illegal characters.

        Args:
        - filename (str): The original filename to be cleaned.

        Returns:
        - str: The cleaned filename without illegal characters.
        """
        # Remove illegal characters from the filename
        cleaned_filename = re.sub(r'[<>:"/\\|?*]', '', filename)

        return cleaned_filename
    
    def _infer_table(self, df):
        """
        Infers the schema from the input DataFrame, creates a temporary view, and uses the inferred schema to create a Delta table.

        Parameters:
        - df (DataFrame): The input DataFrame from which the schema will be inferred.

        Returns:
        - bool: True if the Delta table creation is successful.

        Raises:
        - Exception: If there is an error during the Delta table creation process.
        """
        try:
            #display(df)
            # Infer the schema from the DataFrame
            df.createOrReplaceTempView("temp_view")
            inferred_schema = self._spark.sql(f"DESCRIBE temp_view").toPandas()

            # Create Delta table with the inferred schema
            sqlcode = f"CREATE TABLE {self._bronze_table_path} USING DELTA OPTIONS (header=true) AS SELECT * FROM temp_view"
            print(f'trying to create the inferred delta table: {sqlcode}')
            self._spark.sql(sqlcode)
            return True

        except Exception as e:
            raise Exception(f"Delta table creation failed with Error: {e}")

    def _device_flow_session(self):
        """
        Helper function to set up authentication against SharePoint Online using device flow.

        Returns:
        - requests.Session: Session object with authentication headers set for SharePoint API calls.
        """
        # Check if all required parameters for token acquisition are populated
        if not all([self._sharepoint_uri, self._sharepoint_user, self._sharepoint_pass, self._sharepoint_client_id]):
            raise ValueError("Missing required parameters for token acquisition. Please ensure all SharePoint authentication parameters are provided.")

        try:
            authority_url = 'https://login.microsoftonline.com/common'
            ctx = AuthenticationContext(authority_url, api_version='v2.0')
            tresult = ctx.acquire_token_with_username_password(self._sharepoint_uri, self._sharepoint_user, self._sharepoint_pass, self._sharepoint_client_id)

            session = requests.Session()
            session.headers.update({'Authorization': f'Bearer {tresult["accessToken"]}',
                                    'SdkVersion':   'sample-python-adal',
                                    'x-client-SKU': 'sample-python-adal'})

            self._sharepoint_session = session

            return session

        except Exception as e:
            print(f"Error setting up authentication session to {self._sharepoint_uri}: {e}")
            raise e
    
    def _sharepoint_apicall(self, filename=None):
        """
        Make an API call to retrieve files from a SharePoint folder.

        Parameters:
        - filename (str): The name of the file to retrieve. If specified, the API call will target that specific file.

        Returns:
        - requests.Response: The response object from the API call.
        """
        try:
            if self._sharepoint_session is None:
                graph_session = self._device_flow_session()
            else:
                graph_session = self._sharepoint_session

            folder = '/'.join([stuff for stuff in self._sharepoint_folder.split("/") if stuff not in re.sub(r'^.*?.com', '', self._sharepoint_uri).split("/")]) + '/'

            api_call = f"{self._sharepoint_uri}sites/{self._sharepoint_site}/_api/web/GetFolderByServerRelativeUrl('{folder}')/Files"

            if filename is not None:
                api_call += f"('{filename}')/$value"

            response = graph_session.get(api_call, headers={'Accept': 'application/json;odata=verbose'})

            response.raise_for_status()  # Raise an HTTPError for bad responses

            return response

        except requests.exceptions.RequestException as e:
            print(f"Error making SharePoint API call: {e}")
            raise e
    
class Delta:
    """
        A class for creating and managing Delta tables in Azure Databricks.

        Attributes:
        - db_name (str):                                Required. The name of the database containing the table.
        - table_name (str):                             Required. The name of the table.
        - spark (pyspark.sql.SparkSession):             Required. The SparkSession object to use for interacting with the table.
        - columns (list of dictionaries): Optional. A list of dictionaries, where each dictionary contains the column name, data type, and an optional comment.
        - options (dict):                               Optional. A dictionary containing the table options.
        - primary_key (str): Optional. The name of the primary key column.
        - partitioning (str): Optional. The name of the partitioning column.

        Methods:
        - set_columns(columns): Sets the column list for the table.
        - set_comment(comment):                         Sets the comment for the table.
        - set_options(options):                         Sets the options for the table.
        - set_primary_key(primary_key):                 Sets the primary key for the table.
        - set_partitioning(partitioning):               Sets the partitioning for the table.
        - add_column(column_name, data_type, comment):  Adds a single column to the table.
        - drop_existing():                              Drops the existing table and removes it from the ADFS file system.
        - save():                                       Saves the table to the specified database and location.
    """
    def __init__(self, db_name, table_name, spark, catalog = 'default', container = 'default'):
        """
        Initializes a DeltaTable object with the specified database name, table name, and SparkSession object.

        Args:
        - db_name (str): Required. The name of the database containing the table.
        - table_name (str): Required. The name of the table.
        - spark (pyspark.sql.SparkSession): Required. The SparkSession object to use for interacting with the table.
        """
        # Check if the database exists
        databases = [db.name for db in spark.catalog.listDatabases()]
        if db_name not in databases:
            raise ValueError(f"Database {db_name} not found in the SparkSession.")

        # Check if the table name is valid
        if not re.match(r'^[a-zA-Z0-9_]+$', table_name):
            raise ValueError(f"Invalid table name: {table_name}. Table names can only contain alphanumeric characters and underscores.")

        self._catalog = catalog
        self._db_name = db_name
        self._table_name = table_name
        self._spark = spark
        self._columns = []
        self._table_location = ''   # Table location is empty by default. needs to be set.
        self._options = {}
        self._primary_key = None
        self._partitioning = None
          
    def set_columns(self, columns):
        """
        Sets the column list for the table.

        Args:
        - columns (list of dictionaries): Required. A list of dictionaries, where each dictionary contains the column name, data type, and an optional comment.

        Returns:
        - self (DeltaTable): Returns the DeltaTable object.
        """
        # Check if columns is a list of dictionaries
        if not isinstance(columns, list) or not all(isinstance(col, dict) for col in columns):
            raise ValueError("The columns argument must be a list of dictionaries.")

        # Check if each dictionary in columns contains the required keys
        for col in columns:
            if not all(key in col for key in ["name", "data_type"]):
                raise ValueError("Each dictionary in the columns argument must contain the 'name' and 'data_type' keys.")

        # Add blank comments if not present in the dictionary
        for col in columns:
            if "comment" not in col:
                col["comment"] = ""

        # Check if 'DbxCreated', 'DbxUpdated', and 'IsDeleted' columns are present
        required_columns = ['DbxCreated', 'DbxUpdated', 'IsDeleted']
        existing_columns = [col['name'] for col in columns]
        missing_columns = [col for col in required_columns if col not in existing_columns]

        # Append the missing columns as the first three columns
        for col_name in reversed(missing_columns):
            columns.insert(0, {"name": col_name, "data_type": "timestamp" if col_name in ['DbxCreated', 'DbxUpdated'] else "int", "comment": ""})

        self._columns = columns
        return self
        
    def set_comment(self, comment):
        """
        Sets the comment for the table.

        Args:
        - comment (string): Required. A string containing the table comment.

        Returns:
        - self
        """
        if not isinstance(comment, str) or len(comment.strip()) < 20:
            raise ValueError("The comment argument must be a populated string of at least 20 characters long.")
        self._comment = comment
        return self

    def set_options(self, options):
        """
        Sets the options for the table.

        Args:
        - options (dict): Required. A dictionary containing the table options.

        Returns:
        - None
        """
        self._options = options
        return self
        
    def set_location(self, location):
        """
        Set the location of the table.

        Parameters:
        - location (str): The location where the table will be stored.

        Raises:
        - ValueError: If the location is not a non-empty string.
        """
        if not isinstance(location, str) or not location.strip():
            raise ValueError("The 'location' parameter must be a non-empty string.")

        self._table_location = location

        return self

    def set_primary_key(self, primary_key):
        """
        Sets the primary key for the table.

        Args:
        - primary_key (str): Required. The name of the primary key column.

        Returns:
        - None
        """
        self._primary_key = primary_key
        return self
        
    def set_partitioning(self, partitioning):
        """
        Sets the partitioning for the table.

        Args:
        - partitioning (str): Required. The name of the partitioning column.

        Returns:
        - None
        """
        self._partitioning = partitioning
        return self
        
    def add_column(self, column):
        """
            Adds a column to the table.

            Args:
            - column (dict): Required. A dictionary containing the column name, data type, and comment.

            Returns:
            - self
        """
        # Check if the column is in the right format
        if not isinstance(column, dict) or not all(key in column for key in ["name", "data_type", "comment"]):
            raise ValueError("The column argument must be a dictionary with 'name', 'data_type', and 'comment' keys.")

        # Check if the column name is at least 3 characters long
        if len(column["name"].strip()) < 3:
            raise ValueError("The 'name' value in the column argument must be at least 3 characters long.")

        # Check if the comment is not identical to the column name
        if column["name"].strip().lower() == column["comment"].strip().lower():
            raise ValueError("The 'comment' value in the column argument must not be identical to the column name.")

        # Check if the comment is at least 10 characters long
        if len(column["comment"].strip()) < 10:
            raise ValueError("The 'comment' value in the column argument must be at least 10 characters long.")
        
        # Check if the column already exists in the table
        existing_columns = [col["name"] for col in self._columns]
        if column["name"] in existing_columns:
            raise ValueError(f"The column '{column['name']}' already exists in the table.")

        # Alter the table to add the column
        alter_table_query = f"ALTER TABLE {self._catalog}.{self._db_name}.{self._table_name} ADD COLUMN {column['name']} {column['data_type']} COMMENT '{column['comment']}'"
        self._spark.sql(alter_table_query)

        # Add the column to the list of columns
        self._columns.append(column)

        return self

    def drop_existing(self):
        """
        Drops the existing table and removes it from the ADFS file system.

        Returns:
        - None
        """
        
        try:
            drop_sql_str = f"DROP TABLE IF EXISTS {self._db_name}.{self._table_name}"
            self._spark.sql(drop_sql_str)
                        
            dbutils = self._get_dbutils()

            dbutils.fs.rm(self._table_location, True)
            return self
        except Exception as e:
            print(f'Error during Table Drop: {e}')
            return False
            
    def create_table(self):
        """
        Saves the table to the specified database.

        Returns:
        - None
        """
        columns = ", ".join([f"{col['name']} {col['data_type']} COMMENT '{col['comment']}'" for col in self._columns])
        options = ", ".join([f"{key} = '{value}'" for key, value in self._options.items()])
        primary_key = f"tblproperties('primary_key'='{self._primary_key}')" if self._primary_key else ""
        partitioning = f"PARTITIONED BY ({self._partitioning})" if self._partitioning else ""
        table_comment = f'COMMENT "{self._comment}"' if self._comment else ""
        
        create_table_query = f"""
            CREATE TABLE IF NOT EXISTS {self._catalog}.{self._db_name}.{self._table_name} (
                {columns}
            )
            USING DELTA
            location "{self._table_location}"
            {partitioning}
            {primary_key}
            {options}
            {table_comment}
        """
        try:
            self._spark.sql(create_table_query)
            return self._show()
        except Exception as e:
            if "Table already exists" in str(e):
                existing_table_desc = self._spark.sql(f"describe detail {self._db_name}.{self._table_name}").toPandas()
                existing_table_desc_str = "\n".join([f"{row['col_name']}\t{row['data_type']}\t{row['comment']}" for _, row in existing_table_desc.iterrows()])
                error_msg = f"Table {self._db_name}.{self._table_name} already exists. Please add the 'drop_existing()' function to the create statement if you want to overwrite the existing table.\n\nExisting table description:\n{existing_table_desc_str}"
            else:
                error_msg = f"Error during table save: {e}"
            raise Exception(error_msg)

    def _show(self):
        """
        Returns a DataFrame object containing the description of the table.

        Returns:
        - df (pyspark.sql.DataFrame): A DataFrame object containing the description of the table.
        """
        describe_sql_str = f"DESCRIBE DETAIL {self._db_name}.{self._table_name}"
        return self._spark.sql(describe_sql_str)

    def _get_dbutils(self):
        """
        Private function to get a dbutils instance available allowing the drop_existing function to drop a table from ADLS

        Returns:
        - dbutils object
        """
        dbutils = None
        
        if self._spark.conf.get("spark.databricks.service.client.enabled") == "true":
            
            from pyspark.dbutils import DBUtils
            dbutils = DBUtils(self._spark)
        
        else:
            
            import IPython
            dbutils = IPython.get_ipython().user_ns["dbutils"]
        
        return dbutils