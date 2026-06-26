#Till now (21/1/2025) export is done based on selected messages and one xls file per thread id, should this be changed to Post level in case of channel messages?
#how to identify and name on Post level? query would be top-level-guid:(parent.guid)
#Problem if i export more than 1 conversation, the attachments are not exported, if only 1 they are exported?
# --> because the item was not selected - should we always export children attachments even if they are not selected?

import javax.swing as swing
import java.awt as awt
from java.awt import Component, Cursor
import os
import sys
import nuix
from java.io import File
from javax.swing import JFileChooser, JOptionPane
from java.awt import Desktop
import codecs
from datetime import datetime, timedelta
import re
from java.util import TimeZone, Date
import csv
import sys
import threading
import time
import nuix
from java.awt.event import MouseAdapter, WindowAdapter
#import org.apache.poi
from org.apache.poi.hssf.usermodel import HSSFWorkbook
from org.apache.poi.hssf.usermodel import HSSFSheet
from org.apache.poi.hssf.usermodel import HSSFCell
from org.apache.poi.hssf.usermodel import HSSFHyperlink
from org.apache.poi.ss.usermodel import CreationHelper
from org.apache.poi.ss.usermodel import IndexedColors
from org.apache.poi.hssf.usermodel import HSSFCellStyle
from org.apache.poi.hssf.usermodel import HSSFFont
from org.apache.poi.ss.usermodel import Hyperlink
from org.apache.poi.ss.usermodel import CellStyle, Font, HorizontalAlignment, VerticalAlignment
from java.io import FileOutputStream
from org.apache.poi.ss.usermodel import Hyperlink
from org.apache.poi.common.usermodel import HyperlinkType
from org.apache.poi.ss.usermodel import CreationHelper
from java.io import File
from javax.swing import AbstractAction, JScrollPane, JOptionPane, JDialog, JPanel, JProgressBar, JLabel, BoxLayout
from thread import start_new_thread

#if we export a channel message, test if there is a post name (get family, exclude the parent item (only the channel messages), loop through them to find if any contains a subject)
#Should we first deduplicate or leave it to the NO to deduplicate before exporting?
def show_error(message):
    JOptionPane.showMessageDialog(None, message, "Error", JOptionPane.ERROR_MESSAGE)
class MyDialog(JDialog):
    def __init__(self, content, title="", cancellable=True):
        # Initialize the dialog with content and title.
        self.setModal(True)
        self.setTitle(title)
        self.setContentPane(content)
        self.setDefaultCloseOperation(JDialog.DO_NOTHING_ON_CLOSE)
        self.addWindowListener(DontClose(content, cancellable))
        self.pack()
        self.setLocationRelativeTo(None)
        self.setVisible(True)


class DontClose(WindowAdapter):
    def __init__(self, panel, cancellable=False):
        # Initialize the window adapter to handle close events.
        self.panel = panel
        self.cancellable = cancellable
        
    def windowClosing(self, event):
        # Handle the window closing event.
        if self.cancellable:
            self.panel.cancel_action(event)
def get_channel_name(anitem):
    channel_name = anitem.getProperties().get("Mapi-IOpenTypedFacet.SkypeSpaces_ConversationPost_Extension#Topic", None)
    if channel_name:
        return unicode(channel_name)
    return "No Teams Channel Name."


def get_team_name(anitem):
    if anitem.getProperties().get("Mapi-IOpenTypedFacet.SkypeSpaces_ConversationPost_Extension#TeamName", None):
        return str(anitem.getProperties().get("Mapi-IOpenTypedFacet.SkypeSpaces_ConversationPost_Extension#TeamName", None))
    return "No Team Name."  

def get_post_subject(anitem):
    if len(anitem.getFamily()) > 1:
        for item in anitem.getFamily():
            if str(item.getType()) == "application/vnd.microsoft.m365.teams.channel-message":
                if item.getProperties().get("Subject", None):
                    return str(item.getProperties().get("Subject", None))
    return "No Post Subject."  

def is_deleted(anitem):
    if anitem.getProperties().get ("Mapi-SkypeIsMessageSoftDeleted = True"):
        return True
    else:
        return False
   
def get_meeting_subject(anitem):
    if anitem.getProperties().get("Mapi-IOpenTypedFacet.SkypeSpaces_ConversationPost_Extension#Topic", None):
        return str(anitem.getProperties().get("Mapi-IOpenTypedFacet.SkypeSpaces_ConversationPost_Extension#Topic", None))
    return "No meeting subject found." 


