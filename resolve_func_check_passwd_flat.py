import angr
import claripy

load_options = {}

# Android NDK library path:
# load_options['custom_ld_path'] = ['/mnt/d/android-ndk-r16b/platforms/android-21/arch-arm/usr/lib/']
# target="./libs/armeabi-v7a/ck"
# func=0x004085B0
# find=0x004085f8
# avoid=0x00408602

#load_options['custom_ld_path'] = ['/mnt/d/android-ndk-r16b/platforms/android-21/arch-arm/usr/lib/']
target="./check_passwd_flat"
func=0x400530
find=0x40091B
avoid=0x40097C

b = angr.Project(target, load_options = load_options)

state = b.factory.blank_state(addr=func)
initial_path = b.factory.path(state)
path_group = b.factory.path_group(state)

print("exploring...")
path_group.explore(find=find, avoid=avoid)
found_len=len(path_group.found)
print("explore done,found:%d"%(found_len))
if found_len >0:
    found = path_group.found[0]
    #now the simulator pause at 0x40091B,and rdx is the answer,dump it from memory
    answer=found.state.solver.eval(found.state.memory.load(found.state.regs.rdx,10),cast_to=str)
    print("answer:%s"%(answer))