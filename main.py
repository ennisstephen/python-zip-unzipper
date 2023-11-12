# Import the zipfile module
import zipfile

# Specify the name of the zip file
zip_file = "./helloworld.zip"

# Open the zip file in read mode
with zipfile.ZipFile(zip_file, "r") as zf:
    # Extract all the files to a temporary directory
    zf.extractall("temp")

# Specify the name of the text file to modify
text_file = "helloworld.txt"

# Open the text file in read mode
with open("./" + text_file, "r") as tf:
    # Read the content of the text file
    content = tf.read()

# Modify the content of the text file as you wish
# For example, replace the word "hello" with "hi"
modified_content = content.replace("hello world", "helloworld 2")

# Open the text file in write mode
with open("./" + text_file, "w") as tf:
    # Write the modified content to the text file
    tf.write(modified_content)

# Create a new zip file with the modified text file
with zipfile.ZipFile("./" + zip_file, "w") as zf:
    # Write the modified text file to the new zip file
    zf.write("./" + text_file, text_file)

# Delete the temporary directory and its contents
import shutil
shutil.rmtree("temp")