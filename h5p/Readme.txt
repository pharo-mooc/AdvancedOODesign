- Pay attention the JSON produced can be incorrect so I validated it and stored the contents into ValidatedJSON

- pharo-Template-withVariableNames2 contains the skeleton of a project

- current working experience is the following
	- edit by hand contentXXX.json (higher number = newer experience)
	- then on the h5p folder run 
	
	createH5P 
i.e., 
	cp ValidatedJSON/content3.json pharo-Template-withVariableNames2/content/content.json
	cd pharo-Template-withVariableNames2
	zip -r -D -X pharo-Template-withVariableNames2.h5p *
	
It generates a loadable pharo-Template-withVariableNames2.h5p file.