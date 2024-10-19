####################################################################################
#*************************************** Sdk *************************************** 
####################################################################################
from PyDefold import Defold
from google.protobuf.descriptor import FieldDescriptor
from google.protobuf.text_format import  Parse , MessageToString
from google.protobuf.json_format import MessageToDict , MessageToJson , ParseDict
import collections 

class SdkListType(list) : 

	def __init__(self,data = list(),PARENT = None , typ = None , name = None) : 
		super().__init__(data)
		self.PARENT = PARENT
		self.name = name  
		self.types = {typ}

	def add_types(self,*args) : 
		self.types.update(args)


	def append(self,item) : 
		assert item.__class__.__name__ in self.types , f"can not append {item.__class__.__name__ } to List[{self.type}]"
		super().append(item)
		if self.PARENT != None : 
			self.PARENT.on_field_changed(msg = "")

	def extend(self,items) : 
		for itm in items : 
			self.append(item=itm )

class SdkType : 
	__id__ = None
	__sdk__ = None 
	def __init__(self,__init__ = True , **kwargs): 
		self.GAME = kwargs.get('GAME' , None)
		self.PARENT = kwargs.get('PARENT' , None)
		self.__preinit__(**kwargs)
		self.__init_message__(**kwargs)
		self.__postinit__(**kwargs)

	def __setAttr__(self,value , name) : 
		setattr(self,f"_{value}",name)
		self.on_field_changed()

	def __init_message__(self,**kwargs) : 
		self.on_field_changed()
		for name in self.fields() : 
			value = kwargs.get(name,None)
			if value is not None : 
				self.__setAttr__(value =  name , name = value )




	def __getAttr__(self,name) : 
		if not hasattr(self,f'_{name}') : self.__init__field__(name)
		return getattr(self,f'_{name}')

	def __init__field__(self,field_name) : 
		field = self.___naitive___.DESCRIPTOR.fields_by_name.get(field_name)
		if field.type == field.TYPE_MESSAGE and field.label != field.LABEL_REPEATED  : # memeber type message
			memeber_type_string  = field.message_type._concrete_class.__name__ 
			message_type = getattr(self.__class__ , memeber_type_string , None) 
			message_type = getattr(self.__class__.__sdk__,memeber_type_string) if message_type is None else message_type
			assert message_type is not None 
			setattr(self,f'_{field_name}' , message_type() )
		if field.type == field.TYPE_MESSAGE and field.label == field.LABEL_REPEATED  : # memeber type list of message
			setattr(self,f'_{field_name}' , SdkListType(typ=field.message_type._concrete_class.__name__ , PARENT = self , name = field_name ) )
		if field.type != field.TYPE_MESSAGE and field.label == field.LABEL_REPEATED  : # memeber type list of prirmitive_types
			setattr(self,f'_{field_name}' , SdkListType(typ = self.__sdk__.PROTOBUF_TYPE_TO_PYTHON_TYPE.get(field.type) ,  PARENT = self , name = field_name) )		
		if field.type != field.TYPE_MESSAGE and field.label != field.LABEL_REPEATED  : # memeber type prirmitive
			setattr(self , f'_{field_name}',field.default_value)	




	def to_proto(self) : 
		self.on_proto()
		instance = self.___naitive___()
		for field_name in self.fields() : 
			attr = getattr(self,field_name,None) # field did not intialized 
			if attr is not None : 
				attr = getattr(self,f'_{field_name}')
				field = instance.DESCRIPTOR.fields_by_name.get(field_name)
				if field.type == field.TYPE_MESSAGE and field.label != field.LABEL_REPEATED  : # memeber type message
					memeber_type  = field.message_type._concrete_class.__name__ 
					getattr(instance , field_name).CopyFrom(attr.to_proto())
				if field.type == field.TYPE_MESSAGE and field.label == field.LABEL_REPEATED  : # memeber type list of message
					[getattr(instance , field_name).append(elem.to_proto()) for elem in attr ] 
				if field.type != field.TYPE_MESSAGE and field.label == field.LABEL_REPEATED  : # memeber type list of prirmitive_types
					[getattr(instance , field_name).append(elem) for elem in attr ] 				
				if field.type != field.TYPE_MESSAGE and field.label != field.LABEL_REPEATED  : # memeber type prirmitive
					setattr(instance , field_name,attr)	
		return instance 

	def on_proto(self) : 
		return True 
		pass 

	def update(self , **kwargs) : 
		for k , v in kwargs.items() : 
			setattr(self,k , v )
	@classmethod
	def fields(cls) : 
		return {property_name for property_name, field in cls.___naitive___.DESCRIPTOR.fields_by_name.items() }

	@classmethod
	def enums(cls) : 
		return {enum_name for enum_name in cls.___naitive___.DESCRIPTOR.enum_types_by_name  }


	def __preinit__(self, **kwargs): 
		pass 

	def __postinit__(self, **kwargs): 
		pass 

	def on_field_changed(self,msg = "") : 
		pass


