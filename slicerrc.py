customLayout = """
<layout type="horizontal" split="false">
  <item>
  <view class="vtkMRMLSliceNode" singletontag="Red">
    <property name="orientation" action="default">Axial</property>
    <property name="viewlabel" action="default">R</property>
    <property name="viewcolor" action="default">#F34A33</property>
  </view>
  </item>
  <item>
  <view class="vtkMRMLSliceNode" singletontag="Green">
    <property name="orientation" action="default">Coronal</property>
    <property name="viewlabel" action="default">G</property>
    <property name="viewcolor" action="default">#6EB04B</property>
  </view>
  </item>
  <item>
  <view class="vtkMRMLSliceNode" singletontag="Yellow">
    <property name="orientation" action="default">Sagittal</property>
    <property name="viewlabel" action="default">Y</property>
    <property name="viewcolor" action="default">#EDD54C</property>
  </view>
  </item>
</layout>
 
 
"""

class CloseApplicationEventFilter(qt.QWidget):
  def eventFilter(self, object, event):
    if event.type() == qt.QEvent.Close:
      event.accept()
      return True
    return False

 
# Built-in layout IDs are all below 100, so you can choose any large random number
# for your custom layout ID.
customLayoutId=501
 
layoutManager = slicer.app.layoutManager()
layoutManager.layoutLogic().GetLayoutNode().AddLayoutDescription(customLayoutId, customLayout)
 
# Switch to the new custom layout
layoutManager.setLayout(customLayoutId)

#Hide module panel view
mainWindow().findChild('QDockWidget','PanelDockWidget').hide()

#hide toolbars
slicer.util.setToolbarsVisible(False)

#disable default program close dialog window
filter = CloseApplicationEventFilter()
slicer.util.mainWindow().installEventFilter(filter)