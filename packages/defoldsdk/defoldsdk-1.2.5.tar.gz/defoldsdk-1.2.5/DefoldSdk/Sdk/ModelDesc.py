






class ModelDesc : 
	__mule__ = True
	def setMaterial(self,name = "model") : 
		self.materials = [sdk.Material(name = "default" , material = self.GAME.get_material_by_name(name))]

	def setMesh(self,name) : 
		self.mesh = self.GAME.get_mesh_by_name(name)

	def setTexture(self,key,name) : 
		# check key is valid  : !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		material_proto_file = self.GAME.projectpath_2_fullpath(self.materials[0].material)
		texture_path = self.GAME.get_material_texture_by_name(name)
		texture_found  = False 
		for index , texture in enumerate(self.materials[0].textures) : 
			if texture.sampler == key : 
				self.self.materials[0].textures[index].texture = texture_path
				texture_found  = True 
		if not texture_found  : 
			self.materials[0].textures.append(
				sdk.Texture(sampler = key, texture = texture_path)
			)
		self.on_field_changed()

	def on_field_changed(self,name = None, value = None) : 
		if self.PARENT is not None : 
			self.PARENT.data = MessageToString(self.to_proto(),as_one_line = False)