def create_xls_file(acollection, mydirectory):
    text_file_path = ""
    row_counter = 0

    # Create a new workbook
    workbook = HSSFWorkbook()
    # Create a new sheet within the workbook
    sheet = workbook.createSheet("Conversation")
    first_element = True

    for item in acollection:
        if first_element:
            # Write header data to the sheet
            # Create a cell style for the headers
            header_style = workbook.createCellStyle()
            header_style.setAlignment(HorizontalAlignment.CENTER)
            header_style.setVerticalAlignment(VerticalAlignment.CENTER)
            header_font = workbook.createFont()
            header_font.setBold(True)  # Make the font bold
            header_style.setFont(header_font)
            header_row = sheet.createRow(0)
            headers = ["Preview Text", "Sender", "Recipients", "Date", "TeamsChatConversationID", "Name", "Path Name", "Position", "MD5 Digest", "GUID", "Name of the Teams Post", "Name of the Teams Channel", "Name of the Team"]
            # Write the headers to the first row of the sheet
            for col, header in enumerate(headers):
                cell = header_row.createCell(col)
                cell.setCellValue(header)
                cell.setCellStyle(header_style)
            first_element = False

        row_counter += 1
        row = sheet.createRow(row_counter)

        if getmytype(item) == "message" or getmytype(item) == "threadIDchat":
            content = item.getTextObject().toString()
            row.createCell(0).setCellValue(content)
            channelname = str(get_channel_name(item))
            postname = str(get_post_subject(item))
            teamname = str(get_team_name(item))
        elif getmytype(item) == "attachment":
            #What to do if an attachment is not available? Attachment + name + not available or something? Put it in red
            #For attachments, how to get the parent's channel name etc, avoid that it is populated later on
            channelname = str(get_channel_name(item.parent))
            postname = str(get_post_subject(item.parent))
            teamname = str(get_team_name(item.parent))
            if str(item.getType()) == "filesystem/inaccessible":
                cell = row.createCell(0)
                cell.setCellValue("Attachment with GUID: " + item.guid + " is not available.")
                # Create a cell style with a red font
                red_font = workbook.createFont()
                red_font.setColor(IndexedColors.RED.getIndex())
                red_font_style = workbook.createCellStyle()
                red_font_style.setFont(red_font)
                # Apply the style to the cell
                cell.setCellStyle(red_font_style)
            else:
                extension = item.getCorrectedExtension()
                myfile = item.name + '.' + extension
                content = "Attachment: " + myfile
                # Save the file
                exportFile = os.path.join(mydirectory, myfile)
                utilities.binaryExporter.exportItem(item, exportFile)
                target_file_name = myfile
                relative_path = "./" + target_file_name
                cell = row.createCell(0)
                cell.setCellValue("Click to open the attachment: " + target_file_name)
                createHelper = workbook.getCreationHelper()
                hlinkstyle = workbook.createCellStyle()
                hlinkfont = workbook.createFont()
                hlinkfont.setUnderline(HSSFFont.U_SINGLE)
                hlinkfont.setColor(IndexedColors.BLUE.index)
                hlinkstyle.setFont(hlinkfont)
                link = createHelper.createHyperlink(HyperlinkType.FILE)
                link.setAddress(relative_path)
                cell.setHyperlink(link)
                cell.setCellStyle(hlinkstyle)

        recipients = getmyrecipients(item)
        sender = getmysender(item)
        shortthreadID = getmyshortthreadid(item)
        cleanedfilename = clean_filename(shortthreadID)
        longthreadID = getmythreadid(item)
        longthreadID = longthreadID.replace(',', '_')
        localdate = localtime(str(item.date))
        datum = str(localdate)
        name = str(item.name)
        name = name.replace(',', '_')
        path = str(item.getPathNames())
        path = path.replace(', ', '/')
        path = path.replace(',', '_')
        md5 = str(item.digests.md5)
        guid = str(item.guid)
        position = str(item.position)
        position = position.replace(', ', '-')


        row.createCell(1).setCellValue(sender)
        row.createCell(2).setCellValue(recipients)
        row.createCell(3).setCellValue(datum)
        row.createCell(4).setCellValue(longthreadID)
        row.createCell(5).setCellValue(name)
        row.createCell(6).setCellValue(path)
        row.createCell(7).setCellValue(position)
        row.createCell(8).setCellValue(md5)
        row.createCell(9).setCellValue(guid)
        row.createCell(10).setCellValue(postname)
        row.createCell(11).setCellValue(channelname)
        row.createCell(12).setCellValue(teamname)

    # Save the workbook to a file
    text_file_path = os.path.join(mydirectory, clean_filename(getmyshortthreadid(item) + ".xls"))
    file_output_stream = FileOutputStream(text_file_path)
    workbook.write(file_output_stream)
    file_output_stream.close()
    workbook.close()


