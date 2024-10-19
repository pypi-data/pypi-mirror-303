
from google.protobuf.descriptor import FieldDescriptor
from google.protobuf.text_format import  Parse , MessageToString
from google.protobuf.json_format import MessageToDict , MessageToJson , ParseDict
import os , configparser , re , json 
from DefoldSdk.Engine.Settings import Settings
from DefoldSdk.Engine.GameProject import configparser_to_object
from DefoldSdk.Sdk import Displatcher

sdk =  Displatcher.CreateSdk()



class BaseProject : 
    def __init__(self,project) : 
        self.project = os.path.abspath(project)
        self.main_folder = os.path.join(self.project,"main")
        self.gameproject = configparser.ConfigParser()
        self.gameproject.read(os.path.join(self.project,"game.project"))
        self.gameproject = configparser_to_object(self.gameproject)
        self.title = self.gameproject.project.title
        self.files = dict()
        self.default_action()



    def default_action(self) : 
        self.MaterialsFolder = os.path.join(self.project,"Materials")
        self.TexturesFolder = os.path.join(self.project,"Textures")
        self.MeshesFolder = os.path.join(self.project,"Meshes")

    def get_relative_path(self,path) : 
        _prj = os.path.abspath(self.project)
        _path = os.path.abspath(path)
        return os.path.relpath(_path,_prj)
    
    def get_project_path(self,path) : 
        return f"/{self.get_relative_path(path)}"

    def projectpath_2_fullpath(self,path) : 
        normal_path = path.removeprefix("/")
        fullpath = os.path.join(self.project,normal_path)
        #assert os.path.exists(fullpath)
        return fullpath

    def get_saved_as(self,obj) : 
        return os.path.join(self.saving_folder(obj) , self.get_filename_saving(obj))

    def update(self) : 
        self.gameproject.write(file = os.path.join(self.project,"game.project"))
        for name , obj in self.files.items() : 
            filename = self.get_filename_saving(obj)
            save_folder = self.saving_folder(obj)
            file_path = os.path.join( save_folder, filename)
            print("<-Exporting->:\t" , file_path)
            proto = obj.to_proto()
 
            print(
                MessageToString(proto) , file = open(file_path,"w")
            )
    def get_filename_saving(self,obj) : 
        template = obj.__form__
        keys = re.findall(r'{(.*?)}', template)
        filename = template.format(**{ key : getattr(obj,key) for key in keys})
        return filename 
    
    def saving_folder(self,obj) : 
        template = Settings.SavingPolicy[type(obj).__name__]
        keys = re.findall(r'{(.*?)}', template)
        foldername = template.format(**{ key : getattr(obj,key) for key in keys})
        save_folder =  os.path.join(self.project,foldername)
        os.makedirs(save_folder,exist_ok=True )
        return save_folder

    def get_material_by_name(self,name) : 
        material_path = os.path.join(self.MaterialsFolder , name)
        #assert os.path.exists(material_path)
        material_path = os.path.join(material_path, f"{name}.material")
        #assert os.path.exists(material_path)
        return self.get_project_path(material_path)


    def get_material_texture_by_name(self,name) : 
        texture_path = os.path.join(self.TexturesFolder, f"{name}.png")
        assert os.path.exists(texture_path)
        return self.get_project_path(texture_path)

    def get_mesh_by_name(self,name) : 
        mesh_path = os.path.join(self.MeshesFolder, f"{name}.dae")
        assert os.path.exists(mesh_path)
        return self.get_project_path(mesh_path)

    def is_in_project(self , path):
        path_checking = Path(path).resolve()
        project = Path(self.project).resolve()
        try: return project in path_checking.parents
        except ValueError: return False




class Project(BaseProject) : 

    def newCollection(self,**kwargs) : 
        result = sdk.CollectionDesc(**kwargs)
        result.GAME = self 
        self.files[kwargs.get('name')] = result
        return result

    def newMaterial(self,**kwargs) : 
        result = sdk.MaterialDesc(**kwargs)
        result.GAME = self 
        self.files[kwargs.get('name')] = result 
        return result

    def install_extension(self,branch) : 
        git.Repo.clone_from(self.editor_config['Extensions']['git'], os.path.join(self.project,branch), branch=branch)


