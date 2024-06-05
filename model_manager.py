import requests
from lxml import html

class ModelManager:
    """
    This class is designed to manage the models.
    It can read models from a library, and display the models to the user.
    """
    def __init__(self, library):
        """
        Initializes the ModelManager object.

        Parameters:
        library (str): The URL of the library where the models are located.
        """
        self.library = library
        self.models = self.get_models_with_tags()

    def get_models_with_tags(self):
        """
        This function gets the models with tags from the library.
        It uses the requests and lxml libraries to scrape the models and tags from the library.

        Returns:
        list: The list of models with tags.
        """
        print(f"Getting models from the library: {self.library}")
        xpath_elements = '//*[@id="repo"]/ul/li/a/h2/span'
        response = requests.get(self.library)
        tree = html.fromstring(response.content)
        elements = tree.xpath(xpath_elements)
        models = []

        for element in elements:
            if 'Archive' in element.text_content():
                continue
            xpath_tags = './ancestor::li/a/div/div/span'
            tags = element.xpath(xpath_tags)

            for tag in tags:
                formatted_element = f"{element.text_content()}:{tag.text_content().lower()}".replace(' ', '').replace('\n', '')
                models.append(formatted_element)

        return models

    def display_models_and_get_choice(self, models):
        """
        This function displays the models to the user and gets the user's choice.

        Parameters:
        models (list): The list of models to display to the user.

        Returns:
        int: The user's choice.
        """
        models.sort()
        for i, model in enumerate(models, 1):
            print(f"{i}. {model}")

        while True:
            try:
                choice = int(input("Enter the model number : "))
                if 1 <= choice <= len(models):
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid choice. Please try again.")

        return choice