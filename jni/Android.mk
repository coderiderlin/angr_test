LOCAL_PATH := $(call my-dir)\..
include $(CLEAR_VARS)
LOCAL_MODULE    := ck

LOCAL_CFLAGS += -fPIE -pie -stdlib=libc++ -fexceptions -llog -ldl -lz
#LOCAL_CFLAGS += -mllvm -fla
LOCAL_CPPFLAGS += -std=c++11 
LOCAL_CFLAGS +=  -mfpu=neon -DHAVE_NEON=1
#LOCAL_CFLAGS += -DENABLE_LOG

$(warning logal_path:$(LOCAL_PATH))
LOCAL_LDLIBS += -llog -latomic -pie
LOCAL_C_INCLUDES += $(LOCAL_PATH)\
 
LOCAL_SRC_FILES :=  \
check_passwd.c


include $(BUILD_EXECUTABLE)
#include $(BUILD_SHARED_LIBRARY)
#include $(BUILD_STATIC_LIBRARY)