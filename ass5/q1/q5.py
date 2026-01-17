#Use Finally for Resource Cleanup
try:
    file = open("sample.txt", "w")
    file.write("Hello Python")
    print("File written successfully.")

except:
    print("Error occurred.")

finally:
    file.close()
    print("File closed.")
