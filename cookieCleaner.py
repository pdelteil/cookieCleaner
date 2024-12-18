from burp import IBurpExtender, IContextMenuFactory, ITab
from javax.swing import JPanel, JTextArea, JScrollPane, JMenuItem,JButton
from java.awt import Color

EXTENSION_NAME = "CookieCleaner"

class BurpExtender(IBurpExtender, IContextMenuFactory, ITab):

    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName(EXTENSION_NAME)

        # Register context menu
        callbacks.registerContextMenuFactory(self)
    
         # Create the main panel
        self._panel = JPanel()
        self._panel.setLayout(None)  # Use absolute positioning

         # Create the text area
        self._text_area = JTextArea(20, 60)
        self._text_area.setEditable(False)
        scroll_pane = JScrollPane(self._text_area)
        scroll_pane.setBounds(10, 10, 460, 300)  # x, y, width, height
        self._panel.add(scroll_pane)

        # Create the "Clean" button
        self._clean_button = JButton("Clean")
        self._clean_button.setBounds(10, 320, 460, 30)  # x, y, width, height
        self._clean_button.setBackground(Color.ORANGE)
        self._clean_button.setForeground(Color.WHITE)
        self._clean_button.addActionListener(self.clean_action)
        self._panel.add(self._clean_button)
        # Add tab to Burp UI
        callbacks.addSuiteTab(self)
    
    def getTabCaption(self):
        return EXTENSION_NAME

    def getUiComponent(self):
        return self._panel
    
    def createMenuItems(self, invocation):
        # Create the context menu item
        menu_item = JMenuItem("Send to CookieCleaner")
        menu_item.addActionListener(lambda x: self.send_to_tab(invocation))
        return [menu_item]
    
    def send_to_tab(self, invocation):
        # Check if messages are selected
        messages = invocation.getSelectedMessages()
        if not messages:
            self._text_area.append("No messages selected.\n")
            return
        
        # Send selected message to the tab
        for msg in messages:
            request_info = self._helpers.analyzeRequest(msg)
            request_url = request_info.getUrl()
            headers = msg.getRequest().tostring().decode('utf-8').split("\r\n")

            self._text_area.append("Request URL: " + str(request_url) + "\n")

            self._text_area.append("Headers:\n")
            for header in headers:
                self._text_area.append("{header}"+ str(header) + "\n")

            self._text_area.append("\n\n")
    def clean_action(self, event):
        # Show debug text when Clean button is pressed
        self._text_area.append("Cleaning...\n")
