import os 




class MaterialDesc : 
	__sdk_patch__ = True 
	__ext__ = ".material"
	__form__ = '{name}.material'

	def __postinit__(self, **kwargs): 
		self.max_page_count = 1

	def __preinit__(self,*args,**kwargs) : 
		self.vp = ""
		self.fp = ""
		self.CONSTANT_TYPE = dict(Viewproj=getattr(self.ConstantType,"CONSTANT_TYPE_VIEWPROJ") ,
			User=getattr(self.ConstantType,"CONSTANT_TYPE_USER" ),
			World=getattr(self.ConstantType,"CONSTANT_TYPE_WORLD" ),
			Texture=getattr(self.ConstantType,"CONSTANT_TYPE_TEXTURE" ),
			View=getattr(self.ConstantType,"CONSTANT_TYPE_VIEW" ),
			Projection=getattr(self.ConstantType,"CONSTANT_TYPE_PROJECTION" ),
			Worldview=getattr(self.ConstantType,"CONSTANT_TYPE_WORLDVIEW" ),
			User_Matrix4=getattr(self.ConstantType,"CONSTANT_TYPE_USER_MATRIX4" ),
			Worldviewproj = getattr(self.ConstantType,"CONSTANT_TYPE_WORLDVIEWPROJ" ),
			Normal=getattr(self.ConstantType,"CONSTANT_TYPE_NORMAL") 
			)
		self.WRAP_MODES = dict(
			edge = getattr(self.WrapMode,"WRAP_MODE_CLAMP_TO_EDGE"), 
			repeat = getattr(self.WrapMode,"WRAP_MODE_REPEAT"),
			mirror = getattr(self.WrapMode,"WRAP_MODE_MIRRORED_REPEAT")
		)
		self.FILTER_MODE_MAG = dict(
			default = getattr(self.FilterModeMag , "FILTER_MODE_MAG_DEFAULT") , 
			linear = getattr(self.FilterModeMag , "FILTER_MODE_MAG_LINEAR"),
			nearest = getattr(self.FilterModeMag , "FILTER_MODE_MAG_NEAREST")
		)
		self.FILTER_MODE_MIN = {
			'default'  : getattr(self.FilterModeMin , "FILTER_MODE_MIN_DEFAULT"), 
			'linear'  : getattr(self.FilterModeMin , "FILTER_MODE_MIN_LINEAR"),
			'nearest' : getattr(self.FilterModeMin , "FILTER_MODE_MIN_NEAREST" ), 
			'linear-linear'  : getattr(self.FilterModeMin , "FILTER_MODE_MIN_LINEAR_MIPMAP_LINEAR"),
			'linear-nearest'  : getattr(self.FilterModeMin , "FILTER_MODE_MIN_LINEAR_MIPMAP_NEAREST"),
			'nearest-linear'  : getattr(self.FilterModeMin , "FILTER_MODE_MIN_NEAREST_MIPMAP_LINEAR"), 
			'nearest-nearest'  : getattr(self.FilterModeMin , "FILTER_MODE_MIN_NEAREST_MIPMAP_NEAREST")
		}

	def on_proto(self) : 
		if (self.name != "") and (self.GAME is not None) : 
			saving_folder = self.GAME.saving_folder(self)
			os.makedirs(saving_folder,exist_ok = True)
			print(saving_folder)
			vp_file = os.path.join(saving_folder,f'{self.name}.vp')
			fp_file = os.path.join(saving_folder,f'{self.name}.fp')
			print(self.vp , file = open(vp_file,"w"))
			print(self.fp , file = open(fp_file,"w"))
			self.fragment_program = self.GAME.get_project_path(fp_file)
			self.vertex_program = self.GAME.get_project_path(vp_file)

	def setvertex_constant(self,name,typ,value = None) :
		constant = self.Constant(name = name , type = self.CONSTANT_TYPE.get(typ) )
		self.vertex_constants.append(constant)

	def setfragment_constant(self,name,typ,value = None ) :
		constant = self.Constant(name = name , type =  self.CONSTANT_TYPE.get(typ))
		self.fragment_constants.append(constant)

	def setvertex_space(self,typ = 'local') : 
		self.vertex_space = {'world' : getattr(self.VertexSpace,'VERTEX_SPACE_WORLD') , 'local' : getattr(self.VertexSpace,'VERTEX_SPACE_LOCAL')}[typ]

	def setTexture(self,name,u = 'edge',v = 'edge' ,min = 'linear',mag ='linear') : 
		tex = self.Sampler(name = name , 
			wrap_u = self.WRAP_MODES.get(u), wrap_v = self.WRAP_MODES.get(v),
			filter_mag = self.FILTER_MODE_MAG.get(mag) , filter_min = self.FILTER_MODE_MIN.get(min)
		)
		self.samplers.append(tex)

	def export(self) : 
		self.on_proto()

