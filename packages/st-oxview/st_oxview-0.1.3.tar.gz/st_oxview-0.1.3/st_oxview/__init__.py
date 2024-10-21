import os
import shutil
import atexit
import tempfile
import IPython
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

class OxviewComponent:
    def __init__(self):
        """Initialize the OxviewComponent class and set up the environment."""
        self.has_setup = False
        self._frame_counter = 0
        self.oxview_folder = None
        self.temp_folder = None
        self.current_temp_files = []  # List to track created temporary files
        self.setup()  # Automatically call setup upon initialization

    def setup(self):
        """Set up the necessary directories for the Oxview component."""
        if not self.has_setup:
            # Create a unique temporary directory for the component
            self.temp_folder = tempfile.mkdtemp(suffix='_st_oxview')
            # Create a subfolder within the temporary directory for the component's resources
            self.oxview_folder = os.path.join(self.temp_folder, "oxview_component")
            if not os.path.exists(self.oxview_folder):
                # Copy the current component directory to the temporary folder
                shutil.copytree(os.path.dirname(os.path.abspath(__file__)), self.oxview_folder)
            self.has_setup = True  # Mark setup as complete to prevent re-initialization

    def oxview_from_text(self, configuration: str = None, topology: str = None, 
                         forces: str = None, pdb: str = None, js_script: str = None, 
                         width: str | int = '99%', height: str | int = 500, 
                         colormap: str = None, 
                         index_colors: list | tuple = (), **kwargs):
        """Load and visualize molecular structures in OxView from text inputs.

        Parameters
        ----------
        configuration : str, optional
            The configuration file content as a string.
        topology : str, optional
            The topology file content as a string.
        forces : str, optional
            The forces file content as a string.
        pdb : str, optional
            The PDB file content as a string.
        js_script : str, optional
            The JavaScript script content as a string.
        width : str or int, optional
            The width of the visualization frame, by default '99%'.
        height : str or int, optional
            The height of the visualization frame, by default 500.
        colormap : str, optional
            The colormap to use for visualization, by default None (you can use any of the colormaps available in matplotlib).
        index_colors : list or tuple, optional
            A list or tuple of integers specifying the nucleotide colors according to the colormap gradient, by default ().
        **kwargs : dict
            Additional keyword arguments to pass to the visualization component.
        Returns
        -------
        bool
            True if the visualization is successfully created, False otherwise.
        Raises
        ------
        ValueError
            If the text type for any file is invalid.
        """
        self.setup()  # Ensure the environment is set up
        self._frame_counter += 1
        file_texts = [configuration, topology, forces, pdb, js_script]
        names = ["struct.dat", "struct.top", "structforces.txt", "struct.pdb", 'script.js']
        oxdna_file_paths = []  # List to store the paths of the created temporary files
        file_types = []  # List to store the types of files being processed
        for text, name in zip(file_texts, names):
            if text is not None:
                try:
                    suffix = name.split('.')[-1]  # Extract the file extension
                    file_types.append(suffix)
                    # Create a temporary file in the oxview folder
                    with tempfile.NamedTemporaryFile(dir=self.oxview_folder, suffix=f'.{suffix}', delete=False) as temp_file:
                        if isinstance(text, bytes):
                            temp_file.write(text)
                        elif isinstance(text, str):
                            temp_file.write(text.encode("utf-8"))  # Write the text content to the file
                        else:
                            raise ValueError(f"Invalid text type for {name}")
                        temp_file.flush()  # Ensure all data is written to disk
                        oxdna_file_paths.append(temp_file.name.split(os.sep)[-1])  # Store the relative path
                        self.current_temp_files.append(temp_file.name)  # Keep track of the file for cleanup
                except Exception as e:
                    print(f"Error processing {name}: {e}")
                    _component_func(files_text='', width=width, height=height, frame_id = self._frame_counter, **kwargs)
                    return False
                
        if topology is None and colormap and index_colors:
            print("Colormap and base colors are only supported when a topology file is provided. Ignoring colormap and base colors.")
            colormap = None
            index_colors = ()
        if colormap and colormap not in plt.colormaps():
            print(f"Colormap '{colormap}' not found in the list of available matplotlib colormaps. Switching to default colormap.")
            colormap = None
        if index_colors:
            if not all(isinstance(c, int) for c in index_colors):
                print("Base colors must be specified as a list of intergers. Ignoring base colors.")
                index_colors = ()
            else:
                try:
                    file_types.append('json')
                    # Create a temporary file in the oxview folder
                    with tempfile.NamedTemporaryFile(dir=self.oxview_folder, suffix=f'.json', delete=False) as temp_file:

                        temp_file.write('{"Positions" :'.encode("utf-8")) # create the json dictionary
                        temp_file.write(str(index_colors).encode("utf-8")) # add the colors
                        temp_file.write("}".encode("utf-8")) # add the closing bracket

                        temp_file.flush()  # Ensure all data is written to disk

                        oxdna_file_paths.append(temp_file.name.split(os.sep)[-1])  # Store the relative path
                        self.current_temp_files.append(temp_file.name)  # Keep track of the file for cleanup
                except Exception as e:
                    if "json" in file_types:
                        file_types.remove("json") 
                    print(f"Error processing base colors: {e}")

        # Call the Oxview component with the list of file paths and their types
        _component_func(files_text=oxdna_file_paths, file_types=file_types, 
                        width=width, height=height, 
                        colormap=colormap,
                        frame_id=self._frame_counter, **kwargs)
        return True

    def oxview_from_file(self, configuration: str = None, topology: str = None, 
                         forces: str = None, pdb: str = None, js_script: str = None, 
                         width: str | int = '99%', height: str | int = 500, 
                         colormap: str = None, 
                         index_colors: list | tuple = (), **kwargs):
        """Load and visualize molecular structures in OxView from text inputs.

        Parameters
        ----------
        configuration : str, optional
            The configuration file content as a string.
        topology : str, optional
            The topology file content as a string.
        forces : str, optional
            The forces file content as a string.
        pdb : str, optional
            The PDB file content as a string.
        js_script : str, optional
            The JavaScript script content as a string.
        width : str or int, optional
            The width of the visualization frame, by default '99%'.
        height : str or int, optional
            The height of the visualization frame, by default 500.
        colormap : str, optional
            The colormap to use for visualization, by default None (you can use any of the colormaps available in matplotlib).
        index_colors : list or tuple, optional
            A list or tuple of integers specifying the nucleotide colors according to the colormap gradient, by default ().
        **kwargs : dict
            Additional keyword arguments to pass to the visualization component.
        Returns
        -------
        bool
            True if the visualization is successfully created, False otherwise.
        Raises
        ------
        ValueError
            If the text type for any file is invalid.
        """
        files_text = []
        for src in [configuration, topology, forces, pdb, js_script]:
            if src is not None:
                with open(src, "r") as f:
                    files_text.append(f.read())  # Read the file content and add it to the list
            else:
                files_text.append(None)
        # Pass the file content to oxview_from_text
        return self.oxview_from_text(configuration=files_text[0], topology=files_text[1], 
                                     forces=files_text[2], pdb=files_text[3], 
                                     js_script=files_text[4], width=width, height=height, 
                                     colormap=colormap, index_colors=index_colors,
                                     **kwargs)
    

    def cleanup_temp_files(self):
        """Clean up temporary files and directories created during the session."""
        try:
            if os.path.exists(self.temp_folder):
                shutil.rmtree(self.temp_folder)  # Remove the entire temporary directory
        except Exception as e:
            print(f"Error deleting temporary Oxview folder {self.temp_folder}: {e}")
            # If the directory can't be deleted, try to delete each file individually
            for temp_file in self.current_temp_files:
                try:
                    os.unlink(temp_file)  # Remove individual temporary files
                except Exception as e:
                    print(f"Error deleting temp file {temp_file}: {e}")

# Instantiate the OxviewComponent class to set up the environment and handle resources
oxview_component = OxviewComponent()
# Register the cleanup function to be called automatically when the program exits
atexit.register(oxview_component.cleanup_temp_files)


### Declare the functions to be used in the Streamlit script
oxview_from_text = oxview_component.oxview_from_text
oxview_from_file = oxview_component.oxview_from_file

# Declare the Streamlit component and link it to the Oxview directory
_component_func = components.declare_component(
    "oxview_frame",
    path=oxview_component.oxview_folder,
)
