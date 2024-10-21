from notion_client import Client
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

from common_utils.config import secret, load_config_yaml
from common_utils.logger import create_logger


class NotionClient:
    """Wrapper for the Notion API. Loads data from a database.

    Attributes:
        api: NotionClient object
        projects_db: List of all projects from the projects database (config)
        project_names: dict, project ids as keys, project names as values
    """

    def __init__(self):
        assert secret("NOTION_SECRET"), "Could not load NOTION_SECRET from environment variables"
        self.log = create_logger("Notion")
        self.api = Client(auth=secret("NOTION_SECRET"))

    def _get_title(self, page, property_name) -> str:
        return page["properties"][property_name]["title"][0]["plain_text"]

    def _get_emoji(self, page) -> str:
        return page["icon"]["emoji"]

    def _get_plaintext(self, page, property_name) -> str:
        plain_texts = [item["plain_text"] for item in page["properties"][property_name]["rich_text"]]
        return "".join(plain_texts)

    def _get_number(self, page, property_name) -> float:
        return page["properties"][property_name]["number"]

    def _get_select(self, page, property_name) -> object:
        select = page["properties"][property_name]["select"]
        return select

    def _get_select_name(self, page, property_name) -> str:
        select = page["properties"][property_name]["select"]["name"]
        return select

    def _get_multi_select(self, page, property_name) -> list[object]:
        multiselect = page["properties"][property_name]["multi_select"]
        return multiselect

    def _get_multi_select_names(self, page, property_name) -> list[str]:
        multiselect = page["properties"][property_name]["multi_select"]
        return [item["name"] for item in multiselect]

    def _get_date(self, task, property_name) -> tuple[str, str]:
        """Returns the start and end dates as strings of a task, empty if a date is not set"""
        date_property = task["properties"][property_name]["date"]
        start_date, due_date = "", ""
        if date_property is not None and date_property["start"] is not None:
            start_date = date_property["start"]
        if date_property is not None and date_property["end"] is not None:
            due_date = date_property["end"]
        date = (start_date, due_date)
        return date

    def get_properties(self, page, property_mapping) -> dict:
        """ Returns all properties of a page using the property_mapping """

        properties = {}
        for name, property_type in property_mapping.items():
            try:
                match property_type:
                    case "title": properties[name] = self._get_title(page, name)
                    case "emoji": properties[name] = self._get_emoji(page)
                    case "text": properties[name] = self._get_plaintext(page, name)
                    case "number": properties[name] = self._get_number(page, name)
                    case "select": properties[name] = self._get_select(page, name)
                    case "select_name": properties[name] = self._get_select_name(page, name)
                    case "multi_select": properties[name] = self._get_multi_select(page, name)
                    case "multi_select_names": properties[name] = self._get_multi_select_names(page, name)
                    case "date": properties[name] = self._get_date(page, name)
                    case _: properties[name] = page["properties"][property_type]
            except Exception as e:
                properties[name] = None
        return properties


    def get_database(self, database_id: str, properties_mapping: dict[str, str], filter={}, sort={}) -> pd.DataFrame:
        """Returns dataframe with data from a specific database.

        Args:
            database_id: Notion ID of the database
            properties_mapping: Mapping of database properties to their types.
                Example: {"Name": "title", "Status": "select"}
                Types: title, emoji, text, number, select, select_name,
                       multi_select, multi_select_names, date
            filter: Filter for the database query
            sort: Sorting for the database query

        Returns:
            pd.DataFrame: Dataframe with all tasks and their properties
        """

        all_entries = pd.DataFrame()
        query_parameter = {}
        if filter:
            query_parameter["filter"] = filter
        if sort:
            query_parameter["sorts"] = sort
        query = self.api.databases.query(database_id, **query_parameter)["results"]
        for page in query:
            properties = self.get_properties(page, properties_mapping)
            all_entries = all_entries._append(properties, ignore_index=True)
        return all_entries

    def get_multiple_databases(self, db_config_dict: dict[dict]) -> dict[str, pd.DataFrame]:
        with ThreadPoolExecutor(max_workers=2) as executor:
            thread_list = {}
            results = {}
            for name, db_config in db_config_dict.items():
                thread = executor.submit(self.get_database, **db_config)
                thread_list[name] = thread

            for name, thread in thread_list.items():
                results[name] = thread.result()

        return results


if __name__ == "__main__":
    from dotenv import load_dotenv
    from common_utils.config import load_config_yaml
    load_dotenv()
    notion = NotionClient()
    config = load_config_yaml("config.yml")
    db_config_dict = config["NOTION_DATABASES"]
    ingredients_config = db_config_dict["ingredients"]
    df = notion.get_database(**ingredients_config)
    print()
