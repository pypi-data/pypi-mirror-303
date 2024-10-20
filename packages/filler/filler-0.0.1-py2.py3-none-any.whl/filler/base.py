from docxtpl import DocxTemplate
import pandas as pd
from pathlib import Path

__all__ = [
    'Filler',
    ]

class Filler:
    """
    A class to fill Word document templates with data.

    Attributes:
        tpl (str): The file path to the Word document template.
        data (pd.Series | dict | pd.DataFrame): The data to fill into the template. Can be a pandas Series, a dictionary, or a DataFrame.
        output_name (str): The file path to save the filled document.
        output_path (str): The directory path to save the filled documents.
        output_name_pat (str): A pattern for the file names of the filled documents.

    Methods:
        fill: Fills the Word document template with data and saves the output.
    """

    def __init__(self, tpl:str, data: pd.Series|dict|pd.DataFrame, output_name:str=None, output_path:str=None, output_name_pat:str=None):
        self.tpl = tpl
        self.data = data
        if isinstance(data, pd.DataFrame):        
            self.output_names = {i: Path(output_path) / output_name_pat.format(**row.to_dict()) for i, row in data.iterrows()}
        else:
            self.output_name = output_name

    def fill(self):
        if isinstance(self.data, pd.Series) or isinstance(self.data, dict):
            return self._fill_row_to_template(self.tpl, self.data, self.output_name)
        elif isinstance(self.data, pd.DataFrame):
            return self._fill_rows_to_template(self.tpl, self.data, self.output_names)
        else:
            return False
        

    def _fill_row_to_template(self, tpl: str, data: pd.Series | dict, output_name: str)->bool:
        """
        Fills a Word document template with data and saves the output.

        Args:
            tpl (str): The file path to the Word document template.
            data (pd.Series | dict): The data to fill into the template. Can be a pandas Series or a dictionary.
            output_name (str): The file path to save the filled document.

        Returns:
            bool: True if the document was filled and saved successfully, False otherwise.
        """
        try:
            doc = DocxTemplate(tpl)
            context = data.to_dict() if isinstance(data, pd.Series) else data
            doc.render(context)
            doc.save(output_name)
            return True
        except Exception as e:
            return False

    def _fill_rows_to_template(self, tpl: str, data: pd.DataFrame, output_names: dict) -> dict:
        """
        Fills a Word document template with data and saves the output.

        Args:
            tpl (str): The file path to the Word document template.
            data (pd.DataFrame): The data to fill into the template.
            output_names (dict): A dictionary where keys are row indices and values are the file paths to save the filled documents.

        Returns:
            dict: A dictionary where keys are row indices and values are booleans indicating if the document was filled and saved successfully.
        """
        result = {}
        for i, row in data.iterrows():
            output_name = output_names[i]
            result[i] = self._fill_row_to_template(tpl, row, output_name)
        return result




