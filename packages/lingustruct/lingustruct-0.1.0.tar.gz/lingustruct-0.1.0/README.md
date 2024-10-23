
# LinguStruct

LinguStruct is an AI-supported system design framework optimized for AI understanding and usability. It provides a structured template for system design documents, facilitating easy and efficient system development for users worldwide.

---

## Installation

Ensure you have Python 3.6 or higher installed. Then, clone the repository and install the package:

```bash
git clone https://github.com/lilseedabe/lingustruct.git
cd lingustruct
pip install -e .
```

---

## Usage

### 1. Setting up API Keys

Create a `.env` file in the root directory to store your API keys and other sensitive information.  
Here is an example:

```ini
# .env file example
GROQ_API_KEY=your-groq-api-key
```

### 2. Running the Framework

Below is an example of how to use the **LinguStruct** framework:

```python
from lingustruct import LinguStruct, AISupport, Validator

# Initialize components
lingu_struct = LinguStruct()
ai_support = AISupport()
validator = Validator()

# Example: Generate a master JSON template
replacements = {"PROJECT_ID": "123", "VERSION": "1.0"}
lingu_struct.generate_master_json(replacements)

# Example: Validate a module using a schema
module_data = {
    "project_id": "123",
    "v": "1.3",
    "meta": {"t_v": "1.0", "p_n": "Project Name", "desc": "Sample project", "scale": "m"}
}
is_valid, message = validator.validate(module_data)
print(f"Validation Result: {message}")

# Example: AI-supported section completion with user-defined parameters
completion = ai_support.complete_design(
    section="meta", 
    content="The purpose of this project is...", 
    model="llama-3.2-90b-text-preview", 
    max_tokens=200, 
    temperature=0.8
)
print("AI Completion:", completion)
```

---

## Abbreviation Reference

Below are the abbreviations used within the **LinguStruct** framework to keep templates concise and manageable:

| Abbreviation | Meaning              | Description                                  |
|--------------|----------------------|----------------------------------------------|
| `t_v`        | Template Version     | The version of the template being used       |
| `p_n`        | Project Name         | The name of the project                      |
| `p_v`        | Project Version      | The version of the project                   |
| `desc`       | Description          | A brief description of the project           |
| `scale`      | Scale                | The scale of the project (small, medium, large, enterprise) |
| `st`         | Style                | The design style                             |
| `c_n`        | Component Name       | The name of the component                    |
| `c_t`        | Component Type       | The type of the component                    |
| `c_p`        | Component Path       | The file path of the component               |
| `c_dep`      | Component Dependencies | Dependencies of the component            |
| `dep_res`    | Dependency Resolution | How dependencies are resolved              |
| `err_handling` | Error Handling     | The error handling approach                  |
| `prio`       | Priority             | The priority level                           |
| `abbr`       | Abbreviations        | List of abbreviations used                   |
| `map`        | Mappings             | Key-value mappings                           |
| `p_order`    | Property Order       | Order of properties                          |
| `v`          | Version              | System or service version                    |
| `l`          | Languages            | Programming languages used                   |
| `f`          | Frameworks           | Frameworks utilized                          |
| `t`          | Tools                | Tools used for development or management     |
| `a`          | Authentication       | Authentication methods                       |
| `az`         | Authorization        | Authorization methods (e.g., RBAC)           |
| `m`          | Microservices        | Microservices architecture                   |
| `p`          | Performance          | Performance optimization information         |
| `ar`         | Architecture         | System architecture overview                 |
| `svc`        | Service              | Services or modules                          |
| `sec`        | Security             | Security measures                            |

---

## Configuration

Ensure your `.env` file is properly configured with your API keys and other settings:

```ini
# Example .env file
GROQ_API_KEY=your-groq-api-key
```

---

## License

This package is provided for **personal and academic use only**.  
**Commercial use** requires a license agreement. Please contact us at `osusume-co@lilseed.jp` for licensing inquiries.

**Terms of Use:**

1. **Non-Commercial Use Only:** This software may only be used for personal or academic purposes.  
2. **Commercial License Required:** For commercial purposes, please contact `osusume-co@lilseed.jp`.  
3. **Redistribution Prohibited:** Redistribution or public sharing of templates and design documents is not allowed.  
4. **No Warranty:** The authors are not responsible for any damages resulting from the use of this software.

---

## Contributing

If you wish to contribute to LinguStruct, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your branch.
4. Submit a pull request for review.

---

## Disclaimer

The authors are not responsible for any misuse or unintended consequences of using this framework. Users must adhere to all applicable laws and regulations when using this software.

---

## Issues & Support

If you encounter any issues, please report them on the [GitHub Issues](https://github.com/lilseedabe/lingustruct/issues) page.

---

## Changelog

- **v0.1.0**: Initial release with basic framework and API integration.

---

## Authors

Developed by Yasunori Abe. For inquiries, contact `osusume-co@lilseed.jp`.

---
