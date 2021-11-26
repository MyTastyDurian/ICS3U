'''
Richard Feng and Kevin Joseph (group)
ICS3U - Ms. Edwards
U3 - A1 information on environmental and health impacts of technology related to a specific context
Richard (I) made the GUI (this code).
Kevin made the other code that implments clear screen
'''

# just importing the tkinter library
import tkinter as tk
import requests
from PIL import ImageTk, Image

# intilizing variables height and width in pixels, this determines the height and width of the actual screen
HEIGHT = 1100
WIDTH = 1200

# this function will esentially print the according informaiton in the label based on what button was pressed
# so if button 0 was pressed then it iwll print the departing message and quit the program 
def get_topic(a):
    if(a == 0):
        print("Thank you for using our database!")
        quit()

    elif(a == 1):
        var.set("\nNegative effects of computer use on the environment:\n\n 1. Healthcare contributes to the world's fastest growing waste strem \n(Many computers in a hospital setting)\n\n 2. Hospitals consume a lot of power\n(A lot of electricity is requird in order to power technology)\n\n 3. Creates large amount of pollution\n(fossil fuels and chemicals is required to manufacture the computer)")

    elif(a == 2):
        var.set("\nNegative effects of computer use on humean health:\n\n 1. Improper use can cause muslces and join pain among adminastrator workers \n\n(neck and back remain in same position, excessive use of wrist when typing)\n\n 2. Harmful towards eyesight\n\n (projection of blue light can damage light-sensitive cells)\n\n 3. Excessive time spent in stationary position will lead to obesity \n\n (everything is accessible at our fingertips, can all be accessed on computer) \n\n 4. Social isolation will deterioate mental health \n\n (Less time spent socially active and social media is easily accessed)") #[2]

    elif(a == 3):
        var.set("\nMeasurses that help reduce the impact of computers on the environment:\n\n 1. Recycling computers at local recycling programs\n\n 2. Avoiding using technology when it isn't necessary \n(turning it off when needed)")

    elif(a == 4):
        var.set("\nMeasures to reduce the impact of computer use on human health:\n\n 1. More information should be spread about dangers of using a computer such as:\n\n - you can protect your eyes by looking at your surroundings \n\nso that you aren't staring at something directly in front of oyu all day \n\n - by taking stretching breaks and occasional walks\n\n which will help with muscle and joint pain as well with countering obesity ") #[4]

    elif(a == 5):
        var.set("\nWays in which computers are or could be used to\n reduce resource use and to support environmental protection measures:\n\n 1. Option for hospital staff to communicate digitally\n(sharing files and documents electronically via email)\n\n 2. Video conferenceing using software such as Zoom for doctors\n(video conferencing is adequate for the healthcare professional to help the patient)")

    else:
        var.set("\nGovernment agencies and community partners that provide resources\n and guidance for environmenttal stweardship:\n\n - EPSC is an industry-led non profit organization\n that promote sustainable recycling solutions for Canada's end of life elctronics\n\n - ERPA is focused on servicing the end of\nlife electronics generate primarily by the consumer secotr\n\n - Local recycling programs near you such as recycle my electronics Ontario\n are non-profit providing management electronics across Ontario") #[6]
        
# this is where all the widgets go: label, button, etc
root = tk.Tk()

var = tk.StringVar()

# canvas is located in the parent function root and height and width are assigned to value of HEIGHT and WIDTH
# pack places it in the parent widget or essentially allows us to actually see it
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# this is the background image, but it won't work unless the same image is installed on your device, so I will comment this out
background_image = ImageTk.PhotoImage(file = "business-people-using-computers-in-office-photo.jpg")
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth = 1, relheight = 1)

# this is the top frame: it will be where the welcome message and what number corresponds to each topic e.g. 1 corresponds to topic abt ...
# place is placing it in the parent widget in a more exact location, the exact length and width are defined as well as its location
frame = tk.Frame(root, bg="#FED9C9")
frame.place(relx=0.5, rely=0.01, relwidth=0.75, relheight=0.2, anchor="n")

# need to figure out how to center this properly
welcome_message = tk.Label(frame, text = "Welcome to the database of information on the impacts of computer use on the environment and on human health. Select one of the following 6 topics: \n 1 - Effects of computer use on the environment\n 2 - Effects of computer use on human health\n 3 - Measures that help reduce the impact of computers on the environment\n 4 - Measures that help reduce the impact of computers on human health in this context\n 5 - Ways in which computers are or could be used to reduce resource use and to support environmental protection measures \n 6 - Government agencies and community partners that provide resources and guidance for environmental stewardship", font = ("Constantia", 10))
welcome_message.place(relx = 0.015, rely = 0.07, relwidth = 0.97, relheight = 0.6)

# this is the lower frame as stated in its name: this where the information regarding each topic should be portrayed upon the click of the button
# the bg is the background colour which is a hexadecimal for a nice aesthetic beautiful lushious gorgeuous not so good looking on replit salmon pink
lower_frame = tk.Frame(root, bg="#FED9C9", bd=10)
lower_frame.place(relx=0.5, rely=0.15, relwidth=0.75, relheight=0.6, anchor="n")

button_0 = tk.Button(lower_frame, text = "0 (exit)", command = lambda a = 0: get_topic(a))
button_0.place(relwidth = 0.23, relheight = 0.1)

button_1 = tk.Button(lower_frame, text = "1 (topic)", command = lambda a = 1: get_topic(a))
button_1.place(rely = 0.15, relwidth = 0.23, relheight = 0.1)

