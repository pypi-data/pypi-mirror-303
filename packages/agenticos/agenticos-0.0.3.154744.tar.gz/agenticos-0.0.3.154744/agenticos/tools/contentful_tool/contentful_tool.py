import logging
import os
from typing import Any, List, Optional, Type

import requests
from crewai_tools import BaseTool
from pydantic import BaseModel, Field, PrivateAttr, field_validator
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry  # type: ignore


# Represents an individual concept in the taxonomy
class Concept(BaseModel):
    name: str = Field(..., description="The name of the concept")
    description: str = Field(..., description="A description of the concept")
    sub_concepts: Optional[List["Concept"]] = Field(
        None, description="A list of sub-concepts under this concept"
    )

    # Ensures that 'name' and 'description' fields are not empty or just whitespace
    @field_validator("name", "description")
    def validate_not_empty(cls, value):
        if not value.strip():
            raise ValueError("Field cannot be empty")
        return value


# Represents the overall taxonomy schema, which contains a root concept
class TaxonomySchema(BaseModel):
    root_concept: Concept = Field(..., description="The root concept of the taxonomy")


# Defines the input schema for the Contentful tool using Pydantic for validation
class ContentfulToolSchema(BaseModel):
    taxonomy: TaxonomySchema = Field(
        ..., description="The taxonomy structure, following the TaxonomySchema format."
    )

    # Validates that the root concept has a non-empty name
    @field_validator("taxonomy")
    def validate_taxonomy(cls, value):
        if not value.root_concept.name.strip():
            raise ValueError("Root concept must have a name.")
        return value


# Main tool class that interacts with the Contentful API
class ContentfulTool(BaseTool):
    name: str = "Contentful"  # Name of the tool
    description: str = "A tool to save a taxonomy to Contentful."
    args_schema: Type[BaseModel] = ContentfulToolSchema  # Input schema definition

    # Fields that hold Contentful API credentials, retrieved from environment variables
    organization_id: str = Field(
        default_factory=lambda: os.getenv("CONTENTFUL_ORGANIZATION_ID")
    )
    bearer_token: str = Field(
        default_factory=lambda: os.getenv("CONTENTFUL_BEARER_TOKEN")
    )
    base_url: str = "None"  # Base URL for API requests (set during initialization)
    headers: Optional[dict] = None  # API request headers (set during initialization)

    # A private session object used to handle HTTP requests
    _session: requests.Session = PrivateAttr()

    # Constructor method for the tool, initializes the session and checks required credentials
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Ensure that required environment variables are set
        if not self.organization_id or not self.bearer_token:
            raise ValueError(
                "Environment variables CONTENTFUL_ORGANIZATION_ID and CONTENTFUL_BEARER_TOKEN must be set."
            )

        # Construct the base URL for interacting with the Contentful API
        self.base_url = f"https://api.contentful.com/organizations/{self.organization_id}/taxonomy/concepts"

        # Set up API request headers, including authorization and content type
        self.headers = {
            "Authorization": f"Bearer {self.bearer_token}",
            "Content-Type": "application/vnd.contentful.management.v1+json",
        }

        # Initialize the session with retry logic
        self._session = self._initialize_session()

    # Initializes an HTTP session with retry behavior for handling transient errors
    def _initialize_session(self) -> requests.Session:
        session = requests.Session()
        # Retry policy: retry up to 3 times with exponential backoff for certain status codes
        retry = Retry(
            total=3, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504]
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount("https://", adapter)  # Apply retry policy to HTTPS requests
        return session

    # Main method for running the tool, creates taxonomy concepts recursively in Contentful
    def _run(self, taxonomy: TaxonomySchema, **kwargs: Any) -> str:
        try:
            # Initiates the creation of the root concept, which cascades to sub-concepts
            self.create_concept(taxonomy.root_concept)
            return "Concepts successfully created in Contentful."
        except Exception as e:
            # Logs error details for debugging if something goes wrong
            logging.error(f"An error occurred: {str(e)}")
            logging.error(f"Taxonomy data: {taxonomy}")
            return f"An error occurred: {str(e)}"

    # Recursive function to create a concept and its sub-concepts in Contentful
    def create_concept(self, data: Concept, parent_id=None):
        """
        Recursive function to create a concept and its sub-concepts in Contentful.
        """
        if not self.base_url:
            raise ValueError("Base URL is not set.")

        # Prepare the data for the API request
        concept_data = self._prepare_concept_data(data, parent_id)

        # Send the API request to create the concept
        response = self._session.post(
            self.base_url, headers=self.headers, json=concept_data
        )

        # If the creation is successful, handle the response and recursively create sub-concepts
        if response.status_code == 201:
            concept_id = response.json()["sys"]["id"]
            logging.info(f"Created concept '{data.name}' with ID: {concept_id}")

            # If there are sub-concepts, recursively create each of them under this concept
            if data.sub_concepts:
                for sub_concept in data.sub_concepts:
                    self.create_concept(sub_concept, parent_id=concept_id)
        else:
            # Raise an error if the concept creation fails, logging the response details
            raise RuntimeError(
                f"Failed to create concept '{data.name}': {response.status_code} - {response.text}"
            )

    # Helper function to prepare the concept data in the format required by the Contentful API
    def _prepare_concept_data(self, data: Concept, parent_id=None) -> dict:
        """
        Prepares the concept data payload for the API request.
        """
        # Basic concept information, including name and description
        concept_data = {
            "prefLabel": {"en-US": data.name},  # Preferred label
            "altLabels": {"en-US": []},  # Alternate labels (empty for now)
            "hiddenLabels": {"en-US": []},  # Hidden labels (empty for now)
            "notations": [],  # Notations (empty for now)
            "note": {"en-US": data.description},  # Description
            "changeNote": {"en-US": ""},  # Change note (empty for now)
            "definition": {
                "en-US": data.description
            },  # Definition (same as description for now)
            "editorialNote": {"en-US": ""},  # Editorial note (empty for now)
            "example": {"en-US": ""},  # Example (empty for now)
            "historyNote": {"en-US": ""},  # History note (empty for now)
            "scopeNote": {"en-US": ""},  # Scope note (empty for now)
        }

        # If there's a parent concept, add a reference to it in the "broader" field
        if parent_id:
            concept_data["broader"] = [
                {"sys": {"type": "Link", "linkType": "Concept", "id": parent_id}}
            ]

        return concept_data
