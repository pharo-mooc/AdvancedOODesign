

for OUTPUT in $(find __results -name '*.pdf')
do
	x=$OUTPUT
	echo $x
	/Users/ducasse/Documents/Pharo/images/H5P/../../vms/100-x64/Pharo.app/Contents/MacOS/Pharo --headless /Users/ducasse/Documents/Pharo/images/H5P/H5P.image clap h5p /Users/ducasse/Workspace/FirstCircle/MyBooks/Bk-Writing/AdvancedOODesign/$x
done
