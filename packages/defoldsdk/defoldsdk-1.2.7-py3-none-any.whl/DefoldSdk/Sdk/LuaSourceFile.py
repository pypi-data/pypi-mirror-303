

import os , tempfile , subprocess

class LuaSourceFile : 
	__mule__ = True
	__ext__ = ".script"
	def __init__(self,id   = None, GAME = None , PARENT = None ) :
		self.GAME  = GAME
		self.PARENT  = PARENT
		self.id = id 
		self._filename = self.GAME.get_project_path(self.GAME.get_saved_as(self))
		self._script  = "\n\nfunction init(self)\n\t-- Add initialization code here\n\t-- Learn more: https://defold.com/manuals/script/\n\t-- Remove this function if not needed\nend\n\nfunction final(self)\n\t-- Add finalization code here\n\t-- Learn more: https://defold.com/manuals/script/\n\t-- Remove this function if not needed\nend\n\nfunction update(self, dt)\n\t-- Add update code here\n\t-- Learn more: https://defold.com/manuals/script/\n\t-- Remove this function if not needed\nend\n\nfunction fixed_update(self, dt)\n\t-- This function is called if 'Fixed Update Frequency' is enabled in the Engine section of game.project\n\t-- Can be coupled with fixed updates of the physics simulation if 'Use Fixed Timestep' is enabled in\n\t-- Physics section of game.project\n\t-- Add update code here\n\t-- Learn more: https://defold.com/manuals/script/\n\t-- Remove this function if not needed\nend\n\nfunction on_message(self, message_id, message, sender)\n\t-- Add message-handling code here\n\t-- Learn more: https://defold.com/manuals/message-passing/\n\t-- Remove this function if not needed\nend\n\nfunction on_input(self, action_id, action)\n\t-- Add input-handling code here. The game object this script is attached to\n\t-- must have acquired input focus:\n\t--\n\t--    msg.post(\".\", \"acquire_input_focus\")\n\t--\n\t-- All mapped input bindings will be received. Mouse and touch input will\n\t-- be received regardless of where on the screen it happened.\n\t-- Learn more: https://defold.com/manuals/input/\n\t-- Remove this function if not needed\nend\n\nfunction on_reload(self)\n\t-- Add reload-handling code here\n\t-- Learn more: https://defold.com/manuals/hot-reload/\n\t-- Remove this function if not needed\nend"
		self.on_field_changed()

	@property
	def script(self) : 
		return self._script

	@script.setter
	def script(self,value) : 
		self._script = self.prettyLua(value)
		if self.GAME is not None : 
			with open(self.GAME.projectpath_2_fullpath(self._filename),"w") as buff : 
				buff.write(self.script)
		self.on_field_changed()	

	@property
	def filename(self) : 
		return self._filename

	@filename.setter
	def filename(self,value) : 
		'''
		if is set the old file deleted and the new one will be created and write the script in it 
		'''
		file_fullpath  = self.GAME.projectpath_2_fullpath(self._filename)
		if os.path.exists(file_fullpath) : 
			self.script = open(file_fullpath).read()
			os.remove(file_fullpath)
		self._filename = value
		if self.GAME is not None : 
			with open(self.GAME.projectpath_2_fullpath(self._filename),"w") as buff : 
				buff.write(self.script)
		self.on_field_changed()

	def read(self,file) : 
		if self.GAME.is_in_project(file): 
			with open(file) as buff : self.source = buff.read()
			self.filename = self.GAME.get_project_path(file) 
			self.id = os.path.basename(self.filename).replace(".script","")
		else : 
			# project path 
			full_path = file 
			with open(full_path) as buff : self.source = buff.read()
			if self.GAME.is_in_project(file) : 
				self.filename = self.GAME.get_project_path(file)
				self.id = os.path.basename(self.filename).replace(".script","")
		self.on_field_changed()

		

	def on_field_changed(self,msg = "") : 
		if self.PARENT is not None : 
			self.PARENT.component = self.filename 

	def prettyLua(self,luacode) : 
		result = luacode
		temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False) 
		temp_file.write(luacode)
		temp_file.flush()
		temp_file_path = temp_file.name
		luaformatter_binary = os.path.join(os.path.split(__file__)[0],"lua-format")
		luaformatter_binary_config = os.path.join(os.path.split(__file__)[0],"lua-format.config")
		cmd = [luaformatter_binary,temp_file_path,"-c" , luaformatter_binary_config ]
		process = subprocess.Popen(
				cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
		)
		output = bytes.decode(process.stdout.read())
		error = bytes.decode(process.stderr.read())
		if error == "": 
			print(error)
			result = output
		temp_file.close()
		return result
