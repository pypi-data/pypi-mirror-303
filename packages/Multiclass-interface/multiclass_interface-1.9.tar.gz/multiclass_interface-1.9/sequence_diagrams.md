# Sequence diagrams
- [ThreadClass](#threadclass)
- [ProcessClass](#processclass)
- [MultiThreadClassInterface](#multithreadclassinterface)
- [MultiProcessClassInterface](#multiprocessclassinterface)
- [MPIClassInterface](#mpiclassinterface)
- [MPIClassInterface(LOOP_UNTIL_CLOSE=False)](#mpiclassinterfaceloop_until_closefalse)
- [MPIClassInterface(COLLECTIVE_MPI=False)](#mpiclassinterfacecollective_mpifalse)

## ThreadClass
```mermaid
sequenceDiagram
    participant U as Main
    participant TC as ThreadClass
    
    U->>+TC: cls=A
    
    create participant Q as IOQueue
    TC->>Q: 
    TC->>-U: ~A
    U->>+TC: ~A(*args,**kwargs)
    create participant T as Thread
    TC->>T: A, IOQueue, args, kwargs
    create participant A
    T->>A: __init__(*args, **kwargs)
    T->>+T: Run()
    T->>+Q: get()
    TC->>-U: ~a
    U->>+TC: ~a.f(*args,**kwargs)
    TC->>Q: put(f,args,kwargs)
    
    Q->>-T: f,args,kwargs
    T->>+A: f(*args, **kwargs)
    A->>-T: res
    TC->>+Q: get()
    T->>Q: put(res)
    Q->>-TC: res
    TC->>-U: res
    TC->>T: close()
    T->>-T: 


```

## ProcessClass

The `ProcessClass` is similar to the `ThreadClas` except that it uses a seprate Process instead of a Thread.
This means:
- More time used to spawn process
- Changes to `os.environ['LD_LIBRARY_PATH']` are effective in the process
- Libraries (dll/so) will have their own memory space (important if multiple instances are launched)
- Multiple processes allows parallel execution

## MultiThreadClassInterface

```mermaid
sequenceDiagram
    participant U as Main
    participant TC as MultiThreadClassInterface
    
    U->>+TC: cls=A, [args1,args2])
    
    create participant Q1 as IOQueue1
    TC->>Q1: 
    create participant T1 as Thread1
    TC->>T1: A, IOQueue1, args1
    create participant A1
    T1->>A1: __init__(*args1)
    T1->>+T1: Run()
    T1->>+Q1: get()

    create participant Q2 as IOQueue2
    TC->>Q2: 
    create participant T2 as Thread2
    TC->>T2: A, IOQueue2, args2
    create participant A2
    T2->>A2: __init__(*args2)
    T2->>+T2: Run()
    T2->>+Q2: get()

    TC->>-U: ~a
    U->>+TC: ~a.f(*args,**kwargs)
    TC->>Q1: put(f,args,kwargs)
    TC->>Q2: put(f,args,kwargs)
    
    Q1->>-T1: f,args,kwargs
    Q2->>-T2: f,args,kwargs
    T1->>+A1: f(*args, **kwargs)
    T2->>+A2: f(*args, **kwargs)
    A1->>-T1: res1
    A2->>-T2: res2
    TC->>+Q1: get()
    T1->>Q1: put(res)
    T2->>Q2: put(res)
    Q1->>-TC: res1
    TC->>+Q2: get()
    Q2->>-TC: res2
    TC->>-U: [res1,res2]
    
    TC->>T1: close()
    T1->>-T1: 
    TC->>T2: close()
    T2->>-T2: 
```


## MultiProcessClassInterface

The `MultiProcessClassInterface` is similar to the `MultiThreadClassInterfaces` except that it uses a seprate processes instead of a threads.
This means:
- More time used to spawn processes
- Changes to `os.environ['LD_LIBRARY_PATH']` are effective in the processes
- Libraries (dll/so) executed in the processes will their own individual memory space (changes to a variable in one dll does not affect the others)
- Parallel execution of class functions

## MPIClassInterface
```mermaid
sequenceDiagram
    actor U as User
    
    participant MPI0 as MPI,rank0<br>MPIClassInterface
    
    
    MPI0->>+MPI0: cls=A, [(args0),(args1)]
    
    
    create participant A0
    MPI0->>+A0: args0
    MPI0->>-U: ~a
    participant MPI1 as MPI,rank1<br>MPIClassInterface
    MPI1->>+MPI1: cls=A, [(args0),(args1)]
    create participant A1
    MPI1->>A1: args1
    participant MPI2 as MPI,rank2<br>MPIClassInterface
    MPI2->>MPI2: cls=A, [(args0),(args1)]
    MPI1->>-U: 
    MPI2->>U:  
    
    U->>+MPI0:~a.f([args0,args1])
    MPI0->>+MPI0: run_task()
    MPI1->>+MPI1: work_loop
    MPI2->>+MPI2: work_loop
    
    rect rgb(191, 223, 255)
    note right of MPI0: Scatter
    MPI0->>MPI0: f,args0
    MPI0->>MPI1: f,args1
    MPI0->>MPI2: "skip",[]
    end
    MPI0->>+A0: f(args0)
        MPI1->>+A1: f(args1)
    A0->>-MPI0: res0
    A1->>-MPI1: res1
    
    rect rgb(191, 223, 255)
    note right of MPI0: Gather
    MPI0->>MPI0: res0
    MPI1->>MPI0: res1
    MPI2->>MPI0: None
    end

    
    MPI0->>-U: [res1,res2]
    
    U->>+MPI0:~a.close()
    MPI0->>+MPI0: run_task()
    rect rgb(191, 223, 255)
    note right of MPI0: Scatter
    MPI0->>MPI0: close
    MPI0->>MPI1: close
    MPI0->>MPI2: close
    end
    MPI0->>-MPI0: 
    MPI1->>-MPI1: 
    MPI2->>-MPI2: 
```

## MPIClassInterface(LOOP_UNTIL_CLOSE=False)

Setting `mpi_interface.LOOP_UNTIL_CLOSE=False` results in the following workflow

```mermaid
sequenceDiagram
    actor U as User
    
    participant MPI0 as MPI,rank0<br>MPIClassInterface
    
    
    MPI0->>+MPI0: cls=A, [(args0),(args1)]
    
    
    create participant A0
    MPI0->>+A0: args0
    MPI0->>-U: ~a
    participant MPI1 as MPI,rank1<br>MPIClassInterface
    MPI1->>+MPI1: cls=A, [(args0),(args1)]
    create participant A1
    MPI1->>A1: args1
    participant MPI2 as MPI,rank2<br>MPIClassInterface
    MPI2->>MPI2: cls=A, [(args0),(args1)]
    MPI1->>-U: 
    MPI2->>U:  
    
    U->>+MPI0:~a.f([args0,args1])
    MPI0->>+MPI0: run_task()
    MPI1->>+MPI1: work_loop
    MPI2->>+MPI2: work_loop
    MPI2->>-MPI2: 
    MPI2->>U: 

    
    rect rgb(191, 223, 255)
    note right of MPI0: Scatter
    MPI0->>MPI0: f,args0
    MPI0->>MPI1: f,args1
    MPI0->>MPI2: "skip",[]
    end
    MPI0->>+A0: f(args0)
        MPI1->>+A1: f(args1)
    A0->>-MPI0: res0
    A1->>-MPI1: res1
    MPI1->>-MPI1: 
    MPI1->>U: 
    
    rect rgb(191, 223, 255)
    note right of MPI0: Gather
    MPI0->>MPI0: res0
    MPI1->>MPI0: res1
    MPI2->>MPI0: None
    end

    
    MPI0->>-U: [res1,res2]
    
```


## MPIClassInterface(COLLECTIVE_MPI=False)
Setting `mpi_interface.COLLECTIVE_MPI=False` results in the following workflow

```mermaid
sequenceDiagram
    
    participant MPI0 as MPI,rank0<br>MPIClassInterface
    
    
    MPI0->>+MPI0: cls=A, [(args0),(args1)]
    
    
    create participant A0
    MPI0->>+A0: args0
    
    participant MPI1 as MPI,rank1<br>MPIClassInterface
    MPI1->>+MPI1: cls=A, [(args0),(args1)]
    create participant A1
    MPI1->>A1: args1
    participant MPI2 as MPI,rank2<br>MPIClassInterface
    MPI2->>MPI2: cls=A, [(args0),(args1)]
    
    MPI0->>+MPI0:~a.f([args0,args1])
    MPI1->>+MPI1:~a.f([args0,args1])
    MPI2->>+MPI2:~a.f([args0,args1])
    
    
    MPI0->>+A0: f(args0)
    MPI1->>+A1: f(args1)
    MPI2->>-MPI2: ChildProcessError
    A0->>-MPI0: res0
    A1->>-MPI1: res1
        
    MPI0->>-MPI0: res0
    MPI1->>-MPI1: res1
    
```

