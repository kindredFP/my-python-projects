import pyperclip

#Defining a function

def returnClipboard():
    #pyperclip.copy('The text to be copied to the clipboard.')
    clipboardValue = pyperclip.paste()
    return clipboardValue

## Print the value of clipboard
while True:
    print("*********Value of Clipboard is below**************")
    print(returnClipboard())
    print("********** End of Clipboard **********************")
    print("-------------------------------------")

    print("Type exit to quit otherwise press enter to grab value in clipboard")
    name = input()
    if name == "exit":
        break
