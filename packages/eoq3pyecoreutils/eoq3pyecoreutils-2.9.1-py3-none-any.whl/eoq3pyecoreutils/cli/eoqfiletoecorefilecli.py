'''
2024 Bjoern Annighoefer
'''

from eoq3.config import Config

from eoq3pyecoreutils.ecoreconversionoptions import EcoreConversionOptions
from eoq3pyecoreutils.eoqfiletoecorefile import EoqFileToEcoreFile

import argparse

'''
MAIN: Execution starts here
'''            
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Converts an eoq file to an ecore file.')
    parser.add_argument('--infile', metavar='infile', type=str, default='model.eoq', help='the file to be converted', dest='infile')
    parser.add_argument('--outfile', metavar='outfile', type=str, default='model.ecore', help='the file to be downloaded', dest='outfile')
    #user model settings
    parser.add_argument('--metafile', metavar='metafile', type=str, default=None, help='the .ecore file (only necessary if a user model is loaded. Otherwise infile will be the metafile.)', dest='metafile')
    parser.add_argument('--checksyntax', metavar='checksyntax', type=int, default=0, help='validate input files before conversion', dest='checksyntax')
    #ecore conversion options
    # parser.add_argument('--subpackages', metavar='subpackages', type=int, default=1, help='conversion options: include subpackages (only in case of a *.ecore is converted)', dest='subpackages')
    # parser.add_argument('--enums', metavar='enums', type=int, default=1, help='conversion options: include enums (only in case of a *.ecore is converted)', dest='enums')
    # parser.add_argument('--documentation', metavar='documentation', type=int, default=1, help='conversion options: include documentation (only in case of a *.ecore is converted)', dest='documentation')
    # parser.add_argument('--constraints', metavar='constraints', type=int, default=0, help='conversion options: include constraints (only in case of a *.ecore is converted)', dest='constraints')
    # parser.add_argument('--permissions', metavar='permissions', type=int, default=0, help='conversion options: include permissions (only in case of a *.ecore is converted)', dest='permissions')
    # parser.add_argument('--muteupdate', metavar='muteupdate', type=int, default=0, help='if true, UPD commands are muted', dest='muteupdate')
    # parser.add_argument('--maxstrlen', metavar='maxstrlen', type=int, default=-1, help='limit the length of strings (default=-1=infinit)', dest='maxstrlen')
    # parser.add_argument('--maxstrtrunsym', metavar='maxstrtrunsym', type=str, default='...', help='is added at the end of the string if truncated (default=...)', dest='maxstrtrunsym')
    # parser.add_argument('--translatechars', metavar='translatechars', type=int, default=0, help='if true, certian characters in strings are replaced', dest='translatechars')
    # parser.add_argument('--translatetable', metavar='translatetable', type=str, default=" _:_\n#-%\r_\t_,_/_(_)_[_]_{_}_;_\\_=_", help='a sequence of chars to be replaced. Each two consecutive chars are a pair of search and replacement char.', dest='translatetable')
    # parser.add_argument('--packageidfeat', metavar='packageidfeat', type=str, default='name', help='name or nsURI (default=name)', dest='packageidfeat')
    args = parser.parse_args()
    print("*******************************************")
    print("*           eoqfiletoecorefilecli         *")
    print("*******************************************")
    print("infile:         %s"%(args.infile))
    print("outfile:        %s"%(args.outfile))
    print("metafile:       %s"%(args.metafile))
    print("checksyntax:    %s"%(args.checksyntax))
    # print("subpackages:    %d"%(args.subpackages))
    # print("enums:          %d"%(args.enums))
    # print("documentation:  %d"%(args.documentation))
    # print("constraints:    %d"%(args.constraints))
    # print("permissions:    %d"%(args.permissions))
    # print("muteupdate:     %d"%(args.muteupdate))
    # print("maxstrlen:      %d"%(args.maxstrlen))
    # print("maxstrtrunsym:  %s"%(args.maxstrtrunsym))
    # print("translatechars: %d"%(args.translatechars))
    # print("packageidfeat:  %s"%(args.packageidfeat))
    print("*******************************************")
    #eoq config    
    config = Config()
    config.remoteCmdSerializer = "TXT"
    config.remoteRawLogging = True
    #config.connectTimeout = 1
    #set conversions options
    options = EcoreConversionOptions()
    # options.includeSubpackes = bool(args.subpackages)
    # options.includeEnums = bool(args.enums)
    # options.includeDocumentation = bool(args.documentation)
    # options.includeConstraints = bool(args.constraints)
    # options.includePermissions = bool(args.permissions)
    # options.muteUpdate = bool(args.muteupdate)
    # options.maxStrLen = args.maxstrlen
    # options.maxStrTruncationSymbol = args.maxstrtrunsym
    # options.translateChars = bool(args.translatechars)
    # if(args.translatechars):
    #     if(len(args.translatetable)%2 != 0 ):
    #         raise ValueError("translatetable must have even length.")
    #     #create tuples from char pairs
    #     options.translateTable = [(args.translatetable[i],args.translatetable[i+1]) for i in range(len(args.translatetable)-1)]
    # options.packageIdFeature = args.packageidfeat
    #interpret commands
    EoqFileToEcoreFile(args.infile,args.outfile,args.metafile,args.checksyntax,options)
    print('Conversion complete.')
        
    