# Pedigree Pro API

A Python Flask REST API for managing dog pedigree data with MongoDB cloud integration. This API provides endpoints for searching dogs and retrieving pedigree lineage information.

## Features

- **Dog Search**: Advanced search functionality with pagination and sorting
- **Pedigree Retrieval**: Hierarchical pedigree tree data for ancestral lineage
- **MongoDB Integration**: Cloud-based MongoDB for scalable data storage
- **RESTful Design**: Clean, intuitive API endpoints

## Prerequisites

- Python 3.7 or higher
- MongoDB Atlas account (or local MongoDB instance)
- pip (Python package installer)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shannonaswanson/pedigreeproapi.git
   cd pedigreeproapi
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the project root:
   ```
   MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/database
   PORT=5001
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```

The API will be available at `http://localhost:5001`

## API Endpoints

### POST /search

Search for dogs with advanced filtering, pagination, and sorting capabilities.

**Request Body:**
```json
{
  "registrationNumber": "DN61764904",    // Exact match (optional)
  "name": "Fido",                       // Partial, case-insensitive match (optional)
  "isMale": true,                       // true for male, false for female (optional)
  "breed": "Labrador Retriever",        // Exact match (optional)
  "startWhelpDate": "2023-01-01",       // Start of date range YYYY-MM-DD (optional)
  "endWhelpDate": "2023-12-31",         // End of date range YYYY-MM-DD (optional)
  "orderBy": "dogName",                 // Sort field: registrationNumber, dogName, whelpDate, breed (optional)
  "orderDirection": "asc",              // Sort direction: asc or desc (optional)
  "page": 1,                            // Page number (default: 1)
  "pageSize": 25                        // Results per page (default: 10, max: 1000)
}
```

**Response:**
```json
{
  "dogs": [...],                        // Array of dog objects
  "pagination": {
    "currentPage": 1,
    "pageSize": 25,
    "totalCount": 150,
    "totalPages": 6,
    "hasNext": true,
    "hasPrev": false
  }
}
```

**Example:**
```bash
curl -X POST http://localhost:5001/search \
  -H "Content-Type: application/json" \
  -d '{"name": "Moon Fairy", "breed": "Border Collie", "page": 1, "pageSize": 25}'
```

### GET /pedigree

Retrieve a dog's complete pedigree tree including ancestral lineage.

**Query Parameters:**
- `_id` (required): MongoDB ObjectId of the dog

**Response:**
Returns a hierarchical array representing the pedigree tree:
```json
[
  {
    "id": "dog_nameKey",               // Primary dog (root of tree)
    "dogName": "Champion Dog",
    "registrationNumber": "DN123",
    "parentId": null,                  // Root has no parent
    "sireNameKey": "sire_nameKey",
    "damNameKey": "dam_nameKey"
    // ... other dog properties
  },
  {
    "id": "sire_nameKey",              // Sire of primary dog
    "dogName": "Sire Name",
    "parentId": "dog_nameKey",         // References primary dog
    "sex": "male"
    // ... sire's ancestry continues
  },
  {
    "id": "dam_nameKey",               // Dam of primary dog
    "dogName": "Dam Name", 
    "parentId": "dog_nameKey",         // References primary dog
    "sex": "female"
    // ... dam's ancestry continues
  }
  // ... additional ancestors with parentId references
]
```

**Example:**
```bash
curl -X GET "http://localhost:5001/pedigree?_id=6856cc40f9a8bfcbe4b7b0b3"
```

## Development

### Project Structure
```
pedigreeproapi/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
└── .env               # Environment variables (create this)
```

### Dependencies

The project uses the following main dependencies:
- **requests**: HTTP library for external API calls
- **pymongo**: MongoDB driver for Python
- **Flask**: Web framework (add to requirements.txt)
- **python-dotenv**: Environment variable management (add to requirements.txt)


