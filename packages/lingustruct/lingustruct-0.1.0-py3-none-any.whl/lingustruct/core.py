import json
import os
from jsonschema import validate, ValidationError, SchemaError
from jinja2 import Environment, FileSystemLoader
from .converters import (
    lingu_struct_to_human_readable,
    human_readable_to_lingu_struct,
    lingu_struct_to_markdown,
    markdown_to_human_readable
)

class LinguStruct:
    def __init__(self, template_dir=None):
        if template_dir is None:
            # テンプレートディレクトリのパスを初期化
            template_dir = os.path.join(os.path.dirname(__file__), 'templates')
        self.env = Environment(loader=FileSystemLoader(template_dir))
        self.template_dir = template_dir

    def generate_master_json(self, replacements, output_path='master.json'):
        """master_template.jsonを使ってmaster.jsonを生成"""
        template = self.env.get_template('master_template.json')
        rendered = template.render(replacements)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(rendered)

    def generate_overview_json(self, replacements, output_path='overview.json'):
        """overview_template.jsonを使ってoverview.jsonを生成"""
        template = self.env.get_template('overview_template.json')
        rendered = template.render(replacements)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(rendered)

    def load_module(self, module_id, project_dir='src'):
        """指定したIDのモジュールをロードする"""
        module_path = os.path.join(project_dir, 'lingustruct', 'templates', f'm{module_id}.json')
        print(f"Loading module from: {module_path}")  # デバッグ用

        if not os.path.exists(module_path):
            raise FileNotFoundError(f"Module {module_id} not found at {module_path}.")

        try:
            with open(module_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            print(f"Successfully loaded module {module_id}")  # デバッグ用
            return data
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in module {module_id}: {str(e)}")
        except Exception as e:
            raise Exception(f"Unexpected error while loading module {module_id}: {str(e)}")

    def validate_module(self, module_id, schema_path):
        """モジュールのJSONをスキーマで検証する"""
        try:
            module_data = self.load_module(module_id)
            with open(schema_path, 'r', encoding='utf-8') as f:
                schema = json.load(f)
            validate(instance=module_data, schema=schema)
            print(f"Module {module_id} is valid according to the schema.")
        except ValidationError as e:
            raise ValueError(f"Validation error in module {module_id}: {e.message}")
        except SchemaError as e:
            raise ValueError(f"Invalid schema: {e.message}")
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found: {e.filename}")
        except Exception as e:
            raise Exception(f"Unexpected error: {e}")

    def convert_to_human_readable(self, lingu_struct_data, key_mapping):
        """LinguStructデータを人間が読める形式に変換"""
        return lingu_struct_to_human_readable(lingu_struct_data, key_mapping)

    def convert_from_human_readable(self, human_readable_data, key_mapping_reverse):
        """人間が読める形式のデータをLinguStruct形式に変換"""
        return human_readable_to_lingu_struct(human_readable_data, key_mapping_reverse)

    def convert_to_markdown(self, lingu_struct_data, key_mapping):
        """LinguStructデータをMarkdown形式に変換"""
        return lingu_struct_to_markdown(lingu_struct_data, key_mapping)

    def convert_from_markdown(self, markdown_text, key_mapping_reverse):
        """Markdown形式のデータを人間が読める形式に変換"""
        return markdown_to_human_readable(markdown_text, key_mapping_reverse)
