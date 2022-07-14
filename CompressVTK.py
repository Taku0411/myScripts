import vtk
import os
import glob
import re
import shutil
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process
import time

def vtkCompressor(readpath : str, outputdirpath : str, name : str):
    # check path
    if not os.path.exists(readpath):
        print("no such file or directory: {}".format(readpath))

    filename = readpath[:readpath.find(".", 3)]
    digit = re.findall("\d+", readpath)
    exportname = "{}{}{}.vtu".format(outputdirpath, name, digit[1])

    print(exportname)

    # set reader instance
    reader = vtk.vtkUnstructuredGridReader()
    reader.SetFileName(readpath)
    reader.Update()

    writer = vtk.vtkXMLUnstructuredGridWriter()
    writer.SetInputData(reader.GetOutput())
    writer.SetFileName(exportname)
    writer.SetCompressorTypeToLZMA()
    writer.SetCompressionLevel(5)
    writer.Write()

    
def getInfo():
    wholelist = glob.glob("./vtk/*.vtk")
    
    firstlist = glob.glob("./vtk/opt0001*")
    
    target = wholelist[0]

    # check strings
    args = re.split(r"\d+", target)
    
    digit = re.findall(r"\d+", target)
    if(len(digit) != 2):
        print("File name format is invalid")
        sys.exit(-1)

    # make digit list
    digitlist= []
    for i in range(len(wholelist)):
        digitlist.append(re.findall(r"\d+", wholelist[i]))
    
    numopt  = max(int(i[0]) for i in digitlist)
    numstep = max(int(i[1]) for i in digitlist)

    print("number of optimization iteration: {}\number of analysis step: {}".format(numopt, numstep))

    print("please input the time step for topology flow")

    index = int(input())
    if(index > numstep):
        print("Index out of range")
        sys.exit(1);
    print(args)

    firstlist = glob.glob("{}{:0>4}{}*{}".format(args[0], 1, args[1], args[2]))
    lastlist  = glob.glob("{}{:0>4}{}*{}".format(args[0], numopt, args[1], args[2]))
    flowlist  = glob.glob("{}*{}{:0>4}{}".format(args[0], args[1], index, args[2]))
    return [numopt, numstep, firstlist, lastlist, flowlist]


if __name__ == "__main__":
    shutil.rmtree("output")
    os.mkdir("output/")
    # vtkCompressor("flow0256.vtk", "output/")

    numopt, numstep, first, last, flow = getInfo()

    # print("parallel")
    # start_time = time.perf_counter()
    # with ThreadPoolExecutor() as executor:
    #     for i in first:
    #         # vtkCompressor(i, "output/", "first")
    #         executor.submit(vtkCompressor, i, "output/", "first")

    end_time = time.perf_counter()
    elapsed_time1 = end_time - start_time

    print("process")
    start_time = time.perf_counter()
    pro = [
        Process(target=vtkCompressor, args = (i, "output/", "first"))
        for i in first
    ]

    for p in pro:
        p.start()

    for p in pro:
        p.join()

    end_time = time.perf_counter()
    elapsed_time2 = end_time - start_time



    # print("sigle")
    # start_time = time.perf_counter()
    # for i in first:
    #     vtkCompressor(i, "output/", "first")
    # end_time = time.perf_counter()
    # elapsed_time3 = end_time - start_time
