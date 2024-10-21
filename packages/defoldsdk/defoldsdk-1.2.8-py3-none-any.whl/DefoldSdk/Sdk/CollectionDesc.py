






class CollectionDesc : 
	__sdk_patch__ = True 
	__ext__ = ".collection"
	__sdk__ = True
	
	def __preinit__(self, **kwargs): 
		self.scale_along_z = 0

	def addGameObject(self,**kwargs): 
		obj = sdk.EmbeddedInstanceDesc(**kwargs)
		obj.GAME = self.GAME 
		obj.PARENT = self 
		self.embedded_instances.append(obj)
		return obj 

