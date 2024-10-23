import hashlib
import requests
from datetime import datetime
import base64 

class GitLabManager:
    def __init__(self, aic_instance, gitlab_token, gitlab_namespace, gitlab_base_url='https://git.autodatacorp.org/api/v4', use_hash_comparison=True):
        self.aic = aic_instance
        self.gitlab_base_url = gitlab_base_url
        self.gitlab_namespace = gitlab_namespace
        self.use_hash_comparison = use_hash_comparison
        self.gitlab_token = gitlab_token
        self.headers = {
            'Private-Token': self.gitlab_token,
            'Content-Type': 'application/json'
        }

        # Ensure the subgroup exists or use the existing one based on the workspace name
        self.workspace_name = aic_instance.workspace
        self.subgroup_id = self.ensure_correct_subgroup(self.workspace_name)


    def get_token_expiration_date(self):
        """Retrieves the expiration date of the GitLab token."""
        url = f"{self.gitlab_base_url}/personal_access_tokens"
        try:
            response = requests.get(url, headers=self.headers, params={'name': 'fusion-push', 'revoked': 'false'})
            response.raise_for_status()
            tokens = response.json()
            for token in tokens:
                if token['name'] == 'fusion-push' and not token.get('revoked', True):
                    expiration_date = token['expires_at']
                    if 'T' in expiration_date:
                        return datetime.strptime(expiration_date, '%Y-%m-%dT%H:%M:%S.%fZ')
                    else:
                        return datetime.strptime(expiration_date, '%Y-%m-%d')
            print("No matching token found in the response.")
        except requests.exceptions.HTTPError as err:
            print(f"Error checking token expiration: {err}")
            print(f"Response: {response.text}")
        return None

    def check_token_expiration(self):
        """Checks and reports the token expiration date."""
        expiration_date = self.get_token_expiration_date()
        if expiration_date:
            days_left = (expiration_date - datetime.now()).days
            print(f"GitLab Token expires in {days_left} days.")
            if days_left < 7:
                print("Token is expiring soon. Consider updating the token.")
        else:
            print("Failed to retrieve token expiration date.")


    def generate_hash(self, content):
        """Generates a hash for the given content, ensuring consistent encoding and stripping."""
        # Strip unnecessary whitespace and normalize line endings
        normalized_content = content.strip().replace('a\r\n', '\n').replace('\r', '\n')
        return hashlib.md5(normalized_content.encode('utf-8')).hexdigest()


    def get_existing_file_content(self, repo_name, file_name):
        """Fetches the existing content of a file from the specified repository in GitLab."""
        project_url = f"{self.gitlab_base_url}/projects/{repo_name.replace('/', '%2F')}/repository/files/{file_name}?ref=main"
        try:
            response = requests.get(project_url, headers=self.headers)
            if response.status_code == 200:
                file_info = response.json()
                # Decode the base64 content
                encoded_content = file_info.get('content')
                if encoded_content:
                    # Decode, normalize line endings, and strip content
                    return base64.b64decode(encoded_content).decode('utf-8').strip().replace('\r\n', '\n').replace('\r', '\n')
                else:
                    print(f"No content found for {file_name} in repository {repo_name}")
                    return None
            else:
                print('No current repository found.')
                return None
        except Exception as e:
            print(f"Error fetching existing file content: {str(e)}")
            return None
        
        
    def push_file_to_repo(self, repo_name, file_name, file_content):
        """Pushes a file to the specified repository in GitLab, only if the content has changed."""
        repo_path = f"{self.subgroup_id}/{repo_name.replace(' ', '_')}"
        print(f"Checking if repository exists: {repo_path}")


        # Check if the repository exists; create if it does not exist
        if not self.repository_exists(repo_path):
            print(f"Repository {repo_name} does not exist. Creating repository.")
            created_repo = self.create_repository(repo_name)
            if not created_repo:
                print(f"Failed to create repository {repo_name}. Cannot proceed with pushing the file.")
                return  # Exit early since repository creation failed
            else:
                print(f"Repository {repo_name} created successfully. Skipping content comparison as it's a new repo.")
                # Directly push the file without comparison as it is a new repo
                self.push_new_file(repo_path, file_name, file_content)
                return

        # Proceed to check for file content only if the repository exists
        elif self.use_hash_comparison:
            existing_content = self.get_existing_file_content(repo_path, file_name)
            if existing_content:
                existing_hash = self.generate_hash(existing_content)
                current_hash = self.generate_hash(file_content)
                
                # Compare hashes
                if existing_hash == current_hash:
                    print(f"No changes detected for {file_name}. Skipping push.")
                    return  # Exit early if no changes detected
        # Push the file if it's either a new repository or the content has changed
        self.push_new_file(repo_path, file_name, file_content)

    def ensure_correct_subgroup(self, workspace):
        # Add a check to see if the namespace is 'pin/pin-analytics/pin-fusion-2.0/pipelines'
        if self.gitlab_namespace == 'pin/pin-analytics/pin-fusion-2.0/pipelines':
            print(f"Resolving subgroup for workspace: {workspace}")  # Debug print
            if workspace == 'PIN FUSION 2.0':
                return 'pin/pin-analytics/pin-fusion-2.0/pipelines/production'
            elif workspace == 'PIN FUSION 2.0 QA':
                return 'pin/pin-analytics/pin-fusion-2.0/pipelines/qa'
            else:
                print(f"Workspace '{workspace}' not recognized. Proceeding with default namespace.")
                return self.gitlab_namespace
        else:
            # If the namespace is not the special case, return the namespace as is.
            return self.gitlab_namespace


    def create_repository(self, repo_name):
        """Creates a new repository in the specified subgroup."""
        url = f"{self.gitlab_base_url}/projects"
        data = {
            'name': repo_name,
            'namespace_id': self.get_subgroup_id(),  # Ensure subgroup ID is fetched
            'visibility': 'private'
        }
        try:
            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status()
            print(f"Repository {repo_name} created successfully in subgroup {self.subgroup_id}.")
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"Failed to create repository {repo_name}: {response.status_code}")
            print(f"Response: {response.text}")
            return None

    def get_subgroup_id(self):
        """Fetch the GitLab subgroup ID based on the namespace path."""
        subgroup_url = f"{self.gitlab_base_url}/groups/{self.subgroup_id.replace('/', '%2F')}"
        try:
            response = requests.get(subgroup_url, headers=self.headers)
            response.raise_for_status()
            return response.json()['id']
        except requests.exceptions.HTTPError as err:
            print(f"Failed to retrieve subgroup ID for {self.subgroup_id}: {response.status_code}")
            print(f"Response: {response.text}")
            raise ValueError(f"Could not retrieve subgroup ID for namespace {self.subgroup_id}")
    
    def get_namespace_id(self):
        """Retrieves the namespace ID for the current GitLab namespace."""
        url = f"{self.gitlab_base_url}/namespaces?search={self.gitlab_namespace}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            namespaces = response.json()
            for namespace in namespaces:
                if namespace['full_path'] == self.gitlab_namespace:
                    return namespace['id']
        print(f"Namespace '{self.gitlab_namespace}' not found.")
        return None

    def repository_exists(self, repo_path):
        """Check if the repository exists in GitLab."""
        project_url = f"{self.gitlab_base_url}/projects/{repo_path.replace('/', '%2F')}"
        try:
            response = requests.get(project_url, headers=self.headers)
            return response.status_code == 200
        except requests.exceptions.HTTPError as err:
            print(f"Error checking repository existence: {err}")
            return False
        
    def push_new_file(self, repo_path, file_name, file_content):
        """Pushes or updates a file in the specified repository in GitLab."""
        project_url = f"{self.gitlab_base_url}/projects/{repo_path.replace('/', '%2F')}/repository/files/{file_name}"
        data = {
            'branch': 'main',
            'content': file_content,
            'commit_message': f"Update {file_name} - {datetime.now().strftime('%Y-%m-%d')}"
        }

        try:
            # Attempt to create or update the file
            response = requests.post(project_url, headers=self.headers, json=data)
            if response.status_code == 201:
                print(f"Successfully created {file_name} in repository: {repo_path}")
            elif response.status_code == 400 and "already exists" in response.text:
                # File exists; try updating instead
                response = requests.put(project_url, headers=self.headers, json=data)
                if response.status_code == 200:
                    print(f"Successfully updated {file_name} in repository: {repo_path}")
                else:
                    print(f"Failed to update {file_name} in repository: {repo_path}")
                    print(f"Response: {response.text}")
            else:
                print(f"Failed to push {file_name} to repository: {repo_path}")
                print(f"Response: {response.text}")
        except Exception as e:
            print(f"Error pushing file to GitLab: {str(e)}")
            
            
            
