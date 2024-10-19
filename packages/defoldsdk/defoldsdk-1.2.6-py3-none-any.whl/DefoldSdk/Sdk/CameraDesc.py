








class CameraDesc : 
	__sdk_patch__ = True 
	__ext__ = ".camera"
	def on_field_changed(self,name = None, value = None) : 
		if self.PARENT is not None : 
			self.PARENT.data = MessageToString(self.to_proto(),as_one_line = False)


