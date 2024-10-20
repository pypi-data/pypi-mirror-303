# eoq3pyecoreutils - pyecore-eoq3 bridge

An auxilary package for using eoq3 with pyecore, e.g. value type and model conversion as well as operation conversion and Concepts wrappers.

### Usage

eoq3 has a programmatic and CLI interface.

### Programatic

    from eoq3pyecoreutils.ecorefiletoeoqfile import EcoreFileToEoqFile
    from eoq3pyecoreutils.eoqfiletoecorefile import EoqFileToEcoreFile
    
    m2EcoreFile = "testdata/Workspace/Meta/oaam.ecore"
    m1EcoreFile = "testdata/Workspace/MinimalFlightControl.oaam"
    
    LoadEcoreFile(m2EcoreFile,domain,options=resource.options,config=resource.config)
    LoadEcoreFile(m1EcoreFile,domain,metafile=m2EcoreFile,options=resource.options,config=resource.config)
	
	SaveEcoreFile(m2EcoreFileSaved, rootObj, domain, options=resource.options)
	SaveEcoreFile(m1EcoreFileSaved, rootObj, domain, metafile=m2EcoreFile, options=resource.options)
	SaveEcoreFile(m1EcoreFileSaved, rootObj, domain, metafile=m2EcoreFileSaved, saveMetamodelInAddition=True, options=resource.options)

### CLI inteface

eoq and ecore file conversion:

    python -m eoq3pyecoreutils.cli.ecorefiletoeoqfilecli --infile "m2model.ecore" --outfile "m2model.eoq"
    
    python -m eoq3pyecoreutils.cli.ecorefiletoeoqfilecli --infile "m1model.ecore" --outfile "m1model.eoq" --metafile "m2model.ecore"
   
    python -m eoq3pyecoreutils.cli.eoqfiletoecorefilecli --infile "m2model.eoq" --outfile "m2model.ecore"
	
    python -m eoq3pyecoreutils.cli.eoqfiletoecorefilecli --infile "m1model.eoq" --outfile "m1model.eoq" --metafile "m2model.ecore"

File downloading:

    python -m eoq3pyecoreutils.cli.saveecorefiletcpcli --outfile "m2model.ecore" --rootobj "(/*MDB/*M2MODELS:0)"  --host "127.0.0.1" --port 6141

	python -m eoq3pyecoreutils.cli.saveecorefilewscli --outfile "m1model.xmi" --rootobj "(/*MDB/*M1MODELS:0)"  --metafile "m2model.ecore" -savemetamodel 1 --host "127.0.0.1"  --port 5141
	
File uploading:
	
	python -m eoq3pyecoreutils.cli.loadecorefiletcpcli --infile "m2model.ecore" --host "127.0.0.1" --port 6141

    python -m eoq3pyecoreutils.cli.loadecorefilewscli --infile "m2model.ecore" --host "127.0.0.1" --port 5141

    python -m eoq3pyecoreutils.cli.loadecorefilewscli --infile "m1model.xmi" --metafile "m2model.ecore" --host "127.0.0.1" --port 5141

## Documentation

For more information see EOQ3 documentation: https://eoq.gitlab.io/doc/eoq3/

## Author

2024 Bjoern Annighoefer