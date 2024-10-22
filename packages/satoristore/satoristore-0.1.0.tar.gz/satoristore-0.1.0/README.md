# Satori Store

## Introduction

Satori Store is a sophisticated memory architecture designed for AI agents to efficiently store and retrieve hierarchical memory units, such as tasks, subtasks, steps, and actions. It provides a flexible SDK for managing memory structures without the need to modify underlying database schemas. Satori Store leverages both textual and multimodal data, supporting features like similarity search and hierarchical data retrieval.

## Features

- **Flexible hierarchical memory storage**
- **Multimodal embeddings (text and media)**
- **Similarity search across memory units**
- **Twin database approach using SQLite and Qdrant**
- **Model management with support for text and CLIP models**

## SDK Overview

The main components of the Satori Store SDK are:

1. `MemoryBankFactory`: Factory class to create the appropriate memory bank.
2. `TextMemoryBank`: For storing and retrieving text-based memories.
3. `MultimodalMemoryBank`: For storing and retrieving multimodal (text + image) memories.

## Usage

### Initializing the Memory Bank

```python
from satoristore.memory_bank_factory import MemoryBankFactory
factory = MemoryBankFactory()
```

### Using the Text Memory Store

```python
# Create a text memory unit: except for the type, all fields are optional
text_data = {
    'type': 'task',
    'description': 'This is a task memory',
    'metadata': {'key': 'value'},
    'state_before': 'initial_state',
    'state_after': 'final_state',
    'status': 'in_progress',
    'human_comment': 'Human observation',
    'ai_comment': 'AI analysis',
    'parent_id': 'parent_task_id'
}

# Get the appropriate memory bank (default is text)
memory_bank = factory.get_memory_bank()

# Store the memory unit
unique_id = memory_bank.store(text_data)

# Embed the memory unit
memory_bank.embed(unique_id, text_data)

# Retrieve the memory unit
retrieved_data = memory_bank.retrieve_by_id(unique_id)

#Search similar units
query = {
    'description': 'text memory',
    'human_comment': 'observation'
}
similar_ids = memory_bank.retrieve_similar(query, max_results=5)

# Edit the memory unit
edit_data = {'description': 'Updated text memory'}
memory_bank.edit(unique_id, edit_data)

# Delete the memory unit
memory_bank.delete(unique_id)

# Close the memory bank
memory_bank.close()
```

### Using the Multimodal Memory Store

```python
from PIL import Image
from datetime import datetime

# Create a multimodal memory unit: except for the type, all fields are optional
multimodal_data = {
    'type': 'subtask',
    'description': 'This is a subtask memory',
    'metadata': {'key': 'value'},
    'state_before': Image.new('RGB', (100, 100), color='red'),
    'state_after': Image.new('RGB', (100, 100), color='green'),
    'status': 'in_progress',
    'human_comment': 'Human observation of image',
    'ai_comment': 'AI analysis of image',
    'media_blobs': [
        {
            'id': 'image_' + datetime.now().strftime('%Y%m%d%H%M%S'),
            'media_data': Image.new('RGB', (100, 100), color='yellow'),
            'media_type': 'image'
        }
    ]
}

# Get the appropriate memory bank
memory_bank = factory.get_memory_bank(multimodal=True)

# Store the memory unit
unique_id = memory_bank.store(multimodal_data)

# Embed the memory unit
memory_bank.embed(unique_id, multimodal_data)

# Retrieve the memory unit
retrieved_data = memory_bank.retrieve_by_id(unique_id)

# Search for similar memories by text
similar_ids = memory_bank.retrieve_similar({'description': 'multimodal memory'}, max_results=5)

# Search for similar memories by image
query_image = Image.new('RGB', (100, 100), color='red')
similar_ids = memory_bank.retrieve_similar({'state_before': query_image}, max_results=5)

# Search using multiple fields
query = {
    'description': 'multimodal memory',
    'human_comment': 'observation of image'
}
similar_ids = memory_bank.retrieve_similar(query, max_results=5)

# Edit the memory unit
edit_data = {'description': 'Updated multimodal memory'}
memory_bank.edit(unique_id, edit_data)

# Delete the memory unit
memory_bank.delete(unique_id)

# Close the memory bank
memory_bank.close()
```

