import os
import tempfile
from google.cloud import storage
from google.api_core.exceptions import NotFound

class GCSStorage:
    """
    A class to interact with Google Cloud Storage.

    This class provides methods to initialize a GCS client and fetch details of documents
    stored in a GCS bucket.

    Attributes:
        gcs_client (google.cloud.storage.Client): The GCS client instance for performing GCS operations.
    """
    def __init__(self):
        """
        Initialize GCS client for interacting with Google Cloud Storage.
        
        This method creates a GCS client instance using the Google Cloud Storage library,
        which allows for various operations on GCS buckets and objects.
        """
        self.gcs_client = storage.Client()
        print("Initialized Google Cloud Storage client for interacting with GCS.")

    def get_document_details(self, bucket_name, prefix='', file_type=None):
        """
        Fetches details of documents from a Google Cloud Storage bucket with a specific prefix and file type.

        This method retrieves the names, hashes, and sizes of documents in the specified
        GCS bucket, filtering by optional prefix and file type.

        Parameters:
            bucket_name (str): The name of the GCS bucket from which to retrieve documents.
            prefix (str, optional): The folder prefix within the GCS bucket to filter results. 
                                    Defaults to '' (all objects in the bucket).
            file_type (str, optional): The file extension (e.g., '.csv') to filter files. 
                                        Defaults to None (no filtering by file type).

        Returns:
            dict: A dictionary with document details including:
                  - document_name (str): The name of the document without extension.
                  - document_hash (str): The MD5 hash of the document (not directly available from GCS).
                  - document_size (int): The size of the document in bytes.
                  - file_type (str or None): The file type used for filtering (if provided).

        Raises:
            Exception: If the GCS request fails or if the bucket does not exist.

        Examples:
            gcp_service = GCSStorage()
            documents = gcp_service.get_document_details('my-bucket', prefix='data/', file_type='.csv')
            print(documents)

        Notes:
            - The method excludes files containing 'fhir_data' in their name.
            - To use this class, ensure you have the google-cloud-storage library installed and configured.
        """
        if not bucket_name:
            raise ValueError("Bucket name must not be empty.")

        print(f"Fetching document details from Google Cloud Storage: bucket={bucket_name}, prefix={prefix}, file_type={file_type}")

        document_details = {}
        try:
            # Get the bucket
            bucket = self.gcs_client.get_bucket(bucket_name)

            # List blobs in the specified prefix
            blobs = bucket.list_blobs(prefix=prefix)

            for blob in blobs:
                full_document_name = blob.name
                
                # Filter by file type and exclude unwanted files
                if (file_type is None or full_document_name.endswith(file_type)) and 'fhir_data' not in full_document_name:
                    base_document_name = os.path.splitext(os.path.basename(full_document_name))[0]
                    document_size = blob.size
                    document_hash = blob.md5_hash  # MD5 hash from GCS metadata

                    # Store document details
                    document_details[base_document_name] = {
                        'document_name': base_document_name,
                        'document_hash': document_hash,
                        'document_size': document_size,
                        'file_type': file_type
                    }

        except NotFound:
            print(f"Bucket '{bucket_name}' not found.")
            raise Exception(f"Bucket '{bucket_name}' does not exist.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise Exception(f"An unexpected error occurred: {e}")

        return document_details

    def count_documents_in_storage(self, bucket_name, prefix='', file_extension=None):
        """
        Counts total and unique documents of a specific type in a GCS bucket or within a specific prefix (folder).

        This method also returns a list of document names that match the specified criteria.

        Args:
            bucket_name (str): Name of the GCS bucket.
            prefix (str, optional): Prefix to list objects within a specific folder. 
                                    Defaults to '' (all objects).
            file_extension (str, optional): File extension to filter by (e.g., 'xml' for XML files).

        Returns:
            tuple: A tuple containing:
                - total_count (int): The total number of documents found.
                - unique_count (int): The count of unique documents based on MD5 hashes.
                - document_names (list): A list of document names that match the criteria.

        Raises:
            Exception: If there is an error accessing GCS or if the bucket does not exist.

        Examples:
            total, unique, documents = gcp_service.count_documents_in_storage('my-bucket', prefix='data/', file_extension='csv')
            print(total, unique, documents)
        """
        md5_hashes = set()
        total_count = 0
        document_names = []

        try:
            # Get the bucket
            bucket = self.gcs_client.get_bucket(bucket_name)

            # List blobs in the specified prefix
            blobs = bucket.list_blobs(prefix=prefix)

            # Ensure the file extension starts with a dot
            if file_extension and not file_extension.startswith('.'):
                file_extension = '.' + file_extension

            for blob in blobs:
                # Filter objects by file extension and exclude unwanted files
                if (file_extension is None or blob.name.endswith(file_extension)) and 'fhir_data' not in blob.name:
                    total_count += 1
                    md5_hashes.add(blob.md5_hash)  # Use MD5 hash for uniqueness
                    document_names.append(blob.name)  # Collect document names

        except NotFound:
            raise Exception(f"Bucket '{bucket_name}' does not exist.")
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {str(e)}")

        # Unique count is the size of the set of MD5 hashes
        unique_count = len(md5_hashes)
        return total_count, unique_count, document_names
    
    def key_exists_in_storage(self, bucket_name, object_key, processing_info=None, key_to_set=None):
        """
        Check if an object exists in a GCS bucket.

        This method checks for the existence of an object in the specified GCS bucket by
        attempting to retrieve its metadata. If the object exists, it can optionally store
        the object's MD5 hash in a provided dictionary.

        Args:
            bucket_name (str): The name of the GCS bucket to check.
            object_key (str): The key (name) of the object to check for existence.
            processing_info (dict, optional): A dictionary to store additional processing
                                                information. If provided, the MD5 hash of the
                                                object will be stored under `key_to_set`.
                                                Defaults to None.
            key_to_set (str, optional): The key under which to store the MD5 hash in
                                            `processing_info`. Defaults to None.

        Returns:
            bool: True if the object exists, False otherwise.

        Raises:
            Exception: If an error occurs during the request to GCS.

        Examples:
            exists = gcp_service.key_exists_in_storage('my-bucket', 'path/to/my/object.txt')
            print(exists)  # True or False

            processing_info = {}
            exists = gcp_service.key_exists_in_storage('my-bucket', 'path/to/my/object.txt', processing_info, 'md5_key')
            if exists:
                print(processing_info['md5_key'])  # Prints the MD5 hash of the object if it exists
        """
        try:
            # Get the bucket and blob
            bucket = self.gcs_client.get_bucket(bucket_name)
            blob = bucket.get_blob(object_key)

            if blob is not None:
                md5_hash = blob.md5_hash
                if processing_info and key_to_set:
                    processing_info[key_to_set] = md5_hash  # Store MD5 hash in processing_info
                return True
            else:
                print(f"Object with key '{object_key}' does not exist in bucket '{bucket_name}'.")
                return False
                
        except NotFound:
            print(f"Bucket '{bucket_name}' does not exist.")
            return False
        except Exception as e:
            print(f"Error checking for object '{object_key}' in bucket '{bucket_name}': {e}")
            return False

    def parquet_existence_check(self, bucket_name, patient_id, versions):
        """
        Check for the existence of a Parquet file in a GCS bucket for a given patient ID across specified versions.

        This function checks if the Parquet file associated with the specified patient ID 
        exists for any of the provided version numbers. It returns the highest version number 
        where the file is found.

        Args:
            bucket_name (str): The name of the GCS bucket where the Parquet files are stored.
            patient_id (str): The patient ID used to construct the GCS key for the file.
            versions (list): A list of version numbers (integers) to check for the existence of the file.

        Returns:
            int or None: The version number where the Parquet file exists, or None if no file is found.

        Raises:
            ValueError: If `versions` is empty or contains non-integer values.
            Exception: For any other errors encountered during GCS access.

        Examples:
            bucket = 'my-bucket'
            patient = 'patient_123'
            available_versions = [1, 2, 3]
            version_found = parquet_existence_check(bucket, patient, available_versions)
            if version_found is not None:
                print(f'File found for version: {version_found}')
            else:
                print('No file found for any version.')
        """
        # Validate input versions
        if not versions:
            raise ValueError("The 'versions' list must not be empty.")

        if not all(isinstance(v, int) for v in versions):
            raise ValueError("All elements in 'versions' must be integers.")

        # Sort the versions in descending order to check the latest versions first
        versions = sorted(versions, reverse=True)
        
        for version in versions:
            object_key = f"{patient_id}/v{version}/addr.parquet"  # Generate the GCS key for the file
            
            try:
                # Check if the blob exists in GCS
                if self.key_exists_in_storage(bucket_name, object_key):
                    print(f'Parquet exists for Version: {version}')
                    return version  # Return the first version where the file exists
            except Exception as e:
                print(f"Error checking for file existence in bucket '{bucket_name}' for key '{object_key}': {e}")

        return None

    def load_parquet_file(self, bucket_name, object_key, environment, project_root):
        """
        Load a Parquet file from GCS or a local path into a Pandas DataFrame.

        This function attempts to load a Parquet file from a GCS bucket or from a local
        directory, depending on the specified environment. If the loading fails, it returns an empty
        DataFrame with default columns.

        Args:
            bucket_name (str): The name of the GCS bucket.
            object_key (str): The GCS key (path) of the Parquet file to load.
            environment (str): The current environment ('local' or 'production').
            project_root (str): The root path of the project for local file access.

        Returns:
            pd.DataFrame: A DataFrame containing the data from the Parquet file, or an empty
                        DataFrame with default columns if loading fails.

        Raises:
            ValueError: If the object_key is invalid.
            Exception: For any other errors encountered during file loading.

        Examples:
            df = load_parquet_file('my-bucket', 'path/to/file.parquet', 'production', '/path/to/project')
        """
        default_columns = ['section_name', 'document_id']
        gcs_path = f'gs://{bucket_name}/{object_key}'

        # Validate the object key
        if not object_key:
            print("Error: The 'object_key' must not be empty.")
            raise ValueError("The 'object_key' must not be empty.")

        try:
            if environment == "local":
                file_path = f'{project_root}/data/{object_key}'
                print(f"Loading Parquet file from local path: {file_path}")
                df = pd.read_parquet(path=file_path)
            else:
                print(f"Loading Parquet file from GCS: {gcs_path}")
                df = pd.read_parquet(path=gcs_path)  # Use pandas to read from GCS directly
                
            return df

        except FileNotFoundError as e:
            print(f"Error: File not found: {e}")
            return pd.DataFrame(columns=default_columns)
        
        except Exception as e:
            print("Error: An unexpected error occurred while loading the Parquet file.")
            print(e)
            return pd.DataFrame(columns=default_columns)

    def load_json_from_storage(self, bucket_name, file_key):
            """
            Load a JSON file from GCS and return the parsed JSON object.

            This function retrieves a JSON file from the specified GCS bucket and parses its
            content into a Python dictionary. If the file does not exist or an error occurs,
            an empty dictionary is returned.

            Args:
                bucket_name (str): The name of the GCS bucket.
                file_key (str): The key (path) to the JSON file in GCS.

            Returns:
                dict: The parsed JSON object, or an empty dictionary if an error occurs.

            Raises:
                ValueError: If the file_key is empty.

            Examples:
                json_data = load_json_from_gcs('my-bucket', 'path/to/file.json')
            """
            # Validate the file key
            if not file_key:
                print("Error: The 'file_key' must not be empty.")
                raise ValueError("The 'file_key' must not be empty.")

            try:
                # Retrieve the bucket and the blob (file) from GCS
                bucket = self.storage_client.bucket(bucket_name)
                blob = bucket.blob(file_key)

                # Check if the blob exists
                if not blob.exists():
                    print(f"The specified key '{file_key}' does not exist in the bucket '{bucket_name}'.")
                    return {}

                # Read the content of the file and parse it as JSON
                json_content = blob.download_as_text()
                json_data = json.loads(json_content)
                return json_data

            except Exception as e:
                print(f"An unexpected error occurred while loading the JSON file: {e}")
                return {}
            
    def download_folder_from_storage(self, bucket_name, folder_prefix, local_folder):
        """
        Download all files from a specified GCS folder to a local directory.

        This function retrieves all objects in the specified GCS folder (prefix) and
        downloads them to the given local folder. If the local folder does not exist,
        it will be created.

        Args:
            bucket_name (str): The name of the GCS bucket.
            folder_prefix (str): The prefix (folder path) in GCS from which to download files.
            local_folder (str): The local directory to which files will be downloaded.

        Raises:
            ValueError: If the bucket_name or folder_prefix is empty.
            Exception: If any unexpected error occurs during the download process.

        Examples:
            download_gcs_folder('my-bucket', 'path/to/folder/', '/local/path/')
        """
        # Validate input parameters
        if not bucket_name:
            raise ValueError("Bucket name must not be empty.")
        if not folder_prefix:
            raise ValueError("Folder prefix must not be empty.")

        print(f"Starting download from GCS bucket '{bucket_name}' with prefix '{folder_prefix}' to local folder '{local_folder}'.")

        # Ensure the local folder exists
        os.makedirs(local_folder, exist_ok=True)

        try:
            # List objects in the specified GCS folder
            bucket = self.storage_client.bucket(bucket_name)
            blobs = bucket.list_blobs(prefix=folder_prefix)

            total_files = 0
            for blob in blobs:
                total_files += 1
            
            if total_files > 0:
                print(f"Found {total_files} files in GCS folder '{folder_prefix}'. Beginning download...")

                # Reset the blobs generator to iterate over the blobs again
                blobs = bucket.list_blobs(prefix=folder_prefix)

                # Loop through all objects in the GCS folder
                for idx, blob in enumerate(blobs, start=1):
                    file_name = os.path.basename(blob.name)  # Get the file name from the GCS blob name
                    local_file_path = os.path.join(local_folder, file_name)  # Create the local file path

                    # Download the file from GCS to the local folder
                    print(f"Downloading file {idx}/{total_files}: '{file_name}' to '{local_file_path}'...")
                    blob.download_to_filename(local_file_path)

                print(f"Download completed. {total_files} files downloaded to '{local_folder}'.")

            else:
                print(f"No files found in the specified GCS folder '{folder_prefix}'.")

        except Exception as e:
            print(f"An error occurred during the download process: {e}")       

    def generate_signed_url(self, bucket_name, object_key, expiration_time=3600):
        """
        Generate a signed URL to retrieve an object from a GCS bucket.

        This function creates a signed URL that allows users to retrieve a specific 
        object from a GCS bucket without requiring direct access to the Google Cloud credentials.
        
        Parameters:
        - bucket_name (str): The name of the GCS bucket.
        - object_key (str): The key (file path) of the object in the GCS bucket.
        - expiration_time (int, optional): The time in seconds for the signed URL 
        to remain valid (default is 3600 seconds = 1 hour).

        Returns:
        - str: A signed URL for accessing the specified GCS object.

        Raises:
        - ValueError: If either bucket_name or object_key is not provided.
        - Exception: If an error occurs when generating the signed URL.

        Example:
            url = generate_signed_url('my-bucket', 'folder/myfile.txt', expiration_time=1800)
            print(url)

        Notes:
        - Ensure that the Google Cloud credentials used have sufficient permissions to generate
        signed URLs for GCS objects.
        """
        
        # Ensure bucket_name and object_key are provided
        if not bucket_name:
            raise ValueError("Bucket name is required.")
        if not object_key:
            raise ValueError("Object key is required.")

        try:
            # Get the bucket and blob
            bucket = self.storage_client.bucket(bucket_name)
            blob = bucket.blob(object_key)

            # Generate the signed URL
            pre_signed_url = blob.generate_signed_url(
                version='v4',
                expiration=timedelta(seconds=expiration_time),
                method='GET'  # The method can be 'GET' or 'PUT'
            )
            return pre_signed_url

        except Exception as e:
            print(f"An error occurred while generating the signed URL: {e}")
            return None

    def save_data_and_get_signed_url(self, bucket_name, file_name, result, environment, local_dir_path):
        """
        Save a JSON object either locally or to GCS, and generate a signed URL for the GCS object.

        Parameters:
        - bucket_name (str): The name of the GCS bucket where the file will be stored.
        - file_name (str): The name (key) of the file to save in GCS or locally.
        - result (dict): The JSON object to save.
        - environment (str): The current environment ('local' or 'gcs').
        - local_dir_path (str): The local directory path to save the file if the environment is 'local'.

        Returns:
        - tuple:
            - If environment is 'local':
              ('local', None)
            - If environment is 'gcs':
              - str: Signed URL for accessing the file in GCS.
              - str: The file's ETag (hash) from GCS.
              - int: The file's size in bytes.
        
        Raises:
        - ValueError: If required parameters are missing or invalid.
        - Exception: If an error occurs while uploading to or retrieving from GCS.

        Example:
            result_data = {"key": "value"}
            url, file_hash, file_size = save_data_and_get_signed_url(
                'my-bucket', 'data/result.json', result_data, environment='gcs', local_dir_path='/tmp')
        """
        
        # Handle local environment
        if environment == 'local':
            try:
                local_path = f"{local_dir_path}/output/{'/'.join(file_name.split('/')[:-1])}"
                Path(local_path).mkdir(parents=True, exist_ok=True)
                with open(f'{local_dir_path}/output/{file_name}', 'w', encoding='utf-8') as f:
                    json.dump(result, f, ensure_ascii=False)
                return 'local', None
            
            except Exception as e:
                print(f"Error saving file locally: {e}")
                return None, None
        
        # Handle GCS environment
        try:
            bucket = self.storage_client.bucket(bucket_name)
            blob = bucket.blob(file_name)

            # Upload the JSON object to GCS
            blob.upload_from_string(json.dumps(result), content_type='application/json')

            # Get the file's ETag (hash)
            file_hash = blob.etag.strip('"')

            # Get the file size from the blob
            file_size = blob.size

            # Generate the signed URL
            signed_url = blob.generate_signed_url(version='v4', expiration=timedelta(hours=1), method='GET')

            # Return the signed URL, file hash, and file size
            return signed_url, file_hash, file_size

        except Exception as e:
            print(f"An error occurred while saving to GCS: {e}")
            return None, None, None

    def download_ml_models(self, processing_info, bucket_name, gcs_dir_path, local_dir_path):
        """
        Downloads all model files for a specific version from a GCS bucket.

        Args:
        - processing_info (dict): Dictionary containing processing metadata, including model version.
        - bucket_name (str): Name of the GCS bucket.
        - gcs_dir_path (str): Path in the GCS bucket where models are stored (e.g., 'Summary_Models/').
        - local_dir_path (str): Local directory where the files will be downloaded.

        Returns:
        - bool: True if any model files were downloaded, False if no download was required.
        """
        model_download_required = False

        # Ensure the local directory exists
        try:
            os.makedirs(local_dir_path, exist_ok=True)
        except Exception as e:
            print(f"Error creating local directory '{local_dir_path}': {e}")
            return False

        # Get the GCS bucket
        bucket = self.storage_client.bucket(bucket_name)

        # List objects in the specified GCS directory
        blobs = bucket.list_blobs(prefix=gcs_dir_path)

        # Loop through the GCS objects and download relevant files
        for blob in blobs:
            key = blob.name
            
            # Check if the key matches the specified version
            if f"/{processing_info['summary_version']}/" in key:
                filename = os.path.basename(key)  # Extract filename from key
                local_file_path = os.path.join(local_dir_path, filename)
                
                # Ensure local directories exist
                try:
                    os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
                except Exception as e:
                    print(f"Error creating directories for '{local_file_path}': {e}")
                    continue
                
                # Check if the file already exists locally
                if not os.path.exists(local_file_path):
                    try:
                        # Download the file from GCS
                        print(f"Downloading {filename} from GCS...")
                        blob.download_to_filename(local_file_path)
                        print(f"Downloaded '{filename}' to '{local_file_path}'.")
                        model_download_required = True
                    except Exception as e:
                        print(f"Error downloading '{filename}': {e}")
                else:
                    print(f"File '{filename}' already exists locally, skipping download.")
        
        return model_download_required

    def load_json_metadata(self, person_id, version, json_metadata_path):
            """
            Loads metadata for a person from three parquet files: trident changes, MR metadata, and HR metadata.

            Args:
                person_id (str): The ID of the person.
                version (str): The version of the metadata.
                json_metadata_path (str): The base GCS path where JSON metadata is stored.

            Returns:
                tuple: Three DataFrames (trident_changes_metadata_df, hr_metadata_df, mr_metadata_df)
            """
            # Define GCS object keys
            trident_changes_metadata_object_key = f"{version}/trident_changes/{person_id}_trident-changes.parquet"
            mr_object_key = f"{version}/mr_metadata_info/{person_id}_mr-metadata.parquet"
            hr_object_key = f"{version}/hr_metadata_info/{person_id}_hr-metadata.parquet"
            
            # Define expected columns for each DataFrame
            trident_changes_columns = ['person_id', 'document_id', 'org_id', 'org_name', 'section_name', 'section_code', 
                                    'original_column', 'destination_column', 'changes_type', 'overlapping_count', 
                                    'predicted_scores', 'row_count', 'rows_below_95', 'top_5_predictions', 
                                    'merge_status', 'is_unknown', 'create_date']
            mr_metadata_columns = ['document_id', 'section_name', 'row_count', 'create_date']
            hr_metadata_columns = ['document_id', 'section_name', 'row_count', 'unknown_section', 'create_date']
            
            # Helper function to load a parquet file or return an empty DataFrame
            def load_parquet_or_empty(gcs_path, columns):
                try:
                    # Check if the file exists in GCS
                    blob = self.storage_client.bucket(json_metadata_path).blob(gcs_path)
                    if blob.exists():
                        return pd.read_parquet(blob.open("rb"))  # Load parquet file from GCS
                    else:
                        print(f"File '{gcs_path}' does not exist in GCS.")
                        return pd.DataFrame(columns=columns)
                except Exception as e:
                    print(f"Error loading parquet file '{gcs_path}': {e}")
                    return pd.DataFrame(columns=columns)

            # Load metadata
            trident_changes_metadata_df = load_parquet_or_empty(trident_changes_metadata_object_key, trident_changes_columns)
            mr_metadata_df = load_parquet_or_empty(mr_object_key, mr_metadata_columns)
            hr_metadata_df = load_parquet_or_empty(hr_object_key, hr_metadata_columns)

            return trident_changes_metadata_df, hr_metadata_df, mr_metadata_df

    def _save_dataframe_to_gcs(self, dataframe, bucket_name, gcs_path):
        """
        Save a DataFrame to a specified path in Google Cloud Storage as a parquet file.

        Args:
            dataframe (pd.DataFrame): The DataFrame to save.
            bucket_name (str): The name of the GCS bucket.
            gcs_path (str): The GCS path where the file will be stored.
        """
        bucket = self.storage_client.bucket(bucket_name)
        blob = bucket.blob(gcs_path)
        
        # Save DataFrame to a temporary file before uploading to GCS
        with tempfile.NamedTemporaryFile(delete=True) as tmp_file:
            dataframe.to_parquet(tmp_file.name)
            tmp_file.seek(0)  # Move to the beginning of the file
            
            # Upload the temporary file to GCS
            blob.upload_from_file(tmp_file, content_type='application/octet-stream')
            print(f"Saved '{gcs_path}' to GCS.")
    
    def save_json_metadata(self, processing_info, trident_changes_metadata_df, hr_metadata_df, mr_metadata_df, json_metadata_path):
        """
        Save metadata DataFrames to GCS as parquet files.

        Args:
            processing_info (dict): Information about the processing, including 'summary_version' and 'person_id'.
            trident_changes_metadata_df (pd.DataFrame): DataFrame containing trident changes metadata.
            hr_metadata_df (pd.DataFrame): DataFrame containing HR metadata.
            mr_metadata_df (pd.DataFrame): DataFrame containing MR metadata.
            json_metadata_path (str): The base GCS path where JSON metadata is stored.
        """
        summary_version = processing_info['summary_version']
        person_id = processing_info['person_id']
        
        # Define GCS paths for saving the parquet files
        trident_changes_gcs_path = f"{summary_version}/trident_changes/{person_id}_trident-changes.parquet"
        hr_gcs_path = f"{summary_version}/hr_metadata_info/{person_id}_hr-metadata.parquet"
        mr_gcs_path = f"{summary_version}/mr_metadata_info/{person_id}_mr-metadata.parquet"

        try:
            # Save DataFrames to GCS as parquet files
            self._save_dataframe_to_gcs(trident_changes_metadata_df, json_metadata_path, trident_changes_gcs_path)
            self._save_dataframe_to_gcs(hr_metadata_df, json_metadata_path, hr_gcs_path)
            self._save_dataframe_to_gcs(mr_metadata_df, json_metadata_path, mr_gcs_path)

            print(f"Metadata saved for {person_id} in version {summary_version}.")
            
        except Exception as e:
            print(f"An error occurred while saving metadata for {person_id}: {e}")

    def add_unknown_sections(self, bucket_name, prefix, section_column_df):
        """
        Add unknown sections from GCS parquet files to the section_column_df DataFrame.

        Args:
            bucket_name (str): The name of the GCS bucket.
            prefix (str): The GCS prefix to filter the objects.
            section_column_df (pd.DataFrame): DataFrame containing existing section names.

        Returns:
            pd.DataFrame: Updated DataFrame including unknown sections.
        """
        try:
            # Initialize GCS client
            client = storage.Client()
            bucket = client.get_bucket(bucket_name)
            blobs = bucket.list_blobs(prefix=prefix)

            for blob in blobs:
                if blob.name.endswith('_text.parquet'):
                    section_file = blob.name.split('/')[-1].replace('.parquet', '')

                    # Check if the section file is already in the DataFrame
                    if section_file not in section_column_df['hr_table_name'].values:
                        try:
                            section_name, codes = section_file.split('_(')
                            codes = codes.split(')_text')[0]
                        except ValueError:
                            section_name = section_file.replace('_text', '')
                            codes = ''

                        # Add the unknown section to the DataFrame
                        section_column_df.loc[len(section_column_df)] = {
                            'section_name': f"unknown {section_name}",
                            'hr_table_name': section_file,
                            'codes': json.dumps([codes])
                        }

            return section_column_df

        except Exception as e:
            print(f"An error occurred while adding unknown sections: {e}")
            return section_column_df