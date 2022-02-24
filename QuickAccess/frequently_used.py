import tkinter
import json
import subprocess
import add_file_or_dir


def checkFileExistence():
    try:
        f = open('frequents.json')
        f.close()
    except FileNotFoundError:
        f = open('frequents.json', 'w')
        c = {'files': [], 'dirs': []}
        json.dump(c, f)
        f.close()


def updateFile(name, path, target):
    f = open('frequents.json')
    x = json.load(f)
    f.close()
    filesArray = list(x['files'])
    dirsArray = list(x['dirs'])
    path = str(path)
    path = path.replace('/', '\\')
    if target == 'file':
        filesArray.append({'name': name, 'path': path})
    if target == 'dir':
        dirsArray.append({'name': name, 'path': path})
    fileContent = {'files': filesArray, 'dirs': dirsArray}
    f = open('frequents.json', 'w')
    json.dump(fileContent, f)
    f.close()


class FrequentAppsDirs:
    def __init__(self):
        self.addGui = None
        self.root = tkinter.Tk()
        self.root.title('Frequent Apps/Dirs')
        self.root.geometry('+200+220')

        # create title frame
        self.titleFrame = tkinter.Frame(self.root)
        self.titleLabel = tkinter.Label(self.titleFrame, text='Frequent Directories and Application')
        self.titleLabel.pack()
        self.titleFrame.grid(row=0, column=0, columnspan=2)

        # Edit paths
        self.editFrame = tkinter.Frame(self.root)
        self.editPaths = tkinter.Button(self.editFrame, text='Edit Paths')
        self.editPaths['command'] = lambda: subprocess.Popen('notepad frequents.json')
        self.editPaths.pack()
        self.editFrame.grid(row=2, column=0, columnspan=2)

        checkFileExistence()

        # file and dir frames
        self.filesFrame = tkinter.Frame(self.root)
        self.dirsFrame = tkinter.Frame(self.root)
        self.fillFilesFrame()
        self.fillDirsFrame()
        self.filesFrame.grid(row=1, column=0)
        self.dirsFrame.grid(row=1, column=1)

        self.root.mainloop()

    def fillFilesFrame(self):
        f = open(r'frequents.json')
        x = json.load(f)
        f.close()
        for i in x['files']:
            file = tkinter.Button(self.filesFrame, text=i['name'], relief=tkinter.RIDGE)
            file['command'] = lambda obj=file: self.openFileOrDir(obj)
            file.pack()
        addBtn = tkinter.Button(self.filesFrame, text='+')
        addBtn['command'] = self.addFile
        addBtn.pack()

    def fillDirsFrame(self):
        f = open(r'frequents.json')
        x = json.load(f)
        f.close()
        for i in x['dirs']:
            dir = tkinter.Button(self.dirsFrame, text=i['name'], relief=tkinter.RIDGE)
            dir['command'] = lambda obj=dir: self.openFileOrDir(obj)
            dir.pack()
        addBtn = tkinter.Button(self.dirsFrame, text='+')
        addBtn['command'] = self.addDir
        addBtn.pack()

    def addFile(self):
        self.addGui = tkinter.Tk()
        self.addGui.title('Add File Path')
        self.addGui.geometry('+480+220')
        add_file_or_dir.Add(self.addGui, 'file')

    def addDir(self):
        self.addGui = tkinter.Tk()
        self.addGui.title('Add Dir Path')
        self.addGui.geometry('+480+220')
        add_file_or_dir.Add(self.addGui, 'dir')

    def openFileOrDir(self, button):
        f = open(r'frequents.json')
        x = json.load(f)
        f.close()
        text = button['text']
        if self.filesFrame.focus_get():
            for i in x['files']:
                if i['name'] == text:
                    cmd = i['path']
                    subprocess.Popen(cmd)
                    break

        if self.dirsFrame.focus_get():
            for i in x['dirs']:
                if i['name'] == text:
                    cmd = i['path']
                    subprocess.Popen('explorer ' + cmd)
                    break


if __name__ == '__main__':
    FrequentAppsDirs()
