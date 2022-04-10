# Having a string that represents an international phone
# number, create a program that prints the country code and
# the local phone number.
# e.g. “+34 777444665” will print “+34” and “777444665”
# e.g. “+34 777 444 665” will print “+34” and “777444665”
# e.g. “777 444 665” will print “Not an international phone
# number”

aPhone = "+34 777 444 665"

if aPhone[0] != "+":
    print("The phone isn't international")
else:
    print("The phone is international")

    segments = aPhone.split(" ")
    print("Prefix:", segments[0])

    # Solution with for
    # text = ""
    # for segment in segments[1:]:
    #     text += segment

    text = ''.join(segments[1:])

    print("Phone:", text)