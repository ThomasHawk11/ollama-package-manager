import os
from package_manager import PackageManager
from model_manager import ModelManager

class OllamaRunner:
    """
    This class is designed to run the 'ollama' package.
    It checks if the package is installed, and if not, it installs it.
    """
    def __init__(self, model_manager):
        """
        Initializes the OllamaRunner object.

        Parameters:
        model_manager (ModelManager): The ModelManager object that manages the models.
        """
        self.model_manager = model_manager

    def run(self):
        """
        This function is the main function to run the 'ollama' package.
        It checks if the package is installed, and if not, it installs it.
        Then, it displays the models and lets the user choose a model to run.

        Returns:
        None: This function does not return a value but it runs the 'ollama' package.
        """
        package_name = "ollama"
        package_manager = PackageManager()
        if not package_manager.is_package_installed(package_name):
            print(f"The package {package_name} is not installed. Installing...")
            package_manager.install_package(package_name)
            print(f"The package {package_name} has been installed.")

        models = self.model_manager.models
        choice = self.model_manager.display_models_and_get_choice(models)
        chosen_model = models[choice - 1]

        # Split the chosen model into the name and the tag
        name, tag = chosen_model.split(':')

        # Try running the command with the chosen model
        command = f"ollama run {chosen_model}"
        print(f"Running the command : {command}")
        result = os.system(command)

        # If the command failed, try running the command without the tag
        if result != 0:
            command = f"ollama run {name}"
            print(f"Running the command : {command}")
            os.system(command)

if __name__ == "__main__":
    """
    This is the main entry point of the program.
    It creates a ModelManager object and an OllamaRunner object,
    and then it runs the 'ollama' package.
    """
    library = "https://ollama.com/library"
    model_manager = ModelManager(library)
    ollama_runner = OllamaRunner(model_manager)
    ollama_runner.run()