def display_error_message(message):
	messageType = JOptionPane.INFORMATION_MESSAGE
	JOptionPane.showMessageDialog(None, message, "Information", messageType)
	raise Exception(message)


def open_explorer_to_directory(directory_path):
	file = File(directory_path)
	if file.exists() and file.isDirectory():
		Desktop.getDesktop().open(file)
	else:
		error_message = "The specified path '{directory_path}' does not exist or is not a directory."
		display_error_message(error_message)

#Truncate the filename in case it exceeds 255 charachters
#new solution: limit the threadid to 75 characters and if the exported is too long, user needs to select different output folder, higher in the path

def choose_directory():
	while True:
		file_chooser = JFileChooser()
		file_chooser.setDialogTitle("Please select an empty export folder")
		file_chooser.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY)

		result = file_chooser.showOpenDialog(None)

		if result == JFileChooser.APPROVE_OPTION:
			selected_directory = file_chooser.getSelectedFile().getAbsolutePath()
			if len(os.listdir(selected_directory)) != 0:
					error_message = "The selected directory is not empty. Please select an empty directory."
					messageType = JOptionPane.INFORMATION_MESSAGE
					JOptionPane.showMessageDialog(None, error_message, "Information", messageType)
			else:
				return selected_directory
		else:
			error_message = "No directory selected."
			display_error_message(error_message)

#is a given time daylight saving time or not?
def is_dst(timezone, dt):
	tz = TimeZone.getTimeZone(timezone)
	java_date = Date(dt.year - 1900, dt.month - 1, dt.day, dt.hour, dt.minute, dt.second)
	return tz.inDaylightTime(java_date)

#Change the Nuix time (ZULU) to local time
def localtime(utc_time_str):
	# Parse the UTC time string to a datetime object
	utc_time = datetime.strptime(utc_time_str, "%Y-%m-%dT%H:%M:%S.%fZ")

	# Define the UTC time zone
	utc_timezone = TimeZone.getTimeZone("UTC")

	# Convert the UTC time to Central European Time (CET)
	cet_timezone = TimeZone.getTimeZone("Europe/Paris")
	offset_seconds = (cet_timezone.getRawOffset() - utc_timezone.getRawOffset()) / 1000.0
	cet_time = utc_time + timedelta(seconds=offset_seconds)

	# Check if daylight saving time is in effect
	if is_dst("Europe/Paris", cet_time):
		offset_seconds += (cet_timezone.getDSTSavings() / 1000.0)
		cet_time = utc_time + timedelta(seconds=offset_seconds)
	# Format the CET time as a string
	cet_time_str = cet_time.strftime("%Y-%m-%d %H:%M:%S")
	return cet_time_str

#Substitue illegal file name characters with an underscore
def clean_filename(filename):
	# Define a regex pattern to match illegal characters
	illegal_chars = r'[<>:"/\\|?*]'
	# Replace illegal characters with underscores
	cleaned_filename = re.sub(illegal_chars, '_', filename)
	return cleaned_filename

def is_directory_empty(directory):
	for _, _, files in os.walk(directory):
		if files:
			return False
	return True
    
def getmytype(item):
	if str(item.type) == 'application/vnd.microsoft.m365.teams.chat-message' or str(item.type) == 'application/vnd.microsoft.m365.teams.channel-message':
		return "message"        
	elif str(item.type) == 'application/vnd.microsoft.m365.teams.chat-conversation' or str(item.type) == 'application/vnd.microsoft.m365.teams.channel-conversation':   
		return "conversation"
	elif str(item.parent.type) == 'application/vnd.microsoft.m365.teams.chat-message' or str(item.parent.type) == 'application/vnd.microsoft.m365.teams.channel-message':
		return "attachment"
	else:
		    # Check if the item has communication metadata
		if item.getCommunication() is not None:
			return "threadIDchat"
		else:
			error_message = "There is an issue with this item guid: " + item.guid
			display_error_message(error_message)

#limit the threadid to 75 characters to make sure the exported file is not too long
def getmyshortthreadid(item):
	if getmytype(item) == "message" or getmytype(item) == "threadIDchat":
		properties = item.getProperties() #Gets all properties from Microsoft API
	elif getmytype(item) == "attachment":
		properties = item.parent.getProperties() #Gets all properties from Microsoft API
	#limit the threadid to 75 characters, otherwise the exported file might be too long
	threadid = properties["Mapi-IOpenTypedFacet.SkypeSpaces_ConversationPost_Extension#ThreadId"]
	threadid = threadid[:75]
	return threadid
	
