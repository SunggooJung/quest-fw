-include $(BUILD_ROOT)/ROS/fprime_ws/src/fprime/mod.mk

EXTRA_INC_DIRS_ROSRosCycle_DARWIN := $(EXTRA_INC_DIRS_ROSRosCycle_DARWIN) $(EXTRA_INC_DIRS_DARWIN) $(EXTRA_INC_DIRS)
EXTRA_LIBS_ROSRosCycle_DARWIN := $(EXTRA_LIBS_ROSRosCycle_DARWIN) $(EXTRA_LIBS_DARWIN) $(EXTRA_LIBS)

EXTRA_INC_DIRS_DARWIN=
EXTRA_LIBS_DARWIN=
EXTRA_INC_DIRS=
EXTRA_LIBS=