button_2 = tk.Button(lower_frame, text = "2 (topic)", command = lambda a = 2: get_topic(a))
button_2.place(rely = 0.3, relwidth = 0.23, relheight = 0.1)

button_3 = tk.Button(lower_frame, text = "3 (topic)", command = lambda a = 3: get_topic(a))
button_3.place(rely = 0.45, relwidth = 0.23, relheight = 0.1)

button_4 = tk.Button(lower_frame, text = "4 (topic)", command = lambda a = 4: get_topic(a))
button_4.place(rely = 0.6, relwidth = 0.23, relheight = 0.1)

button_5 = tk.Button(lower_frame, text = "5 (topic)", command = lambda a = 5: get_topic(a))
button_5.place(rely = 0.75, relwidth = 0.23, relheight = 0.1)

button_6 = tk.Button(lower_frame, text = "6 (topic)", command = lambda a = 6: get_topic(a))
button_6.place(rely = 0.9, relwidth = 0.23, relheight = 0.1)

button_7 = tk.Button(lower_frame, text = "7 (extra topic)")
button_7.place(rely = 1.05, relwidth = 0.23, relheight = 0.1)

# this is the label or where text will actually be portrayed
# this is where the information each topic will be actually portrayed, it is within the lowerframe is white so text shows up easier
label = tk.Label(lower_frame, font=("Constantia", 13), textvariable = var)
label.place(relx = 0.25, relwidth=0.75, relheight=1)

#execution
root.mainloop()

# the number in the square bracket corresponds to what question this citation was used for
'''
Bibliography:
[2] “Computer-related injuries,” Computer-related injuries - Better Health Channel. [Online]. Available: https://www.betterhealth.vic.gov.au/health/healthyliving/computer-related-injuries. [Accessed: 15-Nov-2021]. 
[2] “Computer vision syndrome (Digital Eye Strain),” AOA.org. [Online]. Available: https://www.aoa.org/healthy-eyes/eye-and-vision-conditions/computer-vision-syndrome?sso=y. [Accessed: 15-Nov-2021]. 
[2] 2019 3 Minute ReadMedically Reviewed by UPMC SusquehannaJanuary 6, “Is screen time really bad for our eyes?,” UPMC HealthBeat, 08-Jun-2021. [Online]. Available: https://share.upmc.com/2019/01/screen-time/. [Accessed: 15-Nov-2021]. 
[2] “How technology and social isolation may affect mental health,” Regis College Online, 26-Oct-2021. [Online]. Available: https://online.regiscollege.edu/blog/technology-and-social-isolation/. [Accessed: 15-Nov-2021]. 
[4] “How to protect eyes from Mobile and computer screens,” Kraff Eye Institute. [Online]. Available: https://kraffeye.com/blog/how-to-protect-eyes-from-mobile-and-computer-screens. [Accessed: 15-Nov-2021]. 
[6] “Electronics Recycling Stewardship Programs in Canada: A Primer - Quantum: Itad &amp; E-waste recycling,” Quantum, 15-May-2020. [Online]. Available: https://quantumlifecycle.com/blog/electronics-recycling-stewardship-programs-canada-primer/. [Accessed: 15-Nov-2021]. 
[1] “Healthcare e-waste and the negative impact of digital technology,” Iron Mountain. [Online]. Available: https://www.ironmountain.com/resources/general-articles/h/healthcare-e-waste-and-the-negative-impact-of-digital-technology. [Accessed: 15-Nov-2021]. 
[1] C. Kent, “How hospitals and the Medtech sector are tackling threats to the environment,” Medical device Network, 28-Sep-2021. [Online]. Available: https://www.medicaldevice-network.com/features/hospitals-medtech-environment/. [Accessed: 15-Nov-2021]. 
[1] L. H. Brown, P. G. Buettner, and D. V. Canyon, “The energy burden and environmental impact of Health Services,” American journal of public health, Dec-2012. [Online]. Available: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3519304/. [Accessed: 15-Nov-2021]. 
[1] E. and C. C. Canada, “Government of Canada,” Canada.ca, 24-Oct-2019. [Online]. Available: https://www.canada.ca/en/environment-climate-change/services/managing-pollution/energy-production/electricity-generation.html. [Accessed: 15-Nov-2021]. 
[3] UNU update: PCS impact on the environment. [Online]. Available: https://archive.unu.edu/update/archive/issue31_5.htm. [Accessed: 15-Nov-2021]. 
[3] “Indiana University,” Indiana University Knowledge Base. [Online]. Available: https://kb.iu.edu/d/erth. [Accessed: 15-Nov-2021]. 
[3] “Record 53.6 million tonnes of e-waste dumped globally last year, says UN Report | CBC News,” CBCnews, 02-Jul-2020. [Online]. Available: https://www.cbc.ca/news/science/global-ewaste-monitor-2020-1.5634759. [Accessed: 15-Nov-2021]. 
[3] “Computers and the Environment - Ethics and law - GCSE computer science revision - BBC bitesize,” BBC News. [Online]. Available: https://www.bbc.co.uk/bitesize/guides/zkhykqt/revision/6. [Accessed: 15-Nov-2021]. 
[5] “How is modern technology improving our health?,” The Fact Site, 27-Jul-2021. [Online]. Available: https://www.thefactsite.com/how-modern-technology-improves-health/. [Accessed: 15-Nov-2021]. 
'''