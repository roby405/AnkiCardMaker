This project is supposed to take screenshots of a certain section of the screen, mark a word as unknown, scan the text inside the image by manually feeding it to an ai/ocr, then using the output to generate cards that are automatically added to an anki deck of your choice.

If you have any issue with the app/instructions, please create an issue or contact me on Discord at @rob405

Requirements:
Python
Anki Desktop
Anki Connect add-on
A Google account

How to download and install the packages required by the project:
Download
If you have git:
git clone https://github.com/roby405/AnkiCardMaker
If you dont have git
press the green button that says "Code" and search for a button there saying "Download zip"

Open a terminal and write "pip3 install -r requirements.txt" or "pip install -r requirements.txt"

How the app is supposed to be used (most of these steps are supposed to be done only once):
1. Choose a game/book, an RPG with textboxes preferably, but anything with a fixed area where text appears should work.
2. Find out the borders of where the text appears. For that I have created a script in utils that prints the screen position when you left click anywhere on the screen. Write somewhere down the position of the top left corner and the bottom right corner.
3. Modify the points list in the screenshotter.py file, you can also create another list if you want to use it with multiple apps.
4. Modify the shortcut for opening the app to write which is the unknown word in the shortcut_detector.py file. Only if you want to, of course. By default it's Alt key + ,
5. Run the script (After the changes from the previous steps all you have to do is run the command python3 src/shortcut_detector.py without doing any other modifications)
6. Open the app with the shortcut you assigned or Alt+','. After that write the unknown word or phrase in the textbar that appears and press enter. You can repeat that process any number of times, in any app you want.
7. Close the terminal you ran commands with when you're done with the app. In the dest/ folder you will have all the images saved.
8. Open an AI model of choice. I personally use gemini because it has superior OCR capabilities, a huge limit for pasting images, is free, and is very fast. The next points are assuming you are using gemini.
9. Create a prompt to tell gemini the format of the output you want from it, in terms of the fields on the card model you want.
For example here's what I asked gemini to help me translate from spanish to english:
"You are tasked with helping me add anki cards to my deck. The cards are destined to be for learning spanish as an english speaker. You have to create the fields for multiple anki cards at once. The fields that must be filled for one card are:

word_sp - the name of the image given to you as parameter, without the extension (if it needs to have a preposition beforehand, add it). Use the general version of the word, if its a different person or gender than common form.
sentence_sp - the text you see in the image given
word_en - translation of the word/phrase given as keyword for word_sp
sentence_en - translation of the sentence given in sentence_sp considering context of the current media that you are translating

You must reply with an array of dictionaries (the contents of the dictionary are the filled fields, that can be copy pasted directly into python to be sent with anki connect to the anki deck.

The context of the media that you are translating: ..."
You can edit this a little and have the results you want regardless of language.
If it's annoying to copy paste this every time, create a gem in gemini and add the prompt as an instruction. You can then copy paste the images and get the output you want.
10. Copy paste gemini's answer (it should be an array with dictionaries inside). Go to the anki_integration.py file, and copy paste as the value of fields_list, edit the deck name, card model name, and tags if you plan to use any.
11. Make sure Anki is open. Run the python script, wait to see if you got a success message (a bunch of numbers). If yes the cards were successfully added.
