import wx
import os,sys

class About(wx.Frame):
    def __init__(self, parent, id, title):
        
        
        wx.Frame.__init__(self, parent, id, title, size=(260, 200))
        
        self.ShowMe()
        self.Centre()
        
    def ShowMe(self):
        licence=""
        cur_dir=os.path.dirname(os.path.abspath((sys.argv[0])))
        description ="Electronic Voting Machine(EVM) is designed to be used for class parliamentary election in schools of Kerala"
        
        f=open(cur_dir+"/licences/licence",'r')
        for i in f.readlines():
            licence=licence+i
            
        
        
        path=cur_dir+'/images/asif.jpg'
        
        #if os.path.exists(path):
            
        #info.SetIcon(wx.Icon(path, wx.BITMAP_TYPE_JPEG))
        info = wx.AboutDialogInfo()
        #path='../icons/icon.gif'
        #if os.path.exists(path):
            
        info.SetIcon(wx.Icon(path, wx.BITMAP_TYPE_JPEG))
        info.SetName('School EVM')
        info.SetVersion('1.0')
        info.SetDescription(description)
        info.SetCopyright('Copy Left')
        info.SetWebSite('asif.kodur@gmail.com')
        info.SetLicence(licence)
        info.AddDeveloper('Muhammed Asif Kodur\nHSST English, GHSS Vythiri\nemail:<asif.kodur@gmail.com>')
        #info.AddDeveloper('\n\nGratitude to\nMaths Blog<http://mathematicsschool.blogspot.in/>')
        
        wx.AboutBox(info)
        self.Close()
        
