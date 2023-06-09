from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
import configparser 

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        # Load configuration settings from file
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        
        # Load level data
        self.level1 = self.loader.loadModel(self.config.get('level1', 'model-file'))
        self.level1.reparentTo(self.render)
        self.level1.setPos(self.config.getfloat('level1', 'start-pos-x'),
                           self.config.getfloat('level1', 'start-pos-y'),
                           self.config.getfloat('level1', 'start-pos-z'))
        
        self.level2 = self.loader.loadModel(self.config.get('level2', 'model-file'))
        self.level2.reparentTo(self.render)
        self.level2.setPos(self.config.getfloat('level2', 'start-pos-x'),
                           self.config.getfloat('level2', 'start-pos-y'),
                           self.config.getfloat('level2', 'start-pos-z'))
        self.level2.hide()
        
        # Set up camera and lighting
        self.disableMouse()
        self.camera.setPos(0, 0, 10)
        
        self.light = self.render.attachNewNode(PointLight("light"))
        self.light.setPos(0, 0, 10)
        self.render.setLight(self.light)
        
        # Set up ambient lighting
        ambientLight = AmbientLight("ambient")
        ambientLight.setColor(Vec4(0.5, 0.5, 0.5, 1))
        ambientNode = self.render.attachNewNode(ambientLight)
        self.render.setLight(ambientNode)
        
        # Set up key bindings
        self.accept('escape', self.quit)
        self.accept('1', self.loadLevel1)
        self.accept('2', self.loadLevel2)
        
    def quit(self):
        self.cleanup()
        self.userExit()
        
    def cleanup(self):
        pass
    
    def loadLevel1(self):
        self.level1.show()
        self.level2.hide()
        
    def loadLevel2(self):
        self.level1.hide()
        self.level2.show()
        
game = Game()
game.run()
    
