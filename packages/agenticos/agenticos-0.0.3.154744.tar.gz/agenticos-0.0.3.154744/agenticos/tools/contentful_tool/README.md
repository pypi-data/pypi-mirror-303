# ContentfulTool

## Overview

`ContentfulTool` is a custom tool build for CrewAI that interacts with the Contentful API to manage taxonomies by creating concepts and sub-concepts in a hierarchical structure. This tool automates the process of uploading and managing content structures in Contentful using an API-based approach, making it ideal for large-scale content management and taxonomy creation.

The tool integrates Pydantic models to ensure schema validation and leverages requests with retry policies to handle transient API errors.

## Features

- **Create Concepts**: Automatically create concepts and their sub-concepts in Contentful.
- **Recursive Concept Creation**: Supports the creation of nested taxonomies.
- **Session Management**: Utilizes HTTP session management with retry policies to ensure robust communication with the Contentful API.
- **Schema Validation**: Ensures that the data conforms to the expected structure using Pydantic validation.
- **API Interaction**: Seamlessly integrates with Contentful's Management API.

## Environment Variables

The ContentfulTool requires two environment variables to interact with the Contentful API:

	•	CONTENTFUL_ORGANIZATION_ID: Your Contentful Organization ID.
	•	CONTENTFUL_BEARER_TOKEN: The bearer token for Contentful API access.

You can export these variables in your shell:

```bash
export CONTENTFUL_ORGANIZATION_ID=your_org_id
export CONTENTFUL_BEARER_TOKEN=your_bearer_token
```

Or include them in your .env file.

## Roadmap

Currently only one specific endpoint ot the powerful Contentful API is covered to create taxonomies through agents in Contentful. It's on our roadmap to support way more endpoints of the Conteful APIs, to allow agents to work with Contentful, by not only consuming content, but also publishing and managing it. 