class DefoldSdk : 
	PROTOBUF_TYPE_TO_PYTHON_TYPE = {
		FieldDescriptor.TYPE_DOUBLE: 'float',
		FieldDescriptor.TYPE_FLOAT: 'float',
		FieldDescriptor.TYPE_INT64: 'int',
		FieldDescriptor.TYPE_UINT64: 'int',
		FieldDescriptor.TYPE_INT32: 'int',
		FieldDescriptor.TYPE_FIXED64: 'int',
		FieldDescriptor.TYPE_FIXED32: 'int',
		FieldDescriptor.TYPE_BOOL: 'bool',
		FieldDescriptor.TYPE_STRING: 'str',
		FieldDescriptor.TYPE_BYTES: 'bytes',
		FieldDescriptor.TYPE_UINT32: 'int',
		FieldDescriptor.TYPE_ENUM: 'int',
		FieldDescriptor.TYPE_SFIXED32: 'int',
		FieldDescriptor.TYPE_SFIXED64: 'int',
		FieldDescriptor.TYPE_SINT32: 'int',
		FieldDescriptor.TYPE_SINT64: 'int',
	}

	@classmethod
	def get_type_enums(cls , typename ) : 
		enums = dict()
		defold_type = getattr(Defold , typename)
		for enum_name , enum_type in defold_type.DESCRIPTOR.enum_types_by_name.items() : 
			enums[enum_name] = {
				f'{typename}.{enum_name}.{key}' : "-"
				for key , value  in enum_type.values_by_name.items()
			}
		return enums

	@classmethod
	def GenerateDocs(cls , docs = "docs/PyDefoldSdk"  ) : 
		os.makedirs(docs,exist_ok=True)
		for typ_name, typ in Defold._asdict().items() : 
			cls.get_type_enums(typ_name)
			typeinfo = cls.inspect(typ_name , silent=True)
			md_file = os.path.join(docs,f"{typ_name}.md")
			doc = jinja2.Template(doc_template).render(
					typeinfo
			)
			print(doc , file = open(md_file,"w"))

	@classmethod
	def CreateSdkType(cls , defold_type) : 
		attributes = {
			'___naitive___' : defold_type , 
			'__sdk__' : cls 
		}
		for property_name, field in defold_type.DESCRIPTOR.fields_by_name.items(): 
			def property_getter(self, name=property_name): return self.__getAttr__(name)
			def property_setter(self, value, name=property_name): self.__setAttr__(name, value)
			attributes[f'{property_name}'] = property(property_getter , property_setter)
		## nested types 
		for member in dir(defold_type) : 
			if not (member in defold_type.DESCRIPTOR.fields_by_name) : 
				if type(getattr(defold_type,member)).__name__ == 'MessageMeta' : 
					attributes[member] = cls.CreateSdkType(getattr(defold_type,member))
		## add enum related types  
		for enum_type in defold_type.DESCRIPTOR.enum_types_by_name : 
			defold_enum = getattr(defold_type ,enum_type)
			enum_dict = {
				enum_key : enum_val
				for enum_key , enum_val in defold_enum.items()
			}
			attributes[enum_type] = collections.namedtuple(enum_type , enum_dict.keys())(**enum_dict)

		sdk_type = type(defold_type.__name__, (SdkType,), attributes)
		return sdk_type

	@classmethod
	def CreateSdk(cls) : 
		result = dict()
		for typ_name, typ in Defold._asdict().items() : 
			sdktype = cls.CreateSdkType(typ)
			result[typ_name] = sdktype
		return result 


####################################################################################
#********************************** Displatched Sdk ********************************
####################################################################################
import pkgutil , inspect , sys , importlib

class Displatcher : 
	@classmethod
	def get_submodules(cls):
		try:
			module = sys.modules[__name__]
			path = module.__path__ if hasattr(module, '__path__') else None
			prefix = module.__name__ + '.'
			submodules = []
			for info in pkgutil.iter_modules(path, prefix):
				submodules.append(info[1])
			return submodules
		except ImportError:
			print(f"Module '{module_name}' not found.")
			return []


	@classmethod
	def get_dispatched_classes(cls) : 
		result = dict()
		submodules = cls.get_submodules()
		for sub_module_name in submodules : 
			sub_module = importlib.import_module(sub_module_name)
			for name, obj in inspect.getmembers(sub_module):
				if inspect.isclass(obj)  : 
					if getattr(obj,'__sdk_patch__' , False) :
						result[obj.__name__]  = obj 
		return result 

	@classmethod
	def CreateSdk(cls) : 
		result = dict()
		originalsdk =  DefoldSdk.CreateSdk()
		_classes = cls.get_dispatched_classes()
		for _name , _cls in _classes.items() : 
			if _name in originalsdk : 
				distcls = type(_name , (_cls,originalsdk.get(_name)), dict())
				originalsdk[_name] = distcls
		sdk = collections.namedtuple('sdk' , originalsdk.keys())(**originalsdk)
		return sdk  







__all__ = ['Displatcher']
	
