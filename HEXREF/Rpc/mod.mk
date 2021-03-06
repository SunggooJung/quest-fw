#
#   Copyright 2004-2008, by the California Institute of Technology.
#   ALL RIGHTS RESERVED. United States Government Sponsorship
#   acknowledged. Any commercial use must be negotiated with the Office
#   of Technology Transfer at the California Institute of Technology.
#
#   Information included herein is controlled under the International
#   Traffic in Arms Regulations ("ITAR") by the U.S. Department of State.
#   Export or transfer of this information to a Foreign Person or foreign
#   entity requires an export license issued by the U.S. State Department
#   or an ITAR exemption prior to the export or transfer.
#

SRC = 

SRC_SDFLIGHT = hexref_stub.c krait_wrap_rpc.c

SRC_DSPAL = hexref_skel.c #hex_wrap_rpc.c

# TODO (mereweth) - replace with some ipc bridge 
SRC_DARWIN =
SRC_LINUX =
SRC_CYGWIN =

HDR = hexref.h 

SUBDIRS = test
