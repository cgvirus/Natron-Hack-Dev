import os
from sys import platform
import subprocess
from NatronEngine import*
from NatronGui import *
from PySide.QtGui import *




def viwer_get():
    app = natron.getGuiInstance(0)
    app.selectAllNodes(app)
    currentNode = app.getSelectedNodes()

    # we check every node's 'ID' in the list #
    for node in currentNode:
        currentID = node.getPluginID()

        # if the current node's ID is of 'viewer' type #
        if currentID == 'fr.inria.built-in.Viewer':

            # then we grab its 'label' #
            viewerLabel = node.getLabel()

            # we select it #
            myViewer = app.getViewer(viewerLabel)
           
            break
    
    return myViewer



def playAudio(sound_file,fps,range_start,range_end):
   
    start_frame = (range_start/fps)
    end_frame = ((range_end - 1)/fps)
    # length = end_frame - start_frame
    if platform == "win32":
        player = 'vlc --intf="dummy" --repeat --no-video \
            --start-time="%f" --stop-time="%f" "%s"'\
                %(start_frame, end_frame, os.path.abspath(sound_file))
    else:
        player = 'vlc --intf="dummy" --repeat --no-video \
            --start-time="%f" --stop-time="%f" "%s"'\
                %(start_frame, end_frame,sound_file)

    return player


proc = 0

def myCallback(thisParam, thisNode, thisGroup, app, userEdited):
    
    global proc

    
    if thisParam == thisNode.play_song:
        range_start = viwer_get().getFrameRange()[0]
        range_end = viwer_get().getFrameRange()[1]
        sound_file = thisNode.Sound_File.get()
        fps = app.frameRate.get()
        play = playAudio(sound_file, fps,range_start,range_end)
        thisNode.start_frame.set(range_start)
        thisNode.end_frame.set(range_end)
        thisNode.FPS.set(fps)
        viwer_get().seek(range_start)
        viwer_get().startForward()

        if platform == "win32":
            proc = subprocess.Popen(play, stdin = subprocess.PIPE, stdout = subprocess.PIPE, shell=True)
        else:
            proc = subprocess.Popen("exec " + play, stdin = subprocess.PIPE, stdout = subprocess.PIPE, shell=True)
        
        

        print(play)
        print ("Playing process pid %s " % (proc.pid))


            
    if thisParam == thisNode.stop_song:
        viwer_get().pause()
        if proc.poll() is None:
            print ("Killing process pid %s " % (proc.pid))
            # os.kill(proc.pid, signal.SIGKILL)
            
            if platform == "win32":
                subprocess.Popen("TASKKILL /F /PID {pid} /T".format(pid=proc.pid))
            else:
                proc.kill()

    if thisParam == thisNode.panic:
        viwer_get().pause()
        if platform == "win32":
            subprocess.Popen("Taskkill /IM vlc.exe /f")
        else:
            subprocess.Popen("killall vlc", stdin = subprocess.PIPE, stdout = subprocess.PIPE, shell=True)

            

