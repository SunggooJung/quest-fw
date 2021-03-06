#!/bin/env python
#===============================================================================
# NAME: InstanceTopologyHTMLVisitor.py
#
# DESCRIPTION: A visitor responsible for the generation of HTML tables
#              of event ID's, etc.
#
# AUTHOR: reder
# EMAIL:  reder@jpl.nasa.gov
# DATE CREATED  : Sep. 13, 2016
#
# Copyright 2016, California Institute of Technology.
# ALL RIGHTS RESERVED. U.S. Government Sponsorship acknowledged.
#===============================================================================
#
# Python standard modules
#
import logging
import os
import sys
import time
from optparse import OptionParser
import exceptions
#
# Python extention modules and custom interfaces
#
#from Cheetah import Template
#from utils import version
from utils import ConfigManager
from models import ModelParser
#from utils import DiffAndRename
from generators.visitors import AbstractVisitor
from generators.visitors import ComponentVisitorBase
from generators import formatters
#
# Import precompiled templates here
#
from generators.templates.html import HtmlEventsTablePage
#
# Universal globals used within module go here.
# (DO NOT USE MANY!)
#
# Global logger init. below.
PRINT = logging.getLogger('output')
DEBUG = logging.getLogger('debug')
#
# Module class or classes go here.
class InstanceTopologyEventsHTMLVisitor(AbstractVisitor.AbstractVisitor):
    """
    A visitor class responsible for generation of component header
    classes in C++.
    """
    __instance = None
    __config   = None
    __fp_dict  = None
    __form     = None
    __form_comment = None
    __model_parser = None
    
    def __init__(self):
        """
        Constructor.
        """
        #self.initBase(self, "HTMLCmdTable")
        self.__config       = ConfigManager.ConfigManager.getInstance()
        self.__form         = formatters.Formatters()
        self.__form_comment = formatters.CommentFormatters()
        self.__model_parser = ModelParser.ModelParser.getInstance()
        self.__cmd_dir = "events"
        DEBUG.info("InstanceTopologyHTMLVisitor: Instanced.")
        self.bodytext       = ""
        self.prototypetext  = ""
        self.__fp_dict      = dict() # dictionary of instance name keyword to file handle pointer

        
    def _writeTmpl(self, instance, c, visit_str):
        """
        Wrapper to write tmpl to files desc.
        """
        DEBUG.debug('InstanceTopologyHTMLVisitor:%s' % visit_str)
        DEBUG.debug('===================================')
        DEBUG.debug(c)
        self.__fp_dict[instance].writelines(c.__str__())
        DEBUG.debug('===================================')
        
        
    def initFilesVisit(self, obj):
        """
        Defined to generate files for generated code products.
        @parms obj: the instance of the model to visit.
        """
        # Check for command dir here and if none creat it but always switch into it
        if not os.path.exists(self.__cmd_dir):
            os.mkdir(self.__cmd_dir)
        os.chdir(self.__cmd_dir)
        # Iterate over types
        for k in obj.get_base_id_dict().keys():
            tlist = obj.get_base_id_dict()[k]
            #print "Type: %s\n" % k,
            # Iterate over instances and get name
            # Open file if events exist if not do nothing
            for t in tlist:
                # print "\tInstance: %s, Base ID: %s\n" % (t[0],t[1])
                name = t[0]
                events_list = t[3].get_comp_xml().get_events()
                if len(events_list) > 0:
                    filename = "%s_events.html" % t[0]
                    # Open file for writing here...
                    DEBUG.info('Open file: %s' % filename)
                    try:
                        self.__fp_dict[name] = open(filename,'w')
                        DEBUG.info('Completed')
                    except exceptions.IOError:
                        PRINT.info("Could not open %s file." % filename)
                        sys.exit(-1)
                    PRINT.info("Generating HTML Event Table for %s:%s component instance..." % (t[0], k))
        os.chdir("..")

    def startSourceFilesVisit(self, obj):
        """
        Defined to generate starting static code within files.
        """
        pass


    def includes1Visit(self, obj):
        """
        Defined to generate includes within a file.
        Usually used for the base classes but also for Port types
        @parms args: the instance of the concrete element to operation on.
        """
        pass


    def includes2Visit(self, obj):
        """
        Defined to generate internal includes within a file.
        Usually used for data type includes and system includes.
        @parms args: the instance of the concrete element to operation on.
        """
        pass


    def namespaceVisit(self, obj):
        """
        Defined to generate namespace code within a file.
        Also any pre-condition code is generated.
        @parms args: the instance of the concrete element to operation on.
        """
        pass

    def eventArgsStr(self):
        '''
        Make a list of event args into a string
        '''
        def f(args):
            def g(lst): 
                name = lst[0]
                return name
            return self.argsString(map(g, args))
        return f
    
    def publicVisit(self, obj):
        """
        Defined to generate public stuff within a class.
        @parms args: the instance of the concrete element to operation on.
        """
        #os.chdir(self.__cmd_dir)
        c = HtmlEventsTablePage.HtmlEventsTablePage()
        for k in obj.get_base_id_dict().keys():
            tlist = obj.get_base_id_dict()[k]
            #print "Type: %s\n" % k,
            for t in tlist:
                if (t[0] in self.__fp_dict.keys()):
                    # print "\tInstance: %s, Base ID: %s\n" % (t[0],t[1])
                    eobj = t[3].get_comp_xml()
                    c.name = "%s:%s" % (t[0], k)
                    c.base_id = t[1]
                    c.has_events = len(eobj.get_events()) > 0
                    c.events = self.__model_parser.getEventsList(eobj)
                    c.event_enums = self.__model_parser.getEventEnumList(eobj)
                    c.event_args = self.__model_parser.getEventArgsDict(eobj)
                    c.event_params = c.event_args
                    c.event_args_str = self.eventArgsStr()
                    c.event_param_strs = self.__model_parser.getEventArgsPrototypeStringDict(eobj)
                    self._writeTmpl(t[0], c, "InstanceTopologyEventsHTML_Visitor")


    def protectedVisit(self, obj):
        """
        Defined to generate protected stuff within a class.
        @parms args: the instance of the concrete element to operation on.
        """
        pass


    def privateVisit(self, obj):
        """
        Defined to generate private stuff within a class.
        @parms args: the instance of the concrete element to operation on.
        """
        pass


    def finishSourceFilesVisit(self, obj):
        """
        Defined to generate ending static code within files.
        """
        for fp in self.__fp_dict.keys():
            self.__fp_dict[fp].close()
        PRINT.info("Completed generating HTML event tables...")


if __name__ == '__main__':
    pass
