import angr
import claripy
if __name__ == "__main__":
    target="./check_passwd_flat"
    find=0x400B2A
    avoids=[0x400B48,0x400ADE]

    # target="./libs/armeabi-v7a/ck"
    # find=0x00400000+0x8620
    # # find=0x00400000+0x8632
    # avoids=[0x00400000+0x863E]

    #target="./libs/armeabi-v7a/ck"
    proj=angr.Project(target)
    argv1 = claripy.BVS('argv1',5*8)
    state = proj.factory.entry_state(args=[target,argv1])
    simgr = proj.factory.simgr(state)
    print("exploring..")
    simgr.explore(find=find,avoid=avoids)
    print("explore done,found:%d"%(len(simgr.found)))
    print(simgr.found[0].solver.eval(argv1,cast_to=str))
    