def getmysender(item):
	afzender = ""  # Assign a default value
	if getmytype(item) == "message" or getmytype(item) == "threadIDchat":
		afzender = ", ".join(x.toRfc822String() for x in item.communication.from)
	elif getmytype(item) == "attachment":
		afzender = ', '.join(x.toRfc822String() for x in item.getParent().communication.from)
	return afzender

def getmyrecipients(item):
	ontvangers = ""  # Assign a default value
	if getmytype(item) == "message" or getmytype(item) == "threadIDchat":
		ontvangers = ", ".join(x.toRfc822String() for x in item.communication.to)
	elif getmytype(item) == "attachment":
		ontvangers = ', '.join(x.toRfc822String() for x in item.getParent().communication.to)
	return ontvangers

def getmythreadid(item):
	try:
		properties = ""
		if getmytype(item) == "attachment":
			properties = item.parent.getProperties() #Gets all properties from Microsoft API
		else:
			properties = item.getProperties() #Gets all properties from Microsoft API
		return properties["Mapi-IOpenTypedFacet.SkypeSpaces_ConversationPost_Extension#ThreadId"]
	except KeyError:
		error_message = "Is the selected item a Teams Chat Message? Problem with this item: " + item.guid
		display_error_message(error_message)

def createmycustomdate(item):
#there is a problem with the item dates of attachments like images and other files, their item date is around 20 seconds later
#to solve: create a new metadata itemdate, this new itemdate is the item.date except if the item is an attachment, in that case it should have the exact same date as its parent
#this also needs to be corrected in the export scripts
	item_custom_metadata = item.getCustomMetadata()
	if getmytype(item) == "message" or getmytype(item) == "threadIDchat":
		item_custom_metadata.put("SortDate", item.date)
	elif getmytype(item) == "attachment":
		mydate = item.parent.date.plusMillis(1)
		item_custom_metadata.put("SortDate", mydate)
class ProgressPanel(JPanel):
    def __init__(self, text=""):
        # Initialize the progress panel with a label and progress bar.
        super(ProgressPanel, self).__init__()
        self.setLayout(BoxLayout(self, BoxLayout.Y_AXIS))
        self.label = JLabel(text)
        self.progress_bar = JProgressBar()
        self.progress_bar.setIndeterminate(True)
        
        self.add(self.label) 
        self.add(self.progress_bar)

    def destroy(self):
        # Dispose of the dialog containing this panel.
        comp = self
        while not isinstance(comp, MyDialog):
            comp = comp.parent
        comp.dispose()

    def cancel_action(self, event):
        # Set cancel flag to True to stop the process.
        self.cancel = True
class DontClose(WindowAdapter):
    def __init__(self, panel, cancellable=False):
        # Initialize the window adapter to handle close events.
        self.panel = panel
        self.cancellable = cancellable
        
    def windowClosing(self, event):
        # Handle the window closing event.
        if self.cancellable:
            self.panel.cancel_action(event)

def center(panel, margin=0):
    # Center a panel with optional margin.
    out = createHorizontalBox()
    if margin:
        out.add(createHorizontalStrut(margin))
    out.add(createHorizontalGlue())
    out.add(panel)
    out.add(createHorizontalGlue())
    if margin:
        out.add(createHorizontalStrut(margin))
    return out

#class ExportWindow(swing.JFrame):
    # def __init__(self):
        # swing.JFrame.__init__(self, "Exporting")
        # self.setDefaultCloseOperation(swing.JFrame.EXIT_ON_CLOSE)
        # self.setSize(200, 100)
        # self.setLayout(awt.BorderLayout())

        # self.label = swing.JLabel("Exporting")
        # self.add(self.label, awt.BorderLayout.CENTER)

        # self.dots_thread = threading.Thread(target=self.animate_dots)
        # self.dots_thread.daemon = True
        # self.dots_thread.start()

    # def animate_dots(self):
        # while True:
            # for _ in range(3):
                # dots = "."
                # self.label.setText("Exporting" + dots)
                # time.sleep(1)
            # self.label.setText("Exporting")
            # time.sleep(1)

