
import configparser 


class GameProject : 
	def on_value_changed(self,name, value) : 
		if name in  ["width" , "height"] : 
			if type(value) == str : 
				setattr(self,name,int(value))

	def __setattr__(self, name, value):
		super().__setattr__(name, value)
		self.on_value_changed(name, value)
	
	def write(self,file) : 
		config_object = configparser.ConfigParser()
		for section , sectionvalue in vars(self).items() :
			config_object.add_section(section)
			for field , fieldvalue  in vars(sectionvalue).items() : 
				config_object.set(section, field, str(fieldvalue))
		stream = open(file,"w")
		config_object.write(stream)
		stream.close()



def configparser_to_object(config) :
	sections = config._sections
	result = GameProject()
	for k , v in sections.items() :
		memeber = GameProject()
		for kk , vv in v.items() : 
			setattr(memeber,kk,vv) 
		setattr(result,k,memeber)
	return result
