

class EmbeddedInstanceDesc : 
	__sdk_patch__ = True 
	def __preinit__(self, **kwargs): 
		self.COMPONENTS = list()

	def get_collection_parent(self,parent = None) : 
		_parent = self.PARENT 
		if _parent is None : 
			return None
		if type(_parent).__name__ == 'CollectionDesc' : 
			return _parent
		else : 
			return self.get_collection_parent(parent=_parent)

	def on_proto(self) : 
		for cmp in self.COMPONENTS : 
			if type(cmp).__name__ == "ComponentDesc" : 
				self.data += "components {\n " + f"{cmp.to_proto()}" + "}\n"
			if type(cmp).__name__ == "EmbeddedComponentDesc": 
				self.data += "embedded_components {\n " + MessageToString(cmp.to_proto(),as_one_line = False).replace('\n',"\n  ")  + "}\n"


	def addModel(self,id ,**kwargs) : 
		cmp = sdk.EmbeddedComponentDesc(id = id , type = "model" , PARENT = self , GAME = self.GAME)
		model = sdk.ModelDesc(**kwargs , PARENT = cmp , GAME = self.GAME)
		return model 
	def addCamera(self,id ,**kwargs) : 
		cmp = sdk.EmbeddedComponentDesc(id = id , type = "camera" , PARENT = self , GAME = self.GAME)
		model = sdk.CameraDesc(**kwargs , PARENT = cmp , GAME = self.GAME)
		return model 

	def addGameObject(self,**kwargs): 
		obj = self.get_collection_parent().addGameObject(**kwargs,GAME = self.GAME , PARENT = self)
		self.children.append(obj.id)
		return obj 

	def addScriptFile(self,id ,**kwargs) : 
		component = sdk.ComponentDesc(id = id ,  PARENT = self , GAME = self.GAME)
		scriptfile = sdk.LuaSourceFile(id = id , PARENT = component , GAME = self.GAME)
		self.COMPONENTS.append(component)
		return scriptfile