class Exporter(threading.Thread):
    def __init__(self, window, selected_dir):
        threading.Thread.__init__(self)
        self.window = window
        self.selected_dir = selected_dir

    def run(self):
        self.window.setCursor(Cursor.getPredefinedCursor(Cursor.WAIT_CURSOR))
        for mythreadid, collection in collections.items():
            conversation_dir = "Conversation " + clean_filename(mythreadid[:75])
            conversation_path = os.path.join(self.selected_dir + '\\' + conversation_dir)
            os.mkdir(conversation_path)
            #first_element = True
            #text_file_path = ""
	#create_csv_file(collection, conversation_path)
            
	#There is a risk that the path and file are too long for certain file systems, check if the length is larger than 255 and exit if so
            # if len(text_file_path) > 255:
                # error_message = "The file path is too long, select an export directory with a shorter name and start again."
                # display_error_message(error_message)
        self.window.setCursor(Cursor.getPredefinedCursor(Cursor.DEFAULT_CURSOR))
        self.window.dispose()
        
def dotheexport(selected_dir, progress_panel):
    try:
        for mythreadid, collection in collections.items():
            conversation_dir = "Conversation " + clean_filename(mythreadid[:75])
            conversation_path = os.path.join(selected_dir + '\\' + conversation_dir)
            os.mkdir(conversation_path)
            # There is a risk that the path and file are too long for certain file systems, check if the length is larger than 255 and exit if so
            if len(text_file_path) > 255:
                error_message = "The file path is too long, select an export directory with a shorter name and start again."
                display_error_message(error_message)
                return
            create_xls_file(collection, conversation_path)
            print mythreadid
        progress_panel.destroy()
    except Exception as e:
        progress_panel.destroy()
        show_error("An error occurred: {}".format(e))
# Get the Nuix license information
my_license = utilities.getLicence()

# Extract the short name of the license type
short_name = my_license.getShortName()

# Check if the short name is not equal to "enterprise-workstation" (case-insensitive)
if not short_name.lower() == "enterprise-workstation":
    # Your logic if the license is not an enterprise workstation
	error_message = "You can only use this script on a Nuix Server"
	display_error_message(error_message)

# Specify the custom delimiter (e.g., a comma)
delimiter = ","
collections = {}
first_element = False
text_file_path = ""
current_case = currentCase
selected_items = currentSelectedItems
#If one of the selected items is not chat message or channel message:error_message
# Define the predefined collection of strings
# Do we allow the conversation item to be selected, we can skip it at a later stage as it should never be exported?
supported_items_predefined_collection = ['application/vnd.microsoft.m365.teams.chat-message', 'application/vnd.microsoft.m365.teams.channel-message', 'application/vnd.microsoft.m365.teams.channel-conversation' , 'application/vnd.microsoft.m365.teams.chat-conversation']
def main():
    try:
        progress_panel = ProgressPanel("Creating Export")
        for item in selected_items:
            #Here we also need to take attachments into account
            #And also the parent item, the conversation item itself or not?
            if str(item.type) not in supported_items_predefined_collection:
                if str(item.parent.type) not in supported_items_predefined_collection:
                    error_message = "This item is not a Teams chat or channel message: " + item.guid
                    show_error(error_message)
                    return
        #choose the directory first
        selected_directory = choose_directory()

        #if multiple conversations are selected, Create a dictionary of collections based on the threadID and create the custom date for attachments (needed for correct sorting)
        for item in selected_items:
            if not getmytype(item) == "conversation":
                createmycustomdate(item)
                #print localtime(str(item.getCustomMetadata().get("SortDate")))
                mythreadid = getmythreadid(item)
                if mythreadid in collections:
                    # Add the selected item to the existing collection
                    collections[mythreadid].append(item)
                else:
                    # Create a new collection for the GUID
                    collections[mythreadid] = [item]

        #Sort the collections - This takes a long time?
        for mythreadid,collection in collections.items():
            collection.sort(key=lambda item: item.getCustomMetadata().get("SortDate"))
        
        # Start the Export in a new thread
        thread = start_new_thread(dotheexport, (selected_directory, progress_panel))
    
    # Display the dialog
        dialog = MyDialog(progress_panel, title="Exporting", cancellable=False)
        #first_element = True

        # export_window = ExportWindow()
        # export_window.setLocationRelativeTo(None)
        # export_window.setVisible(True)

        # exporter = Exporter(export_window, selected_directory)
        # exporter.start()



        open_explorer_to_directory(selected_directory.replace("\\", "\\\\"))
    except Exception as e:
        error_message = "An error occurred: " + str(e)
        show_error(error_message)
try:
    main()
except Exception as e:
    show_error("An error occurred: {}".format(e))
