# Leave it empty. This is just a special file that tells pip that your main module is in this folder. 
# No need to add anything here. Feel free to delete this line when you make your own package.

#from any import EC_Data


from .project.util_paths import Project_Paths, pDATA_RAW, pDATA_TREATED
from .file.file_dict import save_dict_to_file, load_dict_from_file, save_dict_to_tableFile
from .data_treatment import AutoClaveSynthesis
#from .data_treatment import EC_Data,EC_Datas,CV_Data,CV_Datas,AutoClaveSynthesis


#from .ec_data import * 

#__path__ = [os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data_treatment')]

#print("loading arenz_group_python")
#print(__path__)

__version__ = "0.3.1"

__all__ = ["Project_Paths","pDATA_RAW", "pDATA_TREATED",
            #"ec_data","EC_Data","EC_Datas","CV_Data","CV_Datas",
            "AutoClaveSynthesis", 
            "save_dict_to_file","load_dict_from_file", "save_dict_to_tableFile"
           ]


# public interface

#def rowdata():
#    """Try to apply the pattern at the start of the string, returning
#    a Match object, or None if no match was found."""
#    return Project_Paths().rawdata_path



