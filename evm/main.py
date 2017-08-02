#Main Function
import wx
from poll import poll

if __name__ == "__main__":
    
    
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = poll(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